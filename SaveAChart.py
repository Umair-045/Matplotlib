import matplotlib.pyplot as plt

brands = ["Oneplus","Apple","Samsung","Nokia","Redmi"]
x= [22,35,30,3,10]
ex = [0,0,0,0,0.1]
plt.pie(x,labels=brands,explode=ex,shadow=True,autopct='%1.1f%%',startangle=180)

plt.savefig("piechart.png")
plt.show()