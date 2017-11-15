import bpy

        
for i in range (70,100):

    for ob in bpy.data.objects:
        if ob.type == 'MESH':
            try:
                bpy.context.scene.objects.unlink(ob)
            except:
                pass

    type = "features"
    #type = "labels"

    imported_object = bpy.ops.import_scene.obj(filepath="/home/twak/Desktop/labelcity/%d_%s_0.obj" % (i,  type) )

    for ob in bpy.data.objects:
        if ob.type == 'MESH':
            for poly in ob.data.polygons:
                poly.use_smooth = False            
            
    for material in bpy.data.materials:
        material.raytrace_mirror.use = False
        material.use_transparency = False
        material.specular_intensity = 0

    bpy.context.scene.render.filepath="/home/twak/Desktop/labelcity/renders/%s_%d_" % (type,  i)
    bpy.ops.render.opengl(animation=True)


#bpy.context.scene.render.engine = 'CYCLES'   
#bpy.ops.ml.refresh()
