import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False


# some simple data
x=[1,2,3,4,5]
y=[6,10,4,5,1]

plt.barh(x,y,align='center',color='k',
        tick_label=['A','B','C','D','E'])

# set x,y_axis label
plt.ylabel('测试难度')
plt.xlabel('试卷分数')

# set yaxis grid
plt.grid(True,axis='x',ls=':',color='r',alpha=0.3)
plt.show()