from detector import *
from usefuls import * 
from glfw_ import *


class Object:
    def __init__(self, name, **kwargs):     #position_vector, VAO, ABO, texture, obj_file_path
        self.__dict__.update(kwargs)
        if(name == 'car'):
            self.texture_file_path = "meshes/car.png"
        self.name = name
        self.VAO = glGenVertexArrays(1)
        self.VBO = glGenBuffers(1)
        self.obj_definition()
    
    def draw(self):
        glBindVertexArray( self.VAO)
        glBindTexture(GL_TEXTURE_2D,  self.texture)
        glUniformMatrix4fv(model_loc, 1, GL_FALSE,  self.position)
        glDrawArrays(GL_TRIANGLES, 0,  len(self.indices))
    

    def obj_definition(self):
        self.indices, self.buffer = ObjLoader.load_model(self.obj_file_path)                    # LOAD 3d mesh here
        self.texturing()                                                                        # Texturing call
        glBindVertexArray(self.VAO)                                                             # VAO
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)                                                 # VBO
        glBufferData(GL_ARRAY_BUFFER, self.buffer.nbytes, self.buffer, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.buffer.itemsize * 8, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, self.buffer.itemsize * 8, ctypes.c_void_p(12))
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, self.buffer.itemsize * 8, ctypes.c_void_p(20))
        glEnableVertexAttribArray(2)
        self.positioning()
        
    def positioning(self):
        self.position = pyrr.matrix44.create_from_translation(pyrr.Vector3(self.position_vector))
    
    def texturing(self):
        self.texture = glGenTextures(1)
        load_texture(self.texture_file_path, self.texture)


#middle one ie for height, x for backward, z for sideways

o = [(Object(data['Name'][i], position_vector = data['vector'][i], obj_file_path = "meshes/"+data['Name'][i]+".obj", texture_file_path = "meshes/texture.jpg"))
     for i in range(len(data['vector']))]

pv = [-20.0, -1.0, 25]
names_ = ['road', 'background',  'output']
paths_ = [  ["meshes/road.obj","meshes/road.jpg"],
            ["meshes/background.obj", "meshes/backgrounds.jpg"],
            ["meshes/output.obj", "./output/newimage" + str(image_num) +".jpg"],
            ]

for i in range(len(names_)):
    o.append(Object(names_[i], position_vector = pv, obj_file_path = paths_[i][0], texture_file_path = paths_[i][1]))

number_of_obj = len(o)