import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]

NOP1 = [5,10,30,20,35,50,80]
NOP2 = [10,20,30,25,40,50,90]
NOP3 = [8,30,50,60,70,90,100]\

plt.stackplot(days,NOP1,NOP2,NOP3,labels=["week1","week2","week3"])
plt.legend()
plt.show()