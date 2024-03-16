#!/bin/bash

while read lines
do
    echo $lines | cut -c 1-4
done