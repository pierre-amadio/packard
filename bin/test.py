#!/usr/bin/env python3
from packard import *
from noun import *
from adjective import *
from verb import *
from misc import *
from pronoun import * 
from bs4 import BeautifulSoup
import sys

def instanciate(code):
  t=code[0]
  if t=="N":
    return Noun(code)
  if t=="A":
    return Adjective(code)
  if t=="R":
    return Pronoun(code)
  if t=="V":
    return Verb(code)
  if t in "CXIMPD":
    return Misc(code)
  raise IndexError("Invalid code:%s"%code)

#code="V1I-IMI3P"
#code="A1C-NSMC"
#print(code)
#a=instanciate(code)
#print(a.desc())

#code="VAI-AAI3S"
#a=instanciate(code)
#print(a.desc())
#sys.exit()

osisLXX="/home/melmoth/dev/LXX/20210223-lxx.osis.xml"
with open(osisLXX) as fp:
  soup = BeautifulSoup(fp, 'xml')
  for w in soup.find_all("w"):
    print(w)
    print(w["morph"])
    code=w["morph"].replace("packard:","")
    a=instanciate(code)
    print(a.desc())

