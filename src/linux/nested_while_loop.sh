# !/bin/bash

echo -n "Enter a Number : "
read number
i=0
j=0
while [ $i -lt $number ]
do
	while [ $j -lt $number ]
	do
		echo -n  "$j"
		let j++
	done
	let i++
	let j=0
	echo ""
done
