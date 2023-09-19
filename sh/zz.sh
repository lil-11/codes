#!/bin/bash
# A script which can be used to look for a particular file.

read -p "Enter file full path: " path

if [ -f "$path" ]; then
    echo "File found, opening..."
    sleep 2
    vi "$path"
else
    echo "File not found"
fi

<<comment
#This does thesame thing but for a directory (folder)
read -p "Enter file full path:" path
if [ -d ~path ]; then
	echo "File found, opening..."
	sleep 2
	vi ~path
else 
	echo "File not found"
fi
comment

