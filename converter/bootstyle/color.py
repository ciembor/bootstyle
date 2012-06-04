from __future__ import division
from colormath.color_objects import RGBColor, HSLColor

class Color(HSLColor):
  
  def _fromHSLColor(self, hslcolor):
    self.hsl_h = hslcolor.hsl_h
    self.hsl_s = hslcolor.hsl_s
    self.hsl_l = hslcolor.hsl_l
    
  def _fromRGBColor(self, rgbcolor):
    self._fromHSLColor(rgbcolor.convert_to("HSL"))

  def fromRGBHex(self, rgb_hex):
    rgb = RGBColor()
    rgb.set_from_rgb_hex(rgb_hex)
    self._fromRGBColor(rgb)
    
  def fromRGBAHex(self, rgba_hex, background_hex):
    self.fromRGBHex(rgba_hex[:7])
    
    if len(rgba_hex) > 7:
      opacity = int(100 * (int(rgba_hex[7:], 16) / 255))
      background = RGBColor()
      if len(background_hex) > 7:
        background_hex = "#ffffff"
      background.set_from_rgb_hex(background_hex)
      self.mix(background, opacity)

  def mix(self, mask, opacity):
    opacity /= 100.0
    rgbcolor = self.convert_to("RGB")
    rgbmask = mask.convert_to("RGB")
    mixed = RGBColor()
    
    mixed.rgb_r = (rgbcolor.rgb_r * opacity) + (rgbmask.rgb_r * (1 - opacity))
    mixed.rgb_g = (rgbcolor.rgb_g * opacity) + (rgbmask.rgb_g * (1 - opacity))
    mixed.rgb_b = (rgbcolor.rgb_b * opacity) + (rgbmask.rgb_b * (1 - opacity))
  
    self._fromRGBColor(mixed)

  def getHex(self):
    return self.convert_to("RGB").get_rgb_hex()

  def getHUE(self):
    return self.hsl_h

  def getSaturation(self):
    return self.hsl_s
  
  def getLightness(self):
    return self.hsl_l

  def eq(self, color):
    if (self.hsl_h == color.getHUE() and self.hsl_s == color.getSaturation() and self.hsl_l == color.getLightness()):
      return True
    else:
      return False

  def nearestColor(self, colors):
    nearest = {"color": None, "distance": None}
    
    for current_color in colors:
      current_distance = self.delta_e(current_color)
      if not nearest["distance"] or current_distance < nearest["distance"]:
        nearest["distance"] = current_distance
        nearest["color"] = current_color
        
    return nearest["color"]

def hexToColors(hex_colors):
  colors = []
  
  for hex_color in hex_colors:
    color = Color()
    color.fromRGBHex(hex_color)
    colors.append(color.convert_to("HSL"))
    
  return colors