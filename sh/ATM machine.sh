#!/bin/bash
ini_Bal=1000
echo -e "Good day. Enter card No to be saved: \c"
read No
echo -e "Enter PIN to be saved: \c"
read PIN
echo "Saving..."
sleep 3

echo -e "Wecome to K2Soft Bank. Enter card No to proceed: \c"
read NO
if $[$NO -eq $No]
	echo "Enter the No of what you'd like to do"
	echo "1. Withdraw"
	echo "2. Deposit"
	echo "3. Check balance"
	echo "4. Exit"

	read choice

	case $choice in
		1)
			echo "How much do you want to withdraw?"
			read amount
			if [amount -ge ini_Bal]
				ini_Bal-=amount
				echo "You have withdrawn $amount FCFA. Your new balance is $ini_Bal"

	fi
	*) echo "Invaid input"

esac

