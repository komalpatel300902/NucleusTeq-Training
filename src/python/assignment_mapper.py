#!/bin/python3

import sys
import re

punctuator = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for lines in sys.stdin:

    lines = lines.strip()
    words = lines.split(" ")
    for word in words:
        w = ""
        for character in word:
            if character not in punctuator:
                w += character
            else:
                break
        print(w , 1)

