"""
Assignment: 31
Problem: 03
Topic: dict
Description: Write a python script to create a dictionary where key values are cricket player names and data-values are tuple of 4 elements -matches played, total runs, half centuries and centuries. All data should be taken from user.
Date: 07-07-2026
"""

def inputData():
    name=input("Enter Player name: ")
    matches=int(input("Number of Matches played: "))
    runs=int(input("Enter total runs: "))
    hc=int(input("Number of Half-Centuries: "))
    c=int(input("Number of Centuries: "))
    return [name,matches,runs,hc,c]

def add_player(d,player):
    d[player[0]]=tuple(player[1::])

d1=dict()

while True:
    match input("Add another Player: 'y'\nView the Dictionary: 'v'\n"):
        case 'y':
            add_player(d1,inputData())
        case 'v':
            for k,o in d1.items():
                print(k,o)
            break
        case _:
            break