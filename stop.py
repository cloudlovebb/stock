import tushare as ts
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import Column, Integer, String,BigInteger,Text
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR
import time
import datetime


def get_new_stock_codes():
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
    code_list = []
    for row in session.query(Concept_stock.code).filter_by(c_name='次新股'):
            code_list.append(row)
    return code_list


new_codes = get_new_stock_codes()




Base = declarative_base()
class Stock_base_info(Base):
   # 表的名字:
	__tablename__ = 'stock_base_info'
   # 表的结构:
   #index = Column(BigInteger,primary_key=True)
   #code = Column(Text)
   #name = Column(Text)
   #c_name = Column(Text)
	code             =  Column(VARCHAR,primary_key=True)
	name             =  Column(TEXT)
	industry         =  Column(TEXT)
	area             =  Column(TEXT)
	pe               =  Column(DOUBLE)
	outstanding      =  Column(DOUBLE)
	totals           =  Column(DOUBLE)
	totalAssets      =  Column(DOUBLE)
	liquidAssets     =  Column(DOUBLE)
	fixedAssets      =  Column(DOUBLE)
	reserved         =  Column(DOUBLE)
	reservedPerShare =  Column(DOUBLE)
	esp              =  Column(DOUBLE)
	bvps             =  Column(DOUBLE)
	pb               =  Column(DOUBLE)
	timeToMarket     =  Column(BIGINT)
	undp             =  Column(DOUBLE)
	perundp          =  Column(DOUBLE)
	rev              =  Column(DOUBLE)
	profit           =  Column(DOUBLE)
	gpr              =  Column(DOUBLE)
	npr              =  Column(DOUBLE)
	holders          =  Column(BIGINT)

# 初始化数据库连接:
engine = create_engine('mysql://root:123456@127.0.0.1/stock_info?charset=utf8')
# 创建session类型:
Session = sessionmaker(bind=engine)

session = Session()
#for row in session.query(Stock_base_info.code):
for row in session.query(Stock_base_info.code,Stock_base_info.name):
    try:
       # print (row.code)
        df = ts.get_hist_data(row.code)
        df = df.head(30)
        last = count = 1
        for ix, item in df.iterrows():
            p = item.p_change
           # print (item) 
            if int(p) >= 9:
                if (count - last) == 1:
                   if row.code not in new_codes:
                       print (row.code,row.name)
                   break
                last = count
            count += 1    
       # time.sleep(1)
    except:
        continue

