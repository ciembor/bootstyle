from __future__ import division
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