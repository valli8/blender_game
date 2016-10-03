from bge import logic
from mathutils import Vector

GRAVITY = 9.8

def main():
    
    cont = logic.getCurrentController()
    own = cont.owner
    collision = own.sensors["Collision"]
    #print(collision.hitObjectList)
    
    invert = False
    
    for obj in collision.hitObjectList:
        #print(obj)
        if "player" in obj:
            
            
            if own["direction"] == "up":
                up_vec = Vector((0,0,-1))
                down_vec = up_vec * -1
            elif own["direction"] == "down":
                up_vec = Vector((0,0,1))
                down_vec = up_vec * -1
            elif own["direction"] == "to_x":
                target_pos = own.worldPosition.copy()
                target_pos[0] = obj.worldPosition.copy()[0]
                threetup = obj.getVectTo(target_pos)
                down_vec = threetup[1]
                up_vec = down_vec * -1
            
            # set vector length
            down_vec.magnitude = GRAVITY
            obj_velocity = obj.getLinearVelocity()
            down_velocity = obj_velocity.project(down_vec)
            
            if invert == True:
                down_velocity = down_velocity * -1
                down_vec = down_vec *-1
                up_vec = up_vec * -1

            if down_velocity.magnitude < GRAVITY: #if object is falling slower
                obj.applyForce(down_vec*obj.mass)
            elif down_vec.angle(down_velocity) > 1.5708: #if object is moving up
                obj.applyForce(down_vec*obj.mass)
            #print(down_velocity,down_vec.angle(down_velocity))
            obj["player"].up = up_vec.normalized()
                
main()
