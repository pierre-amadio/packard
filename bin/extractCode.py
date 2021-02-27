#!/usr/bin/env python3
from bs4 import BeautifulSoup
import sys

dic=set()

#osisLXX="/home/melmoth/dev/LXX/lxx.osis.xml"
osisLXX=sys.argv[1]

with open(osisLXX) as fp:
  soup = BeautifulSoup(fp, 'xml')
  for w in soup.find_all("w"):
    code=w["morph"].replace("packard:","")
    dic.add(code)

for i in  sorted(dic):
  print(i)
