#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from bootstyle.io import *
from bootstyle.reader import *

reader = Reader()
(input_filename, output_filename) = getFilenames()
colors = reader.getColors(input_filename)

print(colors["special"])

for color in colors["all"]:
  print(color)
