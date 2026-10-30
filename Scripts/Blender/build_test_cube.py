"""M00 scale test: build a 1 m cube and export it as FBX for Unreal import.

Run in a fresh Blender process:
    blender --background --python-exit-code 1 --python Scripts/Blender/build_test_cube.py

Output goes to Saved/BlenderTest/ (git-ignored). Import it into the test map
and confirm it measures 100 x 100 x 100 Unreal units.
"""
import os
import sys

import bpy

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_DIR = os.path.join(PROJECT_ROOT, "Saved", "BlenderTest")
OUT_FILE = os.path.join(OUT_DIR, "SM_M00_TestCube_1m.fbx")


def main():
    bpy.ops.wm.read_factory_settings(use_empty=True)

    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 1.0

    # Pivot at the bottom centre so the cube sits on the ground plane.
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, 0.0, 0.5))
    cube = bpy.context.active_object
    cube.name = "SM_M00_TestCube_1m"
    bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)
    bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    dims = tuple(round(d, 4) for d in cube.dimensions)
    if dims != (1.0, 1.0, 1.0):
        raise RuntimeError(f"Unexpected cube dimensions {dims}")

    os.makedirs(OUT_DIR, exist_ok=True)
    bpy.ops.export_scene.fbx(
        filepath=OUT_FILE,
        use_selection=True,
        apply_unit_scale=True,
        apply_scale_options="FBX_SCALE_UNITS",
        axis_forward="-Y",
        axis_up="Z",
        mesh_smooth_type="FACE",
        add_leaf_bones=False,
    )
    print(f"[M00] Exported {OUT_FILE} with dimensions {dims} m")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # surface failure through --python-exit-code
        print(f"[M00] FAILED: {exc}", file=sys.stderr)
        raise
