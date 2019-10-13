from cloudoWindow import CloudoWindow
from forecaster import Forecaster

class Cloudo:
    def __init__(self):
        self.forecaster = Forecaster()
        self.window = CloudoWindow(self.forecaster.get_weather)
