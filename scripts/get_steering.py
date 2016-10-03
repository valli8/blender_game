import get_keys
import mathutils

class get_steering():
    
    def __init__(self):
        self.keys = get_keys.get_keys()
    
    def get_fps_direction_vector_value(self):
        
        vec = mathutils.Vector([0,0,0])
        if ((self.keys.get('left') == 1) or (self.keys.get('left') == 2)):
            vec[0] -= 1
        if ((self.keys.get('right') == 1) or (self.keys.get('right') == 2)):
            vec[0] += 1
        if ((self.keys.get('fwd') == 1) or (self.keys.get('fwd') == 2)):
            vec[1] += 1
        if ((self.keys.get('bwd') == 1) or (self.keys.get('bwd') == 2)):
            vec[1] -= 1
        #if ((self.keys.get('up') == 1) or (self.keys.get('up') == 2)):
        #    vec[2] += 1
        #if ((self.keys.get('down') == 1) or (kself.keys.get('down') == 2)):
        #    vec[2] -= 1
        
        if vec[0] == 0 and vec[1] == 0:
            value = 0.0
            vec[1] = 1
        else:
            value = 1.0
            
        # normalize
        vec.normalize()
        return vec, value
    
    def get_free_direction_vector_value(self):
        
        vec = mathutils.Vector([0,0,0])
        if ((self.keys.get('left') == 1) or (self.keys.get('left') == 2)):
            vec[0] -= 1
        if ((self.keys.get('right') == 1) or (self.keys.get('right') == 2)):
            vec[0] += 1
        if ((self.keys.get('fwd') == 1) or (self.keys.get('fwd') == 2)):
            vec[1] += 1
        if ((self.keys.get('bwd') == 1) or (self.keys.get('bwd') == 2)):
            vec[1] -= 1
        if ((self.keys.get('up') == 1) or (self.keys.get('up') == 2)):
            vec[2] += 1
        if ((self.keys.get('down') == 1) or (self.keys.get('down') == 2)):
            vec[2] -= 1
        
        if vec[0] == 0 and vec[1] == 0 and vec[2] == 0:
            value = 0.0
            vec[1] = 1
        else:
            value = 1.0
            
        # normalize
        vec.normalize()
        return vec, value
