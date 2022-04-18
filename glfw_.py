import glfw, pyrr, input_
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from TextureLoader import load_texture
from ObjLoader import ObjLoader
from usefuls import *
 

projection = pyrr.matrix44.create_perspective_projection_matrix(projection_angle, WIDTH / HEIGHT, 0.1, 100)


def window_resize_clb(window, width, height):
    glViewport(0, 0, width, height)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)


if not glfw.init():                                                         # initializing glfw library
    raise Exception("glfw can not be initialized!")

window = glfw.create_window(WIDTH, HEIGHT, "ROAD 3D", None, None)  # creating the window

if not window:      # check if window was created
    glfw.terminate()
    raise Exception("glfw window can not be created!")


glfw.set_window_pos(window, 50, 50)                                     # set window's position
glfw.set_window_size_callback(window, window_resize_clb)                # set the callback function for window resize
glfw.set_cursor_pos_callback(window, input_.mouse_look_clb)             # set the mouse position callback
glfw.set_key_callback(window, input_.key_input_clb)                     # set the keyboard input callback
glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)          # capture the mouse cursor
glfw.make_context_current(window)                                       # make the context current

shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

glUseProgram(shader)
glClearColor(0, 0.6, 1, 0.5)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

model_loc = glGetUniformLocation(shader, "model")
proj_loc = glGetUniformLocation(shader, "projection")
view_loc = glGetUniformLocation(shader, "view")
light_loc = glGetUniformLocation(shader, "light")



