#ifndef MAYANAVDEMO_H    
#define MAYANAVDEMO_H





static void draw_3d_cube();
static void animateTextures3(Image *loaded_texture);

static void ReSizeGLScene(int Width, int Height);
static void keyPressed(unsigned char key, int x, int y); 

void olmec_mouse_button(int button, int state, int x, int y);
void olmec_mouse_motion(int x, int y);

void olmec_navigation_demo(int *argc, char** argv);





#endif

