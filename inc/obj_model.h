#ifndef OBJMODEL_H    
#define OBJMODEL_H

#include "math_op.h"


// from math_op  
// struct vec3 {
//     double x;
//     double y;
//     double z;    
// };

typedef struct line{
    int pt1;
    int pt2;
};

typedef struct triangle{
    int pt1;
    int pt2;
    int pt3;    
};

typedef struct quad{
    int pt1;
    int pt2;
    int pt3;    
    int pt4;
};

typedef struct obj_model{
    int num_pts;
    int num_uvs;

    int num_lines;
    int num_tris;
    int num_quads;    

    struct vec2 uvs[1000];         // UV coords 
    struct vec3 points[1000];      // 3 floats  
    //struct vec3 vtx_colors[1000];   

    struct line lines[1000];       //2 point lines 
    struct triangle tris[1000];    //3 point polygons 
    struct quad quads[1000];       //4 point polygons 

};


void test_loader_data(struct obj_model* loader);
void show_loader(struct obj_model* loader);


void load_objfile( char *filepath, struct obj_model* loader);
void save_objfile( char *filepath);




#endif
