from sqlalchemy import create_engine
import pandas as pd
import psycopg2 
import numpy as np
import os


uri = os.environ['URI']
db = create_engine(uri)

df=pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
df.to_sql('rakok',db,if_exists='append',index=False)