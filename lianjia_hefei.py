
#coding:utf-8  
# Filename: lianjia.py
# DateTime: 2017.04.28
# Author : Adair

'''[数据库表结构]
[lianjia_hefei数据库表结构]

CREATE TABLE `lianjia_hefei` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area` varchar(30) DEFAULT NULL,
  `fangxing` varchar(10) DEFAULT NULL,
  `allhouse` int(10) DEFAULT NULL,
  `createdate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=gbk;'''


import urllib.request
import requests
from bs4 import BeautifulSoup
import pymysql
import io,sys,string
import time,re
import numpy as np
import matplotlib.pyplot as plt
#解决中文显示问题
import matplotlib
matplotlib.use('Qt4Agg')  
matplotlib.rcParams['font.sans-serif'] = ['SimHei']   
matplotlib.rcParams['font.family']='sans-serif'  
#解决负号'-'显示为方块的问题  
matplotlib.rcParams['axes.unicode_minus'] = False 




OutFile = open("lianjia_hefei"+".txt","a",encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 
#area = ['baohe', 'shushan', 'luyang', 'yaohai', 'zhengwu', 'binhuxinqu', 'jingkai2', 'gaoxin8', 'xinzhan', 'feidong', 'feixi', 'changfeng']
#fangxing = ['l1', 'l2', 'l3', 'l4', 'l5']
#areaCN = ['包河', '蜀山', '庐阳', '瑶海', '政务', '滨湖新区', '经开', '高新', '新站', '肥东', '肥西', '长丰']

#爬链家数据
def lianjia1():
    area1 = {    'baohe'        : '包河',
                 'shushan'      : '蜀山',
                 'luyang'       : '庐阳',
                 'yaohai'       : '瑶海',
                 'zhengwu'      : '政务',
                 'binhuxinqu'   : '滨湖新区',
                 'jingkai2'     : '经开',
                 'gaoxin8'      : '高新',
                 'xinzhan'      : '新站',
                 'feidong'      : '肥东',
                 'feixi'        : '肥西',
                 'changfeng'    : '长丰'
         }
    fangxing1 = {'l1'       : '一室',
                 'l2'       : '二室',
                 'l3'       : '三室',
                 'l4'       : '四室',
                 'l5'       : '五室'
         }
    urls = ['http://hf.lianjia.com/ershoufang/']
    #'http://hf.fang.lianjia.com/loupan/',
    for u in urls:
        for key, val in area1.items():
            for key1, val1 in fangxing1.items():
                url = str(u)+ str(key)+'/'+ str(key1)+'/'
                time.sleep(10)
                #print ('End:' + '\t' +time.ctime())
                content = urllib.request.urlopen(url).read()
                content = content.decode('UTF-8', 'ignore')
                #print(content)
                soup = BeautifulSoup(content,'html.parser')
                print(soup.prettify())

                for content1 in soup.select('.resultDes'):
                    #print(content)
                    total = content1.select('.total')[0].text[3:]
                    print(val,val1,total)
                    OutFile.write(str(key)+"\t"+str(val)+"\t"+str(key1)+"\t"+str(val1)+"\t"+str(total)+"\n")


#数据库连接
def connLinajia():
    global conn,sql
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='链家', charset='utf8')
    cur = conn.cursor()
    

#文件写入数据库表
def insertLianjia(fileName):
    #print(fileName)
    f = open(fileName, 'rb') # 打开文件
    #f = file('poem.txt')
    # if no mode is specified, 'r'ead mode is assumed by default
    while True:
        line = f.readline().decode('UTF-8', 'ignore')
        if len(line) == 0: # Zero length indicates EOF
            break
        areaKey = line.split('\t')[0]
        fangxingKey = line.split('\t')[1]
        
        p = re.compile(r'\D')
        amount= p.split((line.split('\t')[2]))[1]
        #amount = p.split(amount1)[1]
        #print(areaKey,fangxingKey,amount)
        connLinajia()
        DateTime =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
        sql="INSERT IGNORE INTO `lianjia_hefei` (`area`,`fangxing`,`allhouse`,`createdate`) VALUES (%s,%s,%s,%s)"
        try:
            with conn.cursor() as cursor:
                print(areaKey,fangxingKey,amount)
                cursor.execute(sql,(areaKey,fangxingKey,amount,DateTime))
                conn.commit()
                cursor.close()
        finally:
            pass
        # Notice comma to avoid automatic newline added by Python
    f.close() # close the file



