import maya.cmds as cmds
def Renamer(input_string):

#select multiple object
#seperate objects so only one object is selected
    sels = cmds.ls(selection = True)
    
    input_selection = 1
    
#input is my selection

    for sel in sels:
        
       #input_string = 'L_###_Arm'
           
           
       # count # signs in name
        collection_count = input_string.count('#')
       
        #Tuple= array that can't be changed. 
        #PARTITIONS: how we make tupple. Take imput.partition. partition off # signs
        
        # find # characters and replace them with next number up
        tupple_parts = input_string.partition('#' * collection_count)
        
        
        #tupple_parts[0] = "L_Arm_"
        #numbering_system = "1"
        #tupple_parts[2] = "_Jnt"
        
        #makes a string of the int
        
        numbering_systems = str(input_selection)
    
        if tupple_parts[1]:
            print 'Characters are sequential.'
            replace_zeroes = numbering_systems.zfill(3)
            
            #rename = "L_Arm_001_Jnt"
            #Rename object
            
            cmds.rename(tupple_parts[0] + replace_zeroes + tupple_parts[2])
        
        else:
            #incase they are not sequential. 
            cmds.error('Characters are not sequential. input another string.')
        input_selection += 1
            
            
Renamer("L_Arm_###_Jnt")
