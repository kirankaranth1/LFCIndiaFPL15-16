#!/usr/bin/env python
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
    page = requests.get(url)
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
    return(score,name)

def get_team(name):
    lno=0    
    myFile=open('players-list.txt')
    
    for num, line in enumerate(myFile, 1):
        if name in line:
            #print 'found at line:', num
            lno=num
    #print(lno)
    myFile=open('players-list.txt')
    lines=myFile.readlines()
    team_list=[name]
    for i in range(lno,lno+8):
        id=int(re.findall('\d+', lines[i])[0].strip(' \t\n\r'))
        team_list.append(id)
    return(team_list)    

def print_score(team):
    print("Calculating scores of "+team[0])
    scores=[]
    names=[]
    for i in range(1,9):
        score,name=get_score(team[i])
        scores.append(score)
        names.append(name)
    #print(names,scores)
    print("Team: "+team[0],file=logfile)
    print("Captain: "+names[(team[9]-1)],file=logfile)
    print("Vice Captain: "+names[(team[10]-1)],file=logfile)
    if team[11]=='h':
        print("Home advantage : YES",file=logfile)
        hw=1.2
    else:
        print("Home advantage : NO",file=logfile)
        hw=1
    scores = map(int, scores)
    print("Team scores: "+str(scores),file=logfile)
    max_score=(max(scores))
    t_score=sum((scores))
    captain=(scores[team[9]-1])
    vc=(scores[team[10]-1])
    #print(captain,vc)


    t_score=t_score-max_score+(hw*max_score)+captain+(0.5*vc)

    #print("Total score :"+str(t_score)+"\n")
    print("Total score :"+str(t_score)+"\n",file=logfile)


gw=2

print("Calculating for gameweek "+str(gw))
ans=raw_input("Do you wish to continue? (y/n)")
if ans=='n':
    sys.exit()
logfile=open('Team_Scores_gw'+str(gw),'w')

ars=get_team("Arsenal")+[7,6,'a']#
av=get_team("Aston Villa")+[1,2,'h']#
bnm=get_team("Bournemouth")+[5,3,'a']#
chl=get_team("Chelsea")+[3,8,'a']#
cp=get_team("Crystal Palace")+[8,2,'h']#
eve=get_team("Everton")+[5,8,'a']#
leeds=get_team("Leeds United")+[1,4,'a']#
leic=get_team("Leicester")+[2,1,'a']#
kop=get_team("Liverpool")+[1,3,'h']#
cty=get_team("Manchester City")+[8,6,'h']#
newc=get_team("Newcastle United")+[8,1,'a']#
nrwch=get_team("Norwich City")+[5,2,'a']
sou=get_team("Southampton")+[5,2,'h']#
stk=get_team("Stoke City")+[8,6,'a']#
sun=get_team("Sunderland")+[6,1,'h']#
swn=get_team("Swansea City")+[5,1,'h']
sprs=get_team("Tottenham Hotspur")+[1,2,'h']#
wtf=get_team("Watford")+[3,6,'h']#
wb=get_team("West Bromwich Albion")+[8,2,'a']#
wh=get_team("West Ham United")+[4,1,'h']

print_score(ars)
print_score(av)
print_score(bnm)
print_score(chl)
print_score(cp)
print_score(eve)
print_score(leeds)
print_score(leic)
print_score(kop)
print_score(cty)
print_score(newc)
print_score(nrwch)
print_score(sou)
print_score(stk)
print_score(sun)
print_score(swn)
print_score(sprs)
print_score(wtf)
print_score(wb)
print_score(wh)
