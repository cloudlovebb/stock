from sqlalchemy import create_engine
from sqlalchemy.types import VARCHAR
import tushare as ts
df = ts.get_stock_basics()
engine = create_engine('mysql://root:123456@127.0.0.1/stock_info?charset=utf8')

df.to_sql('stock_base_info',engine,if_exists='replace',dtype={'code':VARCHAR(df.index.get_level_values('code').str.len().max())})
