from krita import *
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QHBoxLayout, QPushButton

class WheelControlPanel:
    def __init__(self):
        self.canvas = None
        self.wheelController = PotteryWheelComponent(None)
        controlsContainer = self.returnWidget()
        self.widget = controlsContainer

    def initializeCanvasTo(self, canvas):
        self.canvas = canvas
        self.initializeWheelUsing(canvas)
          
    def initializeWheelUsing(self, canvas):
        self.wheelController = PotteryWheelComponent(canvas)

    def returnWidget(self):
        mainBox = QGroupBox() #put box inside docker when ported to docker
        layoutForButtons = QHBoxLayout()

        #Add slider for speed changing
        speedSlider = QSlider(Qt.Horizontal)
        speedSlider.setMinimum(1)
        speedSlider.setMaximum(100)
        speedSlider.setTickPosition(QSlider.TicksBelow)
        speedSlider.setTickInterval(5)
        speedSlider.setValue(10)
        speedSlider.valueChanged.connect(self.wheelController.changeSize)


        layoutForButtons.addWidget(speedSlider)

        # add button and layout for button
        newStartButton = QPushButton("Start") 
        layoutForButtons.addWidget(newStartButton)

        newStopButton = QPushButton("Stop") 
        layoutForButtons.addWidget(newStopButton)

        # hook up the buttons 
        newStartButton.clicked.connect(self.wheelController.start_timer)
        newStopButton.clicked.connect(self.wheelController.stop_timer)

        mainBox.setLayout(layoutForButtons)

        return mainBox


class PotteryWheelComponent():
    def __init__(self, canvas):
        self.canvas = canvas
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timer_timeout)
        self.curRotation = 0
        self.rotationSize = 1
        self.rotationInterval = 10

    def on_timer_timeout(self):
        self.curRotation = self.curRotation + self.rotationSize
        self.canvas.setRotation(self.curRotation)
        
    def start_timer(self):
        self.timer.start(self.rotationInterval)

    def stop_timer(self):
        self.timer.stop()   # Stop the timer
        self.canvas.setRotation(0) # Reset orientation

    def changeSize(self, newSize):
        self.rotationSize = newSize / 10
        

