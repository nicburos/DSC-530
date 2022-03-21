# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 10:31:26 2022

@author: njack
"""

def math_oper():
    add_answer = 14 + 42
    print(add_answer)
    sub_answer = 123 - 8
    print(sub_answer)
    mult_answer = 18 * 60
    print(mult_answer)
    dev_answer = 36/6
    print(dev_answer)
    

def lists_tuples():
    my_fav_things = [22, 'tomatoes', 'gardening', 7]
    print(my_fav_things)
    my_fav_things.append('beaches')
    print(my_fav_things)
    fav_things_tuple = (22, 'tomatoes', 'gardening', 7)
    print(fav_things_tuple)


def main():
    welcome_message = ("Hello World! I wonder why that is always the default coding text to start with?")
    other_str = (" Who knows!")
    conc_strs = (welcome_message + other_str)
    print(conc_strs)
    math_oper()
    lists_tuples()


if __name__ == '__main__':
        main()