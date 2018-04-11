#!/bin/bash


#This script will erase the word EMPTY from dakota 6.1.0 tabular output file.


#Write in name_of_the_file the name of the table you want to edit 
input=name_of_the_file

sed 's/EMPTY//g' $input > tmp.txt
rm $input
mv tmp.txt $input