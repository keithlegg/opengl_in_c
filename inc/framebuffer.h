#ifndef FRAMEBUFFER_H    
#define FRAMEBUFFER_H

#include <stdint.h>

#include "point_op.h"

//these are not exclusively framebuffer related, but this is a good home for them since it is used everywhere

void abort_(const char * s, ...);

#define max(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a > _b ? _a : _b; })

#define min(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a < _b ? _a : _b; })

#define PI 3.14159265358979323846

//the "pixel" objects (struct) to fill "framebuffer" objects (grids of these) 


// another image type 
typedef struct Image{
    unsigned int sizeX;
    unsigned int sizeY;
    char *data;
} Image ;


//24 bit color 
typedef struct{
    uint8_t r=0;
    uint8_t g=0;
    uint8_t b=0;
}RGBType;

//32 bit (24 color+ 8 alpha) 
typedef struct{
    uint8_t r=0;
    uint8_t g=0;
    uint8_t b=0;
    uint8_t a=0;    
}RGBAType;

//1 bit (black and white)
typedef struct{
    bool l=0;
}BWI_Type;

//8 bit (grayscale)
typedef struct{
    uint8_t l=0;
}GSI_Type;


//generators
RGBType  newRgb(int r, int g, int b);
RGBAType newRgba(int r, int g, int b, int a);

//framebuffer allocation
BWI_Type* createBuffer1(  int w, int h);    // 1 bit
GSI_Type* createBuffer8(  int w, int h);    // 8 bit
RGBType*  createBuffer24( int w, int h);    // 24 bit
RGBAType* createBuffer32( int w, int h);    // 32 bit 
Image*    createBufferImage(int w, int h);  // Image type (SizeX, SizeY, data)

//copy or "convert" a buffer 24 to 32 
RGBType*  copyBuffer24( RGBType *pixels , int w, int h );
RGBType*  copyBuffer24( RGBAType *pixels, int w, int h );
RGBAType* copyBuffer32( RGBType *pixels , int w, int h );
RGBAType* copyBuffer32( RGBAType *pixels, int w, int h ); 


void copyBuffer24( RGBType* inBuffer , Image* outBuffer   );    // convert an "RGBType" to "Image"
void copyBuffer24( Image* inBuffer   , RGBType* outBuffer );    // convert an "Image" to "RGBType"

void copyBuffer24( Image* inBuffer   , Image* outBuffer   );    // copy an "Image" type 
void copyBuffer24( Image* inBuffer   , Image* outBuffer, int tl[2], int br[2] ); //mask a region  


RGBAType* copyBufferEveryOther32( RGBAType *pixels, int* w, int* h, int step_size );

void ScaleLine(RGBAType *Target, RGBAType *Source, int SrcWidth, int TgtWidth);

void ScaleRect(RGBAType *Target, RGBAType *Source, int SrcWidth, int SrcHeight,
               int TgtWidth, int TgtHeight);

RGBAType* blitBuffer32( RGBAType *pixels, int* w, int* h, int startx, int starty,  int endx, int endy );

void fillbuffer24(Image *imgBuffer, RGBType *color);
void fillbuffer24(RGBType *pixBuffer , int width, int height, int rval, int gval, int bval);
void fillbuffer24(RGBType *pixBuffer , int width, int height, RGBType *color);
void fillbuffer32(RGBAType *pixBuffer, int width, int height, RGBType *color);

short scanner_darkly(int *pix);
short scanner_darkly(RGBType* pixel24);
short scanner_darkly(RGBAType* pixel32);

void draw_point ( Image *imgBuffer, int imagewidth, int xcoord, int ycoord, RGBType *color  );
void draw_point ( RGBAType *fb_image, int imagewidth, int pt[2], int color[3] );//untested 
void draw_point ( RGBAType *fb_image, int imagewidth, int xcoord, int ycoord, int color[3]  );
void draw_point ( RGBType *fb_image , int imagewidth, int xcoord, int ycoord, int color[3]  );
void draw_point ( RGBAType *fb_image, int imagewidth, int xcoord, int ycoord, RGBType *color  );
void draw_point ( RGBType *fb_image , int imagewidth, int xcoord, int ycoord, RGBType *color  );
void draw_point ( RGBType *fb_image , int imagewidth, int xcoord, int ycoord, int dia, RGBType *color  );

void threshold (RGBAType *pixbuffer, int imagewidth, int imageheight, int threshval); 
void threshold (RGBType *pixbuffer, int imagewidth, int imageheight, int threshval);
 
void gaussBlur (RGBAType *pixbuffer, RGBAType *pix2buffer, int imagewidth, int height, int r, bool do_threshold, int threshval); 

void draw_square( Image *imgBuffer, int width, int tl[2], int br[2], RGBType *color );
void draw_square( RGBAType *row_pt, int width, int tl[2], int br[2], int color[3] );

void draw_fill_square( Image *imgBuffer, int x_orig, int y_orig, int dia, RGBType *color);
void draw_fill_square( RGBAType *row_pt, int width, int x_orig, int y_orig, int dia, int color[3]);

void draw_line( RGBAType *fb_image, int imagewidth, int x1, int y1, int x2, int y2, RGBType *color);
void draw_line( RGBType *fb_image, int imagewidth, int x1, int y1, int x2, int y2, RGBType *color);

void draw_poly_line ( RGBAType *fb_image, int imagewidth, pix_coord *vertices, int numpts,  RGBType *color );
void draw_vector ( RGBAType *fb_image, int imagewidth, vec2 vec, int xpos, int ypos, RGBType *color );


void draw_circle ( RGBType *fb_image, int imagewidth, int x_orig, int y_orig, int dia, RGBType *color);
void draw_fill_circle ( RGBType *fb_image, int imagewidth, int x_orig, int y_orig, int dia, RGBType *color);

//void draw_square_pt( png_bytep *row_pt, int center[2], int size, int color[3]);

//void draw_fill_circle (  png_bytep *row_pt, int x_orig, int y_orig, int dia, int color[3]);


#endif