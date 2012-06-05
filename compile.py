#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os
import subprocess

for dirname, dirnames, filenames in os.walk('./output'):
  for subdirname in dirnames:
    print subdirname
    
    try:
      os.chdir('./output/' + subdirname)
    except Exception:
      print("Can't change directory to " + './output/' + subdirname)

    subprocess.call(['lessc', 'bootstyle.less', 'bootstyle.css'])
  
    os.chdir("../..")
