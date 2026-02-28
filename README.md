🚗 Parking Occupancy Classification System
<p align="center"> <img src="https://img.shields.io/badge/YOLOv8-Object%20Detection-blue?style=for-the-badge&logo=python"> <img src="https://img.shields.io/badge/Streamlit-Live%20App-red?style=for-the-badge&logo=streamlit"> <img src="https://img.shields.io/badge/Python-3.10-yellow?style=for-the-badge&logo=python"> </p> <p align="center"> <img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=25&duration=3000&pause=1000&color=00C2FF&center=true&vCenter=true&width=600&lines=AI+Powered+Parking+Detection;YOLOv8+Based+Classifier;Real-Time+Slot+Occupancy+Prediction" /> </p>
🚀 Live Deployment

👉 Try the App Here:
🔗 https://parking-occupancy-classification-kjlrkgzhpvhuctiqhwecpe.streamlit.app/

📌 Project Overview

This project is an AI-powered web application that classifies parking slots as:

✅ Empty

🚫 Occupied

The system uses YOLOv8 deep learning model for image-based parking slot detection and is deployed using Streamlit Cloud for interactive usage.

🧠 How It Works

Upload a parking slot image

YOLOv8 model processes the image

The system predicts:

Parking Status

Confidence Score

Result is displayed with a clean Streamlit UI

🛠️ Tech Stack
Technology	Purpose
🐍 Python	Core programming
🧠 YOLOv8 (Ultralytics)	Object detection model
🎨 Streamlit	Web UI framework
📷 OpenCV	Image processing
☁️ Streamlit Cloud	Deployment
📂 Project Structure
parking_occupancy_system/
│
├── model/
│   └── best.pt
├── test_images/
├── app.py
├── predict.py
├── requirements.txt
└── runtime.txt
⚙️ Installation (Local Setup)
git clone https://github.com/alinashaji-12/parking-occupancy-classification.git
cd parking-occupancy-classification
pip install -r requirements.txt
streamlit run app.py
📊 Features

✔ Modern interactive UI
✔ Real-time prediction
✔ Confidence score display
✔ Cloud deployed
✔ Lightweight & fast

👩‍💻 Contributors

Alina Shaji

Hannah

Aman Hooda

Rishabh

📈 Future Improvements

Multi-slot detection

Real-time camera feed support

Parking analytics dashboard

⭐ If you found this project helpful

Give it a ⭐ on GitHub!

✨ AI Meets Smart Parking ✨
