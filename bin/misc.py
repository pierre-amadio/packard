#!/usr/bin/env python3
"""
C = Conjunction
X = Particle
I = Interjection
M = Indeclinable Number
P = Preposition
D = Adverb

TODO: conjonction can be followed by stuff: C+RPDS
"""

from packard import *

class Misc(Packard):
  extras=None

  def parseRawCode(self):
    if len(self.typeCode)!=1:
      raise IndexError("Invalid misc code:%s"%self.typeCode)
    t=self.typeCode[0]
    if t=="C":
      self.wordType="conjunction"
    elif t=="X":
      self.wordType="particle"
    elif t=="I":
      self.wordType="interjection"
    elif t=="M":
      self.wordType="indeclinable number"
    elif t=="P":
      self.wordType="preposition"
    elif t=="D":
      self.wordType="adverb"
    else:
      raise IndexError("invalid misc code:%s"%self.typeCode)

  def desc(self):
    out=self.wordType
    return out
