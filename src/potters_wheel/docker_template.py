from krita import DockWidget
from .potterScript import WheelControlPanel

DOCKER_TITLE = 'Pottery Wheel'

class DockerTemplate(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(DOCKER_TITLE)
        self.setWidget(WheelControlPanel.widget)

    # notifies when views are added or removed
    # 'pass' means do not do anything
    def canvasChanged(self, canvas):
        pass

