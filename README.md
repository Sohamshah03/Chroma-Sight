# Image Captioning & Traffic Sign Detection for Blind People

This repo contains two core projects:

1. ### Image Captioning for Blind People using Vision Transformer (ViT) from Scratch

   A deep learning model aimed at generating optimized and concise text descriptions for images in real-time to assist blind and visually impaired individuals. The model uses a Vision Transformer (ViT) architecture, built from scratch, to understand and describe the content of an image.

2. ### Traffic Sign Detection using YOLO

   A YOLO-based model for detecting and classifying traffic signs. This project aims to aid autonomous driving systems or assistive technologies for colorblind or visually impaired people in recognizing traffic signs.

## File Structure

<pre><code>Chroma-Sight/
│
├── README.md
├
├── Captioning/
├   ├── captureimageoakd.py
├   ├── Image Captioning.ipynb
├
├── Depth Perception/
├   ├── Depth Anything.py
├   ├── Midas Depth Estimation.py
├   ├── Stereo.py
├   ├── Stereo Inbuilt.py
├
├── Mini Projects/
├   ├── ishihara.ipynb
├   ├── ripe-and-rotten.ipynb
├   ├── Traffic Ligth Detection.ipynb
├ 
├── YOLO/
├   ├── config.py
├   ├── dataset.py
├   ├── loss.py
├   ├── model.py
├   ├── train.py
├   ├── utils.py
├
├── Images/
├   ├── Architecture Images/
├   ├   ├── VGG 16.jpg
├   ├   ├── VIT Architecture.jpg
├   ├  
├   ├── Images Captioning/
├   ├   ├── Image Captioning Output 1.jpg
├   ├   ├── Image Captioning Output 2.jpg
├   ├   ├── Image Captioning Output 3.jpg
├   ├  
├   ├── Traffic/
├   ├   ├── Traffic Output 1.jpg
├   ├   ├── Traffic Output 2.jpg
├   ├   ├── Traffic Output 3.jpg


</code></pre>

## Tech Stack

### Image Captioning:

- Programming Language: Python
- Deep Learning Framework: PyTorch
- Model: Vision Transformer (ViT) trained from scratch
- Text-to-Speech: Google Text-to-Speech (gTTS) API
- Dataset: [COCO Captions](https://www.kaggle.com/datasets/nikhil7280/coco-image-caption)
- Environment: Jupyter Notebooks

### Traffic Sign Detection:

- Programming Language: Python
- Deep Learning Frameworks: TensorFlow, Keras
- Model: YOLOv8 fine-tuned for traffic sign detection
- Text-to-Speech: Google Text-to-Speech (gTTS) API
- Dataset: [Traffic Signs](https://www.kaggle.com/datasets/pkdarabi/cardetection)
- Environment: Jupyter Notebooks

## Project Structure

## Image Captioning using ViT from scratch

### Problem:

Blind and visually impaired individuals face challenges in understanding visual content in their everyday environment, making it difficult to access key information from images. This project aims to solve that problem by providing real-time, concise, and descriptive captions for images, helping visually impaired users gain insights into their surroundings.

### Approach(ViT):

#### Encoder:

- The Vision Encoder divides the input image into patches of a fixed size (16x16 pixels) and flattens each patch into a vector. These vectors are then passed through a fully connected layer to match the transformer’s hidden size.
- Sinusoidal Positional Embeddings are added to the patch embeddings to preserve spatial information.
- The patch embeddings are processed by multiple Transformer blocks, where each block includes:
  - Multi-head Attention for capturing relationships between image patches.
  - Feed-Forward Networks (MLPs) to process the extracted features.

#### Decoder:

- The Decoder generates captions word-by-word, using previously generated words to predict the next word.
- Sinusoidal Positional Embeddings are added to the input sequence (target caption) to preserve word order.
- The decoder includes cross-attention layers, where the decoder attends to the encoder’s output (image patches) to generate contextually appropriate captions.
- Multiple Transformer Blocks are stacked in the decoder to refine the caption output.
  Attention Mechanism:
  Multi-head attention is applied within both the encoder (self-attention on image patches) and decoder (self-attention on the generated words and cross-attention to image features).

#### Outputs:

<img src="Images/Image Captioning/Image Captioning Output 1.jpg" alt="Flowchart" width="300" height="300">
<img src="Images/Image Captioning/Image Captioning Output 2.jpg" alt="Flowchart" width="300" height="300">
<img src="Images/Image Captioning/Image Captioning Output 3.jpg" alt="Flowchart" width="300" height="300">

### Applications:

- **Assistive Tools**: Can be integrated into mobile applications or devices to provide on-the-fly descriptions of surroundings, helping blind individuals navigate or understand visual information.

- **Accessibility Enhancements**: This model can be used to enhance the accessibility of image-heavy content on websites, apps, or devices.

### Implementation & Requirements:

## Traffic Sign Detection using pre-trained YOLOv8

### Problem:

Colorblind individuals often struggle to identify color-coded traffic signs, while autonomous driving systems require fast and accurate detection of signs to ensure safe navigation. This project addresses both challenges by developing a real-time traffic sign detection model using YOLOv8, enhancing road safety for all users.

### Approach:

#### Yolo Architecture:

- Grid System: The input image is divided into a grid (e.g., 7x7). Each grid cell is responsible for detecting objects whose center falls inside that cell.

- Bounding Boxes: For each cell, YOLO predicts multiple bounding boxes. Each box includes the coordinates (x, y, width, height) and a confidence score indicating how likely it is to contain an object.

- Class Prediction: YOLO also predicts which object class (e.g., cat, dog, car) is present in the cell. It outputs a probability for each class.

- Single Forward Pass: The model processes the whole image in a single pass through the network, making predictions for all grid cells at once.

- Post-Processing: After the predictions, non-maximum suppression (NMS) is used to filter out overlapping boxes, keeping only the ones with the highest confidence.


#### Outputs:

<img src="Images/Traffic/Traffic Output 1.jpg" alt="Flowchart" width="300" height="300">
<img src="Images/Traffic/Traffic Output 2.jpg" alt="Flowchart" width="300" height="300">
<img src="Images/Traffic/Traffic Output 2.jpg" alt="Flowchart" width="300" height="300">

### Applications:

- **Assistive Technology for Colorblind Individuals**: This model can be used in smart glasses, apps, or navigation systems to help colorblind users identify traffic signs, providing audio feedback through the gTTS API for safer navigation.
- **Autonomous Driving**: The YOLOv8 model enhances self-driving cars' perception systems by accurately detecting and classifying traffic signs, enabling the vehicle to follow road rules in real time.

## Acknowledgements

<ul>
  <li>We are grateful to <a href="https://github.com/CommunityOfCoders"/li>CoC VJTI</a> and the <a href="https://github.com/ProjectX-VJTI">Project X</a> programme.
  <li>Special thanks to our mentors <a href="https://github.com/Anoushka1009">Anoushka Ruikar</a> and <a href="https://github.com/aditidhu">Aditi Dhumal</a> for perfectly mentoring and supporting us throughout.</li>
  <li>Additionally, we are also thankful for all the Project X mentors for their inputs and advice on our project.</li>
</ul>

## Contact

<a href="https://github.com/KrishShah3011">Krish Shah</a> <br>
<a href="https://github.com/Sohamshah03">Soham Shah</a>
