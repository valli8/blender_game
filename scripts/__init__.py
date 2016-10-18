
# When bpy is already in local, we know this is not the initial import...
if "bpy" in locals():
    # ...so we need to reload our submodule(s) using importlib
    import importlib
    if "player_init" in locals():
        importlib.reload(player_init)
    if "car" in locals():
        importlib.reload(car)
    if "get_keys" in locals():
        importlib.reload(get_keys)
    if "get_steering" in locals():
        importlib.reload(get_steering)
    if "bar" in locals():
        importlib.reload(bar)
    if "get_mouse_move" in locals():
        importlib.reload(get_mouse_move)
    if "get_player_controls" in locals():
        importlib.reload(get_player_controls)
    if "bump" in locals():
        importlib.reload(bump)
    if "get_direction" in locals():
        importlib.reload(get_direction)


# This is only relevant on first run, on later reloads those modules
# are already in locals() and those statements do not do anything.
import bpy
from scripts.player_init import player_init
from scripts.car import car
from scripts.get_keys import get_keys
from scripts.get_steering import get_steering
from scripts.bar import bar
from scripts.get_mouse_move import get_mouse_move
from scripts.get_player_controls import get_player_controls
from scripts.bump import bump
from scripts.get_direction import get_direction
