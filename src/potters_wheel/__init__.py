from krita import DockWidgetFactory, DockWidgetFactoryBase
from .potterydocker import PotteryDocker

DOCKER_ID = 'potters_wheel'
instance = Krita.instance()
dock_widget_factory = DockWidgetFactory(DOCKER_ID,
                                        DockWidgetFactoryBase.DockRight,
                                        PotteryDocker)

instance.addDockWidgetFactory(dock_widget_factory)