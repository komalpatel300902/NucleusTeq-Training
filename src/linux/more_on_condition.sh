#!/bin/bash
read side1
read side2
read side3
num=0
if [ $side1 == $side2 ]
then
    let num++
fi
if [ $side2 == $side3 ]
then
    let num++
fi
if [ $side1 == $side3 ]
then
    let num++
fi

if [ $num == 3 ]
then
    echo "EQUILATERAL"
elif [ $num == 1 ]
then 
    echo "ISOSCELES"
elif [ $num == 0 ]
then
    echo "SCALENE"
fi