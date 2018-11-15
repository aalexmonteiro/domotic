from domotic.simulators.base_object import BaseObject

class AudioVideoBase(BaseObject):
    def __init__(self):
        self.list = {}
        self.current = 0
        self.max = len(self.list)
        super().__init__()
    
    def next(self):
        if self.current == self.max - 1:
            self.current = 0
            return

        self.current += 1
    
    def previous(self):
        if self.current == 0:
            self.current = self.max - 1
            return

        self.current -= 1
    
    def get_current(self):
        return self.list[self.current]
        