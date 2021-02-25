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

  def firstDeclension(self):
    self.declension=1
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
    self.declension=3
    self.extras=""
    """
      TODO: A3E,H,N,U,C  
      indicate the kind of third declension
    """

  def parseRawCode(self):
    self.WordType="Adjective"
    if len(self.typeCode)==1:
      self.declension=0
      self.extras=""
      raise IndexError("incomplete adjective code:%s"%self.typeCode)
    else:
      self.declension=int(self.typeCode[1])
      if self.declension==1:
        self.firstDeclension()
      if self.declension==3:
        self.thirdDeclension()

    print(self.parseCode)
    print(super().parseTriCode(self.parseCode))