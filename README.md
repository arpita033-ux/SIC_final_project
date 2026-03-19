# 🏥 IoT-Based Remote Health Outpost Monitor
### 📊 Outpatient Queue Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![IoT](https://img.shields.io/badge/Domain-IoT-green)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi-red?logo=raspberrypi)

---

## 📌 Overview
This project presents an **IoT-based system** designed to monitor outpatient queues in healthcare centers, especially in rural and remote areas.

The system uses sensors and a Raspberry Pi to track patient flow, estimate waiting time, and display real-time updates through a web dashboard. It also logs data to Google Sheets for analysis.

---

## ❗ Problem Statement
Outpatient healthcare facilities often rely on manual methods to manage patient queues, leading to:
- Confusion in patient handling  
- Long waiting times  
- Inefficient service management  

This project provides a **low-cost automated solution** to monitor patient flow efficiently.

---

## 🎯 Objectives
- Monitor outpatient queues using IoT  
- Detect patient arrivals using sensors  
- Estimate waiting time dynamically  
- Display real-time data via a web dashboard  
- Store data in the cloud (Google Sheets)  
- Demonstrate IoT in healthcare applications  

---

## 🛠️ Technologies Used

### 🔌 Hardware
- Raspberry Pi  
- Ultrasonic Sensor (HC-SR04)  
- Touch Sensor  
- Jumper Wires  

### 💻 Software
- Python  
- Flask (Web Dashboard)  
- Chart.js (Visualization)  
- Google Sheets API  
- gspread (Python Library)  

### ⚙️ Tools
- Raspberry Pi OS  
- Google Cloud Console  
- GitHub  

---

## 🧠 System Architecture
- Ultrasonic sensor detects patient arrival  
- Touch sensor simulates doctor calling the next patient  
- Raspberry Pi processes sensor data  
- Flask dashboard displays queue status  
- Data is uploaded to Google Sheets for logging and analysis  

---

## 📁 Project Structure

health-monitor-project/
│── monitor.py
│── credentials.json
│── requirements.txt
│── README.md


---

## 🚀 Features
- 📡 Real-time queue monitoring  
- ⏱️ Automatic waiting time estimation  
- 📊 Live dashboard displaying patient data  
- 📈 Graph visualization of queue trends  
- ☁️ Cloud data logging using Google Sheets  

---

## ⚠️ Challenges Faced
- Handling unstable ultrasonic sensor readings  
- Preventing duplicate patient detection  
- Integrating Google Sheets API  
- Designing a responsive real-time dashboard  
- Managing sensor timing and synchronization  

---

## 🔮 Future Improvements
- Camera-based patient detection using computer vision  
- SMS or mobile alerts for long queues  
- Integration with hospital appointment systems  
- Mobile application for remote monitoring  
- AI-based prediction of waiting time  
- Multi-room monitoring for large healthcare facilities  

---

## ▶️ How to Run

# Clone the repository
git clone https://github.com/your-username/health-monitor-project.git

# Navigate into the project
cd health-monitor-project

# Install dependencies
pip install -r requirements.txt

# Run the project
python monitor.py
edgement

Developed as part of the Samsung Innovation Campus Program.
