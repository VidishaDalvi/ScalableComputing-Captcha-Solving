import os
from PIL import Image
for file in os.listdir('C:/TCD/DS/Scalable_Computing/Lab_Project3/new2/grayscale/'):
    img = Image.open('C:/TCD/DS/Scalable_Computing/Lab_Project3/new2/grayscale/' + file)
    new_img = img.resize((128,64))
    new_img.save('C:/TCD/DS/Scalable_Computing/Lab_Project3/new2/grayscale/' + file, "PNG", optimize=True)
