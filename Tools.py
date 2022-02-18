import FreeCADGui
import FreeCAD
import Part,PartGui 
from PySide import QtGui
from Common import ICONPATH
import Common
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

class Query():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'Query.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
				'ToolTip' : "Запросить информацию"}

	def Activated(self):
		try:
			d=FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0]
			if d.ShapeType=='Vertex':
				s=d.Point.__str__()	
			if d.ShapeType=='Edge':
				if d.Curve.TypeId=='Part::GeomLine':
					s="Длина "+round(d.Length,2).__str__()	
				else:
					s="Диаметр: "+ round((d.Curve.Radius*2),2).__str__()
			if d.ShapeType=='Face':
				s="Размеры: X="+ round(d.BoundBox.XLength,2).__str__()+"; Y="+ round(d.BoundBox.YLength,2).__str__()+"; Z="+ round(d.BoundBox.ZLength,2).__str__()
		except Exception:
			s="не выделенно"
		m = QtGui.QMessageBox()
		m.setText(s)
		m.exec_()
		return

	def IsActive(self):
		return True
		
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
		Common.localMode=not(index==0)
		#FreeCAD.Console.PrintMessage(PTPModeLocal)
		return	
	def GetDefaultCommand(self): # return the index of the tuple of the default command. This method is optional and when not implemented '0' is used 
		return 0

      
	def IsActive(self): # optional
		return True
FreeCADGui.addCommand('PTPModeL',PTPModeL()) 
FreeCADGui.addCommand('PTPModeG',PTPModeG()) 
FreeCADGui.addCommand('PTPMode',PTPMode()) 
FreeCADGui.addCommand('Box',Box()) 
FreeCADGui.addCommand('Query',Query()) 




