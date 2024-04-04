#!/bin/python3
import sys

current_word = None
word_count = 0
for lines in sys.stdin:
    word , count = lines.split(" ",1)
    count = int(count)
    if current_word == word:
        word_count += count
    
    elif current_word and current_word != word:
        print(current_word , word_count)
        current_word = word
        word_count = count

    else:
        current_word = word
        word_count = count
print(current_word , word_count)   
