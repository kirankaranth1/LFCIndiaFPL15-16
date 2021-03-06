# LFCIndiaFPL15-16
Web parser and score calculator for LFC India Fantasy League game 15-16  

Usage  
------
1) fpl1516.py is the generic score parser and logger script. The fpl1516.py.ph* scripts are for sprcific gameweeks (with captains harcoded).  
2) vccount.py reads the files in TeamScores folder and lists the number of times each player has been vice captain so far.  
3) players-list.txt contains list of all players with their FPL IDs. This file is parsed by the main script.  

Working  
--------

1) The individual players' FPL scores are parsed from fantasy.premierleague.com.  
2) Fixtures are obtained from the API at www.football-data.org for that particular gameweek.  
3) The parsed scores and fixture (home/away) are used to calculate team scores.  
4) The calculated team scores are matched again with the fixtures obtained from www.football-data.org to generate final head to head results and bonus points .   
5) All team scores are in the TeamScores directory. Final results in the Results directory.  
6) vccount.py has a gw parameter that needs to be set. It parses all files of gameweeks from 1 to the gw parameter and lists occurrence of each player as a vice captain as kv pair. This works similar to the 'wordcount' algorithm.  

API Reference  
--------------

http://api.football-data.org/documentation  
