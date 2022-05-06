import pandas as pd

record1 = pd.Series({'Name': 'Bogdan', 'Student': 'IA-94', 'Score': '75'})
record2 = pd.Series({'Name': 'Alex', 'Student': 'IA-92', 'Score': '85'})
record3 = pd.Series({'Name': 'Lina', 'Student': 'IN-9', 'Score': '34'})
df = pd.DataFrame([record1, record2, record3], index=["student1", "student2", "student3"])
# print(df.head())
# print(df.loc['student2'])
# print(df.loc['student2', 'Name'])
print(df.T.loc['Name'])

copy_df = df.copy()
copy_df.drop('Name', inplace=True, axis=1)
print(copy_df)
print(df)
del copy_df['Student']
print(copy_df)
df['City'] = 'Poltava'
print(df)
