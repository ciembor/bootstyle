from bootstyle.clustering import *
from bootstyle.color import *

class Writer:
  
  def writeToString(self, colors, output_filename):
    
    string = '<h1>' + output_filename + '</h1>'
    
    ######### specials
    
    string += "<h2>Special colors</h2>"
    
    string += '<ul>'
    for key in colors["special"].keys():
      string += '<li class="special">'
      string += '<span style="background-color: ' + colors["special"][key].getHex() + '">' + key + '</span>'
      string += '</li>'
    string += '</ul>'
    
    ######### all
    
    string += "<h2>All colors</h2>"
    
    string += '<ul>'
    for color in colors["all"]:
      string += '<li class="all">'
      string += '<span style="background-color: ' + color.getHex() + '">' + color.getHex() + '</span>'
      string += '</li>'
    string += '</ul>'
    
    ######### create clusters
    
    lightness = clusterByLightness(colors["all"])
    hue = clusterByHUE(colors["all"])
    saturation = clusterBySaturation(colors["all"])
    
    ######### print clusters
    
    def print_clusters(clusters):
      string = ""
      for cluster in clusters:
        if len(cluster) > 1:
          string += "<hr />"
          string += "<ul>"
          for color in cluster:
            string += '<li class="all">'
            string += '<span style="background-color: ' + color + '">' + color + '</span>'
            string += '</li>'
          string += "</ul>"
        
      return string
    string += "<h2>HUE and lightness clusters intersection</h2>"
    string += print_clusters(clusters2hex(intersection(hue, lightness)))
    string += "<h2>Lightness and saturation clusters intersection</h2>"
    string += print_clusters(clusters2hex(intersection(lightness, saturation)))
    string += "<h2>Saturation and HUE clusters intersection</h2>"
    string += print_clusters(clusters2hex(intersection(saturation, hue)))
    
    return string
    
  def writeToFile(self, colors, output_filename):
    file = open(output_filename, 'w')
    file.write(self.writeToString(colors, output_filename))