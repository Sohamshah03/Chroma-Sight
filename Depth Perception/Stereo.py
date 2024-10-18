import torch
import torch.nn.functional as F
import cv2
import numpy as np


class StereoBM(torch.nn.Module):
    def __init__(self, block_size=15, max_disparity=64):
        super(StereoBM, self).__init__()
        self.block_size = block_size
        self.max_disparity = max_disparity

    def forward(self, left, right):
        b, c, h, w = left.shape

        # Create cost volume
        cost_volume = torch.zeros(b, self.max_disparity, h, w, device=left.device)

        # Prepare sliding window
        window = torch.ones(1, 1, self.block_size, self.block_size, device=left.device)

        for d in range(self.max_disparity):
            # Shift right image
            if d > 0:
                right_shifted = F.pad(right, (d, 0, 0, 0), mode='replicate')[:, :, :, :w]
            else:
                right_shifted = right

            # Compute absolute difference
            diff = torch.abs(left - right_shifted)

            # Apply sliding window (effectively sum absolute differences in each block)
            cost = F.conv2d(diff, window, padding='same')

            # Store in cost volume
            cost_volume[:, d] = cost.squeeze(1)

        # Find minimum cost and corresponding disparity
        best_cost, best_disparity = cost_volume.min(dim=1)

        return best_disparity


def compute_stereo_bm(left_image, right_image, block_size=15, max_disparity=96):
    # Ensure images are grayscale and in the correct format
    left_image = cv2.cvtColor(left_image, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0
    right_image = cv2.cvtColor(right_image, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0

    # Convert to PyTorch tensors and move to GPU
    left_tensor = torch.from_numpy(left_image).unsqueeze(0).unsqueeze(0).cuda()
    right_tensor = torch.from_numpy(right_image).unsqueeze(0).unsqueeze(0).cuda()

    # Create and use the StereoBM model
    model = StereoBM(block_size, max_disparity).cuda()
    with torch.no_grad():
        disparity = model(left_tensor, right_tensor)

    print(disparity)
    # Convert back to numpy array and scale to 0-255 range
    disparity_map = (disparity.cpu().numpy() * (255.0 / max_disparity)).astype(np.uint8)

    # Ensure the disparity map is 2D
    disparity_map = disparity_map.squeeze()

    return disparity_map

def calculate_depth(disparity_map, focal_length, baseline):
    # Avoid division by zero; set disparities close to zero to a small value
    disparity_map[disparity_map == 0] = 1e-6
    depth_map = (focal_length * baseline) / disparity_map
    return depth_map

# Example usage
def run(left_image,right_image):
    # Compute disparity map
    disparity_map = compute_stereo_bm(left_image, right_image)
    for_depth = disparity_map
    disparity_map = cv2.normalize(disparity_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    sharpening_kernel = np.array([[0, -1, 0],
                                  [-1, 5, -1],
                                  [0, -1, 0]])

    # Apply the sharpening kernel to the image
    disparity_map = cv2.filter2D(disparity_map, -1, sharpening_kernel)

    kernel = np.ones((3,3), np.uint8)
    eroded_image = cv2.erode(disparity_map, kernel, iterations=1)
    for i in range(3):
        blurred = cv2.GaussianBlur(eroded_image, (9, 9), 10)
        sharpened = cv2.addWeighted(eroded_image, 1.5, blurred, -0.5, 0)
        eroded_image = sharpened

    focal_length = 800  # Example focal length in pixels
    baseline = 0.75  # Example baseline distance in meters (7.5 cm)

    # Calculate depth map
    depth_map = calculate_depth(for_depth, focal_length, baseline)

    # Example: Get depth at a specific pixel
    pixel_x, pixel_y = 200, 200  # Replace with your pixel coordinates
    depth_at_pixel = depth_map[pixel_y, pixel_x]
    print(f"Depth at pixel ({pixel_x}, {pixel_y}): {depth_at_pixel:.2f} meters")

    cv2.imshow("Sharp", eroded_image)
    cv2.imshow("Disparity Map", disparity_map)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Optionally, save the disparity map
    cv2.imwrite("disparity_map.png", disparity_map)

left_image = cv2.imread(r"C:\Users\Krish\Downloads\Test Left.png")
right_image = cv2.imread(r"C:\Users\Krish\Downloads\Test Right.png")
run(left_image,right_image)