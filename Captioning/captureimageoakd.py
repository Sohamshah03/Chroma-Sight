

import depthai as dai
import cv2


pipeline = dai.Pipeline()


camRgb = pipeline.create(dai.node.ColorCamera)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)


xoutRgb = pipeline.create(dai.node.XLinkOut)
xoutRgb.setStreamName("rgb")
camRgb.preview.link(xoutRgb.input)


with dai.Device(pipeline) as device:
  
    rgbQueue = device.getOutputQueue(name="rgb", maxSize=1, blocking=False)
    
    print("Press 's' to save an image or 'q' to quit.")
    
    while True:
        inRgb = rgbQueue.get()
        frame = inRgb.getCvFrame()

        cv2.imshow("OAK-D Image Capture", frame)

        key = cv2.waitKey(1)

        if key == ord('s'):
            cv2.imwrite("captured_image.png", frame)
            print("Image saved as 'captured_image.png'")

        elif key == ord('q'):
            break

    cv2.destroyAllWindows()