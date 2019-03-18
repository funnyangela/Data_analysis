import re
# from urllib import request
import requests
import csv



url1 = 'https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190312&ie=utf8&bcoffset=7&p4ppushleft=%2C48&ntoffset=7&s=0'
url2 = 'https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190312&ie=utf8&bcoffset=4&p4ppushleft=%2C48&ntoffset=4&s=44'
# url = 'https://s.taobao.com/search?'
body_pattern = '"p4pTags"([\S\s]*?)"shopcard"'
head_pattern = '"raw_title":"([\S\s]*?)",'
store_pattern = '"nick":"([\S\s]*?)",'
price_pattern = '"view_price":"([\S\s]*?)",'
sales_num_pattern = '"view_sales":"([\S\s]*?)",'
location_pattern = '"item_loc":"([\S\s]*?)",'
comment_pattern = '"comment_count":"([\S\s]*?)",'

headers1 = {
'authority': 's.taobao.com',
'method': 'GET',
'path': '/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190312&ie=utf8&bcoffset=7&p4ppushleft=%2C48&ntoffset=7&s=0',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'thw=cn; cna=VLa5FLtiLCcCATyxtx3PRUjC; t=d9665e766f5285a301245ea200c94787; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; l=bBSpdM1Rvi9t-vXTBOfw5uI8Lj79mIOb8sPzw4OGSIB19W5_MppOOHwKt0uwd3Q_E_fIretrbJTb2Rnw8TzNs; v=0; cookie2=1014c5a3512b455b33ae85fd6cf6cfe1; _tb_token_=1039b63e5ee3; skt=b05e95a94b468465; publishItemObj=Ng%3D%3D; csg=c633713e; uc3=vt3=F8dByEv9pnudd2LIAKM%3D&id2=UNk%2BfciBWF45&nk2=2VqZN8shWICm&lg2=URm48syIIVrSKA%3D%3D; existShop=MTU1MjM1ODE1MA%3D%3D; tracknick=%5Cu80E1%5Cu68A6%5Cu5A77may; lgc=%5Cu80E1%5Cu68A6%5Cu5A77may; _cc_=VFC%2FuZ9ajQ%3D%3D; dnk=%5Cu80E1%5Cu68A6%5Cu5A77may; mt=ci=2_1; enc=lgohh%2FcEn%2BgatVu8%2FDB%2Bvsch99zYUOjXB%2FEosyPyyXGLtnHzO7DOxj3d%2Bgh3DOZx%2BIr8jkVlKQeOunWvaUKtJg%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; uc1=cookie14=UoTZ5iFytzKh1w%3D%3D&lng=zh_CN&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false&cookie21=WqG3DMC9FxUx&tag=8&cookie15=V32FPkk%2Fw0dUvg%3D%3D&pas=0; JSESSIONID=F4DA8BFF506A371306DEFCEB2A80C923; isg=BIeH7S_Sl5ZY-RPBTCCXLCN8Fj2RJFoWRghGbll0HZeeyKSKYVxDv9iCasgzJzPm',
'referer': 'https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190312&ie=utf8&bcoffset=4&p4ppushleft=%2C48&s=44&ntoffset=4',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
headers2 = {
'authority': 's.taobao.com',
'method': 'GET',
'path': '/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190312&ie=utf8&bcoffset=4&p4ppushleft=%2C48&ntoffset=4&s=44',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'thw=cn; cna=VLa5FLtiLCcCATyxtx3PRUjC; t=d9665e766f5285a301245ea200c94787; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; l=bBSpdM1Rvi9t-vXTBOfw5uI8Lj79mIOb8sPzw4OGSIB19W5_MppOOHwKt0uwd3Q_E_fIretrbJTb2Rnw8TzNs; v=0; cookie2=1014c5a3512b455b33ae85fd6cf6cfe1; _tb_token_=1039b63e5ee3; skt=b05e95a94b468465; publishItemObj=Ng%3D%3D; csg=c633713e; uc3=vt3=F8dByEv9pnudd2LIAKM%3D&id2=UNk%2BfciBWF45&nk2=2VqZN8shWICm&lg2=URm48syIIVrSKA%3D%3D; existShop=MTU1MjM1ODE1MA%3D%3D; tracknick=%5Cu80E1%5Cu68A6%5Cu5A77may; lgc=%5Cu80E1%5Cu68A6%5Cu5A77may; _cc_=VFC%2FuZ9ajQ%3D%3D; dnk=%5Cu80E1%5Cu68A6%5Cu5A77may; mt=ci=2_1; enc=lgohh%2FcEn%2BgatVu8%2FDB%2Bvsch99zYUOjXB%2FEosyPyyXGLtnHzO7DOxj3d%2Bgh3DOZx%2BIr8jkVlKQeOunWvaUKtJg%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; uc1=cookie14=UoTZ5iFytzKh1w%3D%3D&lng=zh_CN&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false&cookie21=WqG3DMC9FxUx&tag=8&cookie15=V32FPkk%2Fw0dUvg%3D%3D&pas=0; JSESSIONID=5F7298F3BDAC183FE92D3B54AAEEC568; isg=BGdnSUT-9_Z7d3OhLIB3zAPc9p3xRDq2ZqgmzjnUDvZJKIbqQbwHHDdiSmgTwBNG',
'referer': 'https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190312&ie=utf8&bcoffset=4&p4ppushleft=%2C48&s=44&ntoffset=4',
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

