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

class Verb(Packard):
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
