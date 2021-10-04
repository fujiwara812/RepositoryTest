import maya.cmds as cmds
import random

def getVertexPoint(vertex):
	v = vertex
	points = cmds.pointPosition(v, w=True)	
	return(points[0], points[1], points[2])


def copyObjectTo(name, vertexList):
    for s in vertexList:
        selgeo = int(random.uniform(0,len(name)))
        
        rotateX = random.uniform(0,360)
        rotateY = random.uniform(0,360)
        rotateZ = random.uniform(0,360)
        
        scaleX = random.uniform(0.5,2)
        scaleY = random.uniform(0.5,2)
        scaleZ = random.uniform(0.5,2)
        
        vrtpoint = getVertexPoint(s)
        
        copyedObject = cmds.duplicate(name[selgeo], ilf=True)[0]
        getscaleX = cmds.getAttr(copyedObject + '.scaleX')
        getscaleY = cmds.getAttr(copyedObject + '.scaleY')
        getscaleZ = cmds.getAttr(copyedObject + '.scaleZ')
        cmds.setAttr(copyedObject + '.translate', vrtpoint[0], vrtpoint[1], vrtpoint[2], type="double3")
        cmds.setAttr(copyedObject + '.rotate', rotateX, rotateY, rotateZ, type="double3")
        cmds.setAttr(copyedObject + '.scale', getscaleX*scaleX, getscaleY*scaleY, getscaleZ*scaleX, type="double3")



def Run():
    vertexList = cmds.ls(sl=True, fl=True)
    selObject = cmds.ls(sl=True, fl=True, dag=True, g=True)
    ver_num = len(vertexList) - len(selObject)
    del vertexList[ver_num:]
    copyObjectTo(selObject, vertexList)