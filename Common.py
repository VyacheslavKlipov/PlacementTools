
import FreeCAD,FreeCADGui

import inspect, os.path
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))
#FreeCAD.Console.PrintMessage(path)

ICONPATH = path+'/Resources/icons/'

#ICONPATH = FreeCAD.getUserAppDataDir()+'Mod/PlacementTools/Resources/icons/'



def getParent(obj):
	for a in obj.InListRecursive:
		for b in a.ViewObject.claimChildren():
			if b == obj:
#				FreeCAD.Console.PrintMessage('|')
				return a
	return obj

def upperObject(obj):
#	FreeCAD.Console.PrintMessage('[upperObject]')
	par=getParent(obj)
	#FreeCAD.Console.PrintMessage(par.TypeId)
	if par==obj or par.TypeId=='App::DocumentObjectGroup' : 
	#obj.InList.__len__()>0:
		FreeCAD.Console.PrintMessage('[yes]')
		FreeCAD.Console.PrintMessage(obj.Label)
		FreeCAD.Console.PrintMessage(obj.TypeId)
		FreeCAD.Console.PrintMessage('***\n')
		return obj 
		#return upperObject(obj.InList[obj.InList.__len__()-1])
	else:
		FreeCAD.Console.PrintMessage('[no]')
		FreeCAD.Console.PrintMessage(par.Label)
		FreeCAD.Console.PrintMessage(par.TypeId)
		FreeCAD.Console.PrintMessage('***\n')
		return upperObject(par)
def GetSelectedUpperObjectsNew():
	upperobjs=[]
	objs=FreeCADGui.Selection.getSelection() 
	for obj in objs:
		upperobjs.append(upperObject(obj))
	return upperobjs

def GetSelectedUpperObjects():
	s=FreeCADGui.Selection.getSelectionEx("",0)
	upperobjs=[]
	if s.__len__()>0:
		if s.__len__()>1:
			for obj in s:
				upperobjs.append(obj.Object)
		else:
			n=s[0].SubElementNames	
			j=0
			cont=n.__len__()>1
			if not cont:
				j=j+1
			while cont:
				e=n[0].split(".")[j]
				i=1
				while i<n.__len__(): 
					if n[i].split(".")[j]==e:
						i=i+1
					else:
						cont=False
						i=n.__len__()
				j=j+1
			i=0
			j=j-1
			while i<n.__len__(): 
				upperobjs.append(FreeCAD.ActiveDocument.getObject(n[i].split(".")[j]))
				i=i+1
#	for o in upperobjs:
#		FreeCAD.Console.PrintMessage(o.Name)
#		FreeCAD.Console.PrintMessage('\n')
	return upperobjs #FreeCADGui.Selection.getSelection("",0) 
def GetSelectedUpperObjectsOld():
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
