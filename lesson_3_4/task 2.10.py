import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 8))
ax_3d = fig.add_subplot(projection='3d')
x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)
xgrid, ygrid = np.meshgrid(x, y)
zgrid = (np.sin(xgrid**2+ygrid**2))/(xgrid**2+ygrid**2)
ax_3d.plot_surface(xgrid, ygrid, zgrid, rstride=3, cstride=3, cmap='ocean')
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.yticks(np.arange(min(x), max(x)+1, 1.0))
plt.show()
