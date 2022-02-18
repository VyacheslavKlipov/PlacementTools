import FreeCADGui
import FreeCAD
import Part,PartGui 
from PySide import QtGui
from Common import ICONPATH

import Common
#ICONPATH = os.path.join(os.path.dirname(__file__), "resources")



def PTPLocal(lock):
		SelList=Common.getSelectionList()
		if SelList.__len__()<2: return
		sel1=SelList[SelList.__len__()-2]
		sel2=SelList[SelList.__len__()-1]
		if sel1[sel1.__len__()-1]=="" or sel2[sel2.__len__()-1]=="": return
		P1=Common.GetSelectedPoint(sel1[sel1.__len__()-2],sel1[sel1.__len__()-1])
		P2=Common.GetSelectedPoint(sel2[sel2.__len__()-2],sel2[sel2.__len__()-1])
		for sel in SelList: #удаляю 2 последних
			sel.pop()
			sel.pop()
		P1=Common.toGlobalCoordinates(sel1,P1)
		P2=Common.toGlobalCoordinates(sel2,P2)
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
		
		u=FreeCADGui.Selection.getSelection()
		i=0
		#FreeCAD.ActiveDocument.openTransaction("Move") 
		dP = P2-P1
		Path=Common.GetSelectedLowerObjectsPath()
		objs=Common.GetSelectedLowerObjects()		
		while i<objs.__len__()-1:
			obj = objs[i]
			a=Common.toGlobalCoordinates(Path[i],obj.Placement.Base)
			b=a+dP
			c=Common.toLocalCoordinates(Path[i],b)
			obj.Placement.Base=c
			i=i+1
		return		
def PTPLocalOld(lock):
		SelList=Common.getSelectionList()
		if SelList.__len__()<2: return
		sel1=SelList[SelList.__len__()-2]
		sel2=SelList[SelList.__len__()-1]
		if sel1[sel1.__len__()-1]=="" or sel2[sel2.__len__()-1]=="": return
		P1=Common.GetSelectedPoint(sel1[sel1.__len__()-2],sel1[sel1.__len__()-1])
		P2=Common.GetSelectedPoint(sel2[sel2.__len__()-2],sel2[sel2.__len__()-1])
		for sel in SelList: #удаляю 2 последних
			sel.pop()
			sel.pop()
		P1=Common.toGlobalCoordinates(sel1,P1)
		P2=Common.toGlobalCoordinates(sel2,P2)
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
		u=FreeCADGui.Selection.getSelection()
		i=0
		#FreeCAD.ActiveDocument.openTransaction("Move") 
		dP = P2-P1
		while i<u.__len__()-1:
			obj = u[i]
			if hasattr(obj,'_Body'): 
				obj=FreeCAD.ActiveDocument.getObject(SelList[i].pop())
			a=Common.toGlobalCoordinates(SelList[i],obj.Placement.Base)
			b=a+dP
			c=Common.toLocalCoordinates(SelList[i],b)
			obj.Placement.Base=c
			i=i+1
		return		
def dMoveLOld(dx=False,dy=False,dz=False):
	#objs=Common.GetSelectedLowerObjectsPath()
	u=FreeCADGui.Selection.getSelection()
	if len(u)==0: return
	msg=""
	if dx: msg="dX"
	if dy: msg="dY"
	if dz: msg="dZ"
	FreeCAD.ActiveDocument.openTransaction(msg)
	ret=QtGui.QInputDialog.getDouble(None,"",msg)
	if ret[1]:
		i=0
		SelList=Common.getSelectionList()
		for sel in SelList: #удаляю 2 последних
			sel.pop()
			sel.pop()
		while i<u.__len__():
			obj = u[i]
			if hasattr(obj,'_Body'): 
				obj=FreeCAD.ActiveDocument.getObject(SelList[i].pop())
			p=Common.toGlobalCoordinates(SelList[i],obj.Placement.Base)
			p.x=p.x+ret[0]*dx
			p.y=p.y+ret[0]*dy
			p.z=p.z+ret[0]*dz
			obj.Placement.Base=Common.toLocalCoordinates(SelList[i],p)
			i=i+1
	return		

