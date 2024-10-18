import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load stereo images (ensure they are loaded as grayscale, CV_8UC1)
left_img = cv2.imread(r"C:\Users\Krish\Downloads\Test Left.png", 0)
right_img = cv2.imread(r"C:\Users\Krish\Downloads\Test Right.png", 0)

# Check if images are loaded properly
if left_img is None or right_img is None:
    print("Error loading images!")
    exit()

# Check if images are already in the correct format (CV_8UC1)
if left_img.dtype != np.uint8 or right_img.dtype != np.uint8:
    left_img = cv2.convertScaleAbs(left_img)
    right_img = cv2.convertScaleAbs(right_img)

# Initialize the StereoBM object
stereo_bm = cv2.StereoBM_create(numDisparities=64, blockSize=15)

# Compute the disparity map
disparity = stereo_bm.compute(left_img, right_img)

# Normalize the disparity map for visualization
disparity_normalized = cv2.normalize(disparity, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
disparity_normalized = np.uint8(disparity_normalized)

# Show the disparity map
plt.imshow(disparity_normalized, cmap='gray')
plt.title('Disparity Map')
plt.show()
