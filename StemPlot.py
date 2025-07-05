import matplotlib.pyplot as plt

x = [10,40,20,40,20,40,20,40,60,70,50,40]

plt.stem(x,linefmt="--",markerfmt="o",bottom=5,orientation="horizontal")
plt.show()