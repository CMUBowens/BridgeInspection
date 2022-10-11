# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

list1 = []
try:
    file = open('bowens1010.txt', 'r')
except FileNotFoundError:
    print('File is not found')
else:
    lines = file.readlines()
    for line in lines:
        a = line.split('#')
        x = a[1]
        a = x.replace('(', '')
        b = a.replace(')', '')
        list1.append(b)
file.close()
mpl.rcParams['legend.fontsize'] = 5

# fig = plt.figure()
# ax = fig.gca(projection='3d')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# ax = plt.subplot()
# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
for i in list1[1::]:
    position = []
    value = i.split(',')
    position.append(value)
    z = float(position[0][2])
    x = float(position[0][0])
    y = float(position[0][1])
    ax.plot(x, y, z, label='route')
ax.legend(loc='upper right')
plt.show()

# import matplotlib as mpl
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import matplotlib.pyplot as plt
#
# mpl.rcParams['legend.fontsize'] = 10
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
# z = np.linspace(-2, 2, 100)
# r = z**2 + 1
# x = r * np.sin(theta)
# y = r * np.cos(theta)
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()
#
# plt.show()



