from krita import DockWidget
from .potterScript import WheelControlPanel

DOCKER_TITLE = 'Pottery Wheel'

class PotteryDocker(DockWidget):

    def __init__(self):
        super().__init__()

        self.wheelControlPanelInstance = WheelControlPanel()

        self.setWindowTitle(DOCKER_TITLE)
        
        self.setWidget(self.wheelControlPanelInstance.widget)

    # notifies when views are added or removed
    # 'pass' means do not do anything
    def canvasChanged(self, canvas):
        # if (canvas != None):
        self.wheelControlPanelInstance.initializeWheelUsing(canvas)
        self.setWidget(self.wheelControlPanelInstance.widget)


