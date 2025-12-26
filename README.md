# 📡 R4D4R_Tr4ck3r
**Project:** Real-Time Radar Target Tracking Simulator

---

## What this is
A radar simulation + Kalman-filter tracker with a minimal basic web frontend showing live target tracking, using simulated Data.

---

## Project Structure

radar-tracker/  
├── backend/  
│   ├── tracker.py       # Updates target and Kalman filter  
│   ├── kalman.py        # Kalman filter implementation  
│   ├── simulator.py     # Target simulator with noise  
│   └── app.py           # Flask backend serving live data  
├── frontend/  
│   └── index.html       # Web frontend showing measurements & estimates  
├── requirements.txt     # Python dependencies  
└── README.md  

---

## Final Result

![Radar Tracking Screenshot](assets/Opera%20Snapshot_2025-12-25_212610_127.0.0.1.png)

## Enjoy!
![Radar Tracking Demo](assets/3dgifmaker76786.gif)









