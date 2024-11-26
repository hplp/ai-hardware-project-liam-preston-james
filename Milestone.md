Milestone Progress:
OpenMV Hardware Specifications
- 1 MB RAM
- 2 MB Flash
- 640x480 Image size
- 60 FPS @ 320x240

Training of the resnet and mobilenet_v2 model on kaggle dataset of rock paper and scissors: 
https://colab.research.google.com/drive/1cPB-5h6r93SqMteZEWJnD8yT2T1E6VXF?usp=sharing

Conversion of ONNX file to TFLite float16 and Int8:
https://colab.research.google.com/drive/1Dsc7Og8dJkjjbVFdO5sSCdOGALGsHR2c?usp=sharing

Size of the TFLite Files:
resnet18_int8.tflite: 11,054 kB
resnet18_float16.tflite: 21,841 kB

As seen above, condensing the model significantly reduced the amount of RAM that we would be using, we will now be testing both of them to see if the accuracy is still good enough on quantizied model to be servicable to our project.

Setting Up Hardware:
We were successfully able to download the IDE from openmv.io for the OpenMV and connect to the camera to see real-time footage. The hardware came with an issue of not being able to download the newest firmware and was significantly out of date. Through the IDE bootloader and downloading the newest firmware, we were able to manually install the newest firmware to ensure functionality between the M7 and our computer.
![image](https://github.com/user-attachments/assets/112ccbde-cfcf-4dfa-94a4-c6b0d3d01a75)

With the ResNet-18 model trained to recognize the hand signals and shrunken down to an int-8 size to fit onto the board, we then attempted to integrate the model and the board for the image recognition that we were looking for. 

The image classification model is currently too large to function and we will need to work on shrinking the model down further to work on the board.
