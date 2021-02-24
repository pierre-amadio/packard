#!/usr/bin/env python3
"""
https://www.translatum.gr/converter/beta-code.htm

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

  def firstDeclension(self):
    print("first declension")
    if len(self.typeCode)==2:
      self.extras="1st declension (fem. in -η)"
    else:
      if self.typeCode[2]=='A':
        self.extras="stem ending in -α (fem.)"
      elif self.typeCode[2]=='M':
        self.extras="masc. with nom. in -ης"
      elif self.typeCode[2]=='S':
        self.extras="stem in -η, nom. in -α (f.)"
      elif slef.typecode[2]=='T':
        self.extras="masc. with nom. in -ας"



  def parseRawCode(self):
    self.WordType="Noun"
    if len(self.typeCode)==1:
      self.declension=0
    else:
      self.declension=int(self.typeCode[1])
      if self.declension==1:
        self.firstDeclension()
      if self.declension==2:
        self.secondDeclension()
      if self.declension==3:
        self.thirdDeclension()
