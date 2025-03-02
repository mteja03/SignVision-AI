# SignVision-AI: Sign Language Detection System
SignVision is an AI-powered sign language detection system that enables users to identify sign language alphabets in real-time using a webcam or by uploading images. It leverages deep learning and computer vision to recognize hand gestures, making communication more accessible for individuals who rely on sign language.

# Convolutional Neural Network
SignVision AI utilizes a Convolutional Neural Network (CNN) to accurately recognize sign language alphabets from images and real-time webcam inputs. The CNN processes hand gestures through multiple layers, including convolution, activation (ReLU), pooling, and fully connected layers, to extract meaningful features like shapes, edges, and textures. This deep learning model enables high-precision classification, ensuring fast and reliable sign language detection. By leveraging AI-powered vision, SignVision AI enhances accessibility and communication for individuals using sign language.

<img width="684" alt="Screenshot 2025-03-01 at 11 43 41 pm" src="https://github.com/user-attachments/assets/05bd3362-f396-4c50-8db4-87dc9f51866e" />

# Model Loss and Accuracy
The accuracy and loss curves of SignVision AI’s CNN model demonstrate its strong learning capability. The training and testing accuracy consistently improve, reaching above 95%, indicating high reliability in sign language recognition. The loss function decreases steadily, showing effective learning and minimal overfitting. These results highlight the model’s robust performance, ensuring accurate and efficient real-time sign language detection.

<img width="697" alt="Screenshot 2025-03-01 at 11 45 40 pm" src="https://github.com/user-attachments/assets/909248ec-16f0-4325-a75c-c9d81cab70cc" />

# Accuracy Analysis Using Confusion Matrix
The confusion matrix provides a detailed breakdown of SignVision AI’s classification performance, showcasing how well the model distinguishes between different sign language alphabets. High true positive rates indicate strong accuracy, while minimal misclassifications confirm the model's reliability. By analyzing misclassified gestures, the system can be further optimized, ensuring precise and consistent sign recognition for real-world applications.

<img width="410" alt="Screenshot 2025-03-01 at 11 46 48 pm" src="https://github.com/user-attachments/assets/d5a23dc0-0719-4706-a623-ba7c81fc1b38" />

# System Design
The SignVision AI system follows a client-server architecture, integrating a Django-based backend with a responsive web frontend. Users interact via a website, which sends requests to the backend where the Python-based AI modelprocesses images and predicts sign language gestures. The system efficiently handles requests, returning real-time sign language recognition results, ensuring a seamless, accurate, and accessible user experience.

<img width="673" alt="Screenshot 2025-03-01 at 11 47 24 pm" src="https://github.com/user-attachments/assets/4f035681-816d-4fee-83a2-4a13036c8698" />

# Data Flow Diagrams
The Data Flow Diagram (DFD) of SignVision AI outlines the journey from image acquisition to sign language recognition. The system starts by preprocessing images, performing data normalization and feature extraction, and storing the processed dataset. The CNN model is trained, validated, and saved, enabling sign detection through image upload or webcam capture. The trained model is integrated with Django, where predictions are processed and displayed on the website in real-time. This structured data flow ensures efficient, accurate, and scalable sign language recognition.

<img width="163" alt="Screenshot 2025-03-01 at 11 58 17 pm" src="https://github.com/user-attachments/assets/c7c738b3-42ea-4673-8f03-e2513e3cb2cb" />

# Home Page

The Home Page serves as the entry point, allowing users to choose between image upload or webcam-based real-time recognition. The interface is clean and user-friendly, with a blue-themed UI for a modern and accessible experience.

<img width="1438" alt="Screenshot 2025-03-01 at 11 53 27 PM" src="https://github.com/user-attachments/assets/5dfea693-78b6-4333-a0c0-8b628c85ba2a" />

# Upload Page
The Upload Page allows users to upload an image containing a sign language gesture. Once uploaded, the system processes the image using a CNN-based deep learning model and predicts the corresponding sign.

<img width="1438" alt="Screenshot 2025-03-01 at 11 53 57 PM" src="https://github.com/user-attachments/assets/e548ce3f-43bb-4dce-aac2-6eaf2130a19f" /> <img width="1438" alt="Screenshot 2025-03-01 at 11 54 10 PM" src="https://github.com/user-attachments/assets/19696d5d-617c-4bd3-994b-a0166c0aa539" />

# Real-Time Webcam Detection Page
The Webcam Page enables real-time sign language recognition through a live video feed. The system detects hand gestures, processes them using computer vision (OpenCV) and deep learning (CNNs), and displays the predicted sign. The green bounding box highlights the detected gesture, ensuring accurate sign classification.

<img width="1438" alt="Screenshot 2025-03-01 at 11 55 46 PM" src="https://github.com/user-attachments/assets/c291f53e-9c7d-43d2-968a-0b32fddfab2a" />

## Installation
Create virtual environment
```bash
python3.9 -m venv myenv
myenv\bin\activate
```
Installing dependencies
```bash
pip install -r requirements.txt
```
Running the django server
```bash
python manage.py runserver
```
Link to access the website 
```sh
127.0.0.1:8000/
```












