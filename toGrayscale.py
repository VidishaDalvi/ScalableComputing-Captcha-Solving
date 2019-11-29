import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

for file in os.listdir('C:/TCD/DS/Scalable_Computing/Lab_Project3/new2/images/'):
    image = cv2.imread('C:/TCD/DS/Scalable_Computing/Lab_Project3/new2/images/'+file, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, dsize=(128, 64), interpolation=cv2.INTER_CUBIC)
    fig = plt.figure()

    image_enhanced = cv2.equalizeHist(image)

    plt.imshow(image_enhanced, cmap='gray'), plt.axis("off")
    plt.show()
    fig.savefig("C:/TCD/DS/Scalable_Computing/Lab_Project3/new2/grayscale/"+file)