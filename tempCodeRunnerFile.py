from input_ import *
from usefuls import *
from objects import *
from glfw_ import * 




while not glfw.window_should_close(window):
    glfw.poll_events()
    input_.do_movement()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    view = input_.cam.get_view_matrix()
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
    rot_x=pyrr.Matrix44.from_x_rotation(i_*glfw.get_time())  # from pine tree
    glUniformMatrix4fv(light_loc, 1, GL_FALSE, rot_x)

    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
    
    for i in range(number_of_obj):
        o[i].draw()
    glfw.swap_buffers(window)

glfw.terminate()                           