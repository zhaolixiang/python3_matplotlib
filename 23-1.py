import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

x=np.random.randn(1000)

plt.boxplot(x)

plt.xticks([1],['随机数生成器AlphaRM'])
plt.ylabel('随机数值')
plt.title('随机数生成器抗干扰能力的稳定性')

plt.grid(axis='y',ls=':',lw=1,color='gray',alpha=0.4)

plt.show()