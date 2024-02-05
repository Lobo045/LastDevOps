#!/bin/bash

# Specify the source and destination folders
source_folder="\Users\lopez\OneDrive\Desktop\LastDevOps\clients"
destination_folder="\Users\lopez\OneDrive\Desktop\LastDevOps\copy_clients"

# Check if the source folder exists
if [ -d "$source_folder" ]; then
    # Check if the destination folder exists, if not, create it
    if [ ! -d "$destination_folder" ]; then
        mkdir -p "$destination_folder"
    fi

    # Copy the contents of the source folder to the destination folder
    cp -r "$source_folder"/* "$destination_folder"
    
    # Delete the contents of the source folder
    rm -r "$source_folder"/*
    
    echo "Content copied and source folder emptied successfully."
else
    echo "Source folder does not exist."
fi
