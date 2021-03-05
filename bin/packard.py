#!/usr/bin/env python3

"""
This a virtual class for all morphcode object.
It implement a constructor and a method to parse "tricode" (case/number/gender)

All morphcode looks like the following:
TTT-PPPPPP
 |     |______ "PARSE" CODE (up to 6 columns, as needed, to parse each form) 
 |_____________"TYPE" CODE (3 columns maximum, to identify part of speech)

"""
import re

class Packard:
  rawCode=None
  parseCode=None
  typeCode=None
  wordType=None

  def __init__(self, rawcode):
    self.rawCode = rawcode
    test=re.search("^(.*)-(.*)$",self.rawCode)

    if not test:
      """
        so the raw code does not looke aaa-aaaa
        may be it is one of the undocumented C+ conjonction code such as C+RDGSM
      """
      #if re.search("^C\+.*",self.rawCode):
      #  self.wordType="conjunction"
      #  return
      """
        may be it is one of the following: ["RA+A","RA+AASN","RD+NGSM","RI","RI-D","RP+XNS"]
      """
      if self.rawCode in ["RA+A","RA+AASN","RD+NGSM","RI","RI-D","RP+XNS"]:
        self.typeCode=self.rawCode[0:2]
        self.parseRawCode()
        return 


    if not test and len(rawcode)>1:
      raise IndexError("invalid rawcode:%s"%self.rawCode)
    else:
      if len(rawcode)>1:
        self.typeCode=test.group(1)
        self.parseCode=test.group(2)
      else:
        self.typeCode=rawcode

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
    else:
      raise IndexError("Invalid case in code %s"%tricode)

    if tricode[1]=="S":
      out["number"]="Singular"
    elif tricode[1]=="D":
      out["number"]="Dual"
    elif tricode[1]=="P":
      out["number"]="Plural"
    else:
      raise IndexError("Invalid number in code %s"%tricode)

    """
      looks like some entry lack gender.
    """
    if len(tricode)==3:
      if tricode[2]=="M":
        out["gender"]="Masculine"
      elif tricode[2]=="F":
        out["gender"]="Feminine"
      elif tricode[2]=="N":
        out["gender"]="Neuter"
      else:
        raise IndexError("Invalid gender in code %s"%tricode)
    else:
      out["gender"]="Unknown"

    return(out)
