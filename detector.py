from imageai.Detection import ObjectDetection
import pandas as pd
from usefuls import * 


image_num = 1      # 2(all), 1(car + bus), 3(only cars)

backward = 10
forward_distance = 2
side_distance = 1.1
if (image_num == 1):
    side_distance = 0.5
elif (image_num == 3):
    side_distance == 0.3
gr_ht = 0       # ground height
scale = 0.1

def pos_vec(arg):
    p1, p2 = arg[0], arg[1]
    x, y, z = (p1[1] + p2[1])/2, gr_ht, (p1[0] + p2[0])/2
    
    return [x*scale*forward_distance-backward, y, z*scale*side_distance]       #x, y, z
detector = ObjectDetection()
print("\nPlease Wait While Detecting The Vehicles In The Provided Image\nThis may take some time\nPlease be patient\n...\n")

model_path = "./models/yolo-tiny.h5"
input_path = "./input/" + "cars" + str(image_num) + ".jpg"
output_path = "./output/newimage" + str(image_num) +".jpg"


detector.setModelTypeAsTinyYOLOv3()
print("\n\n..25% DONE\n\n")
detector.setModelPath(model_path)
print("\n\n......30% DONE\n\n")
detector.loadModel()
print("\n..........90% DONE")
detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)
print("\n\nIgnore any errors or warnings\n")

name = []
prob =  []
x =  [[], []]



for eachItem in detection:
    if eachItem['name'] in ['car', 'bus', 'truck']:
        name.append(eachItem["name"])
        prob.append(eachItem["percentage_probability"])
        x[0].append([eachItem["box_points"][0], eachItem["box_points"][1]])
        x[1].append([eachItem["box_points"][2], eachItem["box_points"][3]])

data = pd.DataFrame({'Name': name, "Probability":prob, "P1":x[0], "P2":x[1]})

print("\n!! 100% DONE !!\n")

data['vector'] = data[['P1', 'P2']].apply(pos_vec, axis=1)

