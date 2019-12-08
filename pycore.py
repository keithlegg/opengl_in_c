
import sys


from pygfx.math_ops import  *
from pygfx.point_ops import *
from pygfx.obj3d import  *
from pygfx.render import *

mu = math_util() 



##***********************************************************##

## print(sys.argv, len(sys.argv))

if __name__=="__main__":

    print( sys.argv )


    PYCORE_OBJ_IN   = sys.argv[1]
    PYCORE_GEOMPATH = "3d_obj"
    PYCORE_OBJ_OUT  = "%s/%s"%(PYCORE_GEOMPATH, "PYCORE.obj")

    # print("# PYCORE %s --> %s "% (PYCORE_OBJ_IN, PYCORE_OBJ_OUT) )




##***********************************************************##
##***********************************************************##
##***********************************************************##
##***********************************************************##
## DEFINE PYCORE COMMANDS (FROM PYGFX)

def triangulate():
    obj = object3d()
    obj.load(PYCORE_OBJ_IN)
    obj.triangulate()
    obj.save(PYCORE_OBJ_OUT)


##------------------

def gen_normals():
    obj = object3d() 
    obj.load(PYCORE_OBJ_IN)

    vectors = [] 

    # iterate all faces, calculate a normal for it 
    # transfrom that normal vector to the 3D center of the face 
    for fid in range(len(obj.polygons)):
        nrml = obj.get_face_normal(fid) 
        cntr = obj.get_face_centroid(fid)
        vectors.append( (nrml, cntr) )

    obj2 = object3d()    
    obj2.vectorlist_to_obj(vectors)
    obj2.save(PYCORE_OBJ_OUT) 


##------------------

def matrix_rotate():
    obj = object3d()
    obj.load(PYCORE_OBJ_IN)
    #pts = [(2,2,2), (4,4,4), (8,8,8)]
    pts2 = obj.rotate_pts((45,45,45) )
    #print(pts2)
    obj.save(PYCORE_OBJ_OUT)


##------------------

def copy_sop():
    #be cautious of large number of polys. It gets slow real quick!

    obj = object3d() 
    obj.load(PYCORE_OBJ_IN)
    obj.copy_sop(slice=(1,10), offset=(0,1,0), num=3, distance=.5)
    obj.save(PYCORE_OBJ_OUT)




##------------------


def modify_partial():
    obj = object3d()
    obj.load(PYCORE_OBJ_IN)

    # if the number of points chnages you need to reindex
    # geom = obj.sub_select_geom( slice=(10,700), reindex=True )
    # newpts = obj.rotate_pts((45,45,45), pts=geom[1])
    
    geom = obj.sub_select_geom( slice=(10,700) )
    newpts = obj.points
    
    obj.rotate_pts((0,45,0))

    obj2 = object3d() 
    obj2.insert_polygons(geom[0], newpts  )      
    obj2.save(PYCORE_OBJ_OUT)    



##------------------
def circle_cube_pts():

    # PYCORE_OBJ_IN not needed 
    obj = object3d()
    obj.prim_circle(axis='z', pos=(0,0,0), spokes=34) 
    obj.triangulate(force=True)
    pts = obj.get_face_pts(0) 
    ct = 0
    for pt in pts:
        tmp = object3d()
        tmp.prim_cube(size=.05, pos=pt, rot=(ct,ct,ct), pivot='world')
        ct += 10
        obj.insert(tmp)  
    obj.save(PYCORE_OBJ_OUT)

##------------------
def sphericalcoords():
    """ test of spherical coordinates to a cartesian point 
        done in a nested loop to make a sphere
       
        PYCORE_OBJ_IN not needed 
    """

    obj = object3d()

    for theta in range(-180,180,20):
        print('## theta ', theta )
        for phi in range(-180,180,20):        
            sp = spherical(1.5, mu.dtr(theta), mu.dtr(phi) ) 
            pt=  sp.to_cartesian() 
            obj.prim_cube(pos=pt, size=.1, linecolor=(255,0,0), rot=(0,0,0), pivot='world')

    obj.save(PYCORE_OBJ_OUT) 

##------------------
def primitive(primtype):
    # PYCORE_OBJ_IN not needed 

    obj = object3d() 

    position = (0,0,0)
    rotation = (0,0,0)
    size = 1 
    axis = 'y'

    do_flush = True

    
    # obj.prim_line( axis=axis, pos=position, rot=rotation, size=size)
    # obj.save(PYCORE_OBJ_OUT)
    # if do_flush:
    #     obj.flush()

    if primtype == 'triangle':
        obj.prim_triangle( axis=axis, pos=position, rot=rotation, size=size)
        obj.save(PYCORE_OBJ_OUT)
        if do_flush:
            obj.flush()

    if primtype == 'quad':
        obj.prim_quad( axis=axis, pos=position, rot=rotation, size=size)
        obj.save(PYCORE_OBJ_OUT)
        if do_flush:
            obj.flush()

    if primtype == 'circle':
        obj.prim_circle( axis=axis, pos=position, dia=size) #rot=rotation
        obj.save(PYCORE_OBJ_OUT)
        if do_flush:
            obj.flush()

    if primtype == 'sphere':
        obj.prim_sphere(  pos=position, rot=rotation, size=size)
        obj.save(PYCORE_OBJ_OUT)
        if do_flush:
            obj.flush()

    if primtype == 'locator':
        obj.prim_locator(  pos=position, rot=rotation, size=size)
        obj.save(PYCORE_OBJ_OUT)
        if do_flush:
            obj.flush()

    if primtype == 'locatorxyz':
        obj.prim_locator_xyz(  pos=position, rot=rotation, size=size)
        obj.save(PYCORE_OBJ_OUT)
        if do_flush:
            obj.flush()

    if primtype == 'cone':
        obj.prim_cone( axis=axis, pos=position, dia=size) #rot=rotation
        obj.save(PYCORE_OBJ_OUT)
        if do_flush:
            obj.flush()


