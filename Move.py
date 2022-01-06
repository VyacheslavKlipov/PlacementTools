import FreeCADGui
import FreeCAD
import Part,PartGui 
from PySide import QtGui
from Common import ICONPATH
from Common import GetSelectedUpperObjects
import Common
#ICONPATH = os.path.join(os.path.dirname(__file__), "resources")



class dX():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'dX.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Смещает объект на dX"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		if objs.__len__() > 0:
			ret=QtGui.QInputDialog.getDouble(None,"","dX")
			if ret[1]:
				for obj in objs:
					obj.Placement.Base.x=obj.Placement.Base.x+ret[0]
		return			

class dY():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'dY.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Смещает объект на dY"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		if objs.__len__() > 0:
			ret=QtGui.QInputDialog.getDouble(None,"","dY")
			if ret[1]:
				for obj in objs:
					obj.Placement.Base.y=obj.Placement.Base.y+ret[0]
		return			

class dZ():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'dZ.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Смещает объект на dZ"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		if objs.__len__() > 0:
			ret=QtGui.QInputDialog.getDouble(None,"","dZ")
			if ret[1]:
				for obj in objs:
					obj.Placement.Base.z=obj.Placement.Base.z+ret[0]
		return			

class PointToPoint():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'PointToPoint.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Точка к точке"}
	def Activated(self,lock=0):
		global PTPModeLocal
		#FreeCAD.Console.PrintMessage(PTPModeLocal)
		if PTPModeLocal: 
			self.PTPLocal(lock)
		else:
			self.PTPGroup(lock)
		return
	def PTPLocal(self,lock):
		#SelList=Common.getParcedSelectionList()
		SelList=Common.getSelectionList()
		if SelList.__len__()<2: return
		sel1=SelList[SelList.__len__()-2]
		sel2=SelList[SelList.__len__()-1]
		if sel1[sel1.__len__()-1]=="" or sel2[sel2.__len__()-1]=="": return
		P1=Common.GetSelectedPoint(sel1[sel1.__len__()-2],sel1[sel1.__len__()-1])
		P1=Common.toGlobalCoordinates(sel1,P1)
		P2=Common.GetSelectedPoint(sel2[sel2.__len__()-2],sel2[sel2.__len__()-1])
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
		#u=GetSelectedUpperObjects()
		u=FreeCADGui.Selection.getSelection()
		i=0
		FreeCAD.ActiveDocument.openTransaction(self.__str__()) 
		dP = P2-P1
		while i<u.__len__()-1:
			a=Common.toGlobalCoordinates(SelList[i],u[i].Placement.Base)
			b=a+dP
			c=Common.toLocalCoordinates(SelList[i],b)
			u[i].Placement.Base=c
			i=i+1
		return		
	def PTPGroup(self,lock):
		SelList=Common.getParcedSelectionList()
		if SelList.__len__()<2: return
		sel1=SelList[SelList.__len__()-2]
		sel2=SelList[SelList.__len__()-1]
		if sel1[sel1.__len__()-1]=="" or sel2[sel2.__len__()-1]=="": return
		P1=Common.GetSelectedPoint(sel1[sel1.__len__()-2],sel1[sel1.__len__()-1])
		P1=Common.toGlobalCoordinates(sel1,P1)
		P2=Common.GetSelectedPoint(sel2[sel2.__len__()-2],sel2[sel2.__len__()-1])
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
		u=GetSelectedUpperObjects()
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


class PTPModeG:
    def Activated(self, index):
        pass

    def GetResources(self):
        return { 'Pixmap'  : ICONPATH+'G.svg',
                 'MenuText': 'Учитывать группы'
                 }


class PTPModeL:
    def Activated(self, index):
        pass
        
    def GetResources(self):
        return { 'Pixmap'  : ICONPATH+'L.svg',
                 'MenuText': 'Локальные объекты'}


class PTPMode():
	def GetCommands(self):
		return ("PTPModeG", "PTPModeL") # a tuple of command names that you want to group
	def GetResources(self):
		return {	'ToolTip' : "Local/Group"}
		
	def Activated(self,index):
		global PTPModeLocal
		PTPModeLocal=not(index==0)
		#FreeCAD.Console.PrintMessage(PTPModeLocal)
		return	
	def GetDefaultCommand(self): # return the index of the tuple of the default command. This method is optional and when not implemented '0' is used 
		return 0

      
	def IsActive(self): # optional
		return True

PTPModeLocal = False					
FreeCADGui.addCommand('dX',dX()) 
FreeCADGui.addCommand('dY',dY()) 
FreeCADGui.addCommand('dZ',dZ()) 
FreeCADGui.addCommand('PointToPoint',PointToPoint()) 
FreeCADGui.addCommand('PointToPointX',PointToPointX()) 
FreeCADGui.addCommand('PointToPointY',PointToPointY()) 
FreeCADGui.addCommand('PointToPointZ',PointToPointZ()) 
FreeCADGui.addCommand('PTPModeL',PTPModeL()) 
FreeCADGui.addCommand('PTPModeG',PTPModeG()) 
FreeCADGui.addCommand('PTPMode',PTPMode()) 

FreeCADGui.addCommand('StdMove',StdMove()) 
