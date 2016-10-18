import bge
import mathutils


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
                force = orders["head_direction"] * game_object.mass * 10000.0
                game_object.setLinearVelocity(mathutils.Vector([0, 0, 0]),
                False)
                game_object.applyForce(force.col[1], False)
        else:
            self.cooldown += 1


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

        self.up = mathutils.Vector((0, 0, 1))

        self.head = head()
        self.fire = fire()

        ''' All propperties of this class are not
            available from the collision mesh.
            hit_object.hp -= 10 won't work.
            You have to use this property:
            hit_object["player"].hp -= 10 '''
        self.collision["player"] = self

    def update(self, orders):
        self.__move(orders)
        self.head.update(self.collision, orders)
        self.fire.update(self.collision, orders)

    def __move(self, orders):
        self.visible.worldTransform = self.collision.worldTransform

        if orders["speed"] > 0:
            # rotate direction vector by head matrix. (local -> world)

            #print("1",orders["body_direction"])
            orders["body_direction"].rotate(self.head.mesh.worldTransform)
            #print("2",orders["body_direction"])

            direction_velocity = self.collision.getLinearVelocity().\
            copy().project(orders["body_direction"])

            speed_diff = self.max_speed - direction_velocity.magnitude
            #print((direction_velocity.magnitude,speed_diff))
            if speed_diff > self.speed:
                self.collision.applyForce(orders["body_direction"] *
                orders["speed"] * self.speed * self.collision.mass, False)
            elif speed_diff > 0:
                self.collision.applyForce(orders["body_direction"] *
                orders["speed"] * speed_diff * self.collision.mass, False)
            elif speed_diff < self.speed:
                self.collision.applyForce(orders["body_direction"] *
                orders["speed"] * self.speed * -self.collision.mass, False)
            elif speed_diff < 0:
                self.collision.applyForce(orders["body_direction"] *
                orders["speed"] * speed_diff * -self.collision.mass, False)
