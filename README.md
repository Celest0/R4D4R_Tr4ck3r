# R4D4R_Tr4ck3r
📡 Project: Real-Time Radar Target Tracking Simulator

What this is:
A radar simulation + Kalman-filter tracker with a minimal basic web frontend showing live target tracking, using simulated Data.

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

Install dependencies
pip install -r requirements.txt

💻 Running in PyCharm or VS:
Run from app.py and click the output link from the terminal. 

 * Running on http://127.0.0.1:5000


 style this readmeusing coloradcmds
