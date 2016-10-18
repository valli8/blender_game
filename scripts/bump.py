import bge


class bump():
    def __init__(self, owner):
        self.collision = owner
        self.collision.setDamping(0.0, 0.0)
        self.normal_scale = self.collision.localScale.copy()
        self.state = None
        self.last_collided = None
        self.cooldown = 0

    def bump(self):
        if self.cooldown >= 5:
            if self.last_collided is None:
                oblist = bge.logic.getCurrentController().sensors["Collision"].hitObjectList

                for ob in oblist:
                    if "player" in ob.getPropertyNames():
                        self.last_collided = ob
                        print("First collided", self.last_collided.worldLinearVelocity)

            else: # one frame later
                print(("Second collided",self.last_collided.worldLinearVelocity))
                self.last_collided.worldLinearVelocity = self.last_collided.worldLinearVelocity * 4
                print(("Third collided",self.last_collided.worldLinearVelocity))
                self.last_collided = None
                self.cooldown = 0
        else:
            self.cooldown += 1


def main(controller):
    owner = controller.owner

    if not "init" in owner:
        owner["init"] = bump(owner)
    else:
        owner["init"].bump()
