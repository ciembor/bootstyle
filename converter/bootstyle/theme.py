from bootstrap import default
from copy import deepcopy
from color import Color
import re

class Theme():

  def __init__(self):
    self._theme = deepcopy(default)
    for scope in self._theme:
      for color_name in self._theme[scope]:
        # if color is hex rgb
        if re.search("#[0-90a-fA-F]{6}", self._theme[scope][color_name]):
          color = Color()
          color.fromRGBHex(default[scope][color_name])
          self._theme[scope][color_name] = color

  # param: colors["all"]
  def mapColors(self, colors):
    for scope in self._theme:
      for color_name in self._theme[scope]:
        current_color = self._theme[scope][color_name]
        if Color is type(self._theme[scope][color_name]):
          self._theme[scope][color_name] = current_color.nearestColor(colors)

  # param: colors["special"]
  def mapSpecialColors(self, special_colors):
    self._theme["scaffolding"]["@bodyBackground"] = deepcopy(special_colors["background"])
    self._theme["scaffolding"]["@textColor"] = deepcopy(special_colors["foreground"])

  def adjustGrayscale(self):
    pass

  def adjustAccent(self):
    pass

  def _isDark(self):
    background = self._theme["scaffolding"]["@bodyBackground"]
    foreground = self._theme["scaffolding"]["@textColor"]
    if background.getLightness() < foreground.getLightness():
      return True
    else:
      return False

  def getTheme(self):
    return self._theme