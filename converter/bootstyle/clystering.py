from cluster import *
from colormath.color_objects import RGBColor

def cluster(hex_colors):
  
  colors = []
  
  for hex in hex_colors:
    color = RGBColor()
    color.set_from_rgb_hex(hex)
    colors.append(color)