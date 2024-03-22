#!/bin/bash
read expression
val=$(echo $expression | bc -l)
echo $(printf %.3f $val )