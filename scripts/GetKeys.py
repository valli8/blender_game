import bge


class GetKeys():
    def __init__(self):
        self.keys = {
            "fwd": bge.events.WKEY,
            "bwd": bge.events.SKEY,
            "down": bge.events.LEFTSHIFTKEY,
            "up": bge.events.SPACEKEY,
            "rollleft": bge.events.QKEY,
            "rollright": bge.events.EKEY,
            "left": bge.events.AKEY,
            "right": bge.events.DKEY,
            "use": bge.events.UKEY,
            "boost": bge.events.LEFTCTRLKEY,
            "die": bge.events.DELKEY,
            "type": bge.events.XKEY,
            "zero": bge.events.ZEROKEY,
            "one": bge.events.ONEKEY,
            "two": bge.events.TWOKEY,
            "three": bge.events.THREEKEY,
            "four": bge.events.FOURKEY,
            "five": bge.events.FIVEKEY,
            "six": bge.events.SIXKEY,
            "seven": bge.events.SEVENKEY,
            "eight": bge.events.EIGHTKEY,
            "nine": bge.events.NINEKEY,
            "fire": bge.events.LEFTMOUSE,
            "altfire": bge.events.RIGHTMOUSE,
            "zoompos": bge.events.WHEELUPMOUSE,
            "zoomneg": bge.events.WHEELDOWNMOUSE
        }

        self.last_frame = bge.logic.getFrameTime()

    def get(self, command):  # from wasd
        if self.last_frame != bge.logic.getFrameTime():
            self.last_frame = bge.logic.getFrameTime()
            self.keyevents = bge.logic.keyboard.events  # this is deprecated
            self.mouseevents = bge.logic.mouse.events  # this is deprecated
            #self.keyevents = bge.logic.keyboard.inputs
            #self.mouseevents = bge.logic.mouse.inputs

        if self.keys[command] in self.keyevents:
            return self.keyevents[self.keys[command]]
        elif self.keys[command] in self.mouseevents:
            return self.mouseevents[self.keys[command]]
