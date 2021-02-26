#!/usr/bin/env python3
from bs4 import BeautifulSoup
import sys

dic=set()

osisLXX="/home/melmoth/dev/LXX/20210223-lxx.osis.xml"
with open(osisLXX) as fp:
  soup = BeautifulSoup(fp, 'xml')
  for w in soup.find_all("w"):
    code=w["morph"].replace("packard:","")
    dic.add(code)

for i in  sorted(dic):
  print(i)