##------------------

def pt_transform():

    """ example of translate, rotate, scale of raw points 
        translate tools work with "ptgroups", or raw points
    """

    obj = object3d()
    obj.load(PYCORE_OBJ_IN)

    obj.points = obj.scale_pts( (1,1,1)      , pts=obj.points )   
    
    #obj.points = obj.rotate_pts((0,30,0), pts=obj.points ) 
    
    #obj.points = obj.xform_pts( (0,2,0),  pts=obj.points ) 

    obj.save(PYCORE_OBJ_OUT)


def scratch_obj():
    obj = object3d()
 
    obj.load(PYCORE_OBJ_IN)

    #add new geom and auto increment the ids
    polys = [(1,2,3,4) ]
    pts = [(10,1,1),(0,11,1),(-1,-5,1),(2,-2,1)]
    obj.insert_polygons([], pts) 

    #add new geom and auto increment the ids
    pts = [(0,-3,-1),(2,-2,1),(3,-1,1)]
    obj.insert_polygons([], pts)

    #add polys without new points into same "shell"
    obj.insert_polygons( [(1,2,3,4,5,6,7),(1,7,2)], None, asnew_shell=False)

    #add new polygon in a new "shell" 
    obj.insert_polygons( [(1,2,3,4)], [(3,3,3), (3,-4,5), (-4,-2.5,3.1), (6.2,-2.7,8)], asnew_shell=True)

    obj.save(PYCORE_OBJ_OUT)



def scratch_obj2():

    """ build a new polygon object in memory from points 
        then insert it into an object and export  
        
        PYCORE_OBJ_IN not needed          
    """ 

    geom  = [[],[]]
    geom2 = [[],[]]

    obj = object3d()
    #obj.load(PYCORE_OBJ_IN)

    #add new geom and auto increment the ids

    #3 sided polygons 
    polys = [(1,2,3),  (4,3,1) ]
    pts = [(1,1,1),(0,1,1),(-1,-1,1),(2,-2,1)]
    geom = obj.insert_polygons(polys, pts, geom=geom) 

 
    #4 sided polygons
    polys = [(1,2,3,4) ]
    pts = [(4,-4.3,-3),(1.5,-2.5,-2.1),(-2,2,-4),(4,-4.2,1)]
    geom2 = obj.insert_polygons(polys, pts, geom=geom2) 

    # use insert to add geom to object 
    obj.insert(geom) 
    obj.insert(geom2) 
 
    # see what we have done, or not done 
    #obj.show() 

    obj.save( PYCORE_OBJ_OUT )



def face_extrude():
    """ brute force test of face extrude 
        extrudes all faces in a polygon object 
        also will display a cheapo test "progress bar"
        because it can be slow 
    """

    obj = object3d()
    obj.load(PYCORE_OBJ_IN)

    for i in range(1,len(obj.polygons) ):   
        obj.extrude_face(i, 1)

    obj.save(PYCORE_OBJ_OUT)

##***********************************************************##
##***********************************************************##
##***********************************************************##
##***********************************************************##

## parse commands coming in and run them

def runcommand():
    face_extrude()
    #scratch_obj2()
    #scratch_obj()
    #pt_transform()
    #primitive('sphere')
    #sphericalcoords()
    #circle_cube_pts()
    #modify_partial()
    #triangulate()
    #gen_normals()
    #matrix_rotate()
    #copy_sop()





if __name__=="__main__":

    if sys.argv[2] == 'runcommand':
        runcommand()
    
    #if sys.argv[2] == 'normals':
    #    gen_normals()










###########################################################################
###########################################################################


def build_orthogonal_vector():
    """ treats the "line" as an infinite vector 

    """

    obj = object3d()
    com = vec3() #container for commands

    # the point we are "looking" from 
    pt1 = vec3(-1,1,-4)
    obj.prim_cube(pos=pt1,size=.05,linecolor=(255,0,0),rot=(0,0,0),pivot='world')

    # the point of the line origin
    pt2 = vec3(10,-5, 17)
    obj.prim_cube(pos=pt2,size=.1,linecolor=(255,0,0),rot=(0,0,0),pivot='world')    
    
    # the line, needs to be normalized for the math to work  
    display_unitvec = vec3(0,1,0)
    unitvec = display_unitvec.normal
    
    #render it as full size, not unit length 
    obj.one_vec_to_obj( display_unitvec , pos=pt2) 
    #make a negative version as well, to really get the idea of the size 
    display_unitvec = display_unitvec * -1
    obj.one_vec_to_obj( display_unitvec , pos=pt2) 

    d = com.orthogonal_vec_from_pt(pt2, unitvec, pt1)

    #obj.one_vec_to_obj( d*-1 )   
    obj.one_vec_to_obj( d , pt1 )   

    obj.save('3d_obj/normals.obj')


#build_orthogonal_vector() 