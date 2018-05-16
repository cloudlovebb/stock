import time
import datetime
import tushare as ts

def get_timeToMarket(code):
    df = ts.get_stock_basics()
    d = df.ix[code]['timeToMarket'] 
    return str(d).split('.')[0]

today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
#df = ts.get_concept_classified()
#new_stock = df[df.c_name == '次新股']

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
    for row in session.query(Concept_stock.code,Concept_stock.name).filter_by(c_name='次新股'):
            code_list.append(row)
    return code_list


new_stock  = get_new_stock_codes()

#print (new_stock)
#df[df.c_name == '次新股']
for code,name in new_stock:
#    d1 = datetime.datetime.strptime(today,'%Y-%M-%d')
#    timeToMarket = get_timeToMarket(code)
#    d2= datetime.datetime.strptime(timeToMarket,'%Y%M%d')
#    diff = (d1 - d2).days
#    if int(diff) >= 90:
#        continue
	try:  
		data = ts.get_k_data(code)
    #max_price = max(data['high'])
#    print (data)
		max_price = data.describe().high.loc['max']
		today_price = data[data.date == "2017-03-31"].iloc[0]['low']
   # print max_price
   # print today_price
		num = (max_price - today_price)/max_price
		if num > 0.3:
			print (code,name,num)
	except:
		continue




