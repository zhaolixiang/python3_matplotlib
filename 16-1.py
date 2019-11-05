import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False # 解决图像是负号'-'显示为方块的问题,或者转换负号为字符串

# some simple data
x =[1,2,3,4,5,6,7,8]
y=[3,1,4,5,8,9,7,2]

# create bar
plt.bar(x,y,align='center',color='c',
        tick_label=['q','a','c','e','r','j','b','p'],
        hatch='/')

# set x,y_axis label
plt.xlabel(u"箱子编号")
plt.ylabel(u'箱子重量(kg)')

plt.show()

