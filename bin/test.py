#!/usr/bin/env python3
from packard import *
from noun import *
from adjective import *
from verb import *
from misc import *
from pronoun import * 

#a=Packard("plop")
#print(a.rawCode)

#b=Adjective("A-AZ")

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

code="RA-NDM"
print(code)
a=instanciate(code)
print(a.desc())
