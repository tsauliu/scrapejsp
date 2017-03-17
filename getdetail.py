#-*-coding:utf-8 -*-
def getothers(link):
    import sys
    import pprint
    reload(sys)
    sys.setdefaultencoding('utf-8')

    from bs4 import BeautifulSoup
    import requests
    res=requests.get(link)
    f=open('./html/'+link[-24:]+'.html','w')
    f.write(res.text)
    soup = BeautifulSoup(res.text,"lxml")
    for tr in soup.find_all('tr'):
        th=tr.find_all('th')
        try:
            if '其它'.decode('utf-8') in th[0].text:
                thetext= tr.find('td').text
        except:
            pass
    return thetext

source=open('1.csv','r')
out=open('dianche.txt','w')
thedict={}
for line in source:
    # try:
    if len(line.split(',')) >= 6:
        type= line.split(',')[4]
        link=line.split(',')[6]
        id=line.split(',')[5]
        if '电' in type:
            print [id,type,link]
            text = getothers(link)
            str='@'.join([id,type,link,text])
            print str
            thedict.update({id:[id,type,link,text]})
            out.write(str+'\n')
    # except:
    #     pass

import json
with open('db.json','w') as fp:
    json.dump(thedict,fp)