#!/usr/bin/env python3
"""
R = Pronouns (2 Columns)
RA = Article
RD = Demonstrative
RI = Interrogative/Indefinite
RP = Personal/Possessive
RR = Relative
RX = O(/STIS
"""

from packard import *
from jinja2 import Template, FileSystemLoader, Environment


class Pronoun(Packard):
  extras=None
  case=None
  number=None
  gender=None

  def parseRawCode(self):
    self.wordType="Pronoun"
    if len(self.typeCode)!=2:
      raise IndexError("Invalid pronoun code:%s"%self.typeCode)
    t=self.typeCode[1]
    if t=="A":
      self.extras="article"
    elif t=="D":
      self.extras="demonstrative"
    elif t=="I":
      self.extras="interrogative/indefinite"
    elif t=="P":
      self.extras="personal/possessive"
    elif t=="R":
      self.extras="relative"
    elif t=="X":
      self.extras="ὅστις"
    else:
      raise IndexError("invalid pronoun code:%s"%self.typeCode)
    if self.parseCode:
      t=super().parseTriCode(self.parseCode)
      self.case=t["case"]
      self.number=t["number"]
      self.gender=t["gender"]

  def desc(self):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('pronoun.xml')
    out=template.render(entry=self)
    return out



