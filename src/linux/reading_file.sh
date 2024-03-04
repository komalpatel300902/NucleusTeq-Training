#!/bin/bash

file="temp.txt"

while read -r line;
do 
	echo -e "$line"

done <$file
