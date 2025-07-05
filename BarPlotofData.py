import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("C:/Users/Ahmed/Desktop/Info.xlsx")
df = pd.DataFrame(data)
print(df)

plt.bar(df["Age"],df["Salary"])
plt.xlabel("Age",fontsize=17)
plt.ylabel("Salary",fontsize=17)
plt.show()