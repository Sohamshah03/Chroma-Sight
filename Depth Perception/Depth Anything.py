import cv2
import torch
import numpy as np
from transformers import pipeline
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

depth_pipe = pipeline(
    task="depth-estimation",
    model="depth-anything/Depth-Anything-V2-small-hf",
    device=0 if device == "cuda" else -1
)


def estimate_depth(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    pil_image = Image.fromarray(rgb_frame)

    depth = depth_pipe(pil_image)["depth"]

    depth_np = np.array(depth)

    depth_normalized = cv2.normalize(depth_np, None, 0, 255, cv2.NORM_MINMAX)
    depth_normalized = depth_normalized.astype(np.uint8)

    depth_colored = cv2.applyColorMap(depth_normalized, cv2.COLORMAP_MAGMA)

    return depth_colored


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame.")
            break

        depth_map = estimate_depth(frame)

        cv2.imshow('Output', depth_map)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
