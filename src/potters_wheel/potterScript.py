from krita import *
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QPushButton

class WheelControlPanel:
    def __init__(self):
        controlsContainer = returnWidget()
        self.widget = controlsContainer

    def initializeCanvasTo(self, canvas):
        self.canvas = canvas
          
def returnWidget():
    mainBox = QGroupBox() #put box inside docker when ported to docker
    layoutForButtons = QHBoxLayout()

    #Add slider for speed changing
    speedSlider = QSlider(Qt.Horizontal)
    speedSlider.setMinimum(1)
    speedSlider.setMaximum(100)
    speedSlider.setTickPosition(QSlider.TicksBelow)
    speedSlider.setTickInterval(5)
    speedSlider.setValue(10)
    speedSlider.valueChanged.connect(myFunc)


    layoutForButtons.addWidget(speedSlider)

    # add button and layout for button
    newStartButton = QPushButton("Start") 
    layoutForButtons.addWidget(newStartButton)

    newStopButton = QPushButton("Stop") 
    layoutForButtons.addWidget(newStopButton)

    # hook up the buttons 
    newStartButton.clicked.connect(start_timer)
    newStopButton.clicked.connect(stop_timer)

    # create dialog  and show it
    newDialog = QDialog() 
    newDialog.setLayout(layoutForButtons)
    newDialog.setWindowTitle("New Dialog Title!") 

    mainBox.setLayout(layoutForButtons)

    return mainBox

def showDialog():
    newDialog.show() # show the dialog


canvas = Krita.instance().activeWindow().activeView().canvas()

curRotation = 0
rotationSize = 1

def on_timer_timeout():
    global curRotation  # Declare 'curRotation' as a global variable
    curRotation = curRotation + rotationSize
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

def myFunc(newSize):
    global rotationSize

    rotationSize = newSize / 10
    