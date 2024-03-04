# !/bin/bash

read side

for (( i=1 ; i <= side ; i++))
do
	for (( j=1 ; j <= side ; j++))
	do
		echo -n "* "
	done
	echo ""
done
