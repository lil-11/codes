#!/bin/sh
<<comment
echo "Enter first number"
read num1
echo "Enter second number"
read num2
echo "Choose an operator (+, -, /, *)"
read operator

case $operator in
	+) result=$(($num1 + $num2))
		;;
	-) result=$(($num1 - $num2))
		;;
	\*) result=$(($num1 * $num2))
		;;
	/) result=$(($num1 / $num2))
		;;
	%) result=$(($num1 % $num2))
		;;
	*) echo "Invalid operator";
		exit 1;;
esac
echo "$num1 $operator $num2 = $result"
comment

echo "Please perform your calculations. Use either (+, -, /, *)"
read choice
echo  "Your answer is = " `expr $choice`

