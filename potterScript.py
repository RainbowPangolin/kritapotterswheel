from krita import *
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QPushButton

canvas = Krita.instance().activeWindow().activeView().canvas()

curRotation = 0

def on_timer_timeout():
    global curRotation  # Declare 'curRotation' as a global variable
    curRotation = curRotation + 1
    canvas.setRotation(curRotation)
    print("Timer timeout event occurred.")
    
timer = QTimer()

timer.timeout.connect(on_timer_timeout)

# Set the interval in milliseconds (e.g., 10 ms)
interval = 10
    
def start_timer():
    timer.start(interval)
    print('timer started')


def stop_timer():
    timer.stop()   # Stop the timer
    canvas.setRotation(0) #Reset orientation
    print('timer stopped')


mainBox = QGroupBox() #put box inside docker when ported to docker

# add button and layout for button
layoutForButtons = QHBoxLayout()
newStartButton = QPushButton("Start me") 
layoutForButtons.addWidget(newStartButton)

newStopButton = QPushButton("Stop me") 
layoutForButtons.addWidget(newStopButton)

# hook up the buttons 
newStartButton.clicked.connect(start_timer)
newStopButton.clicked.connect(stop_timer)

# create dialog  and show it
newDialog = QDialog() 
newDialog.setLayout(layoutForButtons)
newDialog.setWindowTitle("New Dialog Title!") 
newDialog.show() # show the dialog

