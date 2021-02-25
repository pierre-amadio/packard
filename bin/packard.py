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
  wordType=None
  fullDescription=None

  def __init__(self, rawcode):
    self.rawCode = rawcode
    test=re.search("^(.*)-(.*)$",self.rawCode)
    if not test:
      raise IndexError("invalid rawcode:%s"%self.rawCode)
    else:
      self.typeCode=test.group(1)
      self.parseCode=test.group(2)

    self.parseRawCode()

  def parseRawCode(self):
    raise NotImplementedError("parseRawCode not implemented in virtual class")

  def parseTriCode(self,tricode):
    """
      Noun, Pronouns, adjective and participes use the same 3 collumn code to store case/number/gender
    """
    out={}
    if tricode[0]=="N":
      out["case"]="Nominative"
    elif tricode[0]=="G":
      out["case"]="Genitive"
    elif tricode[0]=="D":
      out["case"]="Dative"
    elif tricode[0]=="A":
      out["case"]="Accusative"
    elif tricode[0]=="V":
      out["case"]="Vocative"

    if tricode[1]=="S":
      out["number"]="Singular"
    elif tricode[1]=="D":
      out["number"]="Dual"
    elif tricode[1]=="P":
      out["number"]="Plural"

    if tricode[2]=="M":
      out["gender"]="Masculine"
    elif tricode[2]=="F":
      out["gender"]="Feminine"
    elif tricode[2]=="N":
      out["gender"]="Neutral"

    return(out)
