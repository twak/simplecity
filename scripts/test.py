'''
Created on 13 Oct 2017

@author: root
'''
from scripting import *

import random, math

# Get a CityEngine instance
ce = CE()

for i in range(0,100): 
    
    for b in ce.getObjectsFrom(ce.scene, ce.isBlock):
        ce.setAttributeSource(b, "/ce/block/lotWidthMin", "USER")
        ce.setAttribute(b, "/ce/block/lotWidthMin",  random.gauss( 18, 5 ) )
        ce.setAttributeSource(b, "/ce/block/irregularity", "USER")
        ce.setAttribute(b, "/ce/block/irregularity",  math.fabs ( random.gauss( 0, 0.3 ) ) )
        ce.setAttributeSource(b, "/ce/block/seed", "USER")
        ce.setAttribute(b, "/ce/block/seed",  random.randint(0,100000) )    
        
        ce.setAttributeSource(b, "/ce/rule/empty", "USER")
        ce.setAttribute(b, "/ce/rule/empty",  True )
    
    ce.generateModels (ce.getObjectsFrom(ce.scene()), updateSeed=True)

    

#    ce.setSelection(ce.getObjectsFrom(ce.scene()) )
    
    settings = OBJExportModelSettings()
    settings.setOutputPath("/home/twak/Desktop/labelcity")
    settings.setBaseName("%d_labels" % i)
    ce.export(ce.getObjectsFrom(ce.scene()), settings)

    
    for b in ce.getObjectsFrom(ce.scene, ce.isBlock):
        ce.setAttribute(b, "/ce/rule/empty",  False )
        
    ce.generateModels (ce.getObjectsFrom(ce.scene()), updateSeed=False)

#    ce.setSelection(ce.getObjectsFrom(ce.scene()) )
    
    settings = OBJExportModelSettings()
    settings.setOutputPath("/home/twak/Desktop/labelcity")
    settings.setBaseName("%d_features" % i)
    ce.export(ce.getObjectsFrom(ce.scene()), settings)
