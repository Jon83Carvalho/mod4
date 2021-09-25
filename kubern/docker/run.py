import pandas as pd

url='https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'

df=pd.read_csv(url)

print(df.size)

print(df.columns)

print(df.head())

