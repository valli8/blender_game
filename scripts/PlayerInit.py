'''
This script has to be attached to a blender object.
Add a alwas-sensor with true level triggering (pulse mode) and add
"scripts.PlayerInit.main"
to a python controller with execution method = module.

'''


import cProfile
import pstats
import io
# pylint: disable=import-error
import bge
from scripts.Car import Car
from scripts.GetPlayerControls import GetPlayerControls


class PlayerInit(object):
    '''This class initializes a new player.'''
    def __init__(self, position):
        self.player = Car(position)
        self.controls = GetPlayerControls()
        if "team1" not in bge.logic.globalDict:
            bge.logic.globalDict['team1'] = []
        bge.logic.globalDict['team1'].append(self.player)

        self.scene = bge.logic.getCurrentScene()
        self.camera = self.scene.active_camera

        self.camera.setParent(self.player.head.mesh)

    def update(self):
        '''Update every tic'''
        orders = self.controls.update(self.player.up)
        self.player.update(orders)

        if hasattr(bge.logic, 'energybar'):
            bge.logic.energybar.setBar(self.player.fire.cooldown)


def main(controller):
    '''main entry point'''
    owner = controller.owner

    profiling = False

    if "init" in owner:
        if profiling:
            bge.logic.pr.enable()
            owner["init"].update()
            bge.logic.pr.disable()
            bge.logic.ps = pstats.Stats(bge.logic.pr, stream=bge.logic.s).\
                sort_stats('tottime')  # or cumulative

            if bge.logic.print_counter >= 500:
                bge.logic.ps.print_stats()
                print((bge.logic.s.getvalue()))
                bge.logic.print_counter = 0
            else:
                bge.logic.print_counter += 1
        else:
            owner["init"].update()
    else:
        if profiling:
            bge.logic.print_counter = 1
            bge.logic.pr = cProfile.Profile()
            bge.logic.pr.enable()
            owner["init"] = PlayerInit(owner.worldPosition)
            bge.logic.pr.disable()
            bge.logic.s = io.StringIO()
            bge.logic.ps = pstats.Stats(bge.logic.pr, stream=bge.logic.s).\
                sort_stats('tottime')
        else:
            owner["init"] = PlayerInit(owner.worldPosition)

