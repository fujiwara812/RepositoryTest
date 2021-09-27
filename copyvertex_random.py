import maya.cmds as cmds
import random

def getVertexPoint(vertex):
	v = vertex
	points = cmds.pointPosition(v, w=True)	
	return(points[0], points[1], points[2])


def copyObjectTo(name, vertexList):
    randomRX = cmds.floatSliderGrp('rotateXSlider', q=True,value=True)
    randomRY = cmds.floatSliderGrp('rotateYSlider', q=True,value=True)
    randomRZ = cmds.floatSliderGrp('rotateZSlider', q=True,value=True)
    
    randomSXmin = cmds.floatSliderGrp('scaleXSliderMin', q=True,value=True)
    randomSYmin = cmds.floatSliderGrp('scaleYSliderMin', q=True,value=True)
    randomSZmin = cmds.floatSliderGrp('scaleZSliderMin', q=True,value=True)
    
    randomSXmax = cmds.floatSliderGrp('scaleXSliderMax', q=True,value=True)
    randomSYmax = cmds.floatSliderGrp('scaleYSliderMax', q=True,value=True)
    randomSZmax = cmds.floatSliderGrp('scaleZSliderMax', q=True,value=True)
        
    for s in vertexList:
        rotateX = random.uniform(0,randomRX)
        rotateY = random.uniform(0,randomRY)
        rotateZ = random.uniform(0,randomRZ)
        
        scaleX = random.uniform(randomSXmin,randomSXmax)
        scaleY = random.uniform(randomSYmin,randomSYmax)
        scaleZ = random.uniform(randomSZmin,randomSZmax)
        
        vrtpoint = getVertexPoint(s)
        copyedObject = cmds.duplicate(name, ilf=True)[0]
        getscaleX = cmds.getAttr(copyedObject + '.scaleX')
        getscaleY = cmds.getAttr(copyedObject + '.scaleY')
        getscaleZ = cmds.getAttr(copyedObject + '.scaleZ')
        cmds.setAttr(copyedObject + '.translate', vrtpoint[0], vrtpoint[1], vrtpoint[2], type="double3")
        cmds.setAttr(copyedObject + '.rotate', rotateX, rotateY, rotateZ, type="double3")
        cmds.setAttr(copyedObject + '.scale', getscaleX*scaleX, getscaleY*scaleY, getscaleZ*scaleX, type="double3")



def Run():
	selection = cmds.ls(sl=True, fl=True)
	selObject = selection[-1]
	vertexList = selection[:-1]
	copyObjectTo(selObject, vertexList)


def copyRunWindow():
    cmds.window(t='CopyVertex', w=300, h=100)
    cmds.frameLayout(l='頂点選択後にオブジェクトを選択する')
    cmds.floatSliderGrp('rotateXSlider', label='Rotate X', field=True, minValue=-360.0, maxValue=360.0, step=0.1,value=360.0)
    cmds.floatSliderGrp('rotateYSlider', label='Rotate Y', field=True, minValue=-360.0, maxValue=360.0, step=0.1,value=360.0)
    cmds.floatSliderGrp('rotateZSlider', label='Rotate Z', field=True, minValue=-360.0, maxValue=360.0, step=0.1,value=360.0)
    cmds.floatSliderGrp('scaleXSliderMin', label='Scale X の最小値', field=True, minValue=0.1, maxValue=1.0, step=0.1,value=0.5)
    cmds.floatSliderGrp('scaleYSliderMin', label='Scale Y の最小値', field=True, minValue=0.1, maxValue=1.0, step=0.1,value=0.5)
    cmds.floatSliderGrp('scaleZSliderMin', label='Scale Z の最小値', field=True, minValue=0.1, maxValue=1.0, step=0.1,value=0.5)
    cmds.floatSliderGrp('scaleXSliderMax', label='Scale X の最大値', field=True, minValue=1.0, maxValue=10.0, step=0.1,value=2.0)
    cmds.floatSliderGrp('scaleYSliderMax', label='Scale Y の最大値', field=True, minValue=1.0, maxValue=10.0, step=0.1,value=2.0)
    cmds.floatSliderGrp('scaleZSliderMax', label='Scale Z の最大値', field=True, minValue=1.0, maxValue=10.0, step=0.1,value=2.0)
    cmds.button(label = 'Copy', command='Run()')
    cmds.showWindow()