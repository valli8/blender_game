import bge

class get_mouse_move():
    
    def __init__(self):
        self.wPixelsDimensions = (bge.render.getWindowWidth(), bge.render.getWindowHeight())
        self.wPixelsCenter = (int(self.wPixelsDimensions[0] / 2), int(self.wPixelsDimensions[1] / 2))
        self.wPercentCenter = (self.wPixelsCenter[0] / (self.wPixelsDimensions[0] / 100) / 100, self.wPixelsCenter[1] / (self.wPixelsDimensions[1] / 100) / 100)
    
    def update(self):
        mouseevents = bge.logic.mouse.events
        wPercentActual = bge.logic.mouse.position
        y_rot = self.wPercentCenter[1] - wPercentActual[1]# * self.sensitivity
        x_rot = self.wPercentCenter[0] - wPercentActual[0]# * self.sensitivity
        
        # reset mouse
        bge.logic.mouse.position=(0.5,0.5)
        
        return x_rot, y_rot
