import pandas as pd
# d={
#     'name':['a','b','c'],
#     'age':[11,23,45]
# }
# df=pd.DataFrame(d)
# print(df)
# # print(df.to_csv('sample1.csv',index=False))
# print()
# print(df.head(1))
# print()
# print(df.tail(1))
# print()
# print(df.describe())


# import inflect
# p = inflect.engine()

# d=pd.read_csv('sample_employee_data.csv')
# d['Employee ID'][0]='E7000'
# index_words = [p.number_to_words(i) for i in range(1, len(d) + 1)]
# d.index = index_words
# print(d.to_csv('sample_employee_data.csv'))


# d=pd.read_csv('sample_employee_data.csv')
# d.drop(columns=d.columns[d.columns.str.contains('^Unnamed')], inplace=True)

# # Display the remaining column names
# print(d.columns.tolist())
# print(d.to_csv('sample_employee_data.csv'))
# print(d.loc['one'])

# print(d.columns.tolist())





d=pd.read_csv('sample_employee_data.csv')
# print(d)
print(d.index)
print(d.sort_index(axis=0,ascending=False))
print(d['First Name'])

# s=pd.Series(d['First Name'])
# print(type(s))