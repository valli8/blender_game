import mathutils
from scripts.get_steering import get_steering
from scripts.get_direction import get_direction
from scripts.get_keys import get_keys


class get_player_controls():
    def __init__(self):
        self.steering = get_steering()
        self.direction = get_direction()
        self.keys = get_keys()

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
