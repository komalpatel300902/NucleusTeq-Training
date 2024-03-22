#!/bin/bash
read n
sum=0
for((x=0; x<n ; x++))
do
    read num1
    sum=$((num1+sum))
done
result=$(printf %.3f $(echo "$sum/$n" | bc -l ))
echo $result
