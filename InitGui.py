#import os
#from freecad.workbench_starterkit import ICONPATH
import Part


class PlacementTools (Workbench):
    from Common import ICONPATH
    MenuText = "Placement Tools"
    ToolTip = "Placement and allign Objects"
    #Icon = FreeCAD.getUserAppDataDir()+'Mod/PlacementTools/Resources/icons/Main.svg' 
    Icon = ICONPATH+'Main.svg' 

    def Initialize(self):
        """This function is executed when FreeCAD starts"""
        import Allign# import here all the needed files that create your FreeCAD commands
 #       self.list = ["Box","AllignLeft","AllignRight","AllignRear","AllignFront","AllignTop","AllignBottom","Separator","AllignXCenter","AllignYCenter","AllignZCenter","Separator","LeftOf","RightOf","BehindOf","FrontOf","OverOf","UnderOf","Separator","MiddleXOf","MiddleYOf","MiddleZOf"] # A list of command names created in the line above
        self.appendToolbar("Allign",["AllignLeft","AllignRight","AllignRear","AllignFront","AllignTop","AllignBottom","Separator","LeftOf","RightOf","BehindOf","FrontOf","OverOf","UnderOf","Separator","AllignXCenter","AllignYCenter","AllignZCenter","Separator","MiddleXOf","MiddleYOf","MiddleZOf"]) # creates a new toolbar with your commands
        import Move
        self.appendToolbar("Move",["PTPMode","PointToPoint","PointToPointX","PointToPointY","PointToPointZ","Separator","dX","dY","dZ"] ) # creates a new toolbar with your commands
        import Rotation
        self.appendToolbar("Rotation",["rX90","rX_90","rY90","rY_90","rZ90","rZ_90","Separator","rX","rY","rZ"] ) # creates a new toolbar with your commands
        import DraftTools
        self.appendToolbar("Standart",["StdMove","Part_Measure_Linear","Part_Measure_Angular","Draft_Clone"]) # creates a new toolbar with your commands
        import Tools
        self.appendToolbar("Tools",["Query","Box"]) # creates a new toolbar with your commands
     
  #      self.appendMenu("My New Menu",self.list) # creates a new menu
  #      self.appendMenu(["An existing Menu","My submenu"],self.list) # appends a submenu to an existing menu

    def Activated(self):
        """This function is executed when the workbench is activated"""
        return

    def Deactivated(self):
        """This function is executed when the workbench is deactivated"""
        return

    def ContextMenu(self, recipient):
        """This is executed whenever the user right-clicks on screen"""
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("My commands",self.list) # add commands to the context menu

    def GetClassName(self): 
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"
       
Gui.addWorkbench(PlacementTools()) 
#Gui.activateWorkbench("PlacementTools")

