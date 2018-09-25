import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



q=np.linspace(1,10,100).astype(int)
w=np.linspace(1,100,100)
z=np.ones(100)*np.random.randn(100)*10


fig= plt.figure(figsize=(6, 5))
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q,w,z)
plt.show()
