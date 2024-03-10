#!/bin/bash

for ((i=0;i<100;i++))
do
    if [ $((i%2)) -ne 0 ]
    then
        echo "$i"
    fi
done