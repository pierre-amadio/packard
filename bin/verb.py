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
    t=self.typeCode[1]
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

  def aoris(self):
    print("aorist")

  def perfect(self):
    print("perfect")

  def future(self):
    print("future")

  def parseRawCode(self):
    self.WordType="Verb"

    if re.search("\d",self.typeCode[1]):
      self.progressive()
    elif self.typeCode[1] in "ABZHCDVSQ":
      self.aorist()
    elif self.typeCode[1] in "XMPTK":
      self.perfect()
    elif self.typeCode[1]=="F":
      self.future()
    else:
      raise IndexError("invalid verb type code:"%self.typeCode)

    print(self.typeCode,self.parseCode)
