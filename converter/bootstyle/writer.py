from bootstyle.clustering import *
from bootstyle.color import *
from bootstyle.bootstrap import variablesTemplate, requiresTemplate
import os

class Writer:
  
  def writeToString(self, colors, theme_obj, name):
    
    string = '<h1>' + name + '</h1>'
    
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
    
#    ######### create clusters
#    
#    lightness = clusterByLightness(colors["all"])
#    hue = clusterByHUE(colors["all"])
#    saturation = clusterBySaturation(colors["all"])
#    
#    ######### print clusters
#    
#    def print_clusters(clusters):
#      string = ""
#      for cluster in clusters:
#        if len(cluster) > 1:
#          string += "<hr />"
#          string += "<ul>"
#          for color in cluster:
#            string += '<li class="all">'
#            string += '<span style="background-color: ' + color + '">' + color + '</span>'
#            string += '</li>'
#          string += "</ul>"
#        
#      return string
#    string += "<h2>HUE and lightness clusters intersection</h2>"
#    string += print_clusters(clusters2hex(intersection(hue, lightness)))
#    string += "<h2>Lightness and saturation clusters intersection</h2>"
#    string += print_clusters(clusters2hex(intersection(lightness, saturation)))
#    string += "<h2>Saturation and HUE clusters intersection</h2>"
#    string += print_clusters(clusters2hex(intersection(saturation, hue)))

    theme = theme_obj.getTheme()

    for scope in theme.keys():
      string += "<h2>" + scope + "</h2>"
      string += '<ul>'
      for name in theme[scope].keys():
        color = theme[scope][name]
        if Color == type(color):
          string += '<span style="background-color: ' + color.getHex() + '">' + name + '</span>'
      string += '</ul>'
    
    return string
    
  def writeToLessString(self, theme_obj):
    
    def writeScope(theme_obj, scope):
      string = ""
      theme = theme_obj.getTheme()
      
      for variable in theme[scope]:
        if Color == type(theme[scope][variable]):
          value = theme[scope][variable]
          value = value.getHex()
        else:
          value = theme[scope][variable]
          
        string += variable + ":\t\t\t" + value + ";\n"
      
      return string

    string = variablesTemplate.substitute(grayscale = writeScope(theme_obj, "grayscale"),
                                          accent = writeScope(theme_obj, "accent"),
                                          scaffolding = writeScope(theme_obj, "scaffolding"),
                                          tables = writeScope(theme_obj, "tables"),
                                          buttons = writeScope(theme_obj, "buttons"),
                                          forms = writeScope(theme_obj, "forms"),
                                          dropdowns = writeScope(theme_obj, "dropdowns"),
                                          navbar = writeScope(theme_obj, "navbar"),
                                          herounit = writeScope(theme_obj, "herounit"),
                                          alerts = writeScope(theme_obj, "alerts"))
    
    return string
    
  def writeToFile(self, colors, output_filename):
    file = open(output_filename, 'w')
    file.write(self.writeToString(colors, output_filename))
    file.close()
    
  def writeToLessFiles(self, theme, name, output_directory, bootstrap_directory):
    if not os.path.isdir(output_directory + "/" + name + "/"):
      os.mkdir(output_directory + "/" + name + "/")

    variables = open(output_directory + "/" + name + "/variables.less", 'w')
    variables.write(self.writeToLessString(theme))
    variables.close()
    
    bootstyle = open(output_directory + "/" + name + "/bootstyle.less", 'w')
    bootstyle.write(requiresTemplate.substitute(bootstrap_path = bootstrap_directory))
    bootstyle.close()
    