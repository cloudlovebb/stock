from sqlalchemy import create_engine
import tushare as ts
df = ts.get_concept_classified()
engine = create_engine('mysql://root:123456@127.0.0.1/stock_info?charset=utf8')
df.to_sql('concept_classified',engine,if_exists='replace')
