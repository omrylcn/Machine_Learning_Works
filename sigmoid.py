import numpy as np
import matplotlib.pyplot as plt
import math

x=np.linspace(-5,5,21)

fun=1 /(1+(math.e**-x))

plt.plot(x,fun,".")
