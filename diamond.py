#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/07/26 11:06:07.767381
#+ Editado:	2022/07/26 15:36:23.161227
# ------------------------------------------------------------------------------

import sys

# ------------------------------------------------------------------------------

ABC = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# function to call to close the program
def close():
    print('You have to insert a letter as an argument.')
    print(f'Supported letters: {ABC}')
    sys.exit()

# function to do the inial tests on input
def checks():
    # if no argument is provided
    if len(sys.argv)<2:
        close()

    # if the argument provided is not a letter or in the thought of letter list
    if not sys.argv[1].isalpha() or sys.argv[1].upper() not in ABC:
        close()

# returns the position of the letter in the string, hence level
# said level will be used to calculate spacing on the diamond structure
def get_lvl(letter):
    return ABC.find(letter)

# return the previous letter in the ABC
def get_lower_lvl_letter(letter):
    return ABC[get_lvl(letter)-1]

# return the ammount of spaces that goes inside of a function
def get_inside_spaces(spacing, letter):
    return spacing * ((get_lvl(letter)*2) - 1)

def constructor(letter, lst_diamond, spacing, repeated = 0):
    FIRST_LETTER = 'A'

    if letter == FIRST_LETTER:
        lst_diamond.insert(0, repeated*spacing + letter)
        lst_diamond.append(repeated*spacing + letter)

        return lst_diamond

    else:
        lst_diamond.append(repeated*spacing + letter + get_inside_spaces(spacing, letter) + letter)
        if repeated > 0:
            lst_diamond.insert(0, repeated*spacing + letter + get_inside_spaces(spacing, letter) + letter)

        return constructor(get_lower_lvl_letter(letter), lst_diamond, spacing, repeated+1)

# shows the diamond in the screen
def print_diamond(lst_diamond):
    for ele in lst_diamond:
        print(ele)

def main():
    spacing = ' '
    lst_diamond = []

    checks()

    print_diamond(constructor(sys.argv[1].upper(), lst_diamond, spacing))

# ------------------------------------------------------------------------------

main()

# ------------------------------------------------------------------------------
