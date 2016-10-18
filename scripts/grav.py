from bge import logic
from mathutils import Vector

GRAVITY = 9.8


def main():

    cont = logic.getCurrentController()
    own = cont.owner
    collision = own.sensors["Collision"]

    invert = False

    for obj in collision.hitObjectList:
        #print(obj)
        if "player" in obj:

            if own["direction"] == "up":
                up_vec = Vector((0, 0, -1))
                down_vec = up_vec * -1
            elif own["direction"] == "down":
                up_vec = Vector((0, 0, 1))
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

            if invert:
                down_velocity = down_velocity * -1
                down_vec = down_vec * -1
                up_vec = up_vec * -1

            # if object is falling slower
            if down_velocity.magnitude < GRAVITY:
                obj.applyForce(down_vec * obj.mass)
            # if object is moving up
            elif down_vec.angle(down_velocity) > 1.5708:
                obj.applyForce(down_vec * obj.mass)
            #print(down_velocity,down_vec.angle(down_velocity))
            obj["player"].up = up_vec.normalized()

main()
