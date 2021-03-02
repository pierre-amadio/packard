#!/usr/bin/env python3
from packard import *
from noun import *
from adjective import *
from verb import *
from misc import *
from pronoun import *
import sys
from jinja2 import Template, FileSystemLoader, Environment
"""
 This script build the xml dictionary based on a list of code to handle included 
 in the file used as argument.
"""
inputFile=sys.argv[1]

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

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('packard.tei.xml')

allCodes=[]
with open(inputFile) as file_in:
  for line in file_in:
    line=line.strip()
    entry={}
    entry["morphcode"]=line
    try:
      a=instanciate(line)
      entry["definition"]=a.desc()
    except (IndexError,ValueError,TypeError):
      entry["definition"]="none"
    allCodes.append(entry)

output=template.render(allCodes=allCodes)
print(output)

