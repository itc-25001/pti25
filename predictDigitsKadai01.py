import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def imageToData(filename):
    img = Image.open(filename).convert('L')  
    img = img.resize((28, 28))  
    data = np.asarray(img)
    return data


data = imageToData("2.png")


plt.imshow(data, cmap='gray')
plt.title("Input Image")
plt.axis("off")
plt.show()

