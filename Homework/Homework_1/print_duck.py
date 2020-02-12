#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:34:10 2020
@author: zachary.trozenski
DAT-129: Spring 2020
Homework 2: Modularity and Icon Assignement
Modified by Joel Whiteman - 2/10/2020
"""

import os

def file_reader(filepath):
    """Opens a text file and reads the contents into a string variable.

    This file opens the file at the user-inputted filepath and reads it into the 
    file_text string variable. It returns the file_text variable for use elsewhere.
    """
    with open(filepath, "r") as file_reader:
        file_text = file_reader.read()
    return file_text

def list_maker(file_text):
    """Takes the file's encoded icon text and turns it into a list of lists.

    This function takes the string contents of the user's icon text input file. First,
    it casts that string into a list of the 100 characters in the file. Then it slices 
    the list into individual lists of ten characters a piece, and adds the resulting 
    ten lists into a new icon_list that is returned for use elsewhere.
    """
    text_list = list(file_text)
    icon_list = []
    icon_list.append(text_list[0:10])
    icon_list.append(text_list[10:20])
    icon_list.append(text_list[20:30])
    icon_list.append(text_list[30:40])
    icon_list.append(text_list[40:50])
    icon_list.append(text_list[50:60])
    icon_list.append(text_list[60:70])
    icon_list.append(text_list[70:80])
    icon_list.append(text_list[80:90])
    icon_list.append(text_list[90:100])
    return icon_list

def replace_values(values, empty_character, shaded_character):
    """
    Take the iterated list elements and replace the shaded_character and
    empty_character values and replace them with '@' and ' ' respectively.
    After replacement, print the iterated elements.
    """
    if shaded_character in values:
        print(str(values.replace(shaded_character,'@')), end=' ')
    else:
        print(str(values.replace(empty_character,' ')), end=' ')

def pretty_print_the_binary(icon_list, empty_character, shaded_character):
    """
    Take the binary list of lists, where each list within the large list
    is one line of the 10x10 grid and return a picture of a duck 
    with binary replace by '@' and ' '
    """
    for rows in icon_list:
        for values in rows:
            replace_values(values, empty_character, shaded_character)
        print("\n", end='')
    print('\n')

def print_icon_backwards(icon_list, empty_character, shaded_character):
    """
    Take the binary list of lists, where each list within the large list
    is one line of the 10x10 grid and return a backwards picture of a duck 
    with binary replace by '@' and ' '
    """
    for rows in icon_list[:]:
        for values in rows[::-1]:
            replace_values(values, empty_character, shaded_character)
        print("\n", end='')
    print('\n')

def print_icon_upside_down(icon_list, empty_character, shaded_character):
    """
    Take the binary list of lists, where each list within the large list
    is one line of the 10x10 grid and return an upside down picture of a duck 
    with binary replace by '@' and ' '
    """
    for rows in icon_list[::-1]:
        for values in rows[::]:
            replace_values(values, empty_character, shaded_character)
        print('\n', end='')
    print('\n')
    
def filepath_menu():
    """Allows the user to input a filepath name.
    
    This function displays a menu question that allows the user to enter a string
    containing the name of a file they'd like to read for icon data. It also checks 
    that the filename string they've entered actually exists in the current directory.
    If it does not, they are asked to enter a different string. It then returns the 
    validated filepath for use elsewhere.
    """
    filepath = ""
    while filepath == "":
        filepath = input("Please input the name of the text file containing your " + 
            "icon code.\n")
        filepath_exists = os.path.isfile(filepath)
        if not filepath_exists:
            print("\nThat file doesn't appear to exist in this directory!\n")
            filepath = ""
    return filepath

def character_menu():
    """Allows the user to input the characters that represent shaded and empty cells.
    
    This function asks the user to define the characters in their text file that
    represent shaded and empty cells in the icon. It runs the character_validator
    function on the characters they enter and then returns the validated variables for
    use elswhere. 
    """
    empty_character = ""
    shaded_character = ""
    while empty_character == "":
        empty_character = input("\nIn your text file, which character represents " +
            "an empty cell?\n")
        empty_character = character_validator(empty_character)
    while shaded_character == "":
        shaded_character = input("\nIn your text file, which character represents " +
            "a shaded cell?\n")
        shaded_character = character_validator(shaded_character)
    return empty_character, shaded_character

def character_validator(character):
    """Validates that user input is only of one character in length.

    This function checks a user-inputted string to ensure that it is only one
    character long. If it is longer or shorter, it prints a message and sets the
    validated character variable to be empty. If the character string is of one 
    character in length and is valid, it sets the validated character varible
    to be equal to the original string. It returns the validated character variable
    for use elsewhere.
    """
    if len(character) > 1:
        print("\nThat's too many characters!")
        validated_character = ""
    elif len(character) == 0:
        print("Please enter a valid character.")
        validated_character = ""
    else:
        validated_character = character
    return validated_character

def user_menu():
    """Displays a menu to the user and records their input.

    This function controls the user input to the program. It calls other functions
    to get the filepath string, the empty character, and the shaded character. It 
    then returns these varaibles for use elsewhere. 
    """
    filepath = filepath_menu()
    empty_character, shaded_character = character_menu()
    return filepath, empty_character, shaded_character

def main():
    filepath, empty_character, shaded_character = user_menu()
    file_text = file_reader(filepath)
    icon_list = list_maker(file_text)
    
    # Print the picture with new symbol instead of binary
    pretty_print_the_binary(icon_list, empty_character, shaded_character)
    
    # Print the icon backwards
    print_icon_backwards(icon_list, empty_character, shaded_character)

    # Print the icon upside down
    print_icon_upside_down(icon_list, empty_character, shaded_character)

if __name__ == "__main__":
    main()