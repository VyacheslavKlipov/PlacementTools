import FreeCADGui
import FreeCAD
import Part,PartGui 
from PySide import QtGui
from Common import ICONPATH
from Common import GetSelectedUpperObjects
from Common import GetObjectBoundBox
#ICONPATH = os.path.join(os.path.dirname(__file__), "resources")

class Box():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'temp.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "box"}

	def Activated(self):
		#FreeCAD.ActiveDocument.openTransaction(self.__str__())
		cube = Part.makeBox(2, 2, 2)
		Part.show(cube)
		cube = Part.makeBox(3, 3, 4)
		cube.Placement.Base.x =20
		Part.show(cube)
		cube = Part.makeCylinder(3,3)
		cube.Placement.Base.x =50
		Part.show(cube)
		return

	def IsActive(self):
		"""Here you can define if the command must be active or not (greyed) if certain conditions
		are met or not. This function is optional."""
		return True
		#FreeCAD.ActiveDocument.recompute()		
		
		#FreeCADGui.removeWorkbench("MyWorkbench")
		#import  InitGui
		#FreeCADGui.addWorkbench(MyWorkbench())

class AllignLeft():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AllignLeft.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Выравнивает объекты по левой границе"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		if objs.__len__() > 0:
			a=GetObjectBoundBox(objs[objs.__len__()-1]).XMin
			for obj in objs:
				obj.Placement.Base.x=a+(obj.Placement.Base.x-GetObjectBoundBox(obj).XMin)
		return
		
class AllignRight():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AllignRight.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Выравнивает объекты по правой границе"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		if objs.__len__() > 0:
			a=GetObjectBoundBox(objs[objs.__len__()-1]).XMax
			for obj in objs:
				obj.Placement.Base.x=a-(GetObjectBoundBox(obj).XMax-obj.Placement.Base.x)
				
		return
#####################################################################################################3
class AllignFront():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AllignFront.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Выравнивает объекты по передней границе"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		if objs.__len__() > 0:
			a=GetObjectBoundBox(objs[objs.__len__()-1]).YMin
			for obj in objs:
				obj.Placement.Base.y=a+(obj.Placement.Base.y-GetObjectBoundBox(obj).YMin)
		return
		
class AllignRear():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AllignRear.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Выравнивает объекты по задней границе"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		if objs.__len__() > 0:
			a=GetObjectBoundBox(objs[objs.__len__()-1]).YMax
			for obj in objs:
				obj.Placement.Base.y=a-(GetObjectBoundBox(obj).YMax-obj.Placement.Base.y)
				
		return
#####################################################################################################3
class AllignBottom():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AllignBottom.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Выравнивает объекты по нижней границе"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		if objs.__len__() > 0:
			a=GetObjectBoundBox(objs[objs.__len__()-1]).ZMin
			for obj in objs:
				obj.Placement.Base.z=a+(obj.Placement.Base.z-GetObjectBoundBox(obj).ZMin)
		return
		
class AllignTop():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AllignTop.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Выравнивает объекты по верхней границе"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		if objs.__len__() > 0:
			a=GetObjectBoundBox(objs[objs.__len__()-1]).ZMax
			for obj in objs:
				obj.Placement.Base.z=a-(GetObjectBoundBox(obj).ZMax-obj.Placement.Base.z)
				
		return
class AllignXCenter():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AllignXCenter.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Выравнивает объекты по центру оси X"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		if objs.__len__() > 0:
			i=objs.__len__()-1
			bb=GetObjectBoundBox(objs[i])
			a=bb.XMin+(bb.XMax-bb.XMin)/2.0
			for obj in objs:
				bb=GetObjectBoundBox(obj)
				obj.Placement.Base.x=obj.Placement.Base.x+a-(bb.XMin+((bb.XMax-bb.XMin)/2.0))
		return
class AllignYCenter():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AllignYCenter.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Выравнивает объекты по центру оси Y"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		if objs.__len__() > 0:
			i=objs.__len__()-1
			bb=GetObjectBoundBox(objs[i])
			a=bb.YMin+(bb.YMax-bb.YMin)/2.0
			for obj in objs:
				bb=GetObjectBoundBox(obj)
				obj.Placement.Base.y=obj.Placement.Base.y+a-(bb.YMin+((bb.YMax-bb.YMin)/2.0))
		return
class AllignZCenter():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AllignZCenter.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Выравнивает объекты по центру оси Z"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		if objs.__len__() > 0:
			i=objs.__len__()-1
			bb=GetObjectBoundBox(objs[i])
			a=bb.ZMin+(bb.ZMax-bb.ZMin)/2.0
			for obj in objs:
				bb=GetObjectBoundBox(obj)
				obj.Placement.Base.z=obj.Placement.Base.z+a-(bb.ZMin+((bb.ZMax-bb.ZMin)/2.0))
		return				
class RightOf():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'RightOf.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Располагает объект справа объектa"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		i=objs.__len__()-1
		if i > 0:
			a=GetObjectBoundBox(objs[i]).XMax
			j=0
			while j<i:
				objs[j].Placement.Base.x=objs[j].Placement.Base.x+a-GetObjectBoundBox(objs[j]).XMin
				j=j+1
		return		
