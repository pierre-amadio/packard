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
import re
from jinja2 import Template, FileSystemLoader, Environment

class Misc(Packard):
  extras=None
  case=None
  number=None
  gender=None

  def number(self):
    """
      strangely enough, some "indeclinable" number have declension information.
    """
    test=re.search("M-(...)",self.rawCode)
    if test:
      self.parseCode=test.group(1)
      t=super().parseTriCode(self.parseCode)
      self.case=t["case"]
      self.number=t["number"]
      self.gender=t["gender"]

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
      self.number()
    elif t=="P":
      self.wordType="preposition"
    elif t=="D":
      self.wordType="adverb"
    else:
      raise IndexError("invalid misc code:%s"%self.typeCode)

  def desc(self):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('misc.xml')
    out=template.render(entry=self)
    return out

