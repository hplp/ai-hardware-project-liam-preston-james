import sensor
import time
import random
from collections import deque
import ml

# Initialize the camera sensor
sensor.reset()  # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)  # Set pixel format to RGB565
sensor.set_framesize(sensor.QVGA)  # Set frame size to QVGA (320x240)
sensor.set_windowing((224, 224))  # Match the model's expected input size
sensor.skip_frames(time=2000)  # Allow time for settings to take effect.

# Load the TensorFlow Lite model and labels
model_file = "/trained.tflite"  # Update with your model file
labels = ["Paper", "Rock", "Scissors"]  # Your class labels
model = ml.Model(model_file, load_to_fb=True)

# Function to determine the winner
def determine_winner(player, ai):
    if player == ai:
        return "It's a tie!"
    elif (player == "Rock" and ai == "Scissors") or \
         (player == "Paper" and ai == "Rock") or \
         (player == "Scissors" and ai == "Paper"):
        return "Player wins!"
    else:
        return "AI wins!"

# Variables for tracking consecutive predictions
consecutive_count = 0
last_prediction = None
ai_choices = ["Paper", "Rock", "Scissors"]

# Main loop
while True:
    time.sleep(2)  # Wait for 0.5 seconds
    img = sensor.snapshot()  # Capture an image
    print("Polling...")  # Indicate polling action

    # Run the model prediction
    predictions = model.predict([img])[0].flatten().tolist()
    sorted_predictions = sorted(zip(labels, predictions), key=lambda x: x[1], reverse=True)

    # Get the highest confidence prediction
    top_label, top_confidence = sorted_predictions[0]

    # Check if the highest prediction is consistent
    if top_label == last_prediction:
        consecutive_count += 1
    else:
        consecutive_count = 1  # Reset counter
        last_prediction = top_label

    # If the same label is detected three times in a row
    if consecutive_count == 3:
        print(f"Consecutive prediction: {top_label} with confidence {top_confidence:.2f}")
        player_move = top_label

        # AI makes a random choice
        ai_move = random.choice(ai_choices)
        print(f"AI chose: {ai_move}")

        # Determine the winner
        result = determine_winner(player_move, ai_move)
        print(f"Result: {result}")

        # Reset tracking variables
        consecutive_count = 0
        last_prediction = None
