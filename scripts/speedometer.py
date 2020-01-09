import bge


class speedometer(bge. types.KX_FontObject):
    def __init__(self, oldobject):
        setattr(bge.logic, self.name, self)
        self.text = "0.00"
        
    def setSpeed(self, value):
        self.text = str(value)


def main(cont):
    speedometer(cont.owner)
