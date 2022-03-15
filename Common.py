
#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2022 Vyacheslav Klipov                                  *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU General Public License (GPL)            *
#*   as published by the Free Software Foundation; either version 3 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU General Public License for more details.                          *
#*                                                                         *
#*   You should have received a copy of the GNU General Public             *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************
# from importlib import reload  
# import Common  
# reload (Common)


from importlib import reload 

import FreeCAD,FreeCADGui

import inspect, os.path
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))
localMode = False

#FreeCAD.Console.PrintMessage(path) t

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
	#FreeCAD.Console.PrintMessage(point)
	#FreeCAD.Console.PrintMessage(' - Global Point\n')
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
def GetSelectedLowerObjects():
	u=FreeCADGui.Selection.getSelection()
	if len(u)==0: return []
	i=0
	SelList=getSelectionList()
	for sel in SelList: #удаляю 2 последних
		sel.pop()
		sel.pop()
	while i<u.__len__():
		if hasattr(u[i],'_Body'): 
			u[i]=FreeCAD.ActiveDocument.getObject(SelList[i].pop())
		i=i+1
	return u
			
def GetSelectedLowerObjectsPath():
	u=FreeCADGui.Selection.getSelection()
	if len(u)==0: return []
	i=0
	SelList=getSelectionList()
	for sel in SelList: #удаляю 2 последних
		sel.pop()
		sel.pop()
	while i<u.__len__():
		if hasattr( u[i],'_Body'): 
			SelList[i].pop()
		i=i+1
	return SelList	
	
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

def GetMax(v):
	m=v[0]
	for i in v:
		if i>m: m=i
	return m
def GetMin(v):
	m=v[0]
	for i in v:
		if i<m: m=i
	return m
		
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


def GetBoundBoxFromGlobalCoordinates(Path,Obj):
	bb=GetObjectBoundBox(Obj)
	p1=toGlobalCoordinates(Path,FreeCAD.Vector(bb.XMin,bb.YMin,bb.ZMin))
	p2=toGlobalCoordinates(Path,FreeCAD.Vector(bb.XMax,bb.YMin,bb.ZMin))
	p3=toGlobalCoordinates(Path,FreeCAD.Vector(bb.XMax,bb.YMin,bb.ZMax))
	p4=toGlobalCoordinates(Path,FreeCAD.Vector(bb.XMin,bb.YMin,bb.ZMax))
	p5=toGlobalCoordinates(Path,FreeCAD.Vector(bb.XMin,bb.YMax,bb.ZMin))
	p6=toGlobalCoordinates(Path,FreeCAD.Vector(bb.XMax,bb.YMax,bb.ZMin))
	p7=toGlobalCoordinates(Path,FreeCAD.Vector(bb.XMax,bb.YMax,bb.ZMax))
	p8=toGlobalCoordinates(Path,FreeCAD.Vector(bb.XMin,bb.YMax,bb.ZMax))
	bb.XMin=GetMin([p1.x,p2.x,p3.x,p4.x,p5.x,p6.x,p7.x,p8.x])
	bb.XMax=GetMax([p1.x,p2.x,p3.x,p4.x,p5.x,p6.x,p7.x,p8.x])
	bb.YMin=GetMin([p1.y,p2.y,p3.y,p4.y,p5.y,p6.y,p7.y,p8.y])
	bb.YMax=GetMax([p1.y,p2.y,p3.y,p4.y,p5.y,p6.y,p7.y,p8.y])
	bb.ZMin=GetMin([p1.z,p2.z,p3.z,p4.z,p5.z,p6.z,p7.z,p8.z])
	bb.ZMax=GetMax([p1.z,p2.z,p3.z,p4.z,p5.z,p6.z,p7.z,p8.z])
	return bb
				 
	 # v=App.Vector(b.Shape.BoundBox.XMax,b.Shape.BoundBox.YMax,b.Shape.BoundBox.ZMax)
	 #App.ActiveDocument.Part.Placement.multiply( App.Placement(v,App.ActiveDocument.Part.Placement.Rotation))
