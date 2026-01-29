import pandas as pd

df = pd.read_csv(r"C:\Users\cavus\Desktop\Titanic-Dataset.csv")


# print(df.columns)

# print(df.head(5))

filtre = df.loc[(df['Sex'] == 'male') & (df['Age'] > 25)]
print(filtre)