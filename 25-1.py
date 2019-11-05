import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False


# some simple data
x=[1,2,3,4,5]
y=[6,10,4,5,1]

plt.bar(x,y,align='center',color='b',
        tick_label=['A','B','C','D','E'],
        alpha=0.6)

# set x,y_axis label
plt.xlabel('测试难度')
plt.ylabel('试卷分数')

# set yaxis grid
plt.grid(True,axis='y',ls=':',color='r',alpha=0.3)
plt.show()