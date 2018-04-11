How to run me:

The default values in the file wing_naca4.scad are:
camber_max = 8
camber_position = 4
thickness = 12

To modify the airfoil in batch you need to assign the value to the following variable:

curvature
curvature_position
airfoil_thickness

Example:
openscad -o out.stl -D curvature=0 -D curvature_position=0 -D airfoil_thickness=12 wing_naca4.scad 
openscad -o out.stl  wing_naca4.scad 