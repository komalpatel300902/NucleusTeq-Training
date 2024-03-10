declare -a index_array
index=0
while read -r lines
do 
    index_array[$index]=$lines
    let index++
done
start_index=$((index - 20))
for((x=start_index;x <= index; x++))
do
    echo ${index_array[$x]}
done