#/bin/bash

cp table_out.dat tmp.txt 

sed 's/[[:space:]]\+/,/g' tmp.txt > tmp1.txt

awk '{if (NR!=1) {print}}' tmp1.txt > tmp.txt

echo ",id,x1,x2,of," > data1.txt

cat tmp.txt >> data1.txt

rm tmp.txt
rm tmp1.txt