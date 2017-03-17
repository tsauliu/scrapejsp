import sys
import pprint

f=open('1.csv','r')
f_gbk=open('datatable.csv','w')
for line in f:
    print [line]
    f_gbk.write(line.encode('utf-8'))