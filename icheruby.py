import urllib.request
import requests
from bs4 import BeautifulSoup
import pymysql
import io,sys,string
import time,re
import numpy as np
import matplotlib.pyplot as plt
import os

#获取所有医院列表
def getHospital(url):
    contentA = urllib.request.urlopen(url).read()
    contentA = contentA.decode('UTF-8', 'ignore')
    soup = BeautifulSoup(contentA,'html.parser')
    #content = soup.find_all("a" , attrs={"target": "_blank"})
    
    content = soup.select('a[href="https://www.icheruby.com/hospital/"]')
    #print(content)
    urls =''
    for link in soup.find_all('a'):
        url = link.get('href')

        if(url != None): 
            matchObj = re.search( r'hospital', url)
            #print(matchObj)
            
            if(matchObj != None):
                urls= urls+",'"+url.lstrip()+"'"
    #print(urls)
    return urls


#医院详情抓取     
def getHospitalDetail(url):
    #print(url)
    
    contentA = urllib.request.urlopen(url).read()
    contentA = contentA.decode('UTF-8', 'ignore')
    soup = BeautifulSoup(contentA,'html.parser')

    #简介
    for content1 in soup.select('.fl-top-one'):
        title = content1.select('.title')
        title = regexDiv(str(title[0]))

  

        short_desc = content1.select('.content-top-Two')
        short_desc_img = getImgSrc(getImg(short_desc))

        #short_desc_img = re.search(r'src.*', str(short_desc)).group()
        short_desc_content = re.search(r'fr.*', str(short_desc)).group()[4:-6] 
    

        #print(title,short_desc_img,short_desc_content)

    #基本信息
    for content2 in soup.select('#doctor_info'):
        #pass
        #print(content2)
        names = content2.find_all("dt", class_="basicInfo-item name")
        values= content2.find_all("dd", class_="basicInfo-item value")

        for name,value in zip(names,values):
            pass
            #print(name.get_text(),value.get_text())


    #医院概览
    for content3 in soup.select('#hospital_introduction'):
        #print(content3)
        consultation = content3.select('.Consultation')
        jianjie = content3.select('#hospital_jianjie')[0].get_text()
        contents = content3.find_all("p")
        for content in contents:
            print(content.get_text())

        print(jianjie,content)
        
    
def  regexNum(text):

    num = re.sub(r'\D', "", text)
    return num

def  regexDiv(text):

    txt = re.search(r"(>[A-Za-z].*<)", text)
    return txt.group()[1:-1] 

def getImg(result):

    for r in result:

        pattern = '<img[^>]*/>'
        p = re.findall(pattern, str(r))
        
    return p  

def getImgSrc(result):
    for r in result:

        pattern = '(http|https):.*(jpg|png|gif)'
        p = re.search(pattern, str(r))

    return p.group() 

#获取图片
def grap_image(url):
    # 下载网页
    #url = 'https://www.icheruby.com/hospital/743.html'
    html = urllib.request.urlopen(url)
    content = html.read()
    html.close()

    # 使用beautifulsoup匹配图片
    html_soup = BeautifulSoup(content, 'lxml')
    all_img_links = html_soup.find_all('img',)
    #print(all_img_links)

    #指定文件路径
    path = os.getcwd()
    new_path = os.path.join(path, 'pictures')
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
    new_path += '/' #此处需要和windows系统区分开

    # 下载图片
    image_couter = 1
    for img_link in all_img_links:

        file_name = '%s.jpg' % image_couter
        img_url = img_link['src']
        if "https://www.icheruby.com/" not in img_url:
            img_url = 'https://www.icheruby.com/'+img_url
 
        if len(img_url) > 0:
            urllib.request.urlretrieve(img_url, new_path + file_name)
            image_couter += 1
    print('下载图片完成')


    
#入口函数
if __name__ == '__main__':  
    
    url = 'https://www.icheruby.com/yyk.html'
                urls = getHospital(url)
                url='https://www.icheruby.com/hospital/743.html'
                getHospitalDetail(url)
    '''if(urls):
                    #print(urls)
                    url = ''
                    for url in urls.split(','):
                        if(url != ''):
                            #print(url)
                            grap_image(url)
                            getHospitalDetail(url)'''
        
