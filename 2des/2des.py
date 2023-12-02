#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 12:16:32 2023

@author: ahorpeda
"""

input_file = 'input.txt'

def run_1():
    bag_limit = {'red': 12,
                 'green': 13,
                 'blue': 14 
                 }

    with open(input_file, 'r') as file:        
        score = 0
        for line in file.readlines():
            line = line.strip()

            game_nr = int(line[5:line.index(':')])            
            sets = line[line.index(':')+1:].split(';')

            for set_ in sets:
                hand = {'red': 0,
                        'green': 0,
                        'blue': 0
                        }
                
                for item in set_.split(','):
                    color_numb = item.split(' ')[1]
                    color = item.split(' ')[2]
                    hand[color] += int(color_numb)
                
                result = all(hand[key] <= bag_limit[key] for key in bag_limit)
                if not result:
                    break
                 
            if result:
                score += game_nr
        return score


def run_2():
    with open(input_file, 'r') as file:        
        score = 0
        for line in file.readlines():
            line = line.strip()
            sets = line[line.index(':')+1:].split(';')
            
            hand_max = {'red': 0,
                        'green': 0,
                        'blue': 0
                        }
            
            for set_ in sets:
                for item in set_.split(','):
                    color_numb = int(item.split(' ')[1])
                    color = item.split(' ')[2]
                    if color_numb > hand_max[color]:
                        hand_max[color] = color_numb
            
            score += list(hand_max.values())[0]*list(hand_max.values())[1]*list(hand_max.values())[2]
        return score
    
score_1 = run_1()
score_2 = run_2()

print('Question 1 answer: ', score_1)
print('Question 2 answer: ', score_2)