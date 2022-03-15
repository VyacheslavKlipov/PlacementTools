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
import FreeCADGui
import FreeCAD
import Part,PartGui 
from Common import ICONPATH
from Common import GetSelectedUpperObjects
from Common import GetObjectBoundBox
import Common
#ICONPATH = os.path.join(os.path.dirname(__file__), "resources")

translate = FreeCAD.Qt.translate
def QT_TRANSLATE_NOOP(context, text):
	return text


class AlignLeft():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AlignLeft.svg', 
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Aligns objects to the left") }

	
	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			i=0
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			bb_a=Common.GetBoundBoxFromGlobalCoordinates(Path[Path.__len__()-1],objs[objs.__len__()-1])
			while i<objs.__len__():
				bb_i=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				base_i=Common.toGlobalCoordinates(Path[i],objs[i].Placement.Base)
				base_i.x=bb_a.XMin+(base_i.x-bb_i.XMin)			
				objs[i].Placement.Base=Common.toLocalCoordinates(Path[i],base_i)
				i=i+1			
		else:
			objs=GetSelectedUpperObjects() 
			if objs.__len__() > 0:
				a=GetObjectBoundBox(objs[objs.__len__()-1]).XMin
				for obj in objs:
					obj.Placement.Base.x=a+(obj.Placement.Base.x-GetObjectBoundBox(obj).XMin)
		return
		
class AlignRight():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AlignRight.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Aligns objects to the right")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			i=0
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			bb_a=Common.GetBoundBoxFromGlobalCoordinates(Path[Path.__len__()-1],objs[objs.__len__()-1])
			while i<objs.__len__():
				bb_i=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				base_i=Common.toGlobalCoordinates(Path[i],objs[i].Placement.Base)
				base_i.x=bb_a.XMax-(bb_i.XMax-base_i.x)			
				objs[i].Placement.Base=Common.toLocalCoordinates(Path[i],base_i)
				i=i+1			
		else:
			objs=GetSelectedUpperObjects() 
			if objs.__len__() > 0:
				a=GetObjectBoundBox(objs[objs.__len__()-1]).XMax
				for obj in objs:
					obj.Placement.Base.x=a-(GetObjectBoundBox(obj).XMax-obj.Placement.Base.x)
		return
#####################################################################################################3
class AlignFront():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AlignFront.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Aligns objects to the front")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			i=0
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			bb_a=Common.GetBoundBoxFromGlobalCoordinates(Path[Path.__len__()-1],objs[objs.__len__()-1])
			while i<objs.__len__():
				bb_i=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				base_i=Common.toGlobalCoordinates(Path[i],objs[i].Placement.Base)
				base_i.y=bb_a.YMin+(base_i.y-bb_i.YMin)			
				objs[i].Placement.Base=Common.toLocalCoordinates(Path[i],base_i)
				i=i+1			
		else:
			objs=GetSelectedUpperObjects() 
			if objs.__len__() > 0:
				a=GetObjectBoundBox(objs[objs.__len__()-1]).YMin
				for obj in objs:
					obj.Placement.Base.y=a+(obj.Placement.Base.y-GetObjectBoundBox(obj).YMin)
		return
		
class AlignRear():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AlignRear.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Aligns objects to the back")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			i=0
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			bb_a=Common.GetBoundBoxFromGlobalCoordinates(Path[Path.__len__()-1],objs[objs.__len__()-1])
			while i<objs.__len__():
				bb_i=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				base_i=Common.toGlobalCoordinates(Path[i],objs[i].Placement.Base)
				base_i.y=bb_a.YMax-(bb_i.YMax-base_i.y)			
				objs[i].Placement.Base=Common.toLocalCoordinates(Path[i],base_i)
				i=i+1			
		else:
			objs=GetSelectedUpperObjects() 
			if objs.__len__() > 0:
				a=GetObjectBoundBox(objs[objs.__len__()-1]).YMax
				for obj in objs:
					obj.Placement.Base.y=a-(GetObjectBoundBox(obj).YMax-obj.Placement.Base.y)
				
		return
