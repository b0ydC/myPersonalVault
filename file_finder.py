#!/usr/bin/python

#Instructions
#
# To search for any extention file in the entire filesystem, just modify the pattern.
# ex: pattern = '*.py'
# to search for python files.
#
# v1
# 11/15/2019


import fnmatch
import os

rootPath ='/'
pattern = '*.nse'

for root, dirs, files in os.walk(rootPath):
  for filename in fnmatch.filter(files, pattern):
    print(os.path.join(root, filename))

