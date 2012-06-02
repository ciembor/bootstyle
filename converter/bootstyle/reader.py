import sys
from lxml import etree
from bootstyle.color import *

class Reader:
  
  def __init__(self):
    self._COLOR_KEYS = set(["background", "foreground", "caret", "invisibles", "lineHighlight", "selection"])

  def _readTheme(self, input_filename):
  
    try:
      theme = etree.parse(input_filename);
    except IOError:
      print(input_filename + " file doesn't exist.")
    except etree.ParseError:
      print(input_filename + " file is not well-formed.")
  
    return theme
  
  def _readSpecialColors(self, theme):
    
    special_colors = {}
    
    try:
      settings = theme.find(".//array/dict/*[1]").getnext()
    except Exception:
      sys.exit("Can't find <settings> tag with special colors in input file.")
  
    try:
      for child in settings:
        if "key" == child.tag and child.text in self._COLOR_KEYS:
          string = child.getnext()
          if "string" == string.tag:
            special_colors[child.text] = string.text
          else:
            print("Warning: Can't read value of " + child.text + " special color.")
    except AttributeError:
      sys.exit("Something is wrong with <settings> special colors of this theme.")
  
    background_hex = special_colors["background"]
  
    for key in special_colors:
      color = Color()
      color.fromRGBAHex(special_colors[key], background_hex)
      special_colors[key] = color
  
    return special_colors
  
  def _readColors(self, theme):
  
    strings = theme.findall(".//string")
    rgba_colors = set()
    colors = set()
    special_colors = self._readSpecialColors(theme)
    background_hex = special_colors["background"].getHex()
    
    for element in strings: 
      try:
        key = str(element.getprevious().text)
      except AttributeError:
        pass
      if (key in self._COLOR_KEYS):
        rgba_colors.add(element.text.lower())
        
    for rgba in rgba_colors:
      color = Color()
      color.fromRGBAHex(rgba, background_hex)
      colors.add(color)
  
    return colors

  def getColors(self, input_filename):
    
    colors = {}
    colors["special"] = {}
    colors["all"] = {}
    
    try:
      theme = self._readTheme(input_filename)
    except Exception:
      return colors
    
    colors["special"] = self._readSpecialColors(theme)
    colors["all"] = self._readColors(theme)

    return colors
