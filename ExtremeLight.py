import os
import time
import subprocess

def checktheconnectionDV():
    result = subprocess.run(
        ["adb", "devices"],
        stdout=subprocess.PIPE,
        text=True
    )

def checktheapp():
    os.system("adb shell dumpsys package com.positivo.casainteligente | findstr LAUNCHER")
    time.sleep(5)
def main():
    pass

if __name__ == "__main__":
    checktheconnectionDV()


#adb shell dumpsys package com.positivo.casainteligente | findstr LAUNCHER Find the app info