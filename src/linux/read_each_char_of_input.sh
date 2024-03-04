#!/bin/bash

echo -n  "enter a string : "
read  string
length=${#string}

for (( i=0; i<length; i++ ))
do
	echo ${string:i:1}
done
