#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from lxml import etree

try:
  if len(sys.argv) > 3:
    sys.exit("Too many arguments.")
  input = sys.argv[1]
  output = sys.argv[2]
except IndexError:
  print("Too few arguments.")

def readTheme(input):

  try:
    theme = etree.parse(input);
  except IOError:
    sys.exit("File doesn't exist.")
  except etree.ParseError:
    sys.exit("Input file is not well-formed.")

  return theme

COLOR_KEYS = set(["background", "foreground", "caret", "invisibles", "lineHighlight", "selection"])

def getColors(theme):

  strings = theme.findall(".//string")
  colors = set()
  
  for element in strings: 
    try:
      type = str(element.getprevious().text)
    except AttributeError:
      pass
    if (type in COLOR_KEYS):
      colors.add(element.text.lower())
  	
  for color in colors:
    print(color)

def getSpecialColors(theme):
  
  special_colors = {}

  try:
    settings = theme.find(".//array/dict/*[1]").getnext()
  except Exception:
    sys.exit("Can't find <settings> tag with special colors in input file.")

  try:
    for child in settings:
      if "key" == child.tag and child.text in COLOR_KEYS:
        string = child.getnext()
        if "string" == string.tag:
          special_colors[child.text] = string.text
        else:
          print("Warning: Can't read value of " + child.text + " special color.")

  except AttributeError:
    sys.exit("Something is wrong with <settings> special colors of this theme.")

  print(special_colors)

theme = readTheme(input)
getSpecialColors(theme)
getColors(theme)
