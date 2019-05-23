import matplotlib.pyplot  as plt
import numpy as np
a=[1,2,3,4,5,6,7]
b=[1,2,3,4,5,6,7]
plt.plot(a,np.log(b))
plt.show(0)
plt.savefig("test.png")