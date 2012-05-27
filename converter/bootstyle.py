#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from __future__ import division
import sys
from lxml import etree
from colormath.color_objects import RGBColor

def mixRGBColors(color, mask, opacity):
  opacity /= 100.0
  mixed = RGBColor()
  
  mixed.rgb_r = (color.rgb_r * opacity) + (mask.rgb_r * (1 - opacity))
  mixed.rgb_g = (color.rgb_g * opacity) + (mask.rgb_g * (1 - opacity))
  mixed.rgb_b = (color.rgb_b * opacity) + (mask.rgb_b * (1 - opacity))

  return mixed

def rgba2rgb(rgba_hex, background_hex):
  rgb = RGBColor()
  rgb.set_from_rgb_hex(rgba_hex[:7])
  
  if len(rgba_hex) > 7:
    opacity = int(100 * (int(rgba_hex[7:], 16) / 255))
    background = RGBColor()
    background.set_from_rgb_hex(background_hex)
    rgb = mixRGBColors(rgb, background, opacity)
    
  return rgb.get_rgb_hex()

try:
  if len(sys.argv) > 3:
    sys.exit("Too many arguments.")
  input_filename = sys.argv[1]
  output_filename = sys.argv[2]
except IndexError:
  sys.exit("Too few arguments.")

def readTheme(input_filename):

  try:
    theme = etree.parse(input_filename);
  except IOError:
    sys.exit("File doesn't exist.")
  except etree.ParseError:
    sys.exit("Input file is not well-formed.")

  return theme

COLOR_KEYS = set(["background", "foreground", "caret", "invisibles", "lineHighlight", "selection"])

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

  for key in special_colors:
    if (len(special_colors[key]) > 7):
      special_colors[key] = rgba2rgb(special_colors[key], special_colors["background"])

  return special_colors

def getColors(theme):

  strings = theme.findall(".//string")
  colors = set()
  special_colors = getSpecialColors(theme)
  
  for element in strings: 
    try:
      key = str(element.getprevious().text)
    except AttributeError:
      pass
    if (key in COLOR_KEYS):
      color = element.text.lower()
      if (len(color) > 7):
        color = rgba2rgb(color, special_colors["background"])
      colors.add(color)

  return colors

theme = readTheme(input_filename)
special_colors = getSpecialColors(theme)
colors = getColors(theme)

print(special_colors)

for color in colors:
  print(color)
