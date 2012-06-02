from cluster import HierarchicalClustering
from bootstyle.color import *

def clusterByLightness(colors):
  colors_list = list(colors)
  clusters = HierarchicalClustering(colors_list, lambda x, y: abs(x.getLightness() - y.getLightness()))
  return clusters.getlevel(0.1)

def clusterByHUE(colors):
  colors_list = list(colors)
  clusters = HierarchicalClustering(colors_list, lambda x, y: abs(x.getHUE() - y.getHUE()))
  return clusters.getlevel(10)

def clusterBySaturation(colors):
  colors_list = list(colors)
  clusters = HierarchicalClustering(colors_list, lambda x, y: abs(x.getSaturation() - y.getSaturation()))
  return clusters.getlevel(0.05)

def intersection(clusters1, clusters2):
  
  intersected = []
  appended = []
  
  for cluster1 in clusters1:
    for cluster2 in clusters2:
      
      colors = []
      for color1 in cluster1:
        for color2 in cluster2:
          if color1 and color2 and color1.eq(color2):
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
      hex_cluster.append(color.getHex())
      
  return hex_clusters
