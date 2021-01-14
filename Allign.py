import FreeCADGui
import FreeCAD
import Part,PartGui 
from PySide import QtGui
from Common import ICONPATH
from Common import GetSelectedUpperObjects
#ICONPATH = os.path.join(os.path.dirname(__file__), "resources")

class Box():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'temp.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : "box"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
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
			a=objs[objs.__len__()-1].Shape.BoundBox.XMin
			for obj in objs:
				obj.Placement.Base.x=a+(obj.Placement.Base.x-obj.Shape.BoundBox.XMin)
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
			a=objs[objs.__len__()-1].Shape.BoundBox.XMax
			for obj in objs:
				obj.Placement.Base.x=a-(obj.Shape.BoundBox.XMax-obj.Placement.Base.x)
				
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
			a=objs[objs.__len__()-1].Shape.BoundBox.YMin
			for obj in objs:
				obj.Placement.Base.y=a+(obj.Placement.Base.y-obj.Shape.BoundBox.YMin)
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
			a=objs[objs.__len__()-1].Shape.BoundBox.YMax
			for obj in objs:
				obj.Placement.Base.y=a-(obj.Shape.BoundBox.YMax-obj.Placement.Base.y)
				
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
			a=objs[objs.__len__()-1].Shape.BoundBox.ZMin
			for obj in objs:
				obj.Placement.Base.z=a+(obj.Placement.Base.z-obj.Shape.BoundBox.ZMin)
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
			a=objs[objs.__len__()-1].Shape.BoundBox.ZMax
			for obj in objs:
				obj.Placement.Base.z=a-(obj.Shape.BoundBox.ZMax-obj.Placement.Base.z)
				
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
			a=objs[i].Shape.BoundBox.XMin+(objs[i].Shape.BoundBox.XMax-objs[i].Shape.BoundBox.XMin)/2.0
			for obj in objs:
				obj.Placement.Base.x=obj.Placement.Base.x+a-(obj.Shape.BoundBox.XMin+((obj.Shape.BoundBox.XMax-obj.Shape.BoundBox.XMin)/2.0))
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
			a=objs[i].Shape.BoundBox.YMin+(objs[i].Shape.BoundBox.YMax-objs[i].Shape.BoundBox.YMin)/2.0
			for obj in objs:
				obj.Placement.Base.y=obj.Placement.Base.y+a-(obj.Shape.BoundBox.YMin+((obj.Shape.BoundBox.YMax-obj.Shape.BoundBox.YMin)/2.0))
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
			a=objs[i].Shape.BoundBox.ZMin+(objs[i].Shape.BoundBox.ZMax-objs[i].Shape.BoundBox.ZMin)/2.0
			for obj in objs:
				obj.Placement.Base.z=obj.Placement.Base.z+a-(obj.Shape.BoundBox.ZMin+((obj.Shape.BoundBox.ZMax-obj.Shape.BoundBox.ZMin)/2.0))
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
			a=objs[i].Shape.BoundBox.XMax
			j=0
			while j<i:
				objs[j].Placement.Base.x=objs[j].Placement.Base.x+a-objs[j].Shape.BoundBox.XMin
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
			a=objs[i].Shape.BoundBox.XMin
			j=0
			while j<i:
				objs[j].Placement.Base.x=objs[j].Placement.Base.x-(objs[j].Shape.BoundBox.XMax-a)
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
			a=objs[i].Shape.BoundBox.YMax
			j=0
			while j<i:
				objs[j].Placement.Base.y=objs[j].Placement.Base.y+a-objs[j].Shape.BoundBox.YMin
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
			a=objs[i].Shape.BoundBox.YMin
			j=0
			while j<i:
				objs[j].Placement.Base.y=objs[j].Placement.Base.y-(objs[j].Shape.BoundBox.YMax-a)
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
			a=objs[i].Shape.BoundBox.ZMax
			j=0
			while j<i:
				objs[j].Placement.Base.z=objs[j].Placement.Base.z+a-objs[j].Shape.BoundBox.ZMin
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
			a=objs[i].Shape.BoundBox.ZMin
			j=0
			while j<i:
				objs[j].Placement.Base.z=objs[j].Placement.Base.z-(objs[j].Shape.BoundBox.ZMax-a)
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
			a=(objs[i+1].Shape.BoundBox.XMax-objs[i].Shape.BoundBox.XMin)/2.0+objs[i].Shape.BoundBox.XMin
			j=0
			while j<i:
				objs[j].Placement.Base.x=objs[j].Placement.Base.x+a-(objs[j].Shape.BoundBox.XMin+((objs[j].Shape.BoundBox.XMax-objs[j].Shape.BoundBox.XMin)/2.0))
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
			a=(objs[i+1].Shape.BoundBox.YMax-objs[i].Shape.BoundBox.YMin)/2.0+objs[i].Shape.BoundBox.YMin
			j=0
			while j<i:
				objs[j].Placement.Base.y=objs[j].Placement.Base.y+a-(objs[j].Shape.BoundBox.YMin+((objs[j].Shape.BoundBox.YMax-objs[j].Shape.BoundBox.YMin)/2.0))
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
			a=(objs[i+1].Shape.BoundBox.ZMax-objs[i].Shape.BoundBox.ZMin)/2.0+objs[i].Shape.BoundBox.ZMin
			j=0
			while j<i:
				objs[j].Placement.Base.z=objs[j].Placement.Base.z+a-(objs[j].Shape.BoundBox.ZMin+((objs[j].Shape.BoundBox.ZMax-objs[j].Shape.BoundBox.ZMin)/2.0))
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


