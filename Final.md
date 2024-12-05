Link to the Edge Impulse Project: https://studio.edgeimpulse.com/public/571822/live

Link to Presentation Slideds: https://docs.google.com/presentation/d/1lP5mvR__jHIdw0KWdsRgDkHa9oT95vMesb1VH1QHL2o/edit?usp=sharing

Motivation and Goals: 
  - Being able to image train a model
  - Observe Human - AI interaction
  - Applying the image trained model to accomplish a specific goal
  - Learn more about running AI in a low power environment

Project Description: 
- Our project will utilize the camera on the OpenMV H7 to play "Rock, Paper, Scissors" against a human opponent. The AI will first randomly pick either Rock, Paper, or Scissors then it will detect what choice the human made using its camera and decide whether the human won or lost.

Tools Used:
  - Edge Impulse (Online tool)
  - Openmv microcontroller
  - Openmv IDE (python)

Steps:
  - Taking pictures of relevant data utilizing several different angles and distances
  - Split the images into training and test sets in about an 80/20 split
  - Select a model and train on images (MobileNetV1)
  - Change things like learning rate, neuron count, epochs/cycles, and dropout rate
  - Export model onto Openmv
  - Run the code and enjoy this classic game!

Results:
  - 89.7% Accuracy on trained model
  - 0.44 Loss
  - Good clustering of the different labels

Lessons Learned:
  - Openmv has very limited memory available
  - Only smaller models are able to fit (i.e. MobileNetV1)
  - Had to use quantization and pruning of model to reduce size
  - Difficult to upload .onnx files onto Openmv
  - The camera leaves a lot to be desired
  - The model is not perfect
  - Limited Quality of data

Key Takeaways: 

The project demonstrated the successful implementation of an image-based AI model using the OpenMV H7 microcontroller, achieving a functional "Rock, Paper, Scissors" game. Through this effort, the team gained valuable insights into human-AI interaction, model training processes, and the constraints of deploying AI in low-power environments. Notably, the trained model achieved an accuracy of 89.7% and demonstrated effective clustering of the classification labels, underscoring the feasibility of deploying machine learning models on resource-constrained devices.

However, the project highlighted several challenges, including the limited memory capacity of the OpenMV H7, which necessitated the use of smaller models such as MobileNetV1, along with quantization and pruning to ensure compatibility. Additionally, the process revealed difficulties in uploading .onnx files to the microcontroller and limitations in camera quality, which affected data collection and model performance. These challenges emphasized the importance of balancing computational efficiency and model accuracy in constrained environments.

Future work on similar projects could focus on improving data quality by incorporating higher-resolution cameras and more diverse datasets. Additionally, exploring alternative hardware platforms with enhanced processing power and memory could enable the deployment of more complex models. Further optimization of the training pipeline and continued refinement of transfer learning techniques could also lead to better performance and wider applications for AI in low-power scenarios.
