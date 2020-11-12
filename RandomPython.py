import maya.cmds as cmds
import random

def RandomPlacement(numOfDuplicates, minX, maxX, minY, maxY, minZ, maxZ):
    sel = cmds.ls(selection=True)

    for obj in range(len(cmds.ls(selection=True))):
        index = obj

        for obj in range(numOfDuplicates):
            tempObj = (cmds.duplicate(sel[index], rr=True))
            randomX = random.uniform(minX, maxX)
            randomY = random.uniform(minY, maxY)
            randomZ = random.uniform(minZ, maxZ)
            
            cmds.select(tempObj)
            cmds.xform(worldSpace=True, translation=[randomX, randomY, randomZ])
            
RandomPlacement(2,0,3,5,0,2,3)