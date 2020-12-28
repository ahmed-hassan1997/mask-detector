import os 
import re
import pandas as pd
import random 

path = 'F:/darknet/mask_detection/mask_images'

files = [f for f in os.listdir(path) if re.match(r'.*\.jpg', f)]

random.shuffle(files)

for f in files:
	file = open('names_of_images.txt', 'a')

	data = "mask_detection" + "/" + "mask_images" + '/' + str(f)
	
	file.writelines(data)
	file.write("\n")

file.close()

