from domotic.simulators.base_object import BaseObject

class Light(BaseObject):
     def __init__(self):
        super().__init__()
        self.key = 'light_status'