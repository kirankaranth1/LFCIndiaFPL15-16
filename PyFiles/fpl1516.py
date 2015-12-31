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


def isHome(teamname,fixtures):
    for fixture in fixtures:
        #print fixture
        if teamname in fixture['homeTeam']:
            #print(result[gw+1])
            #break
            return True
        elif teamname in fixture['awayTeam']:
            return False
        else:
            continue


def get_score(id):

    url="http://fantasy.premierleague.com/entry/"+str(id)+"/event-history/"+str(gw)+"/"
    while True:
        try:
            page = requests.get(url)
        except requests.ConnectionError:
            continue
        break

    
    #page = requests.get(url)
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
    print("\n"+name)
    for i in range(lno,lno+8):

        print(str(i+1-lno)+". "+lines[i].strip())
    captain=input("Enter Captain: ")
    vc=input("Enter Vice Captain: ")
    team_list=team_list+[captain,vc]
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
    if isHome(team[0],fixtures):
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
    print("Total score :"+str(t_score)+" ~"+str(round(t_score))+"\n",file=logfile)
    return round(t_score) 

def calcresult(n):
    score=(int(math.ceil(n / 15.0)) * 15)/15
    return score

def calcbonus(m):
    if m<121:
        return 0
    elif m>= 121 and m<181:
        return 1
    elif m>= 181 and m<226: 
        return 2
    else:
        return 3    


def getfix(gw):
    res = requests.get("http://www.football-data.org/soccerseasons/398/fixtures?matchday="+str(gw))
    result=json.loads(res.text)
    return result




gw=raw_input("Enter gw numer: ")
gw=int(gw)
print("Calculating for gameweek "+str(gw))
ans=raw_input("Do you wish to continue? (y/n)")
if ans=='n':
    sys.exit()
logfile=open('TeamScores/Team_Scores_gw'+str(gw)+'.txt','w')
fixtures=getfix(gw)
ars=get_team("Arsenal FC")
av=get_team("Aston Villa FC")
bnm=get_team("AFC Bournemouth")
chl=get_team("Chelsea FC")
cp=get_team("Crystal Palace FC")
eve=get_team("Everton FC")
leic=get_team("Leicester City FC")
kop=get_team("Liverpool FC")
leeds=get_team("Manchester United FC")
cty=get_team("Manchester City FC")
newc=get_team("Newcastle United FC")
nrwch=get_team("Norwich City FC")
sou=get_team("Southampton FC")
stk=get_team("Stoke City FC")
sun=get_team("Sunderland AFC")
swn=get_team("Swansea City FC")
sprs=get_team("Tottenham Hotspur FC")
wtf=get_team("Watford FC")
wb=get_team("West Bromwich Albion FC")
wh=get_team("West Ham United FC")

dict={"Manchester United FC":0,"Swansea City FC":0,"Leicester City FC":0,"Everton FC":0,"West Ham United FC":0,"Tottenham Hotspur FC":0,"West Bromwich Albion FC":0,"Sunderland AFC":0,"Stoke City FC":0,"Aston Villa FC":0,"AFC Bournemouth":0,"Watford FC":0,"Arsenal FC":0,"Crystal Palace FC":0,"Liverpool FC":0,"Southampton FC":0,"Newcastle United FC":0,"Manchester City FC":0,"Norwich City FC":0,"Chelsea FC":0}


dict["Arsenal FC"]=print_score(ars)
dict["Aston Villa FC"]=print_score(av)
dict["AFC Bournemouth"]=print_score(bnm)
dict["Chelsea FC"]=print_score(chl)
dict["Crystal Palace FC"]=print_score(cp)
dict["Everton FC"]=print_score(eve)
dict["Leicester City FC"]=print_score(leic)
dict["Liverpool FC"]=print_score(kop)
dict["Manchester United FC"]=print_score(leeds)
dict["Manchester City FC"]=print_score(cty)
dict["Newcastle United FC"]=print_score(newc)
dict["Norwich City FC"]=print_score(nrwch)
dict["Southampton FC"]=print_score(sou)
dict["Stoke City FC"]=print_score(stk)
dict["Sunderland AFC"]=print_score(sun)
dict["Swansea City FC"]=print_score(swn)
dict["Tottenham Hotspur FC"]=print_score(sprs)
dict["Watford FC"]=print_score(wtf)
dict["West Bromwich Albion FC"]=print_score(wb)
dict["West Ham United FC"]=print_score(wh)


g=open("Results/Scores_gw"+str(gw)+".txt",'w')
for fix in fixtures:
    hscore=dict[fix['homeTeam']]
    ascore=dict[fix['awayTeam']]
    if(hscore>ascore):
        fix['goalsAwayTeam']=0
        diff=hscore-ascore
        fix['goalsHomeTeam']=calcresult(diff)
    elif(hscore==ascore):
        fix['goalsAwayTeam']=0
        fix['goalsHomeTeam']=0
        diff=0
    else:
        
        diff=ascore-hscore
        fix['goalsAwayTeam']=calcresult(diff)
        fix['goalsHomeTeam']=0
        
    print(str(fix['homeTeam'])+" vs "+str(fix['awayTeam'])+"\n"+str(dict[fix['homeTeam']])+"-"+str(dict[fix['awayTeam']])+"\nDiff="+str(diff)+"\nBonus points:"+str(calcbonus(diff))+"\n"+str(fix['goalsHomeTeam'])+"-"+str(fix['goalsAwayTeam']),file=g)

g.close()        

