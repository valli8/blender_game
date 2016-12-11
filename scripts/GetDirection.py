import mathutils
from scripts.GetMouseMove import GetMouseMove


class GetDirection(object):

    def __init__(self):
        self.mouse_rotation = GetMouseMove()
        self.rotation_matrix = mathutils.Matrix().to_3x3()
        self.rotation_matrix.col[0] = mathutils.Vector((1, 0, 0))
        self.rotation_matrix.col[1] = mathutils.Vector((0, 1, 0))
        self.rotation_matrix.col[2] = mathutils.Vector((0, 0, 1))
        self.up_down_val = 0.0

    def get_fps_direction(self, up=mathutils.Vector((0, 0, 1))):

        x_rot, y_rot = self.mouse_rotation.update()

        # look at function
        self.rotation_matrix.col[2] = up.normalized()
        self.rotation_matrix.col[0] = self.rotation_matrix.col[1].\
        cross(up).normalized()
        self.rotation_matrix.col[1] = self.rotation_matrix.col[2].\
        cross(self.rotation_matrix.col[0]).normalized()

        # limit up and down
        self.up_down_val += y_rot
        if self.up_down_val < -1.5:
            self.up_down_val = -1.5
        elif self.up_down_val > 1.5:
            self.up_down_val = 1.5

        self.rotation_matrix.rotate(mathutils.Quaternion(
            self.rotation_matrix.col[2], x_rot))
        self.rotation_matrix.rotate(mathutils.Quaternion(
            self.rotation_matrix.col[0], self.up_down_val))

        return self.rotation_matrix

    def get_free_direction(self):

        x_rot, y_rot = self.mouse_rotation.update()

        self.rotation_matrix.rotate(mathutils.Quaternion(
            self.rotation_matrix.col[2], x_rot))
        self.rotation_matrix.rotate(mathutils.Quaternion(
            self.rotation_matrix.col[0], y_rot))

        return self.rotation_matrix
