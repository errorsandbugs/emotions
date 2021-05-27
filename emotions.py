#pip install fer
#pip install matplotlib



from fer import FER
import matplotlib.pyplot as plt 
img = plt.imread("path of image")
detector = FER(mtcnn=True)
print(type(detector.detect_emotions(img)))
plt.imshow(img)




