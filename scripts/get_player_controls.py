import bge
import mathutils
from get_steering import get_steering
from get_direction import get_direction
from get_keys import get_keys

class get_player_controls():
    def __init__(self, object):
        
        self.controlled_object = object
        self.steering = get_steering()
        self.direction = get_direction(self.controlled_object.head.mesh)
        
        self.scene = bge.logic.getCurrentScene()
        self.camera = self.scene.active_camera
        
        self.camera.setParent(object.head.mesh)
        
        self.keys = get_keys()
        
        self.orders = {
            "body_direction":None,
            "head_direction":mathutils.Vector(),
            "up_down":0,
            "speed":0.0,
            "fire":0,
            "alt":0
        }
        
    def update(self):
        self.orders["body_direction"], self.orders["speed"] = self.steering.get_free_direction_vector_value()
        self.orders["head_direction"] = self.direction.get_fps_direction(self.controlled_object.up)
        self.orders["fire"] = self.keys.get("fire")
        return self.orders
