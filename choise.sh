#!/bin/bash

# Declare an array of strings with type
StringArray=("1" "2" "3" "4" "5" "6" "7" "8" "9" "10" "11" "12" "13" "14" "15" "16" "17" "18" "19" "20" "21" "22" "23" "24" "25" "26" "27" "28" "29" "30" "31" "32" "33" "34" "35" "36" "37" "38" "39" "40" "41" "42")

# Iterate the string array using for loop
firstquestion=$(( RANDOM % 42 ))
echo "The first question is ${StringArray[$firstquestion]}"

secondquestion=$firstquestion

while [ "$secondquestion" = "$firstquestion" ]
do
  secondquestion=$(( RANDOM % 42 ))
done

echo "The second question is ${StringArray[$secondquestion]}"

thirdquestion=$firstquestion

while [ "$thirdquestion" = "$firstquestion" ] || [ "$thirdquestion" = "$secondquestion" ]
do
  thirdquestion=$(( RANDOM % 42 ))
done

echo "The third question is ${StringArray[$thirdquestion]}"

filename="src/index.php"

# Take the search string
search1="question1"
search2="question2"
search3="question3"

sed -i "s/$search1/${StringArray[$firstquestion - 1]}/" $filename
sed -i "s/$search2/${StringArray[$secondquestion - 1]}/" $filename
sed -i "s/$search3/${StringArray[$thirdquestion - 1]}/" $filename
