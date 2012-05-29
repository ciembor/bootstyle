class Writer:
  
  def writeToString(self, colors, output_filename):
    
    string = '<h1>' + output_filename + '</h1>'
    
    string += '<ul>'
    for key in colors["special"].keys():
      string += '<li class="special">'
      string += '<span style="background-color: ' + colors["special"][key] + '">' + key + '</span>'
      string += '</li>'
    string += '</ul>'
    
    string += '<ul>'
    for color in colors["all"]:
      string += '<li class="all">'
      string += '<span style="background-color: ' + color + '">' + color + '</span>'
      string += '</li>'
    string += '</ul>'
    
    return string
    
  def writeToFile(self, colors, output_filename):
    file = open(output_filename, 'w')
    file.write(self.writeToString(colors, output_filename))