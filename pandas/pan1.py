import pandas as pd
import numpy as np
# d=[10,20,30,40]
# s=pd.Series(d)
# s.index=['a','b','c','d']
# print(s)

# d={'a':1,'b':2,'c':3}
# s=pd.Series(d)
# print(s)
# print(s.dtype)
# print(s.values)
# print(s.index)
# print(s.get('a'))

# # DataFrame
# d={
#     'name':['Raj','Kohli','Rohit'],
#     'age':[11,23,45]
# }
# df=pd.DataFrame(d,index=['A','B','C'])
# print(df)
# print(df.index)
# print(df.values)
# print(df.name)
# print(df.age)
# print(df.name.get('A'))


# data={
#     'weight':pd.Series([11,22,33]),
#     'length':pd.Series([1,2,3,4])
# }
# df=pd.DataFrame(data)
# # print(df)

# data = {
#     "name": [
#         "Aarav", "Vihaan", "Dhruv", "Anaya", "Myra", 
#         "Aanya", "Advait", "Dhruv", "Anaya", "Riya", 
#         "Aryan", "Krisha", np.nan, "Reyansh", "Kavya", 
#         "Vivaan", "Anvi", "Arjun", "Meera", np.nan
#     ],
#     "age": [25, 22, np.nan, 24, 30, 26, 21, 29, 23, 27, 
#             31, 24, 22, 30, 25, 29, np.nan, 23, 26, 21]
# }
# df=pd.DataFrame(data)
# # print(df)
# print("**")
# print(df.info())
# print(df.isnull())
# print(df.isnull().sum())
# print(df.describe())

# print(df.head())
# print(df.tail())
# print(df.name.duplicated())
# print(df.name.duplicated().sum())
# print(df.sort_index(ascending=False))
# print(df.sort_values('age'))

data = {
    "name": [
        "Aarav", "Vihaan", "Dhruv", "Anaya", "Myra", 
        "Aanya", "Vihaan", "Dhruv", "Anaya", "Riya", 
        "Aryan", "Krisha", np.nan, "Reyansh", "Kavya", 
        "Vivaan", "Anvi", "Arjun", "Vihaan", np.nan
    ],
    "age": [25, 22, np.nan, 24, 30, 26, 21, 29, 23, 27, 
            31, 24, 22, 30, 25, 29, np.nan, 23, 26, 21]
}
df=pd.DataFrame(data)
# print(df["name"])
# print(df[["name","age"]])
# print(df.iloc[2])
# print(df.iloc[1:6])
# print(df.age>25)
# print(df[df.age>25])

# df['Result']='Pass'
df['marks']=[85, 92, 78, 88, 95, 81, 76, 89, 84, 91, 
              87, 90, 79, 93, 82, 86, 80, 94, 83, 77]

# df.insert(1,'Class','Ninth')

# df["Fees"]=df.marks*12


# # df.Result="Fail"
# print(df)


# df.loc[df['age']==25,'marks']=567
# print(df)
# print(df.replace('Aarav','Abhinav'))
# print(df)
# # # df.to_csv('sample.csv')

# # del df['Fees']
# # print(df)

# # df.pop('Result')
# # print(df)

# # df=df.drop(columns=['Class','marks'])
# # print(df)

# df=df.drop_duplicates('name',keep='last')
# print(df)

# dt=df['age'].isin([25,20])
# print(dt)


# dt=df[df['age'].isin([25,30])]
# print(dt)

# # print("*****************************")
# dt1=df[df['marks']>90]
# print(dt1)


# print(df.isna())
# print(df.isna().sum())
# # # print(df.fillna(value=123))
# print(df.fillna(value=df.mean(numeric_only=True)))
# # # print(df.dropna())

# # print(df.bfill()) 1 2 3 N
# # print(df.ffill()) 1 2 3 N 4

# df.loc[19,'name']='kalu'
# print(df)



# # print(df.age.mean())
# # print(df.age.max())
# # print(df.age.min())
# # print(df.age.count())
# # print(df.age.agg(['mean','max','min','count']))

# custom_agg=df.agg(
#     {
#         'age':['mean','max','min','sum'],
#         'marks':['sum','mean']
#     }
# )
# print(custom_agg)

# print(df.age.transform(lambda x:x+1))
# print(df.age.transform(np.sqrt))
# print(df.age.transform(np.square))

