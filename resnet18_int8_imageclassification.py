# This work is licensed under the MIT license.
# Copyright (c) 2013-2024 OpenMV LLC. All rights reserved.
# https://github.com/openmv/openmv/blob/master/LICENSE
#
# TensorFlow Lite ResNet-18 Example
#
# This script performs image classification using a custom-trained TFLite model.

import sensor
import time
import ml

# Initialize the sensor
sensor.reset()  # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)  # Set pixel format to RGB565
sensor.set_framesize(sensor.QVGA)  # Set frame size to QVGA (320x240)
sensor.set_windowing((224, 224))  # Set window size to match model input (224x224)
sensor.skip_frames(time=2000)  # Let the camera adjust.

# Load the custom model and labels
model_file = "/resnet18_int8.tflite"  # Updated to full path
model = ml.Model(model_file, load_to_fb=True)

# Replace with your class labels (e.g., Rock, Paper, Scissors)
labels = ["Rock", "Paper", "Scissors"]

# Start inference loop
clock = time.clock()
while True:
    clock.tick()

    img = sensor.snapshot()  # Capture an image from the camera

    # Run the model prediction
    predictions = model.predict([img])[0].flatten().tolist()

    # Combine labels and predictions, sort by confidence, and print top 3 results
    sorted_predictions = sorted(zip(labels, predictions), key=lambda x: x[1], reverse=True)
    print("**********\nTop 3 Detections")
    for i in range(3):
        print("%s = %f" % (sorted_predictions[i][0], sorted_predictions[i][1]))

    print(clock.fps(), "fps")  # Print frames per second.
