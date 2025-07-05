import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [45,33,56,23,45]

plt.subplot(1,2,1)
plt.plot(x,y)


x = [6,7,8,9,10]
y = [67,50,66,56,82]

plt.subplot(1,2,2)
plt.plot(x,y)
plt.show()