#####################################################################################################3
class AlignBottom():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AlignBottom.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"ВAligns objects to the bottom")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			i=0
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			bb_a=Common.GetBoundBoxFromGlobalCoordinates(Path[Path.__len__()-1],objs[objs.__len__()-1])
			while i<objs.__len__():
				bb_i=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				base_i=Common.toGlobalCoordinates(Path[i],objs[i].Placement.Base)
				base_i.z=bb_a.ZMin+(base_i.z-bb_i.ZMin)			
				objs[i].Placement.Base=Common.toLocalCoordinates(Path[i],base_i)
				i=i+1			
		else:
			objs=GetSelectedUpperObjects() 
			if objs.__len__() > 0:
				a=GetObjectBoundBox(objs[objs.__len__()-1]).ZMin
				for obj in objs:
					obj.Placement.Base.z=a+(obj.Placement.Base.z-GetObjectBoundBox(obj).ZMin)
		return
		
class AlignTop():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AlignTop.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Aligns objects to the top")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			i=0
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			bb_a=Common.GetBoundBoxFromGlobalCoordinates(Path[Path.__len__()-1],objs[objs.__len__()-1])
			while i<objs.__len__():
				bb_i=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				base_i=Common.toGlobalCoordinates(Path[i],objs[i].Placement.Base)
				base_i.z=bb_a.ZMax-(bb_i.ZMax-base_i.z)			
				objs[i].Placement.Base=Common.toLocalCoordinates(Path[i],base_i)
				i=i+1			
		else:
			objs=GetSelectedUpperObjects() 
			if objs.__len__() > 0:
				a=GetObjectBoundBox(objs[objs.__len__()-1]).ZMax
				for obj in objs:
					obj.Placement.Base.z=a-(GetObjectBoundBox(obj).ZMax-obj.Placement.Base.z)					
		return
class AlignXCenter():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AlignXCenter.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Aligns objects to the center of the x-axis")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			if objs.__len__() > 0:
				i=objs.__len__()-1
				bb=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				a=bb.XMin+(bb.XMax-bb.XMin)/2.0
				j=0
				while j<objs.__len__():
					bb_j=Common.GetBoundBoxFromGlobalCoordinates(Path[j],objs[j])			
					base_j=Common.toGlobalCoordinates(Path[j],objs[j].Placement.Base)
					base_j.x=base_j.x+a-(bb_j.XMin+((bb_j.XMax-bb_j.XMin)/2.0))			
					objs[j].Placement.Base=Common.toLocalCoordinates(Path[j],base_j)
					j=j+1			
		else:
			objs=GetSelectedUpperObjects() 
			if objs.__len__() > 0:
				i=objs.__len__()-1
				bb=GetObjectBoundBox(objs[i])
				a=bb.XMin+(bb.XMax-bb.XMin)/2.0
				for obj in objs:
					bb=GetObjectBoundBox(obj)
					obj.Placement.Base.x=obj.Placement.Base.x+a-(bb.XMin+((bb.XMax-bb.XMin)/2.0))
		return
class AlignYCenter():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AlignYCenter.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Aligns objects to the center of the y-axis")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			if objs.__len__() > 0:
				i=objs.__len__()-1
				bb=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				a=bb.YMin+(bb.YMax-bb.YMin)/2.0
				j=0
				while j<objs.__len__():
					bb_j=Common.GetBoundBoxFromGlobalCoordinates(Path[j],objs[j])			
					base_j=Common.toGlobalCoordinates(Path[j],objs[j].Placement.Base)
					base_j.y=base_j.y+a-(bb_j.YMin+((bb_j.YMax-bb_j.YMin)/2.0))			
					objs[j].Placement.Base=Common.toLocalCoordinates(Path[j],base_j)
					j=j+1			
		else:
			objs=GetSelectedUpperObjects() 
			if objs.__len__() > 0:
				i=objs.__len__()-1
				bb=GetObjectBoundBox(objs[i])
				a=bb.YMin+(bb.YMax-bb.YMin)/2.0
				for obj in objs:
					bb=GetObjectBoundBox(obj)
					obj.Placement.Base.y=obj.Placement.Base.y+a-(bb.YMin+((bb.YMax-bb.YMin)/2.0))
		return
