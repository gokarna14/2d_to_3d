from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from TextureLoader import load_texture
from ObjLoader import ObjLoader 
from camera import Camera
import pyrr, glfw


i_ = 1.0


first_mouse = True
cam = Camera()
left, right, forward, backward, light_rotx = False, False, False, False, False
rot = False

# the keyboard input callback
def key_input_clb(window, key, scancode, action, mode):
    global left, right, forward, backward, light_rotx
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)
    if key == glfw.KEY_W and action == glfw.PRESS:
        forward = True
    elif key == glfw.KEY_W and action == glfw.RELEASE:
        forward = False
    if key == glfw.KEY_S and action == glfw.PRESS:
        backward = True
    elif key == glfw.KEY_S and action == glfw.RELEASE:
        backward = False
    if key == glfw.KEY_A and action == glfw.PRESS:
        left = True
    elif key == glfw.KEY_A and action == glfw.RELEASE:
        left = False
    if key == glfw.KEY_D and action == glfw.PRESS:
        right = True
    elif key == glfw.KEY_D and action == glfw.RELEASE:
        right = False
    if key == glfw.KEY_P and action == glfw.PRESS:
        light_rotx = True
    elif key == glfw.KEY_P and action == glfw.RELEASE:
        light_rotx = False


# the mouse position callback function
def mouse_look_clb(window, xpos, ypos):
    global first_mouse, lastX, lastY

    if first_mouse:
        lastX = xpos
        lastY = ypos
        first_mouse = False

    xoffset = xpos - lastX
    yoffset = lastY - ypos

    lastX = xpos
    lastY = ypos

    cam.process_mouse_movement(xoffset, yoffset)


def do_movement():
    global i
    if left:
        cam.process_keyboard("LEFT", 0.05)
    if right:
        cam.process_keyboard("RIGHT", 0.05)
    if forward:
        cam.process_keyboard("FORWARD", 0.05)
    if backward:
        cam.process_keyboard("BACKWARD", 0.05)

