import pandas as pd
import matplotlib.pyplot as plt

# max rows
# pd.options.display.max_rows = 500

df = pd.read_csv("study-data/Mobiles-Dataset.csv", encoding="latin1")

print(df)

print(df.head().T)
# print(df.tail(10))

print(df.info())

new_df = df.dropna()

print(df)

# print(df.duplicated())

df.drop_duplicates(inplace= True)

print(df.info())


cleanned_prices = df["Launched Price (Pakistan)"].str.replace("PKR", "").str.replace(",", "").replace("Not available").astype(float)

x = cleanned_prices.mean()

y = cleanned_prices.median()

z = cleanned_prices.mode()

print(x)
print(y)
print(z)

print(df["Launched Price (Pakistan)"])
# x = df["Launched Price (Pakistan)"].mean()

# print(df.info())
# print(df.dtypes)
# print(df["Screen Size"])

df.plot()

plt.show()