class LeftOf():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'LeftOf.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Располагает объект слева объектa"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		i=objs.__len__()-1
		if i > 0:
			a=GetObjectBoundBox(objs[i]).XMin
			j=0
			while j<i:
				objs[j].Placement.Base.x=objs[j].Placement.Base.x-(GetObjectBoundBox(objs[j]).XMax-a)
				j=j+1
		return		
####################################################################
class BehindOf():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'BehindOf.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Располагает объект за объектом"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		i=objs.__len__()-1
		if i > 0:
			a=GetObjectBoundBox(objs[i]).YMax
			j=0
			while j<i:
				objs[j].Placement.Base.y=objs[j].Placement.Base.y+a-GetObjectBoundBox(objs[j]).YMin
				j=j+1
		return		
class FrontOf():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'FrontOf.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Располагает объект перед объектом"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		i=objs.__len__()-1
		if i > 0:
			a=GetObjectBoundBox(objs[i]).YMin
			j=0
			while j<i:
				objs[j].Placement.Base.y=objs[j].Placement.Base.y-(GetObjectBoundBox(objs[j]).YMax-a)
				j=j+1
		return		
###############3
class OverOf():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'OverOf.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Располагает объект над объектом"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		i=objs.__len__()-1
		if i > 0:
			a=GetObjectBoundBox(objs[i]).ZMax
			j=0
			while j<i:
				objs[j].Placement.Base.z=objs[j].Placement.Base.z+a-GetObjectBoundBox(objs[j]).ZMin
				j=j+1
		return		
class UnderOf():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'UnderOf.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Располагает объект под объектом"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		i=objs.__len__()-1
		if i > 0:
			a=GetObjectBoundBox(objs[i]).ZMin
			j=0
			while j<i:
				objs[j].Placement.Base.z=objs[j].Placement.Base.z-(GetObjectBoundBox(objs[j]).ZMax-a)
				j=j+1
		return		
				
class MiddleXOf():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'MiddleXOf.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Располагает объект между думя объектами по X"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		i=objs.__len__()-2
		if i > 0:
			bb=GetObjectBoundBox(objs[i])
			a=(GetObjectBoundBox(objs[i+1]).XMax-bb.XMin)/2.0+bb.XMin
			j=0
			while j<i:
				bb=GetObjectBoundBox(objs[j])
				objs[j].Placement.Base.x=objs[j].Placement.Base.x+a-(bb.XMin+((bb.XMax-bb.XMin)/2.0))
				j=j+1
		return		
class MiddleYOf():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'MiddleYOf.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Располагает объект между думя объектами по Y"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		i=objs.__len__()-2
		if i > 0:
			bb=GetObjectBoundBox(objs[i])
			a=(GetObjectBoundBox(objs[i+1]).YMax-bb.YMin)/2.0+bb.YMin
			j=0
			while j<i:
				bb=GetObjectBoundBox(objs[j])
				objs[j].Placement.Base.y=objs[j].Placement.Base.y+a-(bb.YMin+((bb.YMax-bb.YMin)/2.0))
				j=j+1
		return		
class MiddleZOf():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'MiddleZOf.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "Располагает объект между думя объектами по Z"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		i=objs.__len__()-2
		if i > 0:
			bb=GetObjectBoundBox(objs[i])
			a=(GetObjectBoundBox(objs[i+1]).ZMax-bb.ZMin)/2.0+bb.ZMin
			j=0
			while j<i:
				bb=GetObjectBoundBox(objs[j])
				objs[j].Placement.Base.z=objs[j].Placement.Base.z+a-(bb.ZMin+((bb.ZMax-bb.ZMin)/2.0))
				j=j+1
		return				


FreeCADGui.addCommand('Box',Box()) 
FreeCADGui.addCommand('AllignLeft',AllignLeft()) 
FreeCADGui.addCommand('AllignRight',AllignRight()) 
FreeCADGui.addCommand('AllignRear',AllignRear()) 
FreeCADGui.addCommand('AllignFront',AllignFront()) 
FreeCADGui.addCommand('AllignBottom',AllignBottom()) 
FreeCADGui.addCommand('AllignTop',AllignTop()) 

FreeCADGui.addCommand('AllignXCenter',AllignXCenter()) 
FreeCADGui.addCommand('AllignYCenter',AllignYCenter()) 
FreeCADGui.addCommand('AllignZCenter',AllignZCenter()) 

FreeCADGui.addCommand('RightOf',RightOf()) 
FreeCADGui.addCommand('LeftOf',LeftOf()) 
FreeCADGui.addCommand('BehindOf',BehindOf()) 
FreeCADGui.addCommand('FrontOf',FrontOf()) 
FreeCADGui.addCommand('OverOf',OverOf()) 
FreeCADGui.addCommand('UnderOf',UnderOf()) 

FreeCADGui.addCommand('MiddleXOf',MiddleXOf()) 
FreeCADGui.addCommand('MiddleYOf',MiddleYOf()) 
FreeCADGui.addCommand('MiddleZOf',MiddleZOf()) 