class AlignZCenter():
	def GetResources(self):
		return {'Pixmap'  : ICONPATH+'AlignZCenter.svg', # the name of a svg file available in the resources
	#              'Accel' : "Shift+S", # a default shortcut (optional)
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Aligns objects to the center of the z-axis")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			if objs.__len__() > 0:
				i=objs.__len__()-1
				bb=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				a=bb.ZMin+(bb.ZMax-bb.ZMin)/2.0
				j=0
				while j<objs.__len__():
					bb_j=Common.GetBoundBoxFromGlobalCoordinates(Path[j],objs[j])			
					base_j=Common.toGlobalCoordinates(Path[j],objs[j].Placement.Base)
					base_j.z=base_j.z+a-(bb_j.ZMin+((bb_j.ZMax-bb_j.ZMin)/2.0))			
					objs[j].Placement.Base=Common.toLocalCoordinates(Path[j],base_j)
					j=j+1			
		else:
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
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools', "Positions objects to the right of the last selected object")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			i=0
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			i=objs.__len__()-1
			if i > 0:
				bb_a=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				j=0
				while j<i:
					bb_j=Common.GetBoundBoxFromGlobalCoordinates(Path[j],objs[j])
					base_j=Common.toGlobalCoordinates(Path[j],objs[j].Placement.Base)
					base_j.x=base_j.x+bb_a.XMax-bb_j.XMin			
					objs[j].Placement.Base=Common.toLocalCoordinates(Path[j],base_j)
					j=j+1			
		else:
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
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Positions objects to the left of the last selected object")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			i=0
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			i=objs.__len__()-1
			if i > 0:
				bb_a=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				j=0
				while j<i:
					bb_j=Common.GetBoundBoxFromGlobalCoordinates(Path[j],objs[j])
					base_j=Common.toGlobalCoordinates(Path[j],objs[j].Placement.Base)
					base_j.x=base_j.x-(bb_j.XMax-bb_a.XMin)			
					objs[j].Placement.Base=Common.toLocalCoordinates(Path[j],base_j)
					j=j+1			
		else:
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
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Positions objects to the behind of the last selected object")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			i=0
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			i=objs.__len__()-1
			if i > 0:
				bb_a=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				j=0
				while j<i:
					bb_j=Common.GetBoundBoxFromGlobalCoordinates(Path[j],objs[j])
					base_j=Common.toGlobalCoordinates(Path[j],objs[j].Placement.Base)
					base_j.y=base_j.y+bb_a.YMax-bb_j.YMin			
					objs[j].Placement.Base=Common.toLocalCoordinates(Path[j],base_j)
					j=j+1			
		else:
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
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Positions objects to the front of the last selected object")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			i=0
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			i=objs.__len__()-1
			if i > 0:
				bb_a=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				j=0
				while j<i:
					bb_j=Common.GetBoundBoxFromGlobalCoordinates(Path[j],objs[j])
					base_j=Common.toGlobalCoordinates(Path[j],objs[j].Placement.Base)
					base_j.y=base_j.y-(bb_j.YMax-bb_a.YMin)			
					objs[j].Placement.Base=Common.toLocalCoordinates(Path[j],base_j)
					j=j+1			
		else:
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
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Positions objects to the over of the last selected object")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			i=0
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			i=objs.__len__()-1
			if i > 0:
				bb_a=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				j=0
				while j<i:
					bb_j=Common.GetBoundBoxFromGlobalCoordinates(Path[j],objs[j])
					base_j=Common.toGlobalCoordinates(Path[j],objs[j].Placement.Base)
					base_j.z=base_j.z+bb_a.ZMax-bb_j.ZMin			
					objs[j].Placement.Base=Common.toLocalCoordinates(Path[j],base_j)
					j=j+1			
		else:
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
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Positions objects to the under of the last selected object")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			i=0
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			i=objs.__len__()-1
			if i > 0:
				bb_a=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				j=0
				while j<i:
					bb_j=Common.GetBoundBoxFromGlobalCoordinates(Path[j],objs[j])
					base_j=Common.toGlobalCoordinates(Path[j],objs[j].Placement.Base)
					base_j.z=base_j.z-(bb_j.ZMax-bb_a.ZMin)			
					objs[j].Placement.Base=Common.toLocalCoordinates(Path[j],base_j)
					j=j+1			
		else:
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
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Сenters objects between the last two selected objects along the x-axis")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			i=objs.__len__()-2
			if i > 0:
				bb1=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				bb2=Common.GetBoundBoxFromGlobalCoordinates(Path[i+1],objs[i+1])
				a=(bb2.XMax-bb1.XMin)/2.0+bb1.XMin
				j=0
				while j<i:
					bb_j=Common.GetBoundBoxFromGlobalCoordinates(Path[j],objs[j])
					base_j=Common.toGlobalCoordinates(Path[j],objs[j].Placement.Base)
					base_j.x=base_j.x+a-(bb_j.XMin+((bb_j.XMax-bb_j.XMin)/2.0))		
					objs[j].Placement.Base=Common.toLocalCoordinates(Path[j],base_j)
					j=j+1			
		else:
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
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Сenters objects between the last two selected objects along the y-axis")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			i=objs.__len__()-2
			if i > 0:
				bb1=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				bb2=Common.GetBoundBoxFromGlobalCoordinates(Path[i+1],objs[i+1])
				a=(bb2.YMax-bb1.YMin)/2.0+bb1.YMin
				j=0
				while j<i:
					bb_j=Common.GetBoundBoxFromGlobalCoordinates(Path[j],objs[j])
					base_j=Common.toGlobalCoordinates(Path[j],objs[j].Placement.Base)
					base_j.y=base_j.y+a-(bb_j.YMin+((bb_j.YMax-bb_j.YMin)/2.0))		
					objs[j].Placement.Base=Common.toLocalCoordinates(Path[j],base_j)
					j=j+1			
		else:
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
	#              'MenuText': "Align Left",
				'ToolTip' : QT_TRANSLATE_NOOP('PlacementTools',"Сenters objects between the last two selected objects along the z-axis")}

	def Activated(self):
		FreeCAD.ActiveDocument.openTransaction(self.__str__())
		if Common.localMode: 
			Path=Common.GetSelectedLowerObjectsPath()
			objs=Common.GetSelectedLowerObjects()
			i=objs.__len__()-2
			if i > 0:
				bb1=Common.GetBoundBoxFromGlobalCoordinates(Path[i],objs[i])
				bb2=Common.GetBoundBoxFromGlobalCoordinates(Path[i+1],objs[i+1])
				a=(bb2.ZMax-bb1.ZMin)/2.0+bb1.ZMin
				j=0
				while j<i:
					bb_j=Common.GetBoundBoxFromGlobalCoordinates(Path[j],objs[j])
					base_j=Common.toGlobalCoordinates(Path[j],objs[j].Placement.Base)
					base_j.z=base_j.z+a-(bb_j.ZMin+((bb_j.ZMax-bb_j.ZMin)/2.0))		
					objs[j].Placement.Base=Common.toLocalCoordinates(Path[j],base_j)
					j=j+1			
		else:
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



