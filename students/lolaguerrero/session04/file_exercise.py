#!/usr/bin/env python3

# ----------------------------------#
# Assignment: file_exercise.py
# Author: Lola Guerrero
# RRoot, 02/02/2019, Created file
# ----------------------------------#


#########################################
print ('## Paths and File Processing ##')
#########################################

# Write a program which prints the full path for all files in the current directory, one per line
import os

def files_in_dir(directory):

    dir_path = os.path.abspath(directory)
    files = os.listdir(directory)

    files_path = []
    for file in files:
        file_path = dir_path + '/' + file
        files_path.append(file_path)

    return ("\n".join(files_path))

#Test:
print (files_in_dir("."))


# Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command)
def copy_file(source_file, destination_file):
    try:
        dest_file = open(destination_file,"x")
    except:
        print (destination_file)
        new_destination_file = input('File already exists, chose a diferrent name: ')
        dest_file = open(new_destination_file, "x")

    source_file = open(source_file, 'r')
    for line in source_file:
        dest_file.write(line)

#Test:
source_file = '/Users/i22041/Documents/Python_Certification_UW/PYTHON210/Python210-W19/students/lolaguerrero/session04/students.txt'
destination_file = '/Users/i22041/Documents/Python_Certification_UW/PYTHON210/Python210-W19/students/lolaguerrero/session04/students2.txt'
copy_file(source_file, destination_file)


# Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once

# This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing).
# Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files


# Test it with both text and binary files (maybe jpeg or something of your choosing).
