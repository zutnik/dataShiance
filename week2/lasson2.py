import pandas as pd

df1 = pd.read_csv('datasets/Admission_Predict.csv', index_col=0)
df = pd.read_csv('datasets/Admission_Predict.csv')
print(df.head())
print(df1.head())
print(df1.columns)

df1 = df1.rename(columns={'LOR ': 'Letter of recomendations'})
print(df1.head())
df1.head()
newdf = df1.rename(mapper=str.strip, axis='columns')
newdf.head()

cols = list(newdf.columns)
print(cols)
cols = [x.lower().strip() for x in cols]

newdf.columns = cols
newdf.head()
