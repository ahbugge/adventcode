#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:21:58 2023

@author: ahorpeda
"""
import re

input_file = 'input.txt'

def run_1():
    data = [] 
    score = 0
    
    with open(input_file, 'r') as file:

        for line in file.readlines():
            line = line.strip()
            data.append(line)
            
    for line_nr, line in enumerate(data):
        search_index = 0
        numbers = re.findall(r'\d+', line)
        for numb in numbers:
            index = line[search_index:].find(numb) + search_index
            search_index = index + len(numb) 
            neighbour = ''
            
            if line_nr == 0:
                if index == 0:
                    neighbour = data[line_nr+1][index:index+len(numb)+1]
                    neighbour += line[index+len(numb)]
                elif index + len(numb) == len(line):
                    neighbour = data[line_nr+1][index-1:index+len(numb)]
                    neighbour += line[index-1]
                else:
                    neighbour = data[line_nr+1][index-1:index+len(numb)+1]
                    neighbour += line[index+len(numb)]
                    neighbour += line[index-1]
            
            elif line_nr == len(data)-1:
                if index == 0:
                    neighbour = data[line_nr-1][index:index+len(numb)+1]
                    neighbour += line[index+len(numb)]
                elif index + len(numb) == len(line):
                    neighbour = data[line_nr-1][index-1:index+len(numb)]
                    neighbour += line[index-1]
                else:
                    neighbour = data[line_nr-1][index-1:index+len(numb)+1]
                    neighbour += line[index+len(numb)]
                    neighbour += line[index-1]
            
            else:
                if index == 0:
                    neighbour = data[line_nr+1][index:index+len(numb)+1]
                    neighbour += data[line_nr-1][index:index+len(numb)+1]
                    neighbour += line[index+len(numb)]
                elif index + len(numb) == len(line):
                    neighbour = data[line_nr+1][index-1:index+len(numb)]
                    neighbour += data[line_nr-1][index-1:index+len(numb)]
                    neighbour += line[index-1]
                else:
                    neighbour = data[line_nr+1][index-1:index+len(numb)+1]
                    neighbour += data[line_nr-1][index-1:index+len(numb)+1]
                    neighbour += line[index+len(numb)]
                    neighbour += line[index-1]
                    
            if all(char == '.' or char.isnumeric() for char in neighbour):
                continue      
            score += int(numb)     
    return score    


def run_2():
    data = [] 
    score = 0
    
    with open(input_file, 'r') as file:

        for line in file.readlines():
            line = line.strip()
            data.append(line)
    
    star_indices = []
    numb_indices = []
    
    for line_nr, line in enumerate(data):
        search_index = 0
        neighbour_numbs = []
        numbers = re.findall(r'\d+', line)
        for numb in numbers:
            numb_index = line[search_index:].find(numb) + search_index
            search_index = numb_index + len(numb)
            neighbour_numbs.append([numb, list(range(numb_index, numb_index+len(numb)))])
        numb_indices.append([line_nr, neighbour_numbs])
        
        for index, char in enumerate(line):
            if char == '*':
                star_indices.append((line_nr,index))
        
    for element in star_indices:
        line_nr = element[0]
        star_index = element[1]
        neighbour_numbs = []
        
        for indices in numb_indices[line_nr-1][1]:
            if star_index-1 in indices[1]:
                neighbour_numbs.append(indices[0])
            elif star_index+1 in indices[1]:
                neighbour_numbs.append(indices[0])
            elif star_index in indices[1]:
                neighbour_numbs.append(indices[0])
            
            
        for indices in numb_indices[line_nr+1][1]:
            if star_index-1 in indices[1]:
                neighbour_numbs.append(indices[0])
            elif star_index+1 in indices[1]:
                neighbour_numbs.append(indices[0])
            elif star_index in indices[1]:
                neighbour_numbs.append(indices[0])
            
        for indices in numb_indices[line_nr][1]:
            if star_index-1 in indices[1]:
                neighbour_numbs.append(indices[0])
            elif star_index+1 in indices[1]:
                neighbour_numbs.append(indices[0])

        if len(neighbour_numbs) != 2:
            continue
        score += int(neighbour_numbs[0])*int(neighbour_numbs[1])
        
    return score    


q_1 = run_1()
q_2 = run_2()

print('Question 1 answer: ', q_1)
print('Question 2 answer: ', q_2)