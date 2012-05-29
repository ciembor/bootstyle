import os
from bootstyle.reader import *
from bootstyle.writer import *

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
          colors = reader.getColors(themes_directory + "/" + filename)
          string += writer.writeToString(colors, filename.replace(".tmTheme", ""))
        except:
          print("Warning! Can't parse " + filename)
          pass
        
  string += """  </body>
  </html>"""
  
  file.write(string)