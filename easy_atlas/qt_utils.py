
from maya import OpenMayaUI as omui
try:
    from PySide6.QtCore import *
    from PySide6.QtGui import *
    from PySide6.QtUiTools import *
    from PySide6.QtWidgets import *
    from shiboken6 import wrapInstance
except ImportError:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtUiTools import *
    from PySide2.QtWidgets import *
    from shiboken2 import wrapInstance
    
import maya.cmds as cmds

class RawWidget:
    def __init__(self, name, type):
        self.name = name
        self.type = type

def loadQtWindow(uiFile, windowName):
    if cmds.window(windowName, exists=True):
        cmds.deleteUI(windowName)

    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget)

    loader = QUiLoader()
    file = QFile(uiFile)
    file.open(QFile.ReadOnly)
    windowUI = loader.load(file, parentWidget=mayaMainWindow)
    file.close()

    return windowUI

def getControl(rawWidget):
    if rawWidget.type == QAction:
        ptr = omui.MQtUtil.findMenuItem(rawWidget.name)
    else:
        ptr = omui.MQtUtil.findControl(rawWidget.name)

    if ptr is None:
        return None

    return wrapInstance(int(ptr), rawWidget.type)
