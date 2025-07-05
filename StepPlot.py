import matplotlib.pyplot as plt
x=["day1","day2","day3","day4","day5"]
y= [30,40,25,30,40]

plt.step(x,y,where="post")
plt.show()