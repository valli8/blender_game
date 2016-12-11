import cProfile
import pstats
import io
import bge
from scripts.Car import Car
from scripts.GetPlayerControls import GetPlayerControls


class PlayerInit(object):
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
        orders = self.controls.update(self.player.up)
        self.player.update(orders)

        if hasattr(bge.logic, 'energybar'):
            bge.logic.energybar.setBar(self.player.fire.cooldown)


def main(controller):
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
                bge.logic.print_counter = 1
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

