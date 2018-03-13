import os
import re

# Count the images in avIAn folders

range_re = re.compile('.*0166_IOU_03[2-5].*')
base_path = 'C:/path_to/image_directories'
list_of_dirs = [f'{base_path}/{x}' for x in os.listdir(base_path) if range_re.match(x)]
number_of_images = 0
tif_re = re.compile('.*\.tif')

for d in list_of_dirs:
    if os.path.exists(f'{d}/JPEG'):
        number_of_images += len(os.listdir(f'{d}/JPEG'))
    else:
        number_of_images += len([x for x in d if tif_re.match(x)])
    
print(number_of_images)
