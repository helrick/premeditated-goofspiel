'''
Modified genetic algorithm to produce strategies of Premeditated Goofspiel
MATH 339: Final Project
Hillary Elrick

'''
filename = ("Results.csv")
base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
bestScore = 0
import collections 
import random
from random import shuffle


def main():
    #read in results from previous tournament
    #take the top 6 competitors
    #use them to seed 15 new strategies for the next iteration
    results = readResults(filename)
    nextGen = crossover(results)
    writeStrategies("in.txt", results, nextGen)
    return bestScore


def writeStrategies(path, parents, children):
    #use the best competitor, 5 random children, and 19 random strategies for next generation
    outstring = ""
    outstring += convertStrat(parents[0])
    outstring += "\n"
    for i in range(5):
        outstring += convertStrat(random.choice(children))
        outstring += "\n"
    for i in range(19):
        random.shuffle(base)
        outstring += convertStrat(base)
        outstring += "\n"
    with open(path, 'w') as f:
        f.write(outstring)

#converts strategy from internal list notation
#to type used in tournament
def convertStrat(strategy):
    outString = ''
    tempString = ' '.join(str(e) for e in strategy)
    outString += '['
    outString += tempString.replace(',',' ')
    outString += ']'
    return outString

#returns the best 6 competitors
def readResults(path):
    import csv
    global bestScore
    with open(path, 'rb') as f:
        reader = csv.reader(f)
        results = list(reader)
    #clean it up, remove heading & team number 
    results.pop(0)
    for row in results:
        del row[0]
    results.sort(key=lambda x:int(x[0]))
    results = results[-6:]
    if(int(results[5][0]) > bestScore):
        bestScore = int(results[5][0])
    for row in results:
        del row[0]
    output = []
    for i in range(6):
        output.append(results[i][0])
    return convert(output)

def convert(strategies):
    output = []
    for s in strategies:
        temp = (s[1:-1]).split(" ")
        output.append(map(int,temp))
    return output

def crossover(prevGen):
    #for every possible pairing
    #take element from each with prob. 0.5
    #mutate while fixing
    offspring = []
    n = len(prevGen)
    for i in range(n):
        for j in range(i+1,n):
            offspring.append(merge(prevGen[i],prevGen[j]))
    for child in offspring:
        legal = isLegal(child)
        while(not legal):
            child = fix(child)
            if(isLegal(child)):
                legal = True
    return offspring

def merge(parentA, parentB):
    n = len(parentA)
    child = [0] * n
    for i in range(n):
        if(bool(random.getrandbits(1))):
            child[i] = parentA[i]
        else:
            child[i] = parentB[i]
    return child


def fix(strategy):
    diff = set(base) - set(strategy)
    diff = list(diff)
    shuffle(diff)
    seen = []
    for i in range(len(strategy)):
        if (strategy[i] in seen):
            strategy[i] = diff.pop(0)
            seen.append(strategy[i])
        else:
            seen.append(strategy[i])
    return strategy


def isLegal(strategy):
    if(len(strategy) == 13):
        if(set(strategy) == set(base)):
            return True
    return False

if __name__ == "__main__":
    main()




