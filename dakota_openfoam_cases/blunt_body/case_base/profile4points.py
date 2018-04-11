'''

to run:

$HOME/salome/appli_V7_7_1/runAppli -t profile4points.py 

####################################################################

This script generates the following geometry:

  |---------------------|
  |			|
  |    N		|
0 |  W   E		| LY
  |    S		|
  |			|
  |---------------------|
       0     LX

where 4 points (N S W E) defined by 8 coordinates (NX NY, SX SY, WX WY, EX EY) 
   generate a b-spline curve with defined directions at the ends (INTERPOLATE)

NB: in Southern and Northern points a horizontal tangent is enforced (see vectors v1 and v2)

The patches names exported by ideasUNVtoFoam are:

profile:	"prof_extruded"
freeSlip:	"free_extruded"
inlet:		"in_extruded"
outlet:		"out_extruded"
frontAndBack:	"defaultFaces"

Mesh is computed via a 2D-1D FULL NETGEN ALGORITHM

####################################################################'''

import salome
salome.salome_init()

import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New(salome.myStudy)

import SMESH, SALOMEDS
from salome.smesh import smeshBuilder
smesh =  smeshBuilder.New(salome.myStudy)

import math
import os

####################################################################
# PARAMETERS DEFINITION
####################################################################

#WX = -1.; WY = 0.; EX = 1.; EY = 0.; NX = 0.; NY = 1.; SX = 0.; SY = -1.;	# rounded square points

WX = -1.5; WY = 0; EX = 1.5; EY = 0.; NX = 0.; NY = 0.25; SX = 0.; SY = 0;	# rounded square points

#WX = 0.; WY = 0.; EX = 5.; EY = -1.; NX = 1.; NY = 0.3; SX = 1.; SY = 0.;	# airfoil-like points

meshFineness = 4	# (0 VeryCoarse, 1 Coarse, 2 Moderate, 3 Fine, 4 VeryFine, 5 Custom)
maxMeshSize = 1		# on the whole domain
refinedMeshSize = 0.05	# on the profile only

LX = 50			# horizontal dim
LY = 40			# vertical dim
X_TRANS = (LX-LY)/2	# in order to equalize LY/2 to the distance of the centre of the cylinder from the inlet

GUI_OUTPUT = 0		# 0 in batch mode, 1 in GUI mode (set the proper path if GUI==1)

if GUI_OUTPUT==1:
   path = "/media/matteo/Desktop/profile4points/mesh.unv"
   gg = salome.ImportComponentGUI("GEOM")
else:
   path = os.getcwd() + "/mesh4points.unv" 


'''####################################################################
#THE FOLLOWING SHALL NOT BE MODIFIED
####################################################################'''

####################################################################
# GEOMETRY GENERATION
####################################################################

print "generating the geometry....."

# create vertices and vectors
O = geompy.MakeVertex(0, 0, 0.)
p0 = geompy.MakeVertex(NX, NY, 0.)
p1 = geompy.MakeVertex(EX, EY, 0.)
p2 = geompy.MakeVertex(SX, SY, 0.)
p3 = geompy.MakeVertex(WX, WY, 0.)

v1 = geompy.MakeVectorDXDYDZ(1, 0, 0)
v2 = geompy.MakeVectorDXDYDZ(-1, 0, 0)

OX = geompy.MakeVertex(X_TRANS, 0, 0.)

p100 = geompy.MakeVertex(100., 0., 0.)
lineRef = geompy.MakeLineTwoPnt(O,p100)
id_lineRef  = geompy.addToStudy(lineRef,"Line")

#create a b-spline curve with defined directions at the ends (INTERPOLATE)
interpol_r = geompy.MakeInterpolWithTangents([p0, p1, p2], v1, v2)
interpol_l = geompy.MakeInterpolWithTangents([p2, p3, p0], v2, v1)

#create outer domain
face1 = geompy.MakeFaceHW(LX, LY, 1)
rectangle = geompy.MakeTranslationTwoPoints(face1, O, OX)

#create profile (wire)
wire = geompy.MakeWire([interpol_r, interpol_l])

#create profile (face)
profile = geompy.MakeFace(wire, 1)

#create domain
cut = geompy.MakeCut(rectangle, profile)

#create groups on geometry
SubFaceList = geompy.SubShapeAllSortedCentres(cut, geompy.ShapeType["EDGE"])

