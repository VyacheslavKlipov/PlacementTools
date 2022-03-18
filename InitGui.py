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
    
import Part

from Common import LANGUAGEPATH
FreeCADGui.addLanguagePath(LANGUAGEPATH)
class PlacementTools (Workbench):
    from Common import ICONPATH
   
    MenuText = "Placement Tools"
    ToolTip = "Placement and align objects"
    Icon = ICONPATH+'Main.svg' 
    def Initialize(self):
        def QT_TRANSLATE_NOOP(scope, text):
            return text
        from Common import LANGUAGEPATH
        FreeCADGui.addLanguagePath(LANGUAGEPATH)
        FreeCAD.Console.PrintMessage(LANGUAGEPATH)
        """This function is executed when FreeCAD starts"""
        import Align
        self.appendToolbar(QT_TRANSLATE_NOOP('PlacementTools',"Align"),["AlignLeft","AlignRight","AlignRear","AlignFront","AlignTop","AlignBottom","Separator","LeftOf","RightOf","BehindOf","FrontOf","OverOf","UnderOf","Separator","AlignXCenter","AlignYCenter","AlignZCenter","Separator","MiddleXOf","MiddleYOf","MiddleZOf"]) # creates a new toolbar with your commands
        import Move
        self.appendToolbar(QT_TRANSLATE_NOOP('PlacementTools',"Move"),["PointToPoint","PointToPointX","PointToPointY","PointToPointZ","Separator","dX","dY","dZ"] ) 
        import Rotation
        self.appendToolbar(QT_TRANSLATE_NOOP('PlacementTools',"Rotation"),["rX90","rX_90","rY90","rY_90","rZ90","rZ_90","Separator","rX","rY","rZ"] ) 
        import DraftTools
        self.appendToolbar(QT_TRANSLATE_NOOP('PlacementTools',"Standart"),["Part_Measure_Linear","Part_Measure_Angular","Std_LinkMake"]) 
        import Tools
        self.appendToolbar(QT_TRANSLATE_NOOP('PlacementTools',"Tools"),["PTPMode","Query","Box"]) 
     
  

    def Activated(self):
        """This function is executed when the workbench is activated"""
        return

    def Deactivated(self):
        """This function is executed when the workbench is deactivated"""
        return

    def ContextMenu(self, recipient):
        """This is executed whenever the user right-clicks on screen"""
        
        self.appendContextMenu("My commands",self.list) 

    def GetClassName(self): 
        
        return "Gui::PythonWorkbench"
      
Gui.addWorkbench(PlacementTools()) 
#Gui.activateWorkbench("PlacementTools")

