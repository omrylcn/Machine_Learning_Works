import numpy as np
import matplotlib.pyplot as plt

a=np.linspace(1,10,10).astype(int)

b=np.ones(10).reshape(10,1)

d=b*a


t=np.transpose(d)

q=d.reshape(100)
w=np.linspace(1,100,100)

import matplotlib.pyplot as plt


from mpl_toolkits.mplot3d import Axes3D

fig= plt.figure(figsize=(6, 5))
ax=fig.add_subplot(111,projection="3d")

z=np.ones(100)*np.random.randn(100)*10
c=z[0:50]

ax.scatter(q,w,z)
plt.show()

fig= plt.figure(figsize=(6, 5))
ax=fig.add_subplot(111,projection="3d")

u=np.arange(1,11)
u=u.reshape(10,1)

y=np.ones(10)
y=y*10

h=u*y

ax.scatter(q,h,z)

plt.show()
