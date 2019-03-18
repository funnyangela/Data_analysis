import re
import requests
import csv



url = 'https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190312&ie=utf8&bcoffset=7&p4ppushleft=%2C48&ntoffset=7&s=0'


body_pattern = '"p4pTags"([\S\s]*?)"shopcard"'
head_pattern = '"raw_title":"([\S\s]*?)",'
store_pattern = '"nick":"([\S\s]*?)",'
price_pattern = '"view_price":"([\S\s]*?)",'
sales_num_pattern = '"view_sales":"([\S\s]*?)",'
location_pattern = '"item_loc":"([\S\s]*?)",'
comment_pattern = '"comment_count":"([\S\s]*?)",'

headers = {
'authority': 's.taobao.com',
'method': 'GET',
'path': '/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190312&ie=utf8&bcoffset=7&p4ppushleft=%2C48&ntoffset=7&s=0',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'xxxx', #输入cookie
'referer': 'xxxx', #输入referer
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

def getstr(x):
    return str(x[0])

#访问淘宝页面
r = requests.get(url2,headers=headers2)
htmls = r.text

# 正则提取数据
taobao_num = []
body_html = re.findall(body_pattern,htmls)

for body in body_html:
    head = re.findall(head_pattern,body)
    store = re.findall(store_pattern,body)
    price = re.findall(price_pattern,body)
    sales = re.findall(sales_num_pattern,body)
    location = re.findall(location_pattern,body)
    comment = re.findall(comment_pattern,body)
    #将返回数据存放字典中
    store_info = {'store':getstr(store),'head':getstr(head),'price':getstr(price),'sales':getstr(sales),'location':getstr(location),'comment':getstr(comment)}
    taobao_num.append(store_info)

 #创建CSV文件存储数据
fq = open('taobao_02.csv','w',encoding='utf-8')
fq.write('store,head,price,sales,location,comment,\n')

for store in taobao_num:
    count = 0
    for v in store.values():
        count += 1
        if count % 6 != 0:
            fq.write(str(v)+',')
        else:
            fq.write(str(v)+'\n')

fq.close()

