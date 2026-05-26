
import maya.cmds as cmds
import maya.mel as mel

def createAtlas(aItems):
    try:
        mel.eval('scriptEditorInfo -e -suppressWarnings true;')
    except:
        pass

    for k in aItems:
        if not cmds.objExists(k.mesh):
            cmds.warning("Mesh does not exist: %s" % k.mesh)
            continue

        try:
            cmds.select(clear=True)
            cmds.select(k.mesh)
            cmds.select(cmds.polyListComponentConversion(toUV=True))

            cmds.polyEditUV(
                pivotU=0,
                pivotV=1,
                scaleU=k.sizeX,
                scaleV=k.sizeY
            )

            cmds.polyMoveUV(
                translationU=k.posX,
                translationV=-k.posY
            )

        except Exception as e:
            cmds.warning("UV atlas failed on %s: %s" % (k.mesh, str(e)))
