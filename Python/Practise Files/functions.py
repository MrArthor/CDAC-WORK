#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:17:32 2024

@author: mr-arthor
"""
# =============================================================================
#  
# Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
# 1. Find out how many students are in the list
# 2. Change Lisa’s favourite colour
# 3. Remove 'Jenny' and her favourite colour
# 4. Sort and print students and their favourite colours alphabetically by name
# =============================================================================

people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}

def count(peopl):
    count = 0
    for x in peopl:
        count += 1
    return count

print(count(people))
def changecolor(people,name,color):
    people[name]=color
    return people
people = changecolor(people, "Jenny","red")
print(people)

def removepep(people,name):
    del people[name]
    return people

people = removepep(people, "Jenny")
print(people)
def sortstu(people):
    print(sorted(people))

sortstu(people)
