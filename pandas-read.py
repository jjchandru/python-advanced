import pandas as pd

data = pd.read_excel("AUTO-AERO.xlsx")

print(data.head(3))
print(data.iloc[:3, :2])
