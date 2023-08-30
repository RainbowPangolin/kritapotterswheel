from krita import *
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout

class WheelControlPanel:
    def __init__(self):
        self.initializeWheelUsing(None)

    def initializeCanvasTo(self, canvas):
        self.canvas = canvas
        self.initializeWheelUsing(canvas)
          
    def initializeWheelUsing(self, canvas):
        self.wheelController = PotteryWheelComponent(canvas)
        controlsContainer = self.returnWidget()
        self.widget = controlsContainer

    def returnWidget(self):
        boxForContainers = QGroupBox() #put box inside docker when ported to docker
        boxForButtons = QGroupBox()
        boxForLabels = QGroupBox()
        layoutForContainers = QVBoxLayout()
        layoutForButtons = QHBoxLayout()
        layoutForLabels = QHBoxLayout()

        #Add slider for speed changing
        speedSlider = QSlider(Qt.Horizontal)
        speedSlider.setMinimum(1)
        speedSlider.setMaximum(100)
        speedSlider.setTickPosition(QSlider.TicksBelow)
        speedSlider.setTickInterval(5)
        speedSlider.setValue(10)
        try: speedSlider.valueChanged.disconnect()
        except: pass
        speedSlider.valueChanged.connect(self.wheelController.changeSize)




        label_left = QLabel('Slower')
        label_right = QLabel('Faster')
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        layoutForLabels.addWidget(label_left)
        layoutForLabels.addItem(spacer)
        layoutForLabels.addWidget(label_right)
        boxForLabels.setLayout(layoutForLabels)

        # add button and layout for button
        self.startButton = QPushButton("Start") 
        self.stopButton = QPushButton("Stop") 
        layoutForButtons.addWidget(self.startButton)
        layoutForButtons.addWidget(self.stopButton)
        boxForButtons.setLayout(layoutForButtons)

        # hook up the buttons 

        try:
            # Disconnect the previous connection (if one exists)
            self.startButton.clicked.disconnect()
            self.stopButton.clicked.disconnect()
        except: pass

        self.startButton.clicked.connect(self.wheelController.start_timer)
        self.stopButton.clicked.connect(self.wheelController.stop_timer)

        layoutForContainers.addWidget(boxForButtons)
        layoutForContainers.addWidget(speedSlider)
        layoutForContainers.addWidget(boxForLabels)
        
        
        reverseRotationButton = QPushButton("Reverse Rotation")
        reverseRotationButton.clicked.connect(self.wheelController.reverseRotation)
        layoutForContainers.addWidget(reverseRotationButton)

        boxForContainers.setLayout(layoutForContainers)

        return boxForContainers



class PotteryWheelComponent():
    def __init__(self, canvas):
        self.canvas = canvas
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timer_timeout)
        self.curRotation = 0
        self.rotationSize = 1
        self.rotationInterval = 10
        self.direction = 1

    def on_timer_timeout(self):
        self.curRotation = self.curRotation + (self.direction * self.rotationSize) # direction is -1 or 1
        self.canvas.setRotation(self.curRotation)
        
    def start_timer(self):
        self.timer.start(self.rotationInterval)

    def stop_timer(self):
        self.timer.stop()   # Stop the timer
        self.canvas.setRotation(0) # Reset orientation

    def changeSize(self, newSize):
        self.rotationSize = newSize / 10

    def reverseRotation(self):
        self.direction = self.direction * -1
    
    def changeTimerInterval(self, interval):
        self.stop_timer()
        self.rotationInterval = interval / 10
        self.start_timer()

