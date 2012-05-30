#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from bootstyle.io import *
from bootstyle.reader import *
from bootstyle.writer import *
from bootstyle.clustering import *
from pprint import pprint

reader = Reader()
writer = Writer()
(input_filename, output_filename) = getFilenames()
colors = reader.getColors(input_filename)
writer.writeToFile(colors, output_filename)
value = clusterByValue(colors["all"])
hue = clusterByHUE(colors["all"])
saturation = clusterBySaturation(colors["all"])

pprint(clusters2hex(intersection(hue, value)))
pprint(clusters2hex(intersection(saturation, value)))
pprint(clusters2hex(intersection(saturation, hue)))