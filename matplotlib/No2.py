import numpy as np
import matplotlib.pyplot as plt

x = [1,2,5,7,9]
y = [4,19,10,56,53]

#plt.bar(x,y)  #条形图
#plt.xlim(12)
#plt.ylim(14)
#plt.axis([0,12,0,100])  # 轴的范围

#plt.show()


x1 = np.random.randint(1,100,100)
bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(x1,bins)  #直方图
plt.show()