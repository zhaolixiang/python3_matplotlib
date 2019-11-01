import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-.", lw='2', c='c', label='plot figure')
plt.legend()

plt.axvspan(xmin=4.0, xmax=6.0, facecolor='y', alpha=0.3)
plt.axhspan(ymin=4.0, ymax=6.0, facecolor='y', alpha=0.3)
plt.show()