profileEdges = geompy.CreateGroup(cut, geompy.ShapeType["EDGE"])
for i in [1,2] :
    FaceID = geompy.GetSubShapeID(cut, SubFaceList[i])
    geompy.AddObject(profileEdges, FaceID)

inlet = geompy.CreateGroup(cut, geompy.ShapeType["EDGE"])
for i in [0] :
    FaceID = geompy.GetSubShapeID(cut, SubFaceList[i])
    geompy.AddObject(inlet, FaceID)

outlet = geompy.CreateGroup(cut, geompy.ShapeType["EDGE"])
for i in [5] :
    FaceID = geompy.GetSubShapeID(cut, SubFaceList[i])
    geompy.AddObject(outlet, FaceID)

freeSlip = geompy.CreateGroup(cut, geompy.ShapeType["EDGE"])
for i in [3,4] :
    FaceID = geompy.GetSubShapeID(cut, SubFaceList[i])
    geompy.AddObject(freeSlip, FaceID)

#add to study
id_p0       = geompy.addToStudy(p0,           "Point1")
id_p1       = geompy.addToStudy(p1,           "Point2")
id_p2       = geompy.addToStudy(p2,           "Point3")
id_p3       = geompy.addToStudy(p3,           "Point4")
id_face1    = geompy.addToStudy(rectangle,    "Rectangle")   
id_wire     = geompy.addToStudy(wire,         "Wire")
id_profile  = geompy.addToStudy(profile,      "Profile")
id_cut      = geompy.addToStudy(cut,          "Domain")
id_prof     = geompy.addToStudy(profileEdges, "Profile")
id_inlet    = geompy.addToStudy(inlet,        "Inlet")
id_outlet   = geompy.addToStudy(outlet,       "Outlet")
id_freeSlip = geompy.addToStudy(freeSlip,     "freeSlip")


#########################################################
# CREATE MESH
#########################################################

# Create a tetrahedral mesh on the domain with NETGEN_1D2D3D algorithm (full netgen)
triaN = smesh.Mesh(cut, "Mesh - NETGEN_1D2D")

# create a Netgen_1D2D3D algorithm for solids
algo2D = triaN.Triangle(smeshBuilder.NETGEN_1D2D)

# define hypotheses
n12_params = algo2D.Parameters()

# set fineness (0 VeryCoarse, 1 Coarse, 2 Moderate, 3 Fine, 4 VeryFine, 5 Custom)
n12_params.SetFineness(meshFineness)

# set optimization (0 False, 1 True)
n12_params.SetOptimize(1)
n12_params.SetSecondOrder(0) # always set to 0 (OF does not support 2nd order)

# define max element size
n12_params.SetMaxSize(maxMeshSize)
n12_params.SetLocalSizeOnShape(profile, refinedMeshSize)


#########################################################
# COMPUTE MESH
#########################################################

print "computing the mesh....."
ret2 = triaN.Compute()
if ret2 == 0:
    print "ERROR: problem when computing the mesh!!"
else:
    print ":) mesh computed."
    pass

#########################################################
# CREATE BOUNDARIES NAMES
#########################################################

# create groups on previously created geometries
profileMesh = triaN.GroupOnGeom(profileEdges, "prof")
freeSlipMesh = triaN.GroupOnGeom(freeSlip, "free")
inletMesh = triaN.GroupOnGeom(inlet, "in")
outletMesh = triaN.GroupOnGeom(outlet, "out")


#########################################################
# EXTRUDE
#########################################################

# create a vector for extrusion
point = SMESH.PointStruct(0., 0., 1.)
vector = SMESH.DirStruct(point)

# create a group to be extruded
GroupTri = triaN.GroupOnGeom(cut, "extrusionGroup", SMESH.FACE)

# perform extrusion of the group
triaN.ExtrusionSweepObject(GroupTri, vector, 1, MakeGroups = True )


#########################################################
# DELETE UNWANTED GROUPS
#########################################################
l_groups =  triaN.GetGroups()

for group in l_groups:
    name = group.GetName()
    if not (name == "prof_extruded" or name == "free_extruded" or name == "in_extruded" or name == "out_extruded"):
        triaN.RemoveGroup(group)

#########################################################
# EXPORT MESH
#########################################################

print "exporting the mesh....."
retexp = triaN.ExportUNV(path)

if retexp == 0:
    print "ERROR: problem when exporting the mesh!"
else:
    print ':) mesh exported in %s.' % path
    pass



from killSalomeWithPort import killMyPort
killMyPort(os.getenv('NSPORT'))	

print "Port killed: %s" % os.getenv('NSPORT')






