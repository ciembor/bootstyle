def isDark(colors):
  foreground = colors["special"]["foreground"]
  background = colors["special"]["background"]
  if background.getLightness() < foreground.getLightness():
    return True
  else:
    return False
