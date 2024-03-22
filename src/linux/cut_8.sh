#!/bin/bash
while read lines
do 
    echo $lines | cut -d " " -f 1-3
done