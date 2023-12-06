#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:53:22 2023

@author: ahorpeda
"""
input_file = 'input.txt'


def run_1():
    with open(input_file, 'r') as file:
        data = file.readlines()
    result = 1    
    race_times = data[0].split(':')[1].split()
    distances_to_beat = data[1].split(':')[1].split()
    for race_nr, race_time in enumerate(race_times):
        charge_option = 0
        for charge_time in range(0, int(race_time)+1):
            speed = charge_time
            distance = speed * (int(race_time)-charge_time)
            if distance > int(distances_to_beat[race_nr]):
                charge_option += 1
        result *= charge_option
    return result


def run_2():
    with open(input_file, 'r') as file:
        data = file.readlines()
    race_time = int(''.join(data[0].split(':')[1].split()))
    distance_to_beat = int(''.join(data[1].split(':')[1].split()))
    charge_options = 0
    for charge_time in range(0, race_time+1):
        speed = charge_time
        distance = speed * (race_time - charge_time)
        if distance > distance_to_beat:
            charge_options += 1

    return charge_options


q_1 = run_1()
q_2 = run_2()

print('Question 1 answer: ', q_1)
print('Question 2 answer: ', q_2)