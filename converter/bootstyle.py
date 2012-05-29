#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from bootstyle.io import *
from bootstyle.reader import *
from bootstyle.writer import *

reader = Reader()
writer = Writer()
(input_filename, output_filename) = getFilenames()
colors = reader.getColors(input_filename)
writer.writeToFile(colors, output_filename)