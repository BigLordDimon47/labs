from numpy import *
import matplotlib.pylab as plt

x  = [2013, 2014, 2015]
y1 = [5260, 6000, 6700]
y2 = [2410, 2700, 3500]
y3 = [6280, 6800, 6700]
y4 = [4340, 4600, 4700]
y5 = [3720, 3800, 4300]
plt.plot(x, y1, label = 'Взуття')
plt.plot(x, y2, label = 'Галантерея')
plt.plot(x, y3, label = 'Одяг та білизна')
plt.plot(x, y4, label = 'Тканини')
plt.plot(x, y5, label = 'Трикотаж')

plt.xticks([2013, 2014, 2015])
plt.legend()

plt.savefig('image.png', dpi = 200)
plt.show()