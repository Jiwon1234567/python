import collections
import random

userNums = []
randNums = []
collect = []

def setUNum(ns):
    global userNums
    userNums = ns

def getUNums():
    return userNums

def setRNums():
    global randNums
    randNums = random.sample(range(1, 46), 6)

def getRNums():
    return randNums

def compareNumbers():
    global userNums
    global randNums
    global collect
    
    for item in userNums:
        if randNums.count(item) != 0:
            collect.append(item)
        
    return collect