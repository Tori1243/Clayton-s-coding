import maya.cmds as cmds

cmds.polyCylinder (radius=1,
                   height=2,
                   subdivisionsX=20,
                   subdivisionsY=1,
                   subdivisionsZ=1,
                   axis=[0,1,0],
                   roundCap=0,
                   createUVs=3,
                   constructionHistory=1)
                   
                   
cmds.select('pCylinder1', add=True)

cmds.move( 0, 1.5, 0, 'pCylinder1', absolute=True)

cmds.polyDisc (sides=3,
               subdivisionMode=4, 
               subdivisions=3,
               radius=2)
               
               
cmds.move( 0, .5, 0, 'pDisc1', absolute=True)
               

