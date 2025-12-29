# 🎸 Air Guitar Project

## About the Project
This project is called **Air Guitar**.  
The idea behind this project is simple — to play guitar sounds using **hand gestures** instead of a real guitar.

Using a webcam, the system detects hand movements in real time and plays guitar sounds based on finger positions.  
No physical instrument is required. Everything works through computer vision.

I built this project to understand how **OpenCV**, **hand tracking**, and **real-time video processing** work together in a practical way.

---

## Why I Made This Project
I wanted to try something fun while learning computer vision.  
Instead of doing a basic project, I chose Air Guitar because it combines:
- real-time processing  
- gesture recognition  
- sound generation  

This project helped me understand how humans can interact with computers using gestures.

---

## Technologies Used
- Python  
- OpenCV  
- MediaPipe  
- NumPy  
- Pygame  

---

## How the Project Works
1. The webcam captures live video  
2. Hand landmarks are detected using MediaPipe  
3. Finger positions are tracked  
4. Based on the gesture, guitar sounds are played  

Everything happens in real time.

---

## How to Run the Project
Make sure Python is installed on your system.

```bash
pip install -r requirements.txt
python air_guitar.py
