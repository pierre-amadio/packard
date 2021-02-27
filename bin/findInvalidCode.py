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

#osisLXX="/home/melmoth/dev/LXX/20210223-lxx.osis.xml"

pb={}

#osisLXX="/home/melmoth/dev/LXX/lxx.osis.xml"

osisLXX=sys.argv[1]


with open(osisLXX) as fp:
  soup = BeautifulSoup(fp, 'xml')
  for w in soup.find_all("w"):
    code=w["morph"].replace("packard:","")
    try:
      a=instanciate(code)
    except:
      word=w.string
      try:
        key=w.parent["osisID"]
      except:
        key=w.parent.parent["osisID"]
      if code not in pb.keys():
        pb[code]={word:[key]}
      else:
        if word in pb[code].keys():
          pb[code][word].append(key)
        else:
          pb[code][word]=[key]

for code in sorted(pb.keys()):
  print(code)
  for word in sorted(pb[code].keys()):
    print(word,pb[code][word])
  print("##########")


