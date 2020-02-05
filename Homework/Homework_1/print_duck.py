#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:34:10 2020

@author: zachary.trozenski
DAT-129: Spring 2020
Homework 1: Icon Assignement
"""

# Initialize the list containing lists of each icon line in binary
binary_icon = [['0','0','0','1','1','1','0','0','0','0'],
                ['0','0','1','0','0','0','1','0','0','0'],
                ['0','1','0','0','1','0','1','0','0','0'],
                ['1','1','0','0','0','0','1','0','1','0'],
                ['0','1','0','0','0','0','0','1','0','1'],
                ['0','0','1','0','0','0','0','0','0','1'],
                ['0','0','1','0','0','0','0','0','1','0'],
                ['0','0','1','0','0','0','0','0','1','0'],
                ['0','0','0','1','0','0','0','1','0','0'],
                ['0','0','0','1','1','1','1','0','0','0']]

def replace_values(values):
    """
    Take the iterated list elements and replace the values '1' and '0' with
    '@' and ' ' respectively and print the iterated elements.
    """
    if '1' in values:
        print(str(values.replace('1','@')), end=' ')
    else:
        print(str(values.replace('0',' ')), end=' ')


def pretty_print_the_binary(any_list):
    """
    Take the binary list of lists, where each list within the large list
    is one line of the 10x10 grid and return a picture of a duck 
    with binary replace by '@' and ' '
    """
    for pieces in any_list:
        for things in pieces:
            replace_values(things)
        print("\n", end='')

def print_icon_backwards(big_list):
    """
    Take the binary list of lists, where each list within the large list
    is one line of the 10x10 grid and return a backwards picture of a duck 
    with binary replace by '@' and ' '
    """
    for lines in big_list[:]:
        for figures in lines[::-1]:
            replace_values(figures)
        print("\n", end='')

def print_icon_upside_down(my_list):
    """
    Take the binary list of lists, where each list within the large list
    is one line of the 10x10 grid and return an upside down picture of a duck 
    with binary replace by '@' and ' '
    """
    for rows in my_list[::-1]:
        for elements in rows[::]:
            replace_values(elements)
        print('\n', end='')

def main():
    # Print the picture with new symbol instead of binary
    pretty_print_the_binary(binary_icon)
    print()
    
    # Print the icon backwards
    print_icon_backwards(binary_icon)
    print()
    
    # Print the icon upside down
    print_icon_upside_down(binary_icon)
    print()

if __name__ == "__main__":
    main()
    
# SCRATCH
# def print_nice_list(better_list):
# """
# Input: List of lists in binary
# Output: Concatenated list formatted without syntax marking
# """
# for series in better_list[:]:
#     for char in series:
#        print(char, end=' ')
#     printed_list = print("\n", end='')
# return printed_list    
