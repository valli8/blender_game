import bge


class GetMouseMove():

    def __init__(self):
        self.wPixelsDimensions = \
        (bge.render.getWindowWidth(), bge.render.getWindowHeight())
        self.wPixelsCenter = \
        (int(self.wPixelsDimensions[0] / 2), int(self.wPixelsDimensions[1] / 2))
        self.wPercentCenter = \
        (self.wPixelsCenter[0] / (self.wPixelsDimensions[0] / 100) / 100,
            self.wPixelsCenter[1] / (self.wPixelsDimensions[1] / 100) / 100)

    def update(self):
        wPercentActual = bge.logic.mouse.position
        y_rot = self.wPercentCenter[1] - wPercentActual[1]
        x_rot = self.wPercentCenter[0] - wPercentActual[0]

        # reset mouse
        bge.logic.mouse.position = (0.5, 0.5)

        return x_rot, y_rot
