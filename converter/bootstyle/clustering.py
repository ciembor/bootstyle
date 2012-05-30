from cluster import *
from bootstyle.color import hex_colors2hsl

def clusterByLightness(hex_colors):
  colors = hex_colors2hsl(hex_colors)
  clusters = HierarchicalClustering(colors, lambda x, y: abs(x.hsl_l - y.hsl_l))
  return clusters.getlevel(0.1)

def clusterByHUE(hex_colors):
  colors = hex_colors2hsl(hex_colors)
  clusters = HierarchicalClustering(colors, lambda x, y: abs(x.hsl_h - y.hsl_h))
  return clusters.getlevel(10)

def clusterBySaturation(hex_colors):
  colors = hex_colors2hsl(hex_colors)
  clusters = HierarchicalClustering(colors, lambda x, y: abs(x.hsl_s - y.hsl_s))
  return clusters.getlevel(0.05)

def intersection(clusters1, clusters2):
  
  intersected = []
  appended = []
  
  for cluster1 in clusters1:
    for cluster2 in clusters2:
      
      colors = []
      for color1 in cluster1:
        for color2 in cluster2:
          if (color1 and color2 
              and (color1.hsl_h == color2.hsl_h) 
              and (color1.hsl_s == color2.hsl_s) 
              and (color1.hsl_l == color2.hsl_l)):
            colors.append(color1)
            appended.append(color1)
      
      if colors:      
        intersected.append(colors)
      
  for cluster in clusters1:
    for color in cluster:
      if color not in appended:
        intersected.append([color])
  
  return intersected

def clusters2hex(clusters):
  
  hex_clusters = []
  
  for cluster in clusters:
    hex_cluster = []
    hex_clusters.append(hex_cluster)
    for color in cluster:
      hex_cluster.append(color.convert_to("RGB").get_rgb_hex())
      
  return hex_clusters
