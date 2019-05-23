import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread(r"Z:\py_lib\rabbit.png")
print(img)
plt.savefig("r.png")
imgplot = plt.imshow(img)
