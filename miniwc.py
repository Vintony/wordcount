# -*- coding: utf-8 -*-
# Author: Jiacheng Li
# Date: 30/9/2018
# Version: 1.0
# Warning: This tool only have the basic function of wc(BSD unix MacOS)
import sys
import os

# Only accept one argument
filename = sys.argv[1]

# Check if argument begins with --
if str(filename)[0:2] == '--':
    sys.exit('wc: illegal option -- -\nusage: wc [-clmw] [file ...]')

# Check if the file exists
if os.path.exists(filename):
    try:
        with open(filename) as file:
            linecount = file.read().count('\n')
            file.close()
        with open(filename) as file:
            charcount = len(file.read())
            file.close()
        with open(filename) as file:
            wordcount = len(file.read().split())
            file.close()
    except IOError as e:
        # Print the same as WC in macOS terminal
        sys.exit('wc: %s: read: Is a directory' % filename)
else:
    # Print the same as WC in macOS terminal
    sys.exit('wc: %s: open: No such file or directory' % filename)


print('\t%(linecount)s\t%(wordcount)s\t%(charcount)s' % locals(), filename)
# print("-------------------------------The Glory Divide Line Of Sneaky-------------------------------")
# Exactly the same because this is WC himself
# import subprocess
# subprocess.run(["wc", "testinputs/test1.txt"])
