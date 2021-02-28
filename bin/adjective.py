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

TODO what about this entry in Isa 43:26 (and some other place)
PRW=TOS                  A1  B      PRW=TOS
TAXU\                    A3U B      TAXU/S

it end up as this non valdid code: A1-B
i guess it should be A1B-NSM but unsure

TODO what about the following in isa 56.5
 AA-ASM is not a valid code

"""

from packard import *
from jinja2 import Template, FileSystemLoader, Environment

class Adjective(Packard):
  declensionCode=None
  declensionLabel=None
  extras=None
  case=None
  number=None
  gender=None
  irregularDegree=None

  def firstDeclension(self):
    self.declensionLabel="1st/2nd"
    if len(self.typeCode)==2:
      self.extras="-ος -η -ον pattern endings"
    else:
      if self.typeCode[2]=='A':
        self.extras="-ος -α -ον"
      elif self.typeCode[2]=='B':
        self.extras="-ος -ος -ον"
      elif self.typeCode[2]=='C':
        self.extras="-ους -ους -ουν"
      elif self.typeCode[2]=='S':
        self.extras="nom. in -α, stem in -η"
      elif self.typeCode[2]=="P":
        """
          This is not documented in the Morph-Coding file, 
          but μέγαν and πολύς are associated with the A1P type code in several verses.
        """
        self.extras="μέγαν,πολύς"
      else :
        raise IndexError("invalid adjective code:%s"%self.typeCode)

  def thirdDeclension(self):
    self.extras=""
    self.declensionLabel="3rd"
    """
      TODO: A3E,H,N,U,C  
      indicate the kind of third declension
    """

  def parseRawCode(self):
    self.wordType="Adjective"
    if len(self.typeCode)==1:
      self.declensionLabel="undefine"
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
   file_loader = FileSystemLoader('templates')
   env = Environment(loader=file_loader)
   template = env.get_template('adjective.xml')
   out=template.render(entry=self)
   return out


