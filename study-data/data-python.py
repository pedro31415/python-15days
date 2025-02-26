import pandas as pd

df = pd.read_csv("study-data/data.csv")

print(df.to_string())

a = [1,7,2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar["z"])
print(pd.__version__)


data =  {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# df = pd.DataFrame(data)

# print(df.to_string())
# print(df)
# print(df.loc[0])
# print(df.loc[[0,1]])

print(pd.options.display.max_rows)