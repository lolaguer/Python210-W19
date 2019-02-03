#!/usr/bin/env python3

# ----------------------------------#
# Assignment: file_exercise.py
# Author: Lola Guerrero
# RRoot, 02/02/2019, Created file
# ----------------------------------#


# #########################################
# print ('## Paths and File Processing ##')
# #########################################
#
# # Write a program which prints the full path for all files in the current directory, one per line
# import os
#
# def files_in_dir(directory):
#
#     dir_path = os.path.abspath(directory)
#     files = os.listdir(directory)
#
#     files_path = []
#     for file in files:
#         file_path = dir_path + '/' + file
#         files_path.append(file_path)
#
#     return ("\n".join(files_path))
#
# #Test:
# print (files_in_dir("."))
#
#
# # Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command)
# def copy_file(source_file, destination_file):
#     try:
#         dest_file = open(destination_file,"x")
#     except:
#         print (destination_file)
#         new_destination_file = input('File already exists, chose a different name: ')
#         dest_file = open(new_destination_file, "x")
#
#     source_file = open(source_file, 'r')
#     for line in source_file:
#         dest_file.write(line)
#
#     # destination_file.close()
#
# #Test:
# source_file = '/Users/i22041/Documents/Python_Certification_UW/PYTHON210/Python210-W19/students/lolaguerrero/session04/students.txt'
# destination_file = '/Users/i22041/Documents/Python_Certification_UW/PYTHON210/Python210-W19/students/lolaguerrero/session04/students2.txt'
# copy_file(source_file, destination_file)
#
#
# # Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once
# # This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing).
# # Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files
# # Test it with both text and binary files (maybe jpeg or something of your choosing).
#
# def copy_large_files(source_file, destination_file):
#     try:
#         dest_file = open(destination_file,"wb")
#     except:
#         print (destination_file)
#         new_destination_file = input('File already exists, chose a different name: ')
#         dest_file = open(new_destination_file, "x")
#
#     source_file = open(source_file, 'rb')
#     count = 0
#     for line in source_file:
#         dest_file.write(line)
#         count += 1
#         if count % 1000 == 0:
#             print ('Clearing memory')
#             dest_file.flush()
#
#     # dest_file.close()
#
# #Test:
# source_file = '/Users/i22041/Documents/Python_Certification_UW/PYTHON210/Python210-W19/students/lolaguerrero/session04/cat-and-dog.jpg'
# destination_file = '/Users/i22041/Documents/Python_Certification_UW/PYTHON210/Python210-W19/students/lolaguerrero/session04/cat-and-dog2.jpg'
# copy_large_files(source_file, destination_file)


########################################
print ('## File reading and parsing ##')
########################################

students = '/Users/i22041/Documents/Python_Certification_UW/PYTHON210/Python210-W19/students/lolaguerrero/session04/students.txt'

file = open(students, 'r')
file_no_header = file.readlines()[1:]

names = {}
nickname = []
lang_dict = {}
track_lang = {}

for lines in file_no_header:
    line = lines.split(':')
    name = line[0]
    names[name] = ''
    nick_lang = line[1]
    row = nick_lang.split(',')
    languages = []
    for r in row:
        try:
            r = r.replace('\n', '').strip()
            if r[0].isupper():
                r_split = r.split(' ')
                if len(r_split) == 2:
                    nickname.append(r_split[0])
                    languages.append(r_split[1])
                    #track_lang[name] = 'ok'
                    continue
                nickname.append(r)
            else:
                if r.lower() == 'vb':
                    r = 'visualbasic'
                if r.lower() == 'mysql':
                    r = 'sql'
                if (r.lower() == 'nothing') or (r.lower() == 'db'):
                    r = None
                languages.append(r)
                #track_lang[name] = 'ok'
        except IndexError as e:
            print ('Value error:', r)
            print (e)
    for language in languages:
        #language = language.lower()
        # if language == 'vb':
        #     language = 'visualbasic'
        # if language == 'mysql':
        #     language = 'sql'
        # if (language == 'nothing') or (language == 'db'):
        #     language = ''
        if language in lang_dict:
            lang_dict[language] +=1
        else:
            lang_dict[language] = 1



import operator
sorted_lang_dict = sorted(lang_dict.items(), key=operator.itemgetter(1))

print (sorted_lang_dict)
print (nickname)
print (names)
print (track_lang)
names.update(track_lang)
print (names)