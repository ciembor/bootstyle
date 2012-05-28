import sys
from lxml import etree
from bootstyle.color import rgba2rgb

class Reader:
  
  def __init__(self):
    self._COLOR_KEYS = set(["background", "foreground", "caret", "invisibles", "lineHighlight", "selection"])

  def _readTheme(self, input_filename):
  
    try:
      theme = etree.parse(input_filename);
    except IOError:
      sys.exit("File doesn't exist.")
    except etree.ParseError:
      sys.exit("Input file is not well-formed.")
  
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
  
    for key in special_colors:
      if (len(special_colors[key]) > 7):
        special_colors[key] = rgba2rgb(special_colors[key], special_colors["background"])
  
    return special_colors
  
  def _readColors(self, theme):
  
    strings = theme.findall(".//string")
    colors = set()
    special_colors = self._readSpecialColors(theme)
    
    for element in strings: 
      try:
        key = str(element.getprevious().text)
      except AttributeError:
        pass
      if (key in self._COLOR_KEYS):
        color = element.text.lower()
        if (len(color) > 7):
          color = rgba2rgb(color, special_colors["background"])
        colors.add(color)
  
    return colors

  def getColors(self, input_filename):
    
    theme = self._readTheme(input_filename)
    colors = {}
    
    colors["special"] = self._readSpecialColors(theme)
    colors["all"] = self._readColors(theme)
    
    return colors
