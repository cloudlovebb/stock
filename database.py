from sqlalchemy import create_engine
import tushare as ts

df = ts.get_tick_data('600848', date='2014-12-22')
engine = create_engine('mysql://user:passwd@127.0.0.1/db_name?charset=utf8')

#存入数据库
df.to_sql('tick_data',engine)

#追加数据到现有表
#df.to_sql('tick_data',engine,if_exists='append')

##########
from sqlalchemy import create_engine
import tushare as ts
df = ts.get_concept_classified()
engine = create_engine('mysql://root:123456@127.0.0.1/stock_info?charset=utf8')
df.to_sql('concept_classified',engine)
##########

from sqlalchemy import create_engine
from sqlalchemy.types import VARCHAR
import tushare as ts
df = ts.get_stock_basics()
engine = create_engine('mysql://root:123456@127.0.0.1/stock_info?charset=utf8')
df.to_sql('stock_base_info',engine)


data.to_sql('stock_base_info',engine,if_exists='replace',dtype={'code':VARCHAR(data.index.get_level_values('code').str.len().max())})
##########
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,BigInteger,Text

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Concept_stock(Base):
    # 表的名字:
    __tablename__ = 'concept_classified'

    # 表的结构:
    index = Column(BigInteger,primary_key=True)
    code = Column(Text)
    name = Column(Text)
    c_name = Column(Text)

# 初始化数据库连接:
engine = create_engine('mysql://root:123456@127.0.0.1/stock_info?charset=utf8')
# 创建session类型:
Session = sessionmaker(bind=engine)

session = Session()
for row in session.query(Concept_stock.code).filter_by(c_name='次新股'):
        print (row.code)