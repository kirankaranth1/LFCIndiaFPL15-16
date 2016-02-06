from __future__ import print_function
import re
import requests
from lxml import html
from StringIO import StringIO
import sys
import os
import json
import math

def get_score(id):
    url="http://fantasy.premierleague.com/entry/"+str(id)+"/event-history/"+str(gw)+"/"
    while True:
        try:
            page = requests.get(url)
        except requests.ConnectionError:
            continue
        break
    tree = html.parse(StringIO(page.text)).getroot()

    points_xpath=".//*[@id='ism']/section[1]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div"
    deductions_xpath=".//*[@id='ism']/section[1]/div[2]/div[1]/div[2]/div/div[3]/div/dl/dd[2]"
    name_xpath=".//*[@id='ism']/section[2]/h1"
 
    t_points=int(tree.xpath(points_xpath)[0].text.strip(' \t\n\r'))
    #print(t_points)

    name=tree.xpath(name_xpath)[0].text.strip(' \t\n\r')
    #print(name)

    try:
        transfers=int(re.findall('\d+', tree.xpath(deductions_xpath)[0].text.strip(' \t\n\r'))[1])
    except IndexError,e :
        transfers=0;
    score=str(t_points-transfers)    
    #print(transfers)
    print("FPL name: "+name+" Score: "+score)    
    print("FPL name: "+name+" Score: "+score,file=f)  


gw=1
f=open("gw1.txt",'w')
for line in open('players-list.txt'):
    line=str(line.strip(' \t\n\r'))
    try:
        id=int(re.findall('\d+', line)[0].strip(' \t\n\r'))
        get_score(id)

    except IndexError,e :
        print(line)
        print(line,file=f)
