import bpy
from bpy import data as D
from bpy import context as C
from mathutils import *
from math import *

#~PYTHON INTERACTIVE CONSOLE 3.10.13 (main, Sep 20 2023, 07:33:17) [MSC v.1928 64 bit (AMD64)]

#~Builtin Modules:       bpy, bpy.data, bpy.ops, bpy.props, bpy.types, bpy.context, bpy.utils, bgl, gpu, blf, mathutils
#~Convenience Imports:   from mathutils import *; from math import *
#~Convenience Variables: C = bpy.context, D = bpy.data

bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(2, 2, 1))
#~ {'FINISHED'}
#~ 
bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=(0, 0, 2), scale=(1, 1, 1))
#~ {'FINISHED'}
#~ 