
# When bpy is already in local, we know this is not the initial import...
if "bpy" in locals():
    # ...so we need to reload our submodule(s) using importlib
    import importlib
    if "PlayerInit" in locals():
        importlib.reload(PlayerInit)
    if "Car" in locals():
        importlib.reload(Car)
    if "GetKeys" in locals():
        importlib.reload(GetKeys)
    if "GetSteering" in locals():
        importlib.reload(GetSteering)
    if "bar" in locals():
        importlib.reload(bar)
    if "speedometer" in locals():
        importlib.reload(speedometer)
    if "GetMouseMove" in locals():
        importlib.reload(GetMouseMove)
    if "GetPlayerControls" in locals():
        importlib.reload(GetPlayerControls)
    if "bump" in locals():
        importlib.reload(bump)
    if "GetDirection" in locals():
        importlib.reload(GetDirection)


# This is only relevant on first run, on later reloads those modules
# are already in locals() and those statements do not do anything.
import bpy
from scripts.PlayerInit import PlayerInit
from scripts.Car import Car
from scripts.GetKeys import GetKeys
from scripts.GetSteering import GetSteering
from scripts.bar import bar
from scripts.GetMouseMove import GetMouseMove
from scripts.GetPlayerControls import GetPlayerControls
from scripts.bump import bump
from scripts.GetDirection import GetDirection
