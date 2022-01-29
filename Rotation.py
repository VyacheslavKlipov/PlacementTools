import FreeCADGui
import FreeCAD
import Part,PartGui 
from PySide import QtGui
from Common import ICONPATH
from Common import GetSelectedUpperObjects
from Common import GetObjectBoundBox

def testRotate(obj,x,y,z):
	c=obj.Placement.Rotation.inverted().multVec(GetObjectBoundBox(obj).Center.sub(obj.Placement.Base))
	if x!=0: obj.Placement.rotate(c,FreeCAD.Vector(1,0,0),x) 
	if y!=0: obj.Placement.rotate(c,FreeCAD.Vector(0,1,0),y)
	if z!=0: obj.Placement.rotate(c,FreeCAD.Vector(0,0,1),z)
	return

def Rotate(obj,x,y,z):
	c=GetObjectBoundBox(obj).Center
	a=obj.Placement.Rotation
	obj.Placement.Rotation=FreeCAD.Rotation(z,y,x)
	obj.Placement.Rotation=obj.Placement.Rotation.multiply(a)
	obj.Placement.Base=obj.Placement.Base+c.sub(GetObjectBoundBox(obj).Center)
	return
def delRotateOld(obj,x,y,z):
	a=obj.Placement.Rotation.toEuler()
	FreeCAD.Console.PrintMessage(a)
	FreeCAD.Console.PrintMessage('\n')
	i=0
	b=[]
	r=[]
	r.append(z)
	r.append(y)
	r.append(x)
	while i<3:
#		FreeCAD.Console.PrintMessage(i)
		c=a[i]+r[i]
		if c>=360:
			c=c-360
		if c<=-360:
			c=c+360
		b.append(c)
		i=i+1
	d=FreeCAD.Rotation(b[0],b[1],b[2])
	#FreeCAD.Console.PrintMessage(b)
	#FreeCAD.Console.PrintMessage(d)
	obj.Placement.Rotation=d
	return
class rX90():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'rX90.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : "Поворачивает объект на 90 градусов по оси X"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		for obj in objs:
			Rotate(obj,90,0,0)
					
		return			
class rY90():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'rY90.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : "Поворачивает объект на 90 градусов по оси Y"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		for obj in objs:
			Rotate(obj,0,90,0)
					
		return		
class rZ90():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'rZ90.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : "Поворачивает объект на 90 градусов по оси Z"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		for obj in objs:
			Rotate(obj,0,0,90)
					
		return			
class rX_90():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'rX_90.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : "Поворачивает объект на -90 градусов по оси X"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		for obj in objs:
			Rotate(obj,-90,0,0)
					
		return			
class rY_90():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'rY_90.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : "Поворачивает объект на -90 градусов по оси Y"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		for obj in objs:
			Rotate(obj,0,-90,0)
					
		return		
class rZ_90():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'rZ_90.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : "Поворачивает объект на -90 градусов по оси Z"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		for obj in objs:
			Rotate(obj,0,0,-90)
					
		return		
class rX():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'rX.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : "Поворачивает объект на r градусов по оси X"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		if objs.__len__() > 0:
			ret=QtGui.QInputDialog.getDouble(None,"","rX")
			if ret[1]:
				for obj in objs:
					Rotate(obj,ret[0],0,0)
		return	
class rY():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'rY.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : "Поворачивает объект на r градусов по оси Y"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		if objs.__len__() > 0:
			ret=QtGui.QInputDialog.getDouble(None,"","rY")
			if ret[1]:
				for obj in objs:
					Rotate(obj,0,ret[0],0)
		return		
class rZ():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'rZ.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : "Поворачивает объект на r градусов по оси Z"}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		objs=GetSelectedUpperObjects() 
		if objs.__len__() > 0:
			ret=QtGui.QInputDialog.getDouble(None,"","rZ")
			if ret[1]:
				for obj in objs:
					Rotate(obj,0,0,ret[0])
		return		
FreeCADGui.addCommand('rX90',rX90())
FreeCADGui.addCommand('rY90',rY90())
FreeCADGui.addCommand('rZ90',rZ90())
FreeCADGui.addCommand('rX_90',rX_90())
FreeCADGui.addCommand('rY_90',rY_90())
FreeCADGui.addCommand('rZ_90',rZ_90())
FreeCADGui.addCommand('rX',rX())
FreeCADGui.addCommand('rY',rY())
FreeCADGui.addCommand('rZ',rZ())
