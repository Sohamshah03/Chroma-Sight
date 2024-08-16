# COURSE4-WEEK3

## OBJECT LOCALIZATION

![alt text](Images/image-30.png)
![alt text](Images/image-29.png)
![alt text](Images/image-31.png)

## LANDMARK DETECTION

Landmark detection refers to the process of identifying and locating specific key points or features in an image, often of human faces or other objects, that are significant for a particular application.
Detecting body landmarks can assist in estimating human poses, which is important in motion tracking, sports analytics, and animation.
![alt text](Images/image-32.png)

## OBJECT DETETION

### SLIDING WINDOW

In this algo we bassically slide a box of a particular sizw through the image and we send that part of the image through a covnet and that covent will detect wheater the picture is present or not in the that particular window
![alt text](Images/image-33.png)

### CONVOLUTIONAL IMPLEMENTATION OF SLIDING WINDOW

If we put the every single cropped image through covnet then the computational cost will increasee alott so we want everything to happen all together
![alt text](Images/image-34.png)
So we implement convolutions in such a way that at the end we have for eg 2 by 2 box in which each part is represents each 1/4 part of the image depicting whether the image is present or not.
![alt text](Images/image-35.png)
![alt text](Images/image-36.png)

## BOUNDING BOX PREDICTIONS

When we have to predict bounding boxes we first divide the image in grids and also we give the actual dinmensions of the box and center of the box as ground truth label in input and then the covnet predicts first ki is the object there in the the particular grid and if there than predicts center and the box dimension and the covnet learns according to the graddesc and wrt to the label as tier target.
![alt text](Images/image-37.png)
![alt text](Images/image-38.png)

## IOU

Intersection of the bounding box NN predicts and actual bounding box.
![alt text](Images/image-39.png)

## NON-MAX SUPRESSION

![alt text](Images/image-40.png)

## ANCHOR BOX

An anchor box is a predefined bounding box used in object detection models like YOLO, Faster R-CNN, and SSD. These boxes have specific shapes (aspect ratios and scales) and are placed at different positions across the image. The purpose of anchor boxes is to detect objects of various sizes and shapes.
![alt text](Images/image-41.png)
![alt text](Images/image-42.png)

## YOLO

YOLO (You Only Look Once) is a real-time object detection system that divides an image into a grid and predicts bounding boxes and class probabilities for objects in each grid cell simultaneously. Unlike traditional methods that run the detection model at multiple locations and scales, YOLO processes the entire image with a single neural network, making it extremely fast and efficient.

YOLO processes the entire image all at once by dividing it into grid cells, predicting bounding boxes, confidence scores, and class probabilities for each cell. This allows YOLO to detect objects in a single forward pass of the network, making it faster than region-based methods.
![alt text](Images/image-43.png)
![alt text](Images/image-44.png)

## Semantic Segmentation with U-Net

Semantic segmentation involves classifying each pixel in an image into a predefined class, meaning every pixel is labeled as belonging to a specific category (e.g., road, car, sky).

Object detection, on the other hand, identifies and localizes objects within an image by drawing bounding boxes around them and assigning class labels to each detected object.
![alt text](Images/image-45.png)
![alt text](Images/image-46.png)
![alt text](Images/image-47.png)

## TRANSPOSE CONVOLUTIONS

ranspose convolutions, also called deconvolutions or upsampling convolutions, are used in neural networks to upsample an input (i.e., increase its spatial resolution).
![alt text](Images/image-48.png)
![alt text](Images/image-49.png)
![alt text](Images/image-50.png)
![alt text](Images/image-51.png)

## U-NET

It first encode the input . Consists of repeated blocks of convolutional layers reduceing the spatial dimensions while capturing features.
A deeper layer that connects the encoder and decoder, capturing the most abstract features.
Consists of upsampling layers followed by convolutional layers. The upsampled features are concatenated with the corresponding encoder layers (skip connections) to retain fine-grained details.
The U-Net combines low-level features from the encoder with high-level features in the decoder to retain both spatial information and learned features.
![alt text](Images/image-52.png)
![alt text](Images/image-53.png)
