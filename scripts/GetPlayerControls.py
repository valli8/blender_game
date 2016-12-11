import mathutils
from scripts.GetSteering import GetSteering
from scripts.GetDirection import GetDirection
from scripts.GetKeys import GetKeys


class GetPlayerControls():
    def __init__(self):
        self.steering = GetSteering()
        self.direction = GetDirection()
        self.keys = GetKeys()

        self.orders = {
            "body_direction": None,
            "head_direction": mathutils.Vector(),
            "up_down": 0,
            "speed": 0.0,
            "fire": 0,
            "alt": 0
        }

    def update(self, up=mathutils.Vector((0, 0, 1))):
        self.orders["body_direction"], self.orders["speed"] = \
            self.steering.get_free_direction_vector_value()
        #self.orders["head_direction"] = \
        #    self.direction.get_free_direction()
        self.orders["head_direction"] = \
            self.direction.get_fps_direction(up)
        self.orders["fire"] = self.keys.get("fire")
        return self.orders
