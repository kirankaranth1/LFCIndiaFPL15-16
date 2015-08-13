import re

def get_team(name):
    lno=0    
    myFile=open('players-list.txt')
    
    for num, line in enumerate(myFile, 1):
        if name in line:
            #print 'found at line:', num
            lno=num
    myFile=open('players-list.txt')
    lines=myFile.readlines()
    team_list=[name]
    for i in range(lno+1,lno+8):
        id=int(re.findall('\d+', lines[i])[0].strip(' \t\n\r'))
        team_list.append(id)
    print(team_list)
    return(team_list)    


ars=get_team("Arsenal")
av=get_team("Aston Villa")
bnm=get_team("Bournemouth")
chl=get_team("Chelsea")
cp=get_team("Crystal Palace")
eve=get_team("Everton")
leeds=get_team("Leeds United")
leic=get_team("Leicester")
kop=get_team("Liverpool")
cty=get_team("Manchester City")
newc=get_team("Newcastle United")
nrwch=get_team("Norwich City")
sou=get_team("Southampton")
stk=get_team("Stoke City")
sun=get_team("Sunderland")
swn=get_team("Swansea City")
sprs=get_team("Tottenham Hotspur")
wtf=get_team("Watford")
wb=get_team("West Bromwich Albion")
wh=get_team("West Ham United")