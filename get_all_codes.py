import tushare as ts

ts.get_stock_basics()

ts.get_hist_data('600848')



df = ts.get_stock_basics()
date = df.ix['600848']['timeToMarket'] 


#########
import time
import tushare as ts
today = time.strftime('%Y-%m-%d',time.localtime(time.time()))

df = ts.get_concept_classified()
#df[df.c_name == '次新股']
for code in df[df.c_name == '次新股']['code']:
    data = ts.get_k_data(code)
    #max_price = max(data['high'])
    max_price = data.describe().high.loc['max']
    today_price = data[data.date == str(today)].iloc[0]['low']
   # print max_price
   # print today_price
    num = (max_price - today_price)/max_price
    if num > 0.3:
    	name = df[df.c_name == '次新股'][df.code == str(code)].iloc[0]['name']
    	print (code,name)


#########
for code,name in df[df.c_name == '次新股'].loc[:,['code','name']]:
	print (code,name)


a.loc[:,['a','b'] ]
#############


历史数据
data = ts.get_k_data('600848')
print data['high']


df = ts.get_stock_basics()
date = df.ix['600848']['timeToMarket']


		code  name        c_name
1195  600908  无锡银行    次新股
1196  600909  华安证券    次新股
1197  600919  江苏银行    次新股
1198  600926  杭州银行    次新股
1199  600936  广西广电    次新股


#########
4% vol >=2.5
#########