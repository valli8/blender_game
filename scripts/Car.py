'''
This module contains all classes for the car object
'''
# pylint: disable=import-error

import bge
import mathutils


class Head(object):
    '''The head object is used for two things:
        - Attach the camera to.
        - Get relative movement.'''
    def __init__(self):
        scene = bge.logic.getCurrentScene()
        self.mesh = scene.addObject("head")

    def update(self, game_object, orders):
        '''update ever tic.'''
        self.mesh.worldOrientation = orders["head_direction"]
        self.mesh.worldPosition = game_object.worldPosition


class Fire(object):
    '''Do some action when fire is activated.'''
    def __init__(self):
        self.cooldown = 0

    def update(self, game_object, orders):
        '''update every tic'''
        if self.cooldown > 100:
            if orders["fire"] != 0:
                self.cooldown = 0
                force = orders["head_direction"] * game_object.mass * 10000.0
                game_object.setLinearVelocity(mathutils.Vector([0, 0, 0]),
                                              False)
                game_object.applyForce(force.col[1], False)
        else:
            self.cooldown += 1


class Car(object):
    '''car funktionality'''
    # pylint: disable=too-many-instance-attributes
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

        self.head = Head()
        self.fire = Fire()

        ''' All propperties of this class are not
            available from the collision mesh.
            hit_object.hp -= 10 won't work.
            You have to use this property:
            hit_object["player"].hp -= 10 '''
        self.collision["player"] = self

    def update(self, orders):
        '''uptade on every tic.'''
        self.__move(orders)
        self.head.update(self.collision, orders)
        self.fire.update(self.collision, orders)

    def __move(self, orders):
        '''movement.'''
        self.visible.worldTransform = self.collision.worldTransform

        if orders["speed"] > 0:
            # rotate direction vector by head matrix. (local -> world)
            orders["body_direction"].rotate(self.head.mesh.worldTransform)

            direction_velocity = self.collision.getLinearVelocity().\
            copy().project(orders["body_direction"])

            speed_diff = self.max_speed - direction_velocity.magnitude
            if speed_diff > self.speed:
                self.collision.applyForce(orders["body_direction"] *
                                          orders["speed"] * self.speed *
                                          self.collision.mass, False)
            elif speed_diff > 0:
                self.collision.applyForce(orders["body_direction"] *
                                          orders["speed"] * speed_diff *
                                          self.collision.mass, False)
            elif speed_diff < self.speed:
                self.collision.applyForce(orders["body_direction"] *
                                          orders["speed"] * self.speed *
                                          -self.collision.mass, False)
            elif speed_diff < 0:
                self.collision.applyForce(orders["body_direction"] *
                                          orders["speed"] * speed_diff *
                                          -self.collision.mass, False)
