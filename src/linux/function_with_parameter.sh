# !/bin/bash

let num1=$1
let num2=$2

add(){
	let v=$1+$2
	echo $v
}

add $num1 $num2