#清空数据库表
def truncate():
    connLinajia()
    try:
        with conn.cursor() as cursor:
            cursor.execute('truncate table lianjia_hefei')
            conn.commit()
            cursor.close()
    finally:
        pass



#伪装浏览器访问
def lianjia2():
    area1 = {     'baohe'       : '包河',
                 'shushan'      : '蜀山',
                 'luyang'       : '庐阳',
                 'yaohai'       : '瑶海',
                 'zhengwu'      : '政务',
                 'binhuxinqu'   : '滨湖新区',
                 'jingkai2'     : '经开',
                 'gaoxin8'      : '高新',
                 'xinzhan'      : '新站',
                 'feidong'      : '肥东',
                 'feixi'        : '肥西',
                 'changfeng'    : '长丰'
         }
    fangxing1 = {'l1'       : '一室',
                 'l2'       : '二室',
                 'l3'       : '三室',
                 'l4'       : '四室',
                 'l5'       : '五室'
         }
    urls = ['http://hf.fang.lianjia.com/loupan/', 'http://hf.lianjia.com/ershoufang/']
    for u in urls:
        #print (url)
        for key, val in area1.items():
            #print(name, address)
            for key1, val1 in fangxing1.items():
                #print(name, address)
                #print (u,key,key1);
                url = str(u)+ str(key)+'/'+ str(key1)+'/'
                #print(url)
                #content = urllib.request.urlopen(url).read()
                #headers = {'User-Agent':'Mozilla / 5.0(X11;Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 50.0.2661.102 Safari / 537.36'}
                headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0'}
                content = requests.get(url, headers = headers).content
                content = content.decode('UTF-8', 'ignore');
                #print(content)
                soup = BeautifulSoup(content,'html.parser')
                #print(soup.prettify())

                for content1 in soup.select('.resultDes'):
                    #print(content)
                    total = content1.select('.total')[0].text[3:]
                    print(val,val1,total)
                    OutFile.write(str(val)+"\t"+str(val1)+"\t"+str(total)+"\n")






#画图
def makepie():
    global la,da,num
    la = ''
    da = ''
    ta = ''
    ca = ''
    num = 0

    connLinajia()
    cursor = conn.cursor()

    sql1 ='select area,sum(allhouse)as alls from lianjia_hefei  GROUP BY area order by sum(allhouse) desc '
    cursor.execute(sql1)
    data1 = cursor.fetchall()

    for k in range(0,len(data1)):
        #print(data1[k][0])
        la = la + ',' + "'" +data1[k][0] + "'"
        da = da + ','+  str(data1[k][1])
        num = num+data1[k][1]
        if(k == 0):
            ca = ca + ','+  str(0.1)
        else:
            ca = ca + ','+  str(0)

    for k in range(0,len(data1)):
        #print(data1[k][1],num)
        ta = ta + ',' + str(round( (data1[k][1]/num)*100) )


    print(tuple(eval(la[1:])) , list(eval(da[1:])) ,num,ta[1:],tuple(eval(ca[1:])))
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    lab = tuple(eval(la[1:]))
    labels = lab
    #print(len(lab),type(lab))
    #print(len(labels),type(labels))
    sizes = list(eval(ta[1:]))
    explode = tuple(eval(ca[1:]))  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()



#入口函数
if __name__ == '__main__':


    lianjia1()
    #truncate()
    insertLianjia('lianjia_hefei.txt')
    makepie()
    #lianjia2()
