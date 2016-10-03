import bge
import car
import get_player_controls
import cProfile, pstats, io, time, profile

class player_init():
    def __init__(self, position):
        self.player = car.car(position)
        self.controls = get_player_controls.get_player_controls(self.player)
        if not "team1" in bge.logic.globalDict:
            bge.logic.globalDict['team1'] = []
        bge.logic.globalDict['team1'].append(self.player)
        #print(bge.logic.globalDict['team1'])
        
    def update(self):
        orders = self.controls.update()
        self.player.update(orders)
        
        if hasattr(bge.logic,'energybar'):
            bge.logic.energybar.setBar(self.player.fire.cooldown)
            
def main(controller):
    owner = controller.owner
    
    profiling = False
    
    if not "init" in owner:
        
        if profiling == True:
            bge.logic.print_counter = 1
            bge.logic.pr = cProfile.Profile()
            bge.logic.pr.enable()
            owner["init"] = player_init(owner.worldPosition)
            bge.logic.pr.disable()
            bge.logic.s = io.StringIO()
            bge.logic.ps = pstats.Stats(bge.logic.pr, stream=bge.logic.s).sort_stats('tottime')
        else:
            owner["init"] = player_init(owner.worldPosition)
    else:
        if profiling == True:
            bge.logic.pr.enable()
            owner["init"].update()
            bge.logic.pr.disable()
            bge.logic.ps = pstats.Stats(bge.logic.pr, stream=bge.logic.s).sort_stats('tottime') #tottime,cumulative
            
            if bge.logic.print_counter >= 500:
                bge.logic.ps.print_stats()
                print(bge.logic.s.getvalue())
                bge.logic.print_counter = 1
            else:
                bge.logic.print_counter+=1
        else:
            owner["init"].update()
