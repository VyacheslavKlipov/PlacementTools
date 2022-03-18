import FreeCADGui
import FreeCAD
import Part,PartGui 
from PySide import QtGui
from Common import ICONPATH
import Common

translate = FreeCAD.Qt.translate
def QT_TRANSLATE_NOOP(context, text):
	return translate(context, text)
	
#ICONPATH = os.path.join(os.path.dirname(__file__), "resources")

class Box():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'temp.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Allign Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Create test objects")}

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
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Request information about the selected element. If an edge is selected, then its length is returned, if a circle, then its diameter, if a point, then its coordinates, if a face, then its dimensions.")}

	def Activated(self):
		try:
			d=FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0]
			if d.ShapeType=='Vertex':
				s=d.Point.__str__()	
			if d.ShapeType=='Edge':
				if d.Curve.TypeId=='Part::GeomLine':
					s=translate('PlacementTools',"Length ")+round(d.Length,2).__str__()	
				else:
					s=translate('PlacementTools',"Diameter: ")+ round((d.Curve.Radius*2),2).__str__()
			if d.ShapeType=='Face':
				s=translate('PlacementTools',"Dimensions: ")+"X="+ round(d.BoundBox.XLength,2).__str__()+"; Y="+ round(d.BoundBox.YLength,2).__str__()+"; Z="+ round(d.BoundBox.ZLength,2).__str__()
		except Exception:
			s=translate('PlacementTools',"nothing selected")
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
				 'MenuText': QT_TRANSLATE_NOOP('PlacementTools',"With groups"),
                 'ToolTip': QT_TRANSLATE_NOOP('PlacementTools','If at least one object of a group is selected, then all the tools of this workbench will be applied to the entire group. If all selected objects are within the same group, then all tools of this workbench will be applied only to the selected objects. Groups are objects Part, Link Group, etc.')
                 
                 }


class PTPModeL:
    def Activated(self, index):
        pass
        
    def GetResources(self):
        return { 'Pixmap'  : ICONPATH+'L.svg',
				 'MenuText': QT_TRANSLATE_NOOP('PlacementTools',"Local only"),
                 'ToolTip': QT_TRANSLATE_NOOP('PlacementTools','All tools of this workbench will be applied to objects locally, regardless of whether they belong to groups. Groups are objects Part, Link Group, etc.')}
				

class PTPMode():
	def GetCommands(self):
		return ("PTPModeG", "PTPModeL") # a tuple of command names that you want to group
	def GetResources(self):
		return {	'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Local/Group")}
		
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




