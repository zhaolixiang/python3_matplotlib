import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

kinds="简易箱","保温箱",'行李箱','蜜蜂箱'
colors=['#e41a1c','#377eb8','#4daf4a','#984ea3']

soldNums=[0.05,0.45,0.15,0.35]

# pie chart
plt.pie(soldNums,labels=kinds,autopct='%3.1f%%',startangle=60,colors=colors)
plt.title('不同类型箱子的销售数量占比')
plt.show()