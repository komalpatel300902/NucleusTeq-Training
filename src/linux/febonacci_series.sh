#!/bin/bash

read num
x=1
y=1
holder=0
for (( z=0; z < num; z++ ))
do
	echo $y
	holder=$((y))
	y=$((y+x))
	x=$((holder))
done
