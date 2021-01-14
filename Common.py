import FreeCAD,FreeCADGui

import inspect, os.path
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))
#FreeCAD.Console.PrintMessage(path)

ICONPATH = path+'/Resources/icons/'

#ICONPATH = FreeCAD.getUserAppDataDir()+'Mod/PlacementTools/Resources/icons/'



def getParent(obj):
	for a in obj.InList:
		for b in a.ViewObject.claimChildren():
			if b == obj:
				FreeCAD.Console.PrintMessage('|')
				return a
	return obj

def upperObject(obj):
#	FreeCAD.Console.PrintMessage('[upperObject]')
	par=getParent(obj)
	if par!=obj: 
	#obj.InList.__len__()>0:
		#FreeCAD.Console.PrintMessage('[yes]')
		#FreeCAD.Console.PrintMessage(obj.Label)
		return upperObject(par)
		#return upperObject(obj.InList[obj.InList.__len__()-1])
	else:
		#FreeCAD.Console.PrintMessage('[no]')
		#FreeCAD.Console.PrintMessage(obj.Label)
		#FreeCAD.Console.PrintMessage('\n')
		return obj
def GetSelectedUpperObjectsNew():
	upperobjs=[]
	objs=FreeCADGui.Selection.getSelection() 
	for obj in objs:
		upperobjs.append(upperObject(obj))
	return upperobjs

def GetSelectedUpperObjects():
	upperobjs=[]
	objs=FreeCADGui.Selection.getSelection() 
	for obj in objs:
		upperobjs.append(upperObject(obj))
	return upperobjs
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

#	import Common	Common.GetObjectBoundBox(App.ActiveDocument.Part)		
def GetObjectBoundBox(obj):
	if obj.TypeId=='App::Part':
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
