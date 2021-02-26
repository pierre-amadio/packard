#!/usr/bin/env python3
"""
https://www.translatum.gr/converter/beta-code.htm

A = Adjective (up to 3 cols.)
  A1 = -OS/-H/-ON pattern endings
     A1A = -OS/-A/-ON
     A1B = -OS/-OS/-ON
     A1C = -OUS/-OUS/-OUN
     A1S = nom. in -A, stem in -H
  A3 = 3rd declension patterns
     A3E,H,N,U,C as for 3 decl. nouns
"""

from packard import *

class Adjective(Packard):
  declension=None
  extras=None
  case=None
  number=None
  gender=None
  irregularDegree=None

  def firstDeclension(self):
    if len(self.typeCode)==2:
      self.extras="-ος -η -ον pattern endings"
    else:
      if self.typeCode[2]=='A':
        self.extras="-ος -α -ον"
      elif self.typeCode[2]=='B':
        self.extras="-ος -ος -ον"
      elif self.typeCode[2]=='C':
        self.extras="-ους -ους -ουν"
      elif slef.typecode[2]=='S':
        self.extras="nom. in -α, stem in -η"
      else :
        raise IndexError("invalid adjective code:%s"%self.typeCode)

  def thirdDeclension(self):
    self.extras=""
    """
      TODO: A3E,H,N,U,C  
      indicate the kind of third declension
    """

  def parseRawCode(self):
    self.wordType="Adjective"
    if len(self.typeCode)==1:
      raise IndexError("incomplete adjective code:%s"%self.typeCode)
    else:
      self.declension=int(self.typeCode[1])
      if self.declension==1:
        self.firstDeclension()
      elif self.declension==3:
        self.thirdDeclension()
      else:
        raise IndexError("invalid declension for adjective: %s"%self.typeCode)

    if len(self.parseCode)==4:
      if self.parseCode[3]=="C":
        self.irregularDegree="comparative"
      elif self.parseCode[3]=="S":
        self.irregularDegree="superlative"
      else:
        raise IndexError("invalid irregular adjective code:%s"%self.parseCode)

      code=super().parseTriCode(self.parseCode[0:3])
      self.case=code["case"]
      self.number=code["number"]
      self.gender=code["gender"]

  def desc(self):
    out="Adjective\n"
    if self.declension==1:
      out+="1st/2nd declension: "
    else:
      out+="3rd declension: "
    out+=self.extras+"\n"
    if self.irregularDegree:
      out+="irregular %s \n"%self.irregularDegree
    out+="%s / %s / %s"%(self.case,self.gender,self.number)


    return(out)
