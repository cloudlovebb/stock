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
for row in session.query(Stock_base_info.code):
	try:
		df = ts.get_k_data(row.code)
		today_price = df.tail(1).iloc[0].close
		today_vol = df.tail(1).iloc[0].volume
		yest_price = df.tail(2).iloc[0].close
		mean_60_vol = df.tail(61)[0:60].describe().ix['mean'].volume
		mean_60_price = df.tail(60).describe().ix['mean'].close
		if (int(today_vol)/int(mean_60_vol)) >=2.5 and ((float(today_price)-float(yest_price))/yest_price) >=0.04 and (float(today_price)- float(mean_60_price)) > 0 and (float(mean_60_price) - float(yest_price)) > 0:
			print (row.code)
	except :
		continue

