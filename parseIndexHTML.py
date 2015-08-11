#! /usr/bin/python
import os
import io
import subprocess
import sys
import re

dirname = os.path.dirname
abspath = os.path.abspath
dataPath = os.path.join(dirname(dirname(dirname(abspath(__file__)))), sys.argv[3])
os.chdir(dataPath)
output = subprocess.check_output(['wget', 
                                  "--output-document=" + sys.argv[2], 
                                  sys.argv[1]])


if (output == ''):
    f = open(sys.argv[2], 'r')
    print "\nhere are the matches ... \n"
    for line in f:
        matchstr = re.search('<a href=\"(.*)\">(.+)</a>', line, re.IGNORECASE)
        if (matchstr and (matchstr.group(1) == matchstr.group(2) or 
                          ".pdf" in matchstr.group(1))):
            print "\nGetting file: "+sys.argv[1]+matchstr.group(1)
            output = subprocess.check_output(['wget', sys.argv[1]+matchstr.group(1)])

    
