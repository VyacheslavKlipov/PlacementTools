
# from importlib import reload  
# import Common  
# reload (Common)

import FreeCAD,FreeCADGui

import inspect, os.path
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))
#FreeCAD.Console.PrintMessage(path)

ICONPATH = path+'/Resources/icons/'

#ICONPATH = FreeCAD.getUserAppDataDir()+'Mod/PlacementTools/Resources/icons/'

def test(lock=0):
		SelList=getParcedSelectionList()
		if SelList.__len__()<2: return
		FreeCAD.Console.PrintMessage(SelList)
		FreeCAD.Console.PrintMessage("\n")
		
		sel1=SelList[SelList.__len__()-2]
		sel2=SelList[SelList.__len__()-1]
		if sel1[sel1.__len__()-1]=="" or sel2[sel2.__len__()-1]=="": return
		P1=GetSelectedPoint(sel1[sel1.__len__()-2],sel1[sel1.__len__()-1])
		P1=ResolveTransform(sel1,P1)
		P2=GetSelectedPoint(sel2[sel2.__len__()-2],sel2[sel2.__len__()-1])
		P2=ResolveTransform(sel2,P2)
		FreeCAD.Console.PrintMessage(P1)
		FreeCAD.Console.PrintMessage("\n")
		FreeCAD.Console.PrintMessage(P2)
		FreeCAD.Console.PrintMessage("\n")
		if lock==1:
			P1.y=0
			P2.y=0
			P1.z=0
			P2.z=0
		if lock==2:
			P1.x=0
			P2.x=0
			P1.z=0
			P2.z=0
		if lock==3:
			P1.y=0
			P2.y=0
			P1.x=0
			P2.x=0
		u=GetSelectedUpperObjects()
		
		i=0
		#FreeCAD.ActiveDocument.openTransaction(self.__str__()) 
		FreeCAD.ActiveDocument.openTransaction("sf") 
		while i<u.__len__()-1:
#			FreeCAD.Console.PrintMessage(u[i].Name)
			u[i].Placement.Base=u[i].Placement.Base+(P2-P1)
			i=i+1
		return		

def ResolveTransform (objList,point):
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
	FreeCAD.Console.PrintMessage(i)
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
	FreeCAD.Console.PrintMessage(getParcedSelectionList())
	FreeCAD.Console.PrintMessage("<<<")
	for obj in getParcedSelectionList():
		objs.append(FreeCAD.ActiveDocument.getObject(obj[0]))
	return objs	
	
def GetSelectedPoint(ObjName,ElementName):
		o=FreeCAD.ActiveDocument.getObject(ObjName).getSubObject(ElementName)
		if o.ShapeType=='Vertex':
			return	o.Point
		else:
			return o.CenterOfMass

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

def GetSelectedUpperObjectsOld():
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
def GetSelectedUpperObjectsOld1():
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
