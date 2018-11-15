from domotic.simulators.base_object import BaseObject

class AirConditioner(BaseObject):
    def __init__(self):
        super().__init__()
        self.key='air_status'
        self.temp = 20
    
    def increase(self):
        self.temp += 1
    
    def decrease(self):
        self.temp -= 1