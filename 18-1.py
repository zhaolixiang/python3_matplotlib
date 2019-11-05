import matplotlib as mpl
import matplotlib.pyplot as  plt
import numpy as np

mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

# set test scores
x=np.random.randint(0,10,100)


# plot histogram
bins=range(0,11,1)
print(bins)
plt.hist(x,bins=bins,color='g',
         histtype='bar',rwidth=1,alpha=0.6)

# set x,y-axis label
plt.xlabel('箱子重量(kg)')
plt.ylabel('销售数量(个)')

plt.show()

