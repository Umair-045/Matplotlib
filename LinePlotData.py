import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("C:/Users/Ahmed/Desktop/Info.xlsx")
df = pd.DataFrame(data)
plt.plot(df["Age"],df["Salary"])
print(df)

plt.show()