Within the GitHub repository, you will see three text files: README.md, Milestone.md, and Final.md. The README.md is the initial project proposal that defined the scope of the work we wanted to accomplish and the hardware we were using. The Milestone.md is the document providing details on how we intiailly set up our hardware and first steps we took to accomplish our goals as defined by the project proposal. The third document, Final.md (this document) served as the final report to describe all of the steps we took during the project and our final results. 

Here are two links to the Edge Impulse Project we set up and the Final presentation slides.
- Link to the Edge Impulse Project: https://studio.edgeimpulse.com/public/571822/live
- Link to Presentation Slideds: https://docs.google.com/presentation/d/1lP5mvR__jHIdw0KWdsRgDkHa9oT95vMesb1VH1QHL2o/edit?usp=sharing

This is a quick overview of what we highlighted in our presentation and the overall achievements from the presentation:

**Motivation and Goals:** 
  - Being able to image train a model
  - Observe Human - AI interaction
  - Applying the image trained model to accomplish a specific goal
  - Learn more about running AI in a low power environment

**Project Description:**
- Our project will utilize the camera on the OpenMV H7 to play "Rock, Paper, Scissors" against a human opponent. The AI will first randomly pick either Rock, Paper, or Scissors then it will detect what choice the human made using its camera and decide whether the human won or lost.

**Tools Used:**
  - Edge Impulse (Online tool)
  - Openmv microcontroller
  - Openmv IDE (python)

**Steps:**
  - Taking pictures of relevant data utilizing several different angles and distances
  - Split the images into training and test sets in about an 80/20 split
  - Select a model and train on images (MobileNetV1)
  - Change things like learning rate, neuron count, epochs/cycles, and dropout rate
  - Export model onto Openmv
  - Run the code and enjoy this classic game!

**Results:**
  - 89.7% Accuracy on trained model
  - 0.44 Loss
  - Good clustering of the different labels

**Lessons Learned:**
  - Openmv has very limited memory available
  - Only smaller models are able to fit (i.e. MobileNetV1)
  - Had to use quantization and pruning of model to reduce size
  - Difficult to upload .onnx files onto Openmv
  - The camera leaves a lot to be desired
  - The model is not perfect
  - Limited Quality of data

We started this project by attempting to train our own model wihtin a google Collab notebook using a GPU and knowledge from the preivous homework assignments and the help of other generative AI programs like ChatGPT. We found an online Kaggle repo that contained a collection of 800 images of each a paper, rock, and scissors hand signal that we then uploaded to the Collab notebook and used ResNet-18 and MobileNetV2 to train the model and then deploy it into a ONNX file. We then developed a second google collab notebook to convert the ONNX file to a quantized int-8 TFlite file to fit on the OpenMV's limited RAM. However, after training about a dozen different TFLite files using a variety of different quanitizations, models, and image datasets with no availability. All of these files can be found in this GitHub Repo underneath the Model folder. 

At this point we decided to pivot and use an online program called Edge Impulse to train our model. We chose to use this program because we knew that it used the FOMO model in order to train a small dataset relatively well and it was able to quantizize it small enough to fit on the OpenMV's memory. 

We originally used the Kaggle dataset within the Edge Impulse project but quickly realized that the quality and type of image that the OpenMV H7 camera was able to "see" and the online image were not matching enough for the model to accurately classify the differing hand signals. At this point we decided to use a program that is uploaded under the OpenMVFinalCode folder called dataset_capture_script.py to use the H7 camera to take pictures of our own hands to train the model. With about 60 images of each hand signal being captured with the camera and uploaded to the Edge Impulse project. We then used these images to train an impulse and used the MobileNetV1 1.0 model since it was the only model small enough to fit on the 100 kB RAM on the OpenMV H7 microcontroller. 

The trained model can be seen in the OpenMVFinalCode folder, the Labels.txt and the trained.tflite files were both transfered to the microcontroller while the RockPaperScissorGame.py was run on the microcontroller through the OpenMV IDE. The python program works by pollnig the camera every 0.5 seconds, taking an image from the camera and then analyzing it to determine if there was a rock, paper, or scissor hand signal in the frame. If three consecutive images are recognized as the same (i.e. Rock, Rock, Rock), then the game will recognize this as an official play and will play this against the random descion that the AI generated. The result of the play is then dispayed in the console (Tie, Win, Lose) and the program carries on. There is a frame recognition portion of the program that will analyize the last 10 plays made by the player to make a smart prediction on what move the player will make.

**Key Takeaways:**

The project demonstrated the successful implementation of an image-based AI model using the OpenMV H7 microcontroller, achieving a functional "Rock, Paper, Scissors" game. Through this effort, the team gained valuable insights into human-AI interaction, model training processes, and the constraints of deploying AI in low-power environments. Notably, the trained model achieved an accuracy of 89.7% and demonstrated effective clustering of the classification labels, underscoring the feasibility of deploying machine learning models on resource-constrained devices.

However, the project highlighted several challenges, including the limited memory capacity of the OpenMV H7, which necessitated the use of smaller models such as MobileNetV1, along with quantization and pruning to ensure compatibility. Additionally, the process revealed difficulties in uploading .onnx files to the microcontroller and limitations in camera quality, which affected data collection and model performance. These challenges emphasized the importance of balancing computational efficiency and model accuracy in constrained environments.

Future work on similar projects could focus on improving data quality by incorporating higher-resolution cameras and more diverse datasets. Additionally, exploring alternative hardware platforms with enhanced processing power and memory could enable the deployment of more complex models. Further optimization of the training pipeline and continued refinement of transfer learning techniques could also lead to better performance and wider applications for AI in low-power scenarios.
