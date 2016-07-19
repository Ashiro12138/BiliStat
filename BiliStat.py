# -*- coding:utf-8 -*-
# Aurthor: Ashiro
# Purpose: Seek AV video stat
# Created: 17/07/2016

from lxml import html
import requests
import time

global attempt,n0,n1,n2,n3,n4,s0,s1,s2,s3,s4
attempt = 0
s0 = s1 = s2 = s3 = s4 = 0
n0 = n1 = n2 = n3 = n4 = 0

def cls():
    print("\n"*30)

def init():
    path = "http://www.kanbilibili.com/video/av"+str(aid)
    page = requests.get(path)
    tree = html.fromstring(page.content)
    #title = tree.xpath('//span[@data-reactid="37"]/text()')
    play = tree.xpath('//span[@class="data"]/text()')
    global n0,n1,n2,n3,n4
    n0 = play[0]
    n1 = play[1]
    n2 = play[2]
    n3 = play[3]
    n4 = play[4]

def update():
    path = "http://www.kanbilibili.com/video/av"+str(aid)
    page = requests.get(path)
    tree = html.fromstring(page.content)
    #title = tree.xpath('//span[@data-reactid="37"]/text()')
    play = tree.xpath('//span[@class="data"]/text()')
    global attempt,n0,n1,n2,n3,n4,s0,s1,s2,s3,s4
    attempt += 1
    s0 = play[0]
    s1 = play[1]
    s2 = play[2]
    s3 = play[3]
    s4 = play[4]
    #timedif = str(int(time.ctime().split()[3].split(":")[0])*60+int(time.ctime().split()[3].split(":")[1])-int(t))
    print("第"+str(attempt)+"次")
    #print("标题:",title[0])
    #print("播放:",play[0],"(在"+timedif+"分钟内增长了:",int(s0)-int(n0),")")
    #print("弹幕:",play[1],"(在"+timedif+"分钟内增长了:",int(s1)-int(n1),")")
    #print("收藏:",play[2],"(在"+timedif+"分钟内增长了:",int(s2)-int(n2),")")
    #print("评论:",play[3],"(在"+timedif+"分钟内增长了:",int(s3)-int(n3),")")
    #print("硬币:",play[4],"(在"+timedif+"分钟内增长了:",int(s4)-int(n4),")")
    print("播放:",play[0],"(在"+str(attempt-1)+"分钟内增长了:",int(s0)-int(n0),")")
    print("弹幕:",play[1],"(在"+str(attempt-1)+"分钟内增长了:",int(s1)-int(n1),")")
    print("收藏:",play[2],"(在"+str(attempt-1)+"分钟内增长了:",int(s2)-int(n2),")")
    print("评论:",play[3],"(在"+str(attempt-1)+"分钟内增长了:",int(s3)-int(n3),")")
    print("硬币:",play[4],"(在"+str(attempt-1)+"分钟内增长了:",int(s4)-int(n4),")")
    cls()
    time.sleep(60)
    #aid = input("AID: ")
    
#t = str(int(time.ctime().split()[3].split(":")[0])*60+int(time.ctime().split()[3].split(":")[1]))

aid = input("AID: ")
init()

while aid:
    update()
    
