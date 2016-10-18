import bge


class bar(bge. types.KX_GameObject):
    def __init__(self, oldobject):
        setattr(bge.logic, self.name, self)

    def setBar(self, value):
        self["bar"] = value


def main(cont):
    bar(cont.owner)
