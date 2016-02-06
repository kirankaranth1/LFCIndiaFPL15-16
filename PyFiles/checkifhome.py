import requests
import json
import sys

def checkifhome(teamname,fixtures):
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
          
##This part is just to test the module. Not required at all            
if __name__ == "__main__":
    gw=sys.argv[1]
    print(gw)
    res = requests.get("http://www.football-data.org/soccerseasons/354/fixtures?matchday="+str(gw))
    fixtures=json.loads(res.text)
    
    if checkifhome('Liverpool'):
        print 'home'
    else:
        print "false"