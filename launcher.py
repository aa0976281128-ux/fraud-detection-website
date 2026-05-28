#!/usr/bin/env python3
import subprocess
import sys
import os
import webbrowser
import time

print("\n" + "="*60)
print("  Fraud Detection Website Launcher")
print("="*60 + "\n")

# Check if requirements.txt exists
if not os.path.exists('requirements.txt'):
    print("ERROR: requirements.txt not found!")
    print("Please make sure you are in the correct directory:")
    print(os.getcwd())
    print("\nPress Enter to exit...")
    input()
    sys.exit(1)

print("Installing dependencies...")
print("This may take 2-3 minutes...\n")

try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
except subprocess.CalledProcessError:
    print("\nERROR: Failed to install dependencies!")
    print("Please make sure Python and pip are installed correctly.")
    print("\nPress Enter to exit...")
    input()
    sys.exit(1)

print("\n" + "="*60)
print("  Installation Complete!")
print("="*60)
print("\nStarting website...\n")
print("Website URL: http://localhost:5000")
print("\nOpening browser in 3 seconds...")
print("\nPress CTRL+C to stop the website\n")

time.sleep(3)

try:
    webbrowser.open('http://localhost:5000')
except:
    pass

try:
    subprocess.call([sys.executable, "app.py"])
except KeyboardInterrupt:
    print("\n\nWebsite stopped. Goodbye!")
    sys.exit(0)
