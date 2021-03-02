#!/usr/bin/env python3
from bs4 import BeautifulSoup
import sys
"""
This script extract all morphcode mentionned in <w> node in the osis file 
used as argument.
"""
dic=set()
osisLXX=sys.argv[1]

with open(osisLXX) as fp:
  soup = BeautifulSoup(fp, 'xml')
  for w in soup.find_all("w"):
    code=w["morph"].replace("packard:","")
    dic.add(code)

for i in  sorted(dic):
  print(i)
