#!/bin/bash
# Author: Koh Karlson
# Email: kohkarlson@gmail.com

# This script creates a branch, initializes git in a directory, creates files, adds files to the staging area, commits files, pulls recent changes, and pushes files to a remote repository

# Save the current directory
original_dir=$(pwd)

# Prompt the user to enter the branch name
echo "Enter the branch name"
read -r branch

# Create and switch to the new branch
git branch "$branch"
git checkout "$branch"

# Prompt the user to enter the directory name
echo "Enter the directory name"
read -r dir

# Check if the directory exists
if [ -e "$dir" ]; then
    echo "Directory exists. Entering directory..."
    sleep 1
    cd "$dir" || {
        echo "Failed to enter directory"
        exit 1
    }
else
    echo "Creating/entering directory..."
    sleep 1
    mkdir "$dir"
    cd "$dir" || {
        echo "Failed to enter directory"
        exit 1
    }
fi

# Initialize git repository
git init

# Prompt the user if they want to create files
echo "Do you want to create files? (Y/N)"
read -r create_files

if [[ $create_files == "Y" || $create_files == "y" ]]; then
    # Prompt the user to enter the number of files to create
    echo "Enter the number of files to create"
    read -r num_files

    # Create the specified number of files
    for ((i = 1; i <= num_files; i++)); do
        touch "file$i.txt"
        echo "File 'file$i.txt' created"
    done
fi

# Add the files to the staging area
echo "Adding files to the staging area..."
git add .

# Commit the files
echo "Enter your commit message"
read -r message

git commit -m "$message"

echo "Files committed"

# Prompt the user to enter the remote URL and alias name
echo "Enter your remote URL"
read -r url
echo "Enter your alias name"
read -r alias

# Check if the remote URL is provided
if [ -n "$url" ]; then
    # Add remote repository
    git remote add "$alias" "$url"

    # Pull recent changes from the remote repository
    git pull "$alias" "$branch"

    # Push the files to the remote repository
    echo "Pushing..."
    sleep 1
    git push "$alias" "$branch"
    echo "Files pushed to $url"
else
    echo "URL not found"
    exit 1
fi

# Revert back to the original branch
git checkout -
cd "$original_dir" || {
    echo "Failed to return to the original directory"
    exit 1
}
