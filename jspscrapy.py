#-*-coding:utf-8 -*-
import sys
import pprint
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
output=open('1.csv','w')
from getdetail import getothers
output2=open('detail.text','w')

for pagenum in range(1,83):

    cookies = {
        'JSESSIONID': '9AFD803E8FB8771A54372F9D1B128E91',
    }

    headers = {
        'Origin': 'http://data.miit.gov.cn',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en,zh-CN;q=0.8,zh;q=0.6,zh-TW;q=0.4,en-US;q=0.2',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Referer': 'http://data.miit.gov.cn/datainfo/miit/cpsb_gs294.jsp',
        'Connection': 'keep-alive',
        'DNT': '1',
    }

    data = [
      ('datainfo_id', ''),
      ('datainfo_action', ''),
      ('count', '4088'),
      ('pages', '82'),
      ('page', str(pagenum)),
      ('qymc', ''),
      ('cpsb', ''),
      ('cpmc', ''),
      ('cpxh', ''),
    ]

    respose=requests.post('http://data.miit.gov.cn/datainfo/miit/cpsb_gs294.jsp', headers=headers, cookies=cookies, data=data)
    import pprint
    f=open('./html/'+str(pagenum)+'.html','w')
    f.write(respose.text)

    page=respose.text
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page,"lxml")

    table=soup.find("table", { "class" : "list-table" })


    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        try:
            for i in tds:
                write=str(i.text).replace('\t','').replace('\n','').replace('\r','')
                if '详情' in i.text:
                    # print [i]
                    the= i.find('a')['href'].split("'")
                    write='http://data.miit.gov.cn/datainfo/miit/cpsb_gsDetails.jsp?cp_month='+ the[1]+'&cp_id='+the[3]
                    link=write
                output.write(write+',')
                # print([write])
                # print [i.text]
            output.write('\n')
        except:
            pass