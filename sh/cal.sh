#!/bin/sh
while true; do
    echo "Select the number of the operation you'd like to carry out"
    echo "1. Addition"
    echo "2. Subtraction"
    echo "3. Multiplication"
    echo "4. Division"
    echo "5. Exit"
    read choice

    case $choice in
        1)
            echo "Enter the first number"
            read num1
            echo "Enter the second number"
            read num2
            result=$[ $num1 + $num2 ]
            echo "$num1 + $num2 = $result"
            sleep 1
            ;;

        2)
            echo "Enter the first number"
            read num1
            echo "Enter the second number"
            read num2
            result=$[ $num1 - $num2 ]
            echo "$num1 - $num2 = $result"
            sleep 1
            ;;

        3)
            echo "Enter the first number"
            read num1
            echo "Enter the second number"
            read num2
	    result=$[ $num1 * $num2 ]
            echo "$num1 * $num2 = $result"
            sleep 1
            ;;

        4)
            echo "Enter the first number"
            read num1
            echo "Enter the second number"
            read num2
            result=$[ $num1 / $num2 ]
            echo "$num1 / $num2 = $result"
            sleep 1
            ;;

        5)
            echo "Thanks for using our service"
            exit
            ;;

        *)
            echo "Invalid option entered"
    esac
done
