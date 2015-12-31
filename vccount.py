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
from operator import itemgetter


#for line in open('Team_Scores_gw2.txt','r'):
#    line=str(line)
#    if re.match('^Vice Captain:', line):
#       print(line)
gw=input("Until gw?: ")
vcop=open('vc_op.txt', 'w')
for i in range(1,gw+1):
    File='TeamScores/Team_Scores_gw'+str(i)+'.txt'
    textfile = open(File, 'r')
    matches = []
    #reg = re.compile("^Vice Captain:")
    for line in textfile:
        line=str(line).strip()
        if line.startswith("Vice Captain:"):
            #print(line)
            print(line.split('Vice Captain:')[1],file=vcop)

    textfile.close()
vcop.close()
file2=open("vc_op.txt","r")
linecount={}
for line in file2:

    line=str(line).strip()
    #print("Entering ",line)
    if line not in linecount:
        linecount[line] = 1
    else:
        linecount[line] += 1
#print(linecount)


template = "{0:25}{1:10}"
for k,v in sorted(linecount.items(), key=itemgetter(1), reverse=True):
    print(template.format(k,v))
