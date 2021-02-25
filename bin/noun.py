#!/usr/bin/env python3
"""
 N = Noun (up to 3 columns)
   N1 = 1st declension (fem. in -H)
     N1A = stem ending in -A (fem.)
     N1M = masc. with nom. in -HS
     N1S = stem in -H, nom. in -A (f.)
     N1T = masc. with nom. in -AS
   N2 = 2nd declension (masc./fem.)
     N2N = neuters (in -ON)
   N3 = 3rd declension
     N3D,E,G,H,I,K,M,N,P,R,S,T,U,V,W
       indicate categories of 3rd
       decl. nouns (see other sheet)
   N alone= indeclinable proper noun
"""

from packard import *

class Noun(Packard):
  declension=None
  extras=None
  case=None
  number=None
  gender=None

  def firstDeclension(self):
    self.declension=1
    if len(self.typeCode)==2:
      self.extras="fem. in -η"
    else:
      if self.typeCode[2]=='A':
        self.extras="stem ending in -α (fem.)"
      elif self.typeCode[2]=='M':
        self.extras="masc. with nom. in -ης"
      elif self.typeCode[2]=='S':
        self.extras="stem in -η, nom. in -α (f.)"
      elif slef.typecode[2]=='T':
        self.extras="masc. with nom. in -ας"
      else:
        raise IndexError("Invalid noun code: %s"%self.typeCode)

  def secondDeclension(self):
    self.declension=2
    if len(self.typeCode)==2:
      self.extras="(masc./fem.)"
    else:
      """
        Only N2N
      """
      if self.typeCode=="N2N":
        self.extras="neuters (in -ον)"
      else:
        raise IndexError("Invalid noun code: %s"%self.typeCode)

  def thirdDeclension(self):
    self.declension=3
    self.extras=""
    """
      TODO: N3D,E,G,H,I,K,M,N,P,R,S,T,U,V,W
      indicate the kind of third declension
    """


  def parseRawCode(self):
    self.wordType="Noun"
    if len(self.typeCode)==1:
      self.declension=0
      self.extras="indeclinable proper noun"
    else:
      self.declension=int(self.typeCode[1])
      if self.declension==1:
        self.firstDeclension()
      elif self.declension==2:
        self.secondDeclension()
      elif self.declension==3:
        self.thirdDeclension()
      else:
        raise IndexError("Wrong declension type for code:%s"%self.typeCode)
    t=super().parseTriCode(self.parseCode)
    self.case=t["case"]
    self.number=t["number"]
    self.gender=t["gender"]

  def desc(self):
    out="Noun\n"
    if self.declension:
      out+="%s declension\n"%self.declension
    out+=self.extras+"\n"
    out+="%s / %s / %s"%(self.case,self.gender,self.number)
    return out

