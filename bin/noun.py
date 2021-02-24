#!/usr/bin/env python3
from packard import *

class Noun(Packard):
  declension=None

  def parseRawCode(self):
    print("need to parse code",self.rawCode)
    print("parse",self.parseCode)
    print("type",self.typeCode)
    self.WordType="Noun"
    print(self.typeCode[1])

