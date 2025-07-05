import matplotlib.pyplot as plt

x = ["day1","day2","day3","day4","day5"]
y = [300,420,250,230,400]
y1 = [500,450,300,250,320]

plt.plot(x,y,marker="o",markersize=5,color="red",ls="-",label = "week1",alpha = 0.5)
plt.plot(x,y1,marker="*",markersize=5,color="blue",ls="--",label="week2")

plt.legend()
plt.show()