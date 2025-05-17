import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.impute 
df=pd.read_csv(r"C:\Users\nitrsh\Downloads\ml_dirty_data.csv")
# print
# print(df.head())
# print(df.shape)
# print(df.isna().sum())
# print(df.isna().sum().sum())
# print(((df.isna().sum())/df.shape[0])*100)

# print((df.isna().sum().sum())/df.shape[0]*df.shape[1])

# print(df.notna().sum())
# sns.heatmap(df.isna())
# plt.show()

# df.fillna(value=10)
# sns.heatmap(df.isna())
# plt.show()

# print(df.isna().sum())
# df.drop(columns=["rating"],inplace=True)
# print(df.head())
# df.fillna(10,inplace=True)
# print(df.isna().sum())

# print(df.info())
# print(df.isna().sum())

# df.bfill(inplace=True)
# df.ffill(inplace=True)
df["department"].fillna(df["department"].mode()[0],inplace=True)


for i in df.select_dtypes("float64").columns:
    df[i].fillna(df[i].mode()[0],inplace=True)

print(df.isna().sum())
