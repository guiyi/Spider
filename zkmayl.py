#http://www.zkmayl.com/
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import requests
from bs4 import BeautifulSoup

"""
info:
author:Adair
github:https://github.com/CriseLYJ/
update_time:2019-08-06
"""

"""
模拟登陆--梅奥

GET /forum.php?mod=viewthread&amp; tid=320&amp; extra=page%3D1%26filter%3Dsortid%26sortid%3D5 HTTP/1.1
Host: www.zkmayl.com
User-Agent: PostmanRuntime/7.15.2
Accept: */*
Cache-Control: no-cache
Postman-Token: 2ac0fc39-e78f-4f52-a32c-c8b82e26b830,00e903e1-e940-419a-8065-6f7e94f7b590
Host: www.zkmayl.com
Cookie: djZq_2132_saltkey=N4U4cCF4; djZq_2132_lastvisit=1564966069; djZq_2132_onlineusernum=56; djZq_2132_visitedfid=41D56D37D38; djZq_2132_sid=o8dLk0; djZq_2132_lastact=1565079631%09forum.php%09viewthread; djZq_2132_st_p=175%7C1565079631%7C3b5f0b8515320930e5ab88b7b9faa611; djZq_2132_ulastactivity=c7f92b31E%2FQTnDKA%2Bilo3AWcbgqMHfUVebR1useLutkebZTuKRId; djZq_2132_auth=2d56BoNJf3QnOL9PfY3eH6gS7Hw8tV21JTeBFWiYfjTyF8XCnHfgzTZyDbKxdvVbp4TdtyLVyh%2BWj8nxuYDkmcI; djZq_2132_st_t=175%7C1565079602%7C463a84e554bc7bf985847e406a2a08cd; djZq_2132_forum_lastvisit=D_41_1565079602; djZq_2132_viewid=tid_320; 
djZq_2132_lip=180.168.36.202%2C1565079618
Accept-Encoding: gzip, deflate
Connection: keep-alive
cache-control: no-cache

"""



url = "http://www.zkmayl.com/forum.php?mod=viewthread&tid=326&extra=page=1&filter=sortid&sortid=5"

headers = {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Cookie" : "djZq_2132_saltkey=N4U4cCF4; djZq_2132_lastvisit=1564966069; djZq_2132_onlineusernum=56; djZq_2132_visitedfid=41D56D37D38; djZq_2132_sid=o8dLk0; djZq_2132_lastact=1565079631%09forum.php%09viewthread; djZq_2132_st_p=175%7C1565079631%7C3b5f0b8515320930e5ab88b7b9faa611; djZq_2132_ulastactivity=c7f92b31E%2FQTnDKA%2Bilo3AWcbgqMHfUVebR1useLutkebZTuKRId; djZq_2132_auth=2d56BoNJf3QnOL9PfY3eH6gS7Hw8tV21JTeBFWiYfjTyF8XCnHfgzTZyDbKxdvVbp4TdtyLVyh%2BWj8nxuYDkmcI; djZq_2132_st_t=175%7C1565079602%7C463a84e554bc7bf985847e406a2a08cd; djZq_2132_forum_lastvisit=D_41_1565079602; djZq_2132_viewid=tid_320; djZq_2132_lip=180.168.36.202%2C1565079618"
}
response = requests.get(url, headers = headers )
#print(response)
contentA = urllib.request.urlopen(url).read()
contentA = contentA.decode('UTF-8', 'ignore')
#print(contentA)
soup = BeautifulSoup(contentA,'html.parser')
for content1 in soup.select('.t_fsz'):
	print(content1)

