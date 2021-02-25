#!/usr/bin/env python3
"""
https://www.translatum.gr/converter/beta-code.htm

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
import re

class Verb(Packard):
  stem=None
  extras=None
  augment=False

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
      self.extras="#1 aorist & future passive (Q-type)"
    elif t=="D":
      self.extras="#2 aorist & future passive (non-Q type)"
    elif t=="V":
      self.extras="labial aorist & future passive"
    elif t=="S":
      self.extras="dental aorist & future passive + ζ"
    elif t=="Q":
      self.extras="guttural aorist & future passive"
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

    if len(self.typeCode)>2 and len(self.typeCode[2])=="I":
      self.augment=True

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

    print(self.typeCode,self.parseCode)
