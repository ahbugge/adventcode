#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:22:58 2023

@author: ahorpeda
"""

input_file = 'input.txt'

def run_1():
    total_score = 0
    
    with open(input_file, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            
            score = 0  
            winning = line.split(':')[1].split('|')[0].split()
            hand = line.split(':')[1].split('|')[1].split()

            win_count = 0
            for numb in hand:         
                if numb in winning:
                    win_count += 1
            
            if win_count:
                score = 1
                if win_count > 1:
                    score = 2**(win_count-1)
            total_score += score     
    return total_score


def run_2():
    cards = {}
    winnings = []
    hands = []
    win_counts = []
    
    with open(input_file, 'r') as file:
        
        for line in file.readlines():
            line = line.strip()
            
            cards[int(line.split(':')[0][-3:])] = 1
            winning = line.split(':')[1].split('|')[0].split()
            hand = line.split(':')[1].split('|')[1].split()
            hands.append(hand)
            winnings.append(winning)
            
            win_count = 0
            for numb in hand:         
                if numb in winning:
                    win_count += 1
            win_counts.append(win_count)
    
    for card, win_count in enumerate(win_counts):
        card += 1
        for j in range(cards[card]):
            for i in range(1, win_count+1):
                cards[card+i] = cards.get(card+i) + 1
            
    score = sum(cards.values())  
    return score



q_1 = run_1()
q_2 = run_2()

print('Question 1 answer: ', q_1)
print('Question 2 answer: ', q_2)

