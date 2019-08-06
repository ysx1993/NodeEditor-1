import numpy as np
import random
import functools
import time
import inspect

from FreeCAD import Vector
import FreeCAD
import FreeCADGui
import Part


from PyFlow import CreateRawPin
from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *
from PyFlow.Packages.PyFlowBase.Nodes import FLOW_CONTROL_COLOR

import nodeeditor.store as store
from nodeeditor.say import *

from PyFlow.Packages.PyFlowFreeCAD.Nodes.FreeCAD_Object import timer, FreeCadNodeBase




class FreeCAD_Tripod(FreeCadNodeBase):
    '''
    position on a surface or curve
    '''

    def __init__(self, name="LOD",**kvargs):

        super(FreeCAD_Tripod, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')

        self.createInputPin('name', 'StringPin','view3d')
        a=self.createInputPin('u', 'FloatPin',0)
        a.recomputeNode=True
        a=self.createInputPin('v', 'FloatPin',0)
        a.recomputeNode=True
        self.createInputPin('Shape', 'ShapePin')
        self.createOutputPin('position', 'VectorPin')
        self.createOutputPin('placement', 'PlacementPin' )
        self.createInputPin("display", 'BoolPin', True)
        self.createInputPin("directionNormale", 'BoolPin', False)
        self.createInputPin("curvatureMode", 'BoolPin', True)
        


    @staticmethod
    def description():
        return FreeCAD_Tripod.__doc__

    @staticmethod
    def category():
        return 'Document'

    @staticmethod
    def keywords():
        return ['Surface','position','Point','uv']





class FreeCAD_YYY(FreeCadNodeBase):
    '''
    position on a surface or curve
    '''

    def __init__(self, name="LOD",**kvargs):

        super(FreeCAD_YYY, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')

        self.createInputPin('name', 'StringPin','view3d')
        a=self.createInputPin('u', 'FloatPin',0)
        a.recomputeNode=True
        a=self.createInputPin('v', 'FloatPin',0)
        a.recomputeNode=True
        self.createInputPin('Shape', 'ShapePin')
        self.createOutputPin('position', 'VectorPin')
        self.createOutputPin('placement', 'PlacementPin' )
        self.createInputPin("display", 'BoolPin', True)
        self.createInputPin("directionNormale", 'BoolPin', False)
        self.createInputPin("curvatureMode", 'BoolPin', True)
        


    @staticmethod
    def description():
        return FreeCAD_YYY.__doc__

    @staticmethod
    def category():
        return 'Document'

    @staticmethod
    def keywords():
        return ['Surface','position','Point','uv']


class FreeCAD_Bar(FreeCadNodeBase):
    '''
    dummy for tests
    '''

#   def __init__(self, name="Fusion"):
#       super(FreeCAD_Bar, self).__init__(name)


    def compute(self, *args, **kwargs):

        sayl()
        import nodeeditor.dev
        reload (nodeeditor.dev)
        nodeeditor.dev.run_bar_compute(self,*args, **kwargs)
        self.outExec.call()

    @staticmethod
    def description():
        return FreeCAD_Bar.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []


class FreeCAD_uIso(FreeCadNodeBase):
    '''
    uIso curve on a surface
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')
        self.createInputPin('Face', 'ShapePin')
        a=self.createInputPin('u', 'FloatPin',5)
        a.recomputeNode=True
        self.createInputPin("display", 'BoolPin', True)
        self.createOutputPin('Edge', 'ShapePin')


    @staticmethod
    def description():
        return FreeCAD_uIso.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []


import traceback
import inspect

class FreeCAD_vIso(FreeCadNodeBase):
    '''
    vIso curve on a surface
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')
        self.createInputPin('Face', 'ShapePin')
        a=self.createInputPin('v', 'FloatPin',5)
        a.recomputeNode=True
        self.createInputPin("display", 'BoolPin', True)
        self.createOutputPin('Edge', 'ShapePin')


    @staticmethod
    def description():
        return FreeCAD_vIso.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []


class FreeCAD_uvGrid(FreeCadNodeBase):
    '''
    uIso and vIso curves grid
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')
        self.createInputPin('Face', 'ShapePin')
        a=self.createInputPin('uCount', 'IntPin',5)
        a.recomputeNode=True
        a=self.createInputPin('vCount', 'IntPin',5)
        a.recomputeNode=True
        self.createInputPin("display", 'BoolPin', True)
        self.createOutputPin('uEdges', 'ShapeListPin')
        self.createOutputPin('vEdges', 'ShapeListPin')

    @staticmethod
    def description():
        return FreeCAD_uvGrid.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []



class FreeCAD_Voronoi(FreeCadNodeBase):
    '''
    voronoi cells, delaunay triangulation on a surface for a given set of uv points  on this surface
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')
        self.createInputPin('Face', 'ShapePin')
#       a=self.createInputPin('uCount', 'IntPin',5)
#       a.recomputeNode=True
#       a=self.createInputPin('vCount', 'IntPin',5)
#       a.recomputeNode=True
        self.createInputPin("useLines", 'BoolPin', True)
        a=self.createInputPin("indA", 'IntPin', True)
        a.recomputeNode=True
        a.setInputWidgetVariant("MyINPUTVARIANT")

        a=self.createInputPin("flipArea", 'BoolPin', True)
        a.recomputeNode=True
        self.createInputPin("indB", 'IntPin', True)
        self.createOutputPin('uEdges', 'ShapeListPin')
        self.createOutputPin('vEdges', 'ShapeListPin')
        self.createInputPin('uList', 'FloatPin', structure=PinStructure.Array,defaultValue=None)
        self.createInputPin('vList', 'FloatPin', structure=PinStructure.Array,defaultValue=None)

        self.createOutputPin('Points', 'ShapePin')
        self.createOutputPin('convexHull', 'ShapePin')
        self.createOutputPin('delaunayTriangles', 'ShapePin')
        self.createOutputPin('voronoiCells', 'ShapePin')


    @staticmethod
    def description():
        return FreeCAD_Voronoi.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []



class FreeCAD_Hull(FreeCadNodeBase):
    '''
    delaynay triangulation, convex hull and alpha hull for a given set of points
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')
        self.createInputPin('Shape', 'ShapePin')
        self.createInputPin("singleSimplex", 'BoolPin', True)

        a=self.createInputPin("simplex", 'IntPin', True)
        a.recomputeNode=True
        a.description="index of the displayd simplex if singleSimplex is set"
#       a.setInputWidgetVariant("MyINPUTVARIANT")

        a=self.createInputPin("showFaces", 'BoolPin', True)
        a.recomputeNode=True
        a.description="display alpha and convex hull by faces" 

        a=self.createInputPin("alpha", 'IntPin', True)
        a.recomputeNode=True

        self.createOutputPin('uEdges', 'ShapeListPin')
        self.createOutputPin('vEdges', 'ShapeListPin')
        self.createInputPin('uList', 'FloatPin', structure=PinStructure.Array,defaultValue=None)
        self.createInputPin('vList', 'FloatPin', structure=PinStructure.Array,defaultValue=None)
        #self.createOutputPin('edges', 'FloatPin', structure=PinStructure.Array,defaultValue=None)
        self.createOutputPin('Points', 'ShapePin')
        self.createOutputPin('convexHull', 'ShapePin')
        self.createOutputPin('delaunayTriangles', 'ShapePin')
        self.createOutputPin('alphaHull', 'ShapePin').description='edges or faces compound of the alpha hull'


    @staticmethod
    def description():
        return FreeCAD_Hull.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []




class FreeCAD_2DGeometry(FreeCadNodeBase):
    '''
    2d Geometry object
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')
        self.createInputPin('Shape', 'ShapePin')

        a=self.createInputPin("ua", 'FloatPin', True)
        a.recomputeNode=True
        a=self.createInputPin("va", 'FloatPin', True)
        a.recomputeNode=True
        a=self.createInputPin("ub", 'FloatPin', True)
        a.recomputeNode=True
        a=self.createInputPin("vb", 'FloatPin', True)
        a.recomputeNode=True

        self.createOutputPin('Shape_out', 'ShapePin')
        self.createOutputPin('geometry', 'ShapePin') #.description='edges or faces compound of the alpha hull'


    @staticmethod
    def description():
        return FreeCAD_2DGeometry.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []



class FreeCAD_2DCircle(FreeCadNodeBase):
    '''
    2d Geometry object
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')
        self.createInputPin('Shape', 'ShapePin')

        a=self.createInputPin("u", 'FloatPin', True)
        a.recomputeNode=True
        a=self.createInputPin("v", 'FloatPin', True)
        a.recomputeNode=True
        a=self.createInputPin("radius", 'FloatPin', True)
        a.recomputeNode=True

        self.createOutputPin('Shape_out', 'ShapePin')
        self.createOutputPin('geometry', 'ShapePin') #.description='edges or faces compound of the alpha hull'


    @staticmethod
    def description():
        return FreeCAD_2DCircle.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []


class FreeCAD_2DEllipse(FreeCadNodeBase):
    '''
    2d Geometry object
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')
        self.createInputPin('Shape', 'ShapePin')

        a=self.createInputPin("uLocation", 'FloatPin', True)
        a.recomputeNode=True
        a=self.createInputPin("vLocation", 'FloatPin', True)
        a.recomputeNode=True

        a=self.createInputPin("direction", 'FloatPin', True)
        a.recomputeNode=True

        a=self.createInputPin("MajorRadius", 'FloatPin', True)
        a.recomputeNode=True
        a=self.createInputPin("MinorRadius", 'FloatPin', True)
        a.recomputeNode=True
        

        self.createOutputPin('Shape_out', 'ShapePin')
        self.createOutputPin('geometry', 'ShapePin') #.description='edges or faces compound of the alpha hull'


    @staticmethod
    def description():
        return FreeCAD_2DEllipse.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []


class FreeCAD_2DArcOfEllipse(FreeCadNodeBase):
    '''
    2d Geometry object
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')
        self.createInputPin('Shape', 'ShapePin')

        a=self.createInputPin("uLocation", 'FloatPin', True)
        a.recomputeNode=True
        a=self.createInputPin("vLocation", 'FloatPin', True)
        a.recomputeNode=True

        a=self.createInputPin("direction", 'FloatPin', True)
        a.recomputeNode=True

        a=self.createInputPin("MajorRadius", 'FloatPin', True)
        a.recomputeNode=True
        a=self.createInputPin("MinorRadius", 'FloatPin', True)
        a.recomputeNode=True

        a=self.createInputPin("startAngle", 'FloatPin', True)
        a.recomputeNode=True
        a=self.createInputPin("endAngle", 'FloatPin', True)
        a.recomputeNode=True
        

        self.createOutputPin('Shape_out', 'ShapePin')
        self.createOutputPin('geometry', 'ShapePin') #.description='edges or faces compound of the alpha hull'


    @staticmethod
    def description():
        return FreeCAD_2DArcOfEllipse.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []


class FreeCAD_2DArcOfParabola(FreeCadNodeBase):
    '''
    2d Geometry object
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')
        self.createInputPin('Shape', 'ShapePin')

        a=self.createInputPin("uLocation", 'FloatPin', True)
        a.recomputeNode=True
        a=self.createInputPin("vLocation", 'FloatPin', True)
        a.recomputeNode=True

        a=self.createInputPin("direction", 'FloatPin', True)
        a.recomputeNode=True

        a=self.createInputPin("MajorRadius", 'FloatPin', True)
        a.recomputeNode=True
        a=self.createInputPin("MinorRadius", 'FloatPin', True)
        a.recomputeNode=True

        a=self.createInputPin("startAngle", 'FloatPin', True)
        a.recomputeNode=True
        a=self.createInputPin("endAngle", 'FloatPin', True)
        a.recomputeNode=True
        

        self.createOutputPin('Shape_out', 'ShapePin')
        self.createOutputPin('geometry', 'ShapePin') #.description='edges or faces compound of the alpha hull'


    @staticmethod
    def description():
        return FreeCAD_2DArcOfParabola.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []


class FreeCAD_2DArcOfCircle(FreeCadNodeBase):
    '''
    2d Geometry object - arc of a circle
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')
        self.createInputPin('Shape', 'ShapePin')

        a=self.createInputPin("uLocation", 'FloatPin', True)
        a.recomputeNode=True
        a=self.createInputPin("vLocation", 'FloatPin', True)
        a.recomputeNode=True

        a=self.createInputPin("radius", 'FloatPin', True)
        a.recomputeNode=True

        a=self.createInputPin("startAngle", 'FloatPin', True)
        a.recomputeNode=True
        a=self.createInputPin("endAngle", 'FloatPin', True)
        a.recomputeNode=True
        

        self.createOutputPin('Shape_out', 'ShapePin')
        self.createOutputPin('geometry', 'ShapePin') #.description='edges or faces compound of the alpha hull'


    @staticmethod
    def description():
        return FreeCAD_2DArcOfCircle.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []




class FreeCAD_Simplex(FreeCadNodeBase):
    '''
    Tetraeder
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')
        
        a=self.createInputPin("noise", 'FloatPin', True)

        a=self.createInputPin("pointA", 'VectorPin', True)
        a.recomputeNode=True
        a.setData(Vector(0,0,0))

        a=self.createInputPin("pointB", 'VectorPin', True)
        a.recomputeNode=True
        a.setData(Vector(10,0,0))
        a=self.createInputPin("pointC", 'VectorPin', True)
        a.recomputeNode=True
        a.setData(Vector(0,10,0))
        a=self.createInputPin("pointD", 'VectorPin', True)
        a.recomputeNode=True
        a.setData(Vector(0,0,10))

        self.createOutputPin('Shape_out', 'ShapePin')
        self.createOutputPin('Compound_out', 'ShapePin') # Faces compound without tolerance


    @staticmethod
    def description():
        return FreeCAD_2DEllipse.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []



class FreeCAD_Tread(FreeCadNodeBase):
    '''
    Schindel oder Stufe
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.inExec = self.createInputPin('produce', 'ExecPin', None, self.produce)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')

        a=self.createInputPin("noise", 'FloatPin', True)

        a=range(8)
        for i in range(8):
            a[i]=self.createInputPin("point_"+str(i), 'VectorPin', True)
            a[i].recomputeNode=True

        v=[
            Vector(0,20),
            Vector(30,20),
            Vector(30,0),
            Vector(80,0),
            
            Vector(80,10),
            Vector(40,10),
            Vector(40,30),
            Vector(0,30),
        ]
        for i in range(8):
            a[i].setData(v[i])

        self.createOutputPin('Shape_out', 'ShapePin')
        self.createOutputPin('Compound_out', 'ShapePin') # Faces compound without tolerance


    @staticmethod
    def description():
        return FreeCAD_2DEllipse.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []

#   def produce(self,**kvargs):
#       self.compute(produce=True)

    def produce(self, *args, **kwargs):
        import nodeeditor.dev
        reload (nodeeditor.dev)
        nodeeditor.dev.run_FreeCAD_Tread(self,produce=True)


class FreeCAD_Discretize(FreeCadNodeBase):
    '''
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
#        self.inExec = self.createInputPin('produce', 'ExecPin', None, self.produce)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')

        a=self.createInputPin("count", 'IntPin', True)
        a=self.createInputPin("Wire", 'ShapePin', True)

        self.createOutputPin('Shape_out', 'ShapePin')
        self.createOutputPin('Compound_out', 'ShapePin') # Faces compound without tolerance


    @staticmethod
    def description():
        return FreeCAD_2DEllipse.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []

#   def produce(self,**kvargs):
#       self.compute(produce=True)

    def XXproduce(self, *args, **kwargs):
        import nodeeditor.dev
        reload (nodeeditor.dev)
        nodeeditor.dev.run_FreeCAD_Tread(self,produce=True)

class FreeCAD_Offset(FreeCadNodeBase):
    '''
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.inExec = self.createInputPin('produce', 'ExecPin', None, self.produce)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')

        a=self.createInputPin("count", 'IntPin', True)
        a=self.createInputPin("Wire", 'ShapePin', True)
        a=self.createInputPin("Shape", 'ShapePin', True)
        a=self.createInputPin("offset", 'FloatPin', True)
        a=self.createInputPin("height", 'FloatPin', True)

        self.createOutputPin('Shape_out', 'ShapePin')
        self.createOutputPin('Compound_out', 'ShapePin') # Faces compound without tolerance


    @staticmethod
    def description():
        return FreeCAD_2DEllipse.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []

#   def produce(self,**kvargs):
#       self.compute(produce=True)

    def produce(self, *args, **kwargs):
        import nodeeditor.dev
        reload (nodeeditor.dev)
        nodeeditor.dev.run_FreeCAD_Offset(self,produce=True)






class FreeCAD_FillEdge(FreeCadNodeBase):
    '''
    closed edge to face
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.inExec = self.createInputPin('produce', 'ExecPin', None, self.produce)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')

        a=self.createInputPin("count", 'IntPin', True)
        a=self.createInputPin("Wire", 'ShapePin', True)
        a=self.createInputPin("Shape", 'ShapePin', True)
        a=self.createInputPin("offset", 'FloatPin', True)
        a=self.createInputPin("height", 'FloatPin', True)

        self.createOutputPin('Shape_out', 'ShapePin')
        self.createOutputPin('Compound_out', 'ShapePin') # Faces compound without tolerance


    @staticmethod
    def description():
        return FreeCAD_2DEllipse.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []

#   def produce(self,**kvargs):
#       self.compute(produce=True)

    def produce(self, *args, **kwargs):
        import nodeeditor.dev
        reload (nodeeditor.dev)
        nodeeditor.dev.run_FreeCAD_Offset(self,produce=True)



class FreeCAD_Solid(FreeCadNodeBase):
    '''
    make solid of faces
    '''

    def __init__(self, name="Fusion"):
        super(self.__class__, self).__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.inExec = self.createInputPin('bake', 'ExecPin', None, self.bake)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')

        #a=self.createInputPin("count", 'IntPin', True)
        #a=self.createInputPin("Wire", 'ShapePin', True)
        a=self.createInputPin("Shapes", 'ShapePin',structure=PinStructure.Array)
        a=self.createInputPin("Faces", 'FacePin',structure=PinStructure.Array)
        a.enableOptions(PinOptions.AllowMultipleConnections)
        a.disableOptions(PinOptions.SupportsOnlyArrays)

        #a=self.createInputPin("offset", 'FloatPin', True)
        #a=self.createInputPin("height", 'FloatPin', True)

        self.createOutputPin('Shape_out', 'ShapePin')
        self.createOutputPin('Compound_out', 'ShapePin') # Faces compound without tolerance


    @staticmethod
    def description():
        return FreeCAD_2DEllipse.__doc__

    @staticmethod
    def category():
        return 'Development'

    @staticmethod
    def keywords():
        return []

#   def produce(self,**kvargs):
#       self.compute(produce=True)

    def Xproduce(self, *args, **kwargs):
        import nodeeditor.dev
        reload (nodeeditor.dev)
        nodeeditor.dev.run_FreeCAD_Offset(self,produce=True)






def nodelist():
    return [
                FreeCAD_Bar,
                FreeCAD_Tripod,
                FreeCAD_YYY,
                FreeCAD_uIso, FreeCAD_vIso,
                FreeCAD_uvGrid,
                FreeCAD_Voronoi,
                FreeCAD_Hull,
                FreeCAD_2DGeometry,
                FreeCAD_2DCircle,
                FreeCAD_2DEllipse,
                FreeCAD_2DArcOfEllipse,
                FreeCAD_2DArcOfParabola,
                FreeCAD_2DArcOfCircle,
                FreeCAD_Simplex,
                FreeCAD_Tread,
                FreeCAD_Discretize,
                FreeCAD_Offset,
                FreeCAD_FillEdge,
                FreeCAD_Solid,
        ]
