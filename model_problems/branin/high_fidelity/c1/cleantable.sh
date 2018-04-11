#!/bin/bash

input=table_out.dat
sed 's/NO_ID//g' $input > tmp1.txt
sed 's/interface//g' tmp1.txt > tmp.txt
rm $input tmp1.txt
mv tmp.txt $input
