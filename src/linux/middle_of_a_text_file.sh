#!/bin/bash

line_count=1
while read -r lines
do
    if [ $line_count -ge 12 ] && [ $line_count -le 22 ];
    then
        echo $lines
    fi
    let line_count++
done