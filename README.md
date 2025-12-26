from colorama import Fore, Style, init
init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + "# R4D4R_Tr4ck3r")
print(Fore.YELLOW + "📡 Project: Real-Time Radar Target Tracking Simulator\n")

print(Fore.GREEN + "What this is:")
print("A radar simulation + Kalman-filter tracker with a minimal basic web frontend showing live target tracking, using simulated Data.\n")

print(Fore.MAGENTA + "Project Structure:")
print(Fore.CYAN + "radar-tracker/")
print(Fore.CYAN + "├── backend/")
print(Fore.CYAN + "│   ├── " + Fore.YELLOW + "tracker.py       " + Fore.WHITE + "# Updates target and Kalman filter")
print(Fore.CYAN + "│   ├── " + Fore.YELLOW + "kalman.py        " + Fore.WHITE + "# Kalman filter implementation")
print(Fore.CYAN + "│   ├── " + Fore.YELLOW + "simulator.py     " + Fore.WHITE + "# Target simulator with noise")
print(Fore.CYAN + "│   └── " + Fore.YELLOW + "app.py           " + Fore.WHITE + "# Flask backend serving live data")
print(Fore.CYAN + "├── frontend/")
print(Fore.CYAN + "│   └── " + Fore.YELLOW + "index.html       " + Fore.WHITE + "# Web frontend showing measurements & estimates")
print(Fore.CYAN + "├── " + Fore.YELLOW + "requirements.txt     " + Fore.WHITE + "# Python dependencies")
print(Fore.CYAN + "└── " + Fore.YELLOW + "README.md\n")

print(Fore.GREEN + "Install dependencies")
print(Fore.WHITE + "pip install -r requirements.txt\n")

print(Fore.GREEN + "💻 Running in PyCharm or VS:")
print(Fore.WHITE + "Run from app.py and click the output link from the terminal.\n")

print(Fore.GREEN + " * Running on " + Fore.YELLOW + "http://127.0.0.1:5000")
