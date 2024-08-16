## Tuning process

![alt text](Images/C2W3L1-1.png)

We should not take inputs at regular intervals from the grid because if hyperparameter1 is of more importance than hyperparameter2 we are still considering equal variations of both which is not efficient. Instead we should choose points randomly from the grid which will increase the variations of both and will be more efficient.

After trying random points from the grid whichever points work the best, we should zoom in our grid in that region and consider more points from that region as shown in images below.

![alt text](Images/C2W3L1-2.png)

![alt text](Images/C2W3L1-3.png)

We need to consider the scale for hyperparameters to ensure we try inputs from the whole range efficiently.

![alt text](Images/C2W3L2-1.png)

![alt text](Images/C2W3L2-2.png)

![alt text](Images/C2W3L3-1.png)

## Normalizing Inputs

Normalizing input data is a crucial step in deep learning as it ensures that each feature contributes equally to the model's learning process. By scaling features to a standard range, such as [0, 1] or [-1, 1], normalization prevents certain features from dominating others, which can lead to inefficient learning. This process also aids in faster convergence by ensuring that the gradients remain within a reasonable range, thereby avoiding issues like vanishing or exploding gradients.

![alt text](Images/C2W3L4-1.png)

Batch normalization, on the other hand, is a technique applied during training to further stabilize and accelerate the learning process. It normalizes the output of a layer by adjusting and scaling the activations within each mini-batch.

![alt text](Images/C2W3L4-2.png)

![alt text](Images/C2W3L5-1.png)

![alt text](Images/C2W3L5-2.png)

![alt text](Images/C2W3L5-3.png)

![alt text](Images/C2W3L6-1.png)

It reduces the internal covariate shift, where the distribution of layer inputs changes during training, allowing the model to learn more effectively.
Additionally, batch normalization enables the use of higher learning rates, leading to faster convergence. It also acts as a form of regularization, sometimes reducing the need for other techniques like dropout, and ultimately contributes to the model's robustness and generalization.

![alt text](Images/C2W3L7-1.png)

![alt text](Images/C2W3L7-2.png)

## Softmax Regression

A softmax classifier is used in multi-class classification problems. It converts the raw output scores of a model into probabilities, with the sum of all probabilities equal to 1. The softmax function emphasizes the highest scores while suppressing the lower ones, making it easier to interpret the model's predictions. The class with the highest probability is selected as the final prediction.

![alt text](Images/C2W3L8-1.png)

![alt text](Images/C2W3L8-2.png)

![alt text](Images/C2W3L9-1.png)

## Problem of Local Optima

The problem of local optima in neural networks occurs when the training process gets stuck in a suboptimal solution— a "local minimum"—instead of finding the best possible solution, or "global minimum." This happens because the optimization algorithm (like gradient descent) might settle in a valley of the loss landscape that isn't the lowest point overall, leading to a model that isn't as accurate as it could be. However, modern techniques like using non-linear activation functions, careful initialization, and optimization methods like Adam help mitigate this issue.

![alt text](Images/C2W3L10-1.png)

![alt text](Images/C2W3L10-2.png)
