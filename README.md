🚗 Parking Occupancy Classification System
<p align="center"> <img src="https://img.shields.io/badge/AI-Powered-0A192F?style=for-the-badge&logo=openai&logoColor=white"/> <img src="https://img.shields.io/badge/YOLOv8-Object%20Detection-2563EB?style=for-the-badge"/> <img src="https://img.shields.io/badge/Streamlit-Live%20Deployment-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/> <img src="https://img.shields.io/badge/Python-3.10-F7DF1E?style=for-the-badge&logo=python&logoColor=black"/> </p> <p align="center"> <img src="https://readme-typing-svg.herokuapp.com?font=Poppins&size=26&duration=2800&pause=800&color=0EA5E9&center=true&vCenter=true&width=700&lines=Smart+Parking+Detection+System;Deep+Learning+Powered+Slot+Classification;Real-Time+Occupancy+Prediction+App" /> </p>
🌍 Live Application
<p align="center"> <a href="https://parking-occupancy-classification-kjlrkgzhpvhuctiqhwecpe.streamlit.app/"> <img src="https://img.shields.io/badge/Launch-App-22C55E?style=for-the-badge&logo=google-chrome&logoColor=white"/> </a> </p>

🔗 Direct Link:
https://parking-occupancy-classification-kjlrkgzhpvhuctiqhwecpe.streamlit.app/

📖 Overview

The Parking Occupancy Classification System is a deep learning–based web application that detects whether a parking slot is:

🟢 Empty

🔴 Occupied

The system leverages the YOLOv8 object detection model to analyze uploaded parking images and classify slot occupancy with high accuracy.

Deployed on Streamlit Cloud, the application provides a fast and interactive web interface for real-time parking slot validation.

🎯 Problem Statement

Manual monitoring of parking spaces is inefficient and error-prone.
This system automates parking slot detection using AI, improving:

🚦 Traffic flow

🅿 Parking management

⏱ Time efficiency

📊 Smart infrastructure readiness

🧠 System Architecture
User Upload
     ↓
Image Preprocessing (OpenCV)
     ↓
YOLOv8 Model Inference
     ↓
Classification Output
     ↓
Confidence Score Display
     ↓
Streamlit UI Rendering
🛠 Tech Stack
Layer	Technology Used
Language	Python
Deep Learning	YOLOv8 (Ultralytics)
Image Processing	OpenCV
UI Framework	Streamlit
Deployment	Streamlit Cloud
Version Control	Git + GitHub
📂 Project Structure
parking_occupancy_system
│
├── model/
│   └── best.pt
│
├── test_images/
│
├── app.py
├── predict.py
├── requirements.txt
└── runtime.txt
⚙️ Local Setup Guide
1️⃣ Clone Repository
git clone https://github.com/alinashaji-12/parking-occupancy-classification.git
cd parking-occupancy-classification
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Application
streamlit run app.py
✨ Core Features

✔ AI-based occupancy classification
✔ Confidence score reporting
✔ Modern responsive UI
✔ Cloud deployment
✔ Lightweight and efficient pipeline

📊 Model Details

Model: YOLOv8

Framework: Ultralytics

Training Platform: Google Colab

Annotation Tool: Roboflow

Dataset: Custom parking slot dataset


⭐ Acknowledgement

This project was developed as part of an academic deep learning application focusing on real-world smart infrastructure automation.
