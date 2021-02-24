#!/usr/bin/env python3

"""
TTT-PPPPPP
 |     |______ "PARSE" CODE (up to 6 columns, as needed, to parse each form) 
 |_____________"TYPE" CODES (3 columns maximum, to identify part of speech)

"""
import re

class Packard:
  rawCode=None
  parseCode=None
  typeCode=None

  def __init__(self, rawcode):
    self.rawCode = rawcode
    test=re.search("^(.*)-(.*)$",self.rawCode)
    if not test:
      print("hmmm,no dash in rawcode",self.rawCode)
    else:
      self.parseCode=test.group(1)
      self.typeCode=test.group(2)

    self.parseRawCode()
    print("done")

  def parseRawCode(self):
    raise NotImplementedError("parseRawCode not implemented in virtual class")


