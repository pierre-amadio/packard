#!/usr/bin/env python3
"""
V = Verbs (up to 3 cols.)
(I in col.3 = augmented, whatever the stem)
"Progressive" Stems
     V1 = regular present
     V2 = contracts in -EW
     V3 =   "       in -AW
     V4 =   "       in -OW
     V5 = regular -MI verbs
     V6 = -A stem -MI verbs
     V7 = -E stem  "    "
     V8 = -O stem  "    "
     V9 = EI)MI/ and EI)=MI
Aorist Stems
     VA = 1st aorist active
     VB = 2nd aorist act. #1
     VZ = 2nd   "     "   #2(irreg)
     VH, VE, VO = -H, -E, -O stem -MI verbs
     VC = #1 aor.& fut.pass.(Q-type)
     VD = #2  "  "  "   "   (non-Q)
     VV = labial " " "  "
     VS = dental " " "  " (+ zeta)
     VQ = guttural" " " "
Perfect Stems (I in col.3 = Plupf.augm.)
     VX = perfect active
     VM =   "     middle
     VP = labial perf. midd.
     VT = dental  "     " (+ zeta)
     VK = guttural "     "
Future Stems
     VF = regular future
     VF2 = liquid type(+ zeta)
     VF3 = E)LAU/NW type
     VFX = future perfect
"""
from packard import *
from jinja2 import Template, FileSystemLoader, Environment

import re

class Verb(Packard):
  stem=None
  extras=None
  augment=False
  tense=None
  voice=None
  mood=None
  person=None
  participle=False
  case=None
  number=None
  gender=None

  def progressive(self):
    self.stem="progressive"
    t=int(self.typeCode[1])
    if t==1:
      self.extras="regular present"
    elif t==2:
      self.extras="contracts in -εω"
    elif t==3:
      self.extras="contracts in -αω"
    elif t==4:
      self.extras="contracts in -οω"
    elif t==5:
      self.extras="regular -μι verb"
    elif t==6:
      self.extras="-α stem -μι verb"
    elif t==7:
      self.extras="-ε stem -μι verb"
    elif t==8:
      self.extras="-ο stem -μι verb"
    elif t==9:
      self.extras="εἰμί and εἶμι"
    else:
      raise IndexError("invalid progressive verb type code:%s"%self.typeCode)

  def aorist(self):
    self.stem="aorist"
    t=self.typeCode[1]
    if t=="A":
      self.extras="1st aorist active"
    elif t=="B":
      self.extras="2nd aorist active (#1)"
    elif t=="Z":
      self.extras="2nd aorist active (#2 irregular)"
    elif t=="H":
      self.extras="-η stem -μι verb"
    elif t=="E":
      self.extras="-ε stem -μι verb"
    elif t=="O":
      self.extras="-ο stem -μι verb"
    elif t=="C":
      self.extras="#1 aorist &amp; future passive (Q-type)"
    elif t=="D":
      self.extras="#2 aorist &amp; future passive (non-Q type)"
    elif t=="V":
      self.extras="labial aorist &amp; future passive"
    elif t=="S":
      self.extras="dental aorist &amp; future passive + ζ"
    elif t=="Q":
      self.extras="guttural aorist &amp; future passive"
    else:
      raise IndexError("invalid aorist verb type code:%s"%self.typeCode)


  def perfect(self):
    self.stem="perfect"
    t=self.typeCode[1]
    if self.augment:
      tname="pluperfect"
    else:
      tname="perfect"
    if t=="X":
      self.extras="%s active"%tname
    elif t=="M":
      self.extras="%s middle"%tname
    elif t=="P":
      self.extras="labial %s middle"%tname
    elif t=="T":
      self.extras="dental %s middle (+ζ)"%tname
    elif t=="K":
      self.extras="guttural %s middle"%tname
    else:
      raise IndexError("invalid perfect verb type code:%s"%self.typeCode)


  def future(self):
    self.stem="future"
    if self.typeCode=="VF":
      self.extras="regular future"
    elif self.typeCode=="VF2":
      self.extras="liquid type (+ζ)"
    elif self.typeCode=="VF3":
      self.extras="ἐλαύνω type"
    elif self.typeCode=="VFX":
      self.extras="future perfect"
    else:
      raise IndexError("invalid future verb stem code:%s"%self.typeCode)


  def parseRawCode(self):
    self.wordType="Verb"

    if len(self.typeCode)>2 and self.typeCode[2]=="I":
      self.augment=True

    if len(self.typeCode)>1:
      if re.search("\d",self.typeCode[1]):
        self.progressive()
      elif self.typeCode[1] in "ABZHEOCDVSQ":
        self.aorist()
      elif self.typeCode[1] in "XMPTK":
        self.perfect()
      elif self.typeCode[1]=="F":
        self.future()
      else:
        raise IndexError("invalid verb type code:%s"%self.typeCode)

    if self.parseCode[0]=="P":
      self.tense="present"
    elif self.parseCode[0]=="I":
      self.tense="imperfect"
    elif self.parseCode[0]=="F":
      self.tense="future"
    elif self.parseCode[0]=="A":
      self.tense="aorist"
    elif self.parseCode[0]=="X":
      self.tense="perfect"
    elif self.parseCode[0]=="Y":
      self.tense="pluperfect"
    else:
      raise IndexError("Invalid tense for code %s"%self.typeCode)

    if self.parseCode[1]=="A":
      self.voice="active"
    elif self.parseCode[1]=="M":
      self.voice="middle"
    elif self.parseCode[1]=="P":
      self.voice="passive"
    else:
      raise IndexError("Invalid voice for code %s"%self.typeCode)

    if self.parseCode[2]=="I":
      self.mood="indicative"
    elif self.parseCode[2]=="D":
      self.mood="imperative"
    elif self.parseCode[2]=="S":
      self.mood="subjonctive"
    elif self.parseCode[2]=="O":
      self.mood="optative"
    elif self.parseCode[2]=="N":
      self.mood="infinitive"
    elif self.parseCode[2]=="P":
      self.mood="participle"
    else:
      raise IndexError("invalid mood code: %s"%self.typeCode)

    if len(self.parseCode)==6:
      self.participle=True
      t=super().parseTriCode(self.parseCode[3:])
      self.case=t["case"]
      self.number=t["number"]
      self.gender=t["gender"]
    else:
      if len(self.parseCode)!=3:
        """
         this is not an infinitive such as V-XAN
        """
        if not re.search("\d",self.parseCode[3]):
          raise IndexError("invalid person for code %s"%self.parseCode)
        self.person=self.parseCode[3]
        n=self.parseCode[4]
        if n=="S":
          self.number="singular"
        elif n=="D":
          self.number="dual"
        elif n=="P":
          self.number="plural"
        else:
          raise IndexError("invalid number code for %s"%self.parseCode)

  def desc(self):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('verb.xml')
    out=template.render(entry=self)
    return out



