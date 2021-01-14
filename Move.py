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

	def RotationCorrect(self,obj,point):
		uobj=Common.getParent(obj)
		if uobj!=obj:
#			obj.InList.__len__()>0:
#			FreeCAD.Console.PrintMessage(uobj.Label)
#			FreeCAD.Console.PrintMessage('\n')
			if uobj.TypeId=='PartDesign::Body' or uobj.TypeId=='App::Part' or uobj.TypeId=='App::Link':
				return self.RotationCorrect(uobj,uobj.Placement.multiply(FreeCAD.Placement(point,uobj.Placement.Rotation)).Base)
			else :
				return point
		else:
			return point
	def GetSelectedPoint(self,i,j):
		#FreeCAD.Console.PrintMessage(i)
		a=FreeCADGui.Selection.getSelectionEx() 
		P=[]
		b=a[i]
		c=b.SubObjects
		if j>(c.__len__()-1):
			j=c.__len__()-1
		d=c[j]
		if d.ShapeType=='Vertex':
			#FreeCAD.Console.PrintMessage(d.Point)
			return	d.Point
		else:
			return d.CenterOfMass

	def Activated(self,lock=0):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		o=FreeCADGui.Selection.getSelection() 
		
		i=o.__len__()-1
		if i>=0:
			if i==0:
				P2=self.RotationCorrect(o[i],self.GetSelectedPoint(i,1))
				P1=self.RotationCorrect(o[i],self.GetSelectedPoint(i,0))
#				if o[i].TypeId=='PartDesign::Body':
#					P1=o[i].Placement.multiply(FreeCAD.Placement(P1,o[i].Placement.Rotation)).Base
#					P2=o[i].Placement.multiply(FreeCAD.Placement(P2,o[i].Placement.Rotation)).Base
			else:
				P2=self.RotationCorrect(o[i],self.GetSelectedPoint(i,0))
#				if o[i].TypeId=='PartDesign::Body':
#					P2=o[i].Placement.multiply(FreeCAD.Placement(P2,o[i].Placement.Rotation)).Base
				i=i-1
				P1=self.RotationCorrect(o[i],self.GetSelectedPoint(i,0))
#				if o[i].TypeId=='PartDesign::Body':
#					P1=o[i].Placement.multiply(FreeCAD.Placement(P1,o[i].Placement.Rotation)).Base
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
			while i>=0:
	#			FreeCAD.Console.PrintMessage("************")
	#			FreeCAD.Console.PrintMessage(P1)
	#			FreeCAD.Console.PrintMessage("\n")
	#			FreeCAD.Console.PrintMessage(P2)
	#			FreeCAD.Console.PrintMessage("\n")
				u=Common.upperObject(o[i])
				u.Placement.Base=u.Placement.Base+(P2-P1)
				i=i-1
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
				
FreeCADGui.addCommand('dX',dX()) 
FreeCADGui.addCommand('dY',dY()) 
FreeCADGui.addCommand('dZ',dZ()) 
FreeCADGui.addCommand('PointToPoint',PointToPoint()) 
FreeCADGui.addCommand('PointToPointX',PointToPointX()) 
FreeCADGui.addCommand('PointToPointY',PointToPointY()) 
FreeCADGui.addCommand('PointToPointZ',PointToPointZ()) 
