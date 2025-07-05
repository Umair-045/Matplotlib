import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [45,67,33,67,12]
y1 = [45,60,13,66,13]

plt.figure(figsize=[5,3])
plt.plot(x,y,label="Male")
plt.plot(x,y1,label="Female")

plt.legend(loc=0)
plt.show()