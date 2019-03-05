#!/bin/bash
input="shuffled_file_numbers.txt"
count=0
while IFS= read -r var
do
	if [ $var -lt 10 ]; then
		original_file_name="00"$var
	elif [ $var -lt 100 ]; then
		original_file_name="0"$var
	else
		original_file_name=$var
	fi
	if [ $count -lt 200 ]; then
		cp ../raw-dataset/$original_file_name.txt ../../docs/Part1-NER/train_set/.
	elif [ $count -lt 300 ]; then
		cp ../raw-dataset/$original_file_name.txt ../../docs/Part1-NER/test_set/.
	fi
	count=$((count + 1))
done < "$input"
