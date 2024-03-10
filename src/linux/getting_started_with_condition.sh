#!/bin/bash
read input
if [ $input = "Y" -o $input = "y" ]
then
    echo "YES"
elif [ $input = "N" -o $input = "n" ]
then 
    echo "NO"
fi