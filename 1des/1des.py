#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 18:07:58 2023

@author: ahorpeda
"""

input_file = input_path = "input.txt"

numb_dict = {'one': 'o1e',
            'two': 't2',
            'three': 't3e',
            'four': '4',
            'five': '5e',
            'six': '6',
            'seven': '7n',
            'eight': 'e8t',
            'nine': 'n9e',
            }

def run_1():
    data = []
    
    with open(input_path, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            digit_1 = 0
            digit_2 = 0
            
            for char in line:
                if char.isnumeric() and digit_1 == 0:
                    digit_1 = char
                    digit_2 = digit_1
                elif char.isnumeric():
                    digit_2 = char
        
            data.append(digit_1 + digit_2)

    answ = sum([int(numb) for numb in data])
    return answ


def run_2():
    data = []
    
    with open(input_path, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            digit_1 = 0
            digit_2 = 0

            for numb in numb_dict:
                if numb in line:
                    line = line.replace(numb, numb_dict[numb])

            for char in line:
                if char.isnumeric() and digit_1 == 0:
                    digit_1 = char
                    digit_2 = digit_1
                elif char.isnumeric():
                    digit_2 = char
        
            data.append(digit_1 + digit_2)
            
    answ = sum([int(numb) for numb in data])
    return answ


q_1 = run_1()
q_2 = run_2()

print('Question 1 answer: ', q_1)
print('Question 2 answer: ', q_2)

