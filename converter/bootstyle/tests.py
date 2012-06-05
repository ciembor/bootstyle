import os
from bootstyle.reader import *
from bootstyle.writer import *
from bootstyle.theme import Theme

def writeHTML(themes_directory, output_filename):
  file = open(output_filename, 'w')
  reader = Reader()
  writer = Writer()
  
  string = """<html>
  <head>
    <link rel="stylesheet" href="style.css" type="text/css">
  </head>
  <body>"""

  for dirname, dirnames, filenames in os.walk(themes_directory):
    for filename in filenames:
      if filename.endswith('.tmTheme'):
        try:
          theme = Theme()
          colors = reader.getColors(themes_directory + "/" + filename)
          theme.mapColors(colors["all"])
          theme.mapSpecialColors(colors["special"])
          string += writer.writeToString(colors, theme, filename.replace(".tmTheme", ""))
        except:
          print("Warning! Can't parse " + filename)
          pass
        
  string += """  </body>
  </html>"""
  
  file.write(string)
  
def writeLESS(themes_directory, output_directory, bootstrap_directory):
  reader = Reader()
  writer = Writer()
  
  for dirname, dirnames, filenames in os.walk(themes_directory):
    for filename in filenames:
      if filename.endswith('.tmTheme'):
        try:
          theme = Theme()
          colors = reader.getColors(themes_directory + "/" + filename)
          theme.mapColors(colors["all"])
          theme.mapSpecialColors(colors["special"])
          writer.writeToLessFiles(theme, filename.replace(".tmTheme", ""), output_directory, bootstrap_directory)
        except:
          print("Warning! Can't convert " + filename)
          pass
        