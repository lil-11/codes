#!/bin/bash
echo "Welcome. Enter your password to continue"
read passwd
sleep 1.5
if (($passwd == 2005))
then
	echo "Correct password. You may proceed"
else 
	echo "Wrong password"
fi