def dMoveL(dx=False,dy=False,dz=False):
	#objs=Common.GetSelectedLowerObjectsPath()
	u=FreeCADGui.Selection.getSelection()
	if len(u)==0: return
	msg=""
	if dx: msg="dX"
	if dy: msg="dY"
	if dz: msg="dZ"
	FreeCAD.ActiveDocument.openTransaction(msg)
	ret=QtGui.QInputDialog.getDouble(None,"",msg)
	if ret[1]:
		i=0
		Path=Common.GetSelectedLowerObjectsPath()
		objs=Common.GetSelectedLowerObjects()
		while i<objs.__len__():
			obj = objs[i]
			p=Common.toGlobalCoordinates(Path[i],objs[i].Placement.Base)
			p.x=p.x+ret[0]*dx
			p.y=p.y+ret[0]*dy
			p.z=p.z+ret[0]*dz
			objs[i].Placement.Base=Common.toLocalCoordinates(Path[i],p)
			i=i+1
	return		
	
	
def dMoveG(dx=False,dy=False,dz=False):
	msg=""
	if dx: msg="dX"
	if dy: msg="dY"
	if dz: msg="dZ"	
	FreeCAD.ActiveDocument.openTransaction(msg)
	objs=Common.GetSelectedUpperObjects() 
	if objs.__len__() > 0:
		ret=QtGui.QInputDialog.getDouble(None,"",msg)
		if ret[1]:
			for obj in objs:
				obj.Placement.Base.x=obj.Placement.Base.x+ret[0]*dx
				obj.Placement.Base.y=obj.Placement.Base.y+ret[0]*dy
				obj.Placement.Base.z=obj.Placement.Base.z+ret[0]*dz
	return

class dX():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'dX.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : "Смещает объект на dX"}

	def Activated(self):
		if Common.localMode: 
			dMoveL(True,False,False)
		else:
			dMoveG(True,False,False)
		return
class dY():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'dY.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : "Смещает объект на dY"}

	def Activated(self):
		if Common.localMode: 
			dMoveL(False,True,False)
		else:
			dMoveG(False,True,False)
		return
class dZ():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'dZ.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : "Смещает объект на dZ"}

	def Activated(self):
		if Common.localMode: 
			dMoveL(False,False,True)
		else:
			dMoveG(False,False,True)
		return

class PointToPoint():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'PointToPoint.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : "Точка к точке"}
	def Activated(self,lock=0):
		if Common.localMode: 
			FreeCAD.ActiveDocument.openTransaction(self.__str__()) 
			PTPLocal(lock)
		else:
			self.PTPGroup(lock)
		return

	def PTPGroup(self,lock):
		SelList=Common.getParcedSelectionList()
		if SelList.__len__()<2: return
		sel1=SelList[SelList.__len__()-2]
		sel2=SelList[SelList.__len__()-1]
		if sel1[sel1.__len__()-1]=="" or sel2[sel2.__len__()-1]=="": return
		P1=Common.GetSelectedPoint(sel1[sel1.__len__()-2],sel1[sel1.__len__()-1])
		sel1.pop()
		sel1.pop()		
		P1=Common.toGlobalCoordinates(sel1,P1)
		P2=Common.GetSelectedPoint(sel2[sel2.__len__()-2],sel2[sel2.__len__()-1])
		sel2.pop()
		sel2.pop()
		P2=Common.toGlobalCoordinates(sel2,P2)
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
		u=Common.GetSelectedUpperObjects()
		i=0
		FreeCAD.ActiveDocument.openTransaction(self.__str__()) 
		dP = P2-P1
		while i<u.__len__()-1:
			u[i].Placement.Base=u[i].Placement.Base+dP
			i=i+1
		return		
class PointToPointX():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'PointToPointX.svg', # the name of a svg file available in the resources
				'ToolTip' : "Точка к точке только по X"}

	def Activated(self):
		PointToPoint().Activated(1)
		return			
class PointToPointY():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'PointToPointY.svg', # the name of a svg file available in the resources
				'ToolTip' : "Точка к точке только по Y"}

	def Activated(self):
		PointToPoint().Activated(2)
		return	
class PointToPointZ():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'PointToPointZ.svg', # the name of a svg file available in the resources
				'ToolTip' : "Точка к точке по Z"}

	def Activated(self):
		PointToPoint().Activated(3)
		return			

class StdMove():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'StdMove.svg', # the name of a svg file available in the resources
				'ToolTip' : "Transform"}

	def Activated(self):
		FreeCADGui.runCommand('Std_TransformManip')
		return			



				
FreeCADGui.addCommand('dX',dX()) 
FreeCADGui.addCommand('dY',dY()) 
FreeCADGui.addCommand('dZ',dZ()) 
FreeCADGui.addCommand('PointToPoint',PointToPoint()) 
FreeCADGui.addCommand('PointToPointX',PointToPointX()) 
FreeCADGui.addCommand('PointToPointY',PointToPointY()) 
FreeCADGui.addCommand('PointToPointZ',PointToPointZ()) 


FreeCADGui.addCommand('StdMove',StdMove()) 
