import bge
import mathutils

class hoover():
    def __init__(self):
        self.distance = 4
        self.gravity = 9.8
        
        
    def update(self, up, collision):
        obj, point, normal = collision.rayCast(up * -1)
        distance_to_ground = collision.getDistanceTo(point)
        
        #print(collision.getLinearVelocity())
        if distance_to_ground < self.distance: # lower
            
            distance_difference = self.distance - distance_to_ground# + self.gravity
            
            currect_force = collision.getLinearVelocity()
            current_down_force = currect_force.project(up * -1)
            
            up.magnitude = (distance_difference+self.gravity)
            
            collision.applyForce(current_down_force*-1, False)

class head():
    def __init__(self):
        scene = bge.logic.getCurrentScene()
        self.mesh = scene.addObject("head")
        
    def update(self, game_object, orders):
        self.mesh.worldOrientation = orders["head_direction"]
        self.mesh.worldPosition = game_object.worldPosition

class fire():
    def __init__(self):
        self.cooldown = 0
        
    def update(self, game_object, orders):
        
        if self.cooldown > 100:
            if orders["fire"] != 0:
                self.cooldown = 0
                force = orders["head_direction"]*game_object.mass*10000.0
                game_object.setLinearVelocity(mathutils.Vector([0,0,0]),False)
                game_object.applyForce(force.col[1], False)
        else:
            self.cooldown+=1
            
            
class car():
    def __init__(self, worldPosition):
        self.scene = bge.logic.getCurrentScene()
        
        # add collision mesh
        self.collision = self.scene.addObject("ship_collision")
        self.collision.worldPosition = worldPosition
        
        # add visible mesh
        self.visible = self.scene.addObject("ship")
        self.visible.worldPosition = worldPosition

        self.hp = 100
        self.speed = 20
        self.max_speed = 40
        #self.energy = 100

        self.up = mathutils.Vector((0,0,1))
        
        self.head = head()
        self.fire = fire()
        
        self.hoover = hoover()
        
        ''' All propperties of this class are not available from the collision mesh.
            hit_object.hp -= 10 won't work.
            You have to use this property:
            hit_object["player"].hp -= 10 '''
        self.collision["player"] = self
        
    def update(self, orders):
        self.move(orders)
        self.head.update(self.collision, orders)
        self.fire.update(self.collision, orders)
        #self.hoover.update(self.up, self.collision)
        
    def move(self, orders):
        #direction_vec, input_speed = self.steering.get_fps_direction_vector_value()
        self.visible.worldTransform = self.collision.worldTransform
                
        if orders["speed"] > 0:
            # rotate direction vector by head matrix. (local -> world)
            
            #print("1",orders["body_direction"])
            orders["body_direction"].rotate(self.head.mesh.worldTransform)
            #print("2",orders["body_direction"])
            
            direction_velocity = self.collision.getLinearVelocity().copy().project(orders["body_direction"])
            
            #if orders["body_direction"].angle(self.collision.getLinearVelocity()) > 0.785398:
            #    self.collision.applyForce(orders["body_direction"]*orders["speed"]*self.speed,False)
            
            speed_diff =  self.max_speed - direction_velocity.magnitude
            #print(direction_velocity.magnitude,speed_diff)
            if speed_diff > self.speed:
                self.collision.applyForce(orders["body_direction"]*orders["speed"]*self.speed*self.collision.mass,False)
            elif speed_diff > 0:
                self.collision.applyForce(orders["body_direction"]*orders["speed"]*speed_diff*self.collision.mass,False)
            elif speed_diff < self.speed:
                self.collision.applyForce(orders["body_direction"]*orders["speed"]*self.speed*-self.collision.mass,False)
            elif speed_diff < 0:
                self.collision.applyForce(orders["body_direction"]*orders["speed"]*speed_diff*-self.collision.mass,False)
        

        
        rotation_y = self.collision.worldOrientation.col[1].rotation_difference(self.head.mesh.worldOrientation.col[1]).to_axis_angle()
        rotation_z = self.collision.worldOrientation.col[2].rotation_difference(self.head.mesh.worldOrientation.col[2]).to_axis_angle()