FreeCADGui.addCommand('AlignLeft',AlignLeft()) 
FreeCADGui.addCommand('AlignRight',AlignRight()) 
FreeCADGui.addCommand('AlignRear',AlignRear()) 
FreeCADGui.addCommand('AlignFront',AlignFront()) 
FreeCADGui.addCommand('AlignBottom',AlignBottom()) 
FreeCADGui.addCommand('AlignTop',AlignTop()) 

FreeCADGui.addCommand('AlignXCenter',AlignXCenter()) 
FreeCADGui.addCommand('AlignYCenter',AlignYCenter()) 
FreeCADGui.addCommand('AlignZCenter',AlignZCenter()) 

FreeCADGui.addCommand('RightOf',RightOf()) 
FreeCADGui.addCommand('LeftOf',LeftOf()) 
FreeCADGui.addCommand('BehindOf',BehindOf()) 
FreeCADGui.addCommand('FrontOf',FrontOf()) 
FreeCADGui.addCommand('OverOf',OverOf()) 
FreeCADGui.addCommand('UnderOf',UnderOf()) 

FreeCADGui.addCommand('MiddleXOf',MiddleXOf()) 
FreeCADGui.addCommand('MiddleYOf',MiddleYOf()) 
FreeCADGui.addCommand('MiddleZOf',MiddleZOf()) 


