import matplotlib.pyplot as plt

x = ["Part1","Part2","Part3","Part4","Part5"]
y = [98,67,88,95,88]

colors = ["red","blue","green","orange","purple"]
plt.bar(x,y,color=colors,edgecolor="black")
plt.xlabel("Parts of Harry Potter",fontsize=17)
plt.ylabel("Popularity",fontsize=17)
plt.title("Popularity of Different Parts of Harry Potter",fontsize=17)
plt.show()