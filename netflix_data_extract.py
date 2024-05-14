import pandas as pd 
df = pd.read_csv('netflix_titles.csv')
import sqlalchemy as sal
engine = sal.create_engine('mssql://ANKIT\SQLEXPRESS/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()

df.to_sql('netflix_raw', con=conn , index=False, if_exists = 'append')
conn.close()

df.head()
df[df.show_id=='s5023']
max(df.description.dropna().str.len())
df.isna().sum()
