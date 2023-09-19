#!/bin/sh
#This is a simple calculator which has 5 functions
#It was written using CLA (Command Line Aguements)
echo "The sum is `expr $1 + $2`"
echo "The product is `expr $1 \* $2`"
echo "The difference is `expr $1 - $2`"
echo "The quotient is `expr $1 / $2`"
echo "The modulle is `expr $1 % $2`"
#To run this use 'sh filename.sh' $1 $2, where '$1' and '$2' represents your desired value