# print(df[['age','marks']].transform(lambda x:x**2))
# print(df.age.value_counts(dropna=False))

df['City']='Rewa'
# # print(df)
# print(df.City.str.lower())
# print(df.City.str.upper())
# print(df.City.str.isalpha())
# print(df.City.str.len())
# print(df.City.str[:3])

# df['email']='User@gmail.com'
# # # print(df)
# print(df.email.str.endswith('@gmail.com'))


# # print(df)

data1 = {
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
}
df1 = pd.DataFrame(data1)

# Create second DataFrame
data2 = {
    'ID': [3, 4, 5, 6],
    'Score': [85, 90, 75, 80]
}
df2 = pd.DataFrame(data2)
# inner_join=pd.merge(df1,df2,on='ID')
# print(inner_join)

# inner_join=pd.merge(df1,df2,on='ID',how='left')
# print(inner_join)

# inner_join=pd.merge(df1,df2,on='ID',how='right')
# print(inner_join)

# inner_join=pd.merge(df1,df2,on='ID',how='outer')
# print(inner_join)



# # data1 = {
# #     'ID': [1, 2, 3, 4],
# #     'Name': ['Alice', 'Bob', 'Charlie', 'David']
# # }
# # df1 = pd.DataFrame(data1)

# # # Create second DataFrame
# # data2 = {
# #     'STU_ID': [3, 4, 5, 6],
# #     'Score': [85, 90, 75, 80]
# # }
# # df2 = pd.DataFrame(data2)

# # # print(pd.merge(df1,df2,left_on='ID',right_on='STU_ID'))


data1 = {
    'Product': ['Smartwatch', 'Camera', 'Printer', 'Speaker'],
    'Price': [250, 1200, 200, 150],
    'Quantity': [30, 8, 20, 45]
}
data2 = {
    'Product': ['Monitor', 'Keyboard', 'Mouse', 'Charger'],
    'Price': [200, 50, 30, 20],
    'Quantity': [15, 40, 60, 25]
}
data3 = {
    'Product': ['Webcam', 'Microphone', 'External HDD', 'USB Hub'],
    'Price': [70, 90, 100, 25],
    'Quantity': [35, 20, 50, 75]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)


# dt=pd.concat([df1,df2,df3])
# print(dt)
# dt=pd.concat([df1,df2,df3],axis=1)
# print(dt)

sales_data = {
    'Store': ['Store A', 'Store B', 'Store A', 'Store C', 'Store B', 'Store C', 'Store A'],
    'Product': ['Laptop', 'Tablet', 'Phone', 'Headphones', 'Laptop', 'Phone', 'Tablet'],
    'Sales': [1000, 300, 800, 100, 1200, 900, 600]
}
df = pd.DataFrame(sales_data)
# print(df)
# print(df.groupby('Product')['Sales'].sum())
# print(df.groupby(['Store', 'Product'])['Sales'].sum())

df=df.groupby('Product').agg({
    'Sales':['sum','mean','max','min','count']
})

# df.to_csv('one.csv',index=False)




# # # data1 = {
# # #     'Product': ['Smartwatch', 'Camera', 'Printer', 'Speaker'],
# # #     'Price': [250, 1200, 200, 150],
# # #     'Quantity': [30, 8, 20, 45]
# # # }
# # # data2 = {
# # #     'Product': ['Monitor', 'Keyboard', 'Mouse', 'Charger'],
# # #     'Price': [200, 50, 30, 20],
# # #     'Quantity': [15, 40, 60, 25]
# # # }
# # # data3 = {
# # #     'Product': ['Webcam', 'Microphone', 'External HDD', 'USB Hub'],
# # #     'Price': [70, 90, 100, 25],
# # #     'Quantity': [35, 20, 50, 75]
# # # }

# # # df1 = pd.DataFrame(data1)
# # # df2 = pd.DataFrame(data2)
# # # df3 = pd.DataFrame(data3)


# # # dt=pd.concat([df1,df2,df3])
# # # # dt.to_excel('sample.xlsx',index=False)

# # # # dt=pd.read_excel('sample.xlsx')
# # # # print(dt)

# # # dt.reset_index(drop=True, inplace=True)

# # # # Convert to JSON
df.to_json('sample1.json', orient='records')

# # # dt2=pd.read_json('sample1.json')
# # print(dt2)