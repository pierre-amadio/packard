#!/usr/bin/env python3


class Packard:
  rawCode=None

  def parseCode(self):
    raise NotImplementedError("parseCode not implemented in virtual class")

  def __init__(self, rawcode):
          self.rawCode = rawcode
          self.parseCode()
