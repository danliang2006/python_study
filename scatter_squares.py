import matplotlib.pyplot as plt

#散点图
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]


plt.scatter(x_values,y_values,s=4,edgecolor='none',c=y_values,cmap=plt.cm.Blues)  #设置颜色映射
plt.title("Square Number",fontsize=24)
plt.xlabel("values",fontsize=14)
plt.ylabel("Square of value",fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)

#设置每个坐标轴的取值范围
#plt.axis([0,1100,0,1100000])

#自动保存图表
#plt.savefig('squares_plot.png',bbox_inches='tight')
plt.show()