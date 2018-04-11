#!/bin/bash

input=rosen_opt_ea.dat
sed 's/NO_ID//g' $input > tmp.txt
sed 's/interface//g' $input > tmp.txt
rm $input
mv tmp.txt $input
