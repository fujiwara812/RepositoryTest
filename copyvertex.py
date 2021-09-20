import maya.cmds as cmds

def getVertexPoint(vertex):
	v = vertex
	points = cmds.pointPosition(v, w=True)	
	return(points[0], points[1], points[2])


def copyObjectTo(name, vertexList):
	for s in vertexList:
		vrtpoint = getVertexPoint(s)
		copyedObject = cmds.duplicate(name, ilf=True)[0]
		cmds.setAttr(copyedObject + '.translate', vrtpoint[0], vrtpoint[1], vrtpoint[2], type="double3")
		nConstraint = cmds.normalConstraint(s, copyedObject, aim=[0,1,0], u=[0,1,0])
		cmds.delete(nConstraint)


def Run():
	selection = cmds.ls(sl=True, fl=True)
	selObject = selection[-1]
	vertexList = selection[:-1]
	copyObjectTo(selObject, vertexList)


def copyRunWindow():
	cmds.window(t='CopyVertex', w=300, h=100)
	cmds.frameLayout(l='頂点選択後にオブジェクトを選択する')
	cmds.button(l='Copy', command='Run')
	cmds.showWindow()