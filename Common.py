# from importlib import reload  
# import Common  
# reload (Common)


from importlib import reload 

import FreeCAD,FreeCADGui

import inspect, os.path
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))
#FreeCAD.Console.PrintMessage(path)

ICONPATH = path+'/Resources/icons/'


#ICONPATH = FreeCAD.getUserAppDataDir()+'Mod/PlacementTools/Resources/icons/'

from PySide import QtGui

def test(lock=0):
	return

		
def toGlobalCoordinates (objHierancy,point):
	i=objHierancy.__len__()-1

	while i>=0:
		uobj=FreeCAD.ActiveDocument.getObject(objHierancy[i])
		if uobj!=None and hasattr(uobj,'Placement') and  not uobj.Placement.isIdentity():
			point=uobj.Placement.multVec(point)
			#point=uobj.Placement.multiply(FreeCAD.Placement(point,uobj.Placement.Rotation.inverted())).Base
			#FreeCAD.Console.PrintMessage(i)
		i=i-1
	point.x=round(point.x,12)
	point.y=round(point.y,12)
	point.z=round(point.z,12)
	FreeCAD.Console.PrintMessage(point)
	FreeCAD.Console.PrintMessage(' - Global Point\n')
	return point	
def toLocalCoordinates (objHierancy,point):
	i= 0
	while i<objHierancy.__len__():
		dobj=FreeCAD.ActiveDocument.getObject(objHierancy[i])
		if dobj!=None and hasattr(dobj,'Placement') and not  dobj.Placement.isIdentity():
			dv=FreeCAD.Vector(point.x-dobj.Placement.Base.x,point.y-dobj.Placement.Base.y,point.z-dobj.Placement.Base.z)
#			dv=dobj.Placement.inverse().multVec(point)
			point=dobj.Placement.Rotation.inverted().multVec(dv)
#			point=dobj.Placement.Rotation.multVec(dv)
		i=i+1
	point.x=round(point.x,12)
	point.y=round(point.y,12)
	point.z=round(point.z,12)
	return point	

def DelResolveTransform (objList,point):
	i=objList.__len__()-3
	while i>=0:
		uobj=FreeCAD.ActiveDocument.getObject(objList[i])
		point=uobj.Placement.multiply(FreeCAD.Placement(point,uobj.Placement.Rotation)).Base
		i=i-1
	return point
			
def getSelectionList():
	lst=[]
	for sel in FreeCADGui.Selection.getSelectionEx("",0):
		if sel.HasSubObjects:
			for subname in sel.SubElementNames:
				lst.append((sel.ObjectName+"."+subname).split("."))
		else:
			lst.append((sel.ObjectName+".").split("."))
	return lst

def getParcedSelectionList():
	SelectionList = getSelectionList()
	lst=[]
	if SelectionList.__len__()<=1: return SelectionList
	i=0
	stop=False
	while i<SelectionList[0].__len__() and not stop:
		ObjName=SelectionList[0][i]
		for item in SelectionList:
			if item[i]!=ObjName:
				stop=True
				exit
		i=i+1
	if i>1:		
		for item in SelectionList:
			j=i-1
			sublst=[]
			while j<item.__len__():
				sublst.append(item[j])
				j=j+1
			lst.append(sublst)
		return lst
	else: return SelectionList


	
def GetSelectedUpperObjects():
	objs=[]
	for obj in getParcedSelectionList():
		objs.append(FreeCAD.ActiveDocument.getObject(obj[0]))
	return objs
		
def GetSelectedLowerObjectsPath():
	objs=[]
	for sel in getSelectionList():
		ss=[]
		for s in sel:
			obj=FreeCAD.ActiveDocument.getObject(s)
			if obj!=None: 
				if len(obj.getSubObjects(1))>0: ss.append(s)
		objs.append(ss)
	return objs	
	
def GetSelectedPoint(ObjName,ElementName):
		o=FreeCAD.ActiveDocument.getObject(ObjName).getSubObject(ElementName)
		if o.ShapeType=='Vertex':
			return	o.Point
		else:
			return o.CenterOfMass


def getMax(v1,v2):
	if v1>v2:
		return v1
	else: 
		return v2
def getMin(v1,v2):
	if v1<v2:
		return v1
	else: 
		return v2

		
def GetObjectBoundBox(obj):
	if not (hasattr(obj,'Shape')) and obj.TypeId=='App::Part':
		bb=FreeCAD.BoundBox()
		for subobj in obj.OutList:
			if subobj.TypeId=='App::Part':
				bb2=GetObjectBoundBox(subobj)
			else: 
				if subobj.TypeId!='App::Origin':
					bb2=subobj.Shape.BoundBox
				else:
					bb2=FreeCAD.BoundBox()
			bb.XMax=getMax(bb.XMax,bb2.XMax)
			bb.YMax=getMax(bb.YMax,bb2.YMax)
			bb.ZMax=getMax(bb.ZMax,bb2.ZMax)
			bb.XMin=getMin(bb.XMin,bb2.XMin)
			bb.YMin=getMin(bb.YMin,bb2.YMin)
			bb.ZMin=getMin(bb.ZMin,bb2.ZMin)
		
		p=[]
		p.append(obj.Placement.multiply(FreeCAD.Placement(FreeCAD.Vector(bb.XMin,bb.YMin,bb.ZMin),obj.Placement.Rotation)))
		p.append(obj.Placement.multiply(FreeCAD.Placement(FreeCAD.Vector(bb.XMax,bb.YMin,bb.ZMin),obj.Placement.Rotation)))
		p.append(obj.Placement.multiply(FreeCAD.Placement(FreeCAD.Vector(bb.XMax,bb.YMax,bb.ZMin),obj.Placement.Rotation)))
		p.append(obj.Placement.multiply(FreeCAD.Placement(FreeCAD.Vector(bb.XMin,bb.YMax,bb.ZMin),obj.Placement.Rotation)))
		p.append(obj.Placement.multiply(FreeCAD.Placement(FreeCAD.Vector(bb.XMin,bb.YMin,bb.ZMax),obj.Placement.Rotation)))
		p.append(obj.Placement.multiply(FreeCAD.Placement(FreeCAD.Vector(bb.XMax,bb.YMin,bb.ZMax),obj.Placement.Rotation)))
		p.append(obj.Placement.multiply(FreeCAD.Placement(FreeCAD.Vector(bb.XMax,bb.YMax,bb.ZMax),obj.Placement.Rotation)))
		p.append(obj.Placement.multiply(FreeCAD.Placement(FreeCAD.Vector(bb.XMin,bb.YMax,bb.ZMax),obj.Placement.Rotation)))
		
		bb=FreeCAD.BoundBox()
		for pp in p:
			bb.XMax=getMax(bb.XMax,pp.Base.x)
			bb.YMax=getMax(bb.YMax,pp.Base.y)
			bb.ZMax=getMax(bb.ZMax,pp.Base.z)
			bb.XMin=getMin(bb.XMin,pp.Base.x)
			bb.YMin=getMin(bb.YMin,pp.Base.y)
			bb.ZMin=getMin(bb.ZMin,pp.Base.z)
		return bb
	else:
		return obj.Shape.BoundBox
	
				 
	 # v=App.Vector(b.Shape.BoundBox.XMax,b.Shape.BoundBox.YMax,b.Shape.BoundBox.ZMax)
	 #App.ActiveDocument.Part.Placement.multiply( App.Placement(v,App.ActiveDocument.Part.Placement.Rotation))
