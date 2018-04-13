import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [4,5,6,7]
x1 = [5,4,3,4]
y1 = [4,5,6,8]

plt.plot(x,y,label = 'line one')   #折线图
plt.plot(x1,y1,label = 'line two')

plt.xlabel('x_data')
plt.ylabel('N')
plt.title('测力曲线')

plt.legend()  #显示曲线标签

plt.show()

