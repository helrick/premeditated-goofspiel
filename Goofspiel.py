''' 
MATH 339 Final Project
Premeditated Goofspiel Tournament

Hillary Elrick, April 2017

This program reads in a file of strategies from the agents in the tournament.
Strategies are represented by 13 element vectors:

[2 3 4 5 6 7 8 9 10 11 12 13 1]

Where the first element (2) represents the card played when the center card is an Ace,
the second (3) the card played when the centre card is a 2, etc.

Each new line represents the strategy of a new agent.
The agents compete against each other round robin style and their total scores recorded.
Once all the rounds have completed, the results are written to a csv, Results.csv,
which reports the Team Number, their Score, and their Strategy.

'''

filename = "in.txt"
resultsFile = "Results.csv"

def main():
    strategies = readFile(filename)
    scores = roundRobin(strategies)
    writeFile(scores,strategies)

#takes in two strategy lists, returns pair of scores
def round(agentOne, agentTwo):
    scoreOne = 0
    scoreTwo = 0
    #iterates through every card in deck
    #allocates points based on agent strategy
    for card in range(13):
        if(agentOne[card] == agentTwo[card]):
            pass #their cards cancel out, do nothing
        elif(agentOne[card] > agentTwo[card]):
            scoreOne += card
            scoreTwo -= card
        else:
            scoreOne -= card
            scoreTwo += card
    return (scoreOne, scoreTwo)

def roundRobin(strategies):
    #number of players
    n = len(strategies)
    #list of the pairs of scores all initially 0
    scores = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            roundScores = round(strategies[i],strategies[j])
            scores[i] += roundScores[0]
            scores[j] += roundScores[1]
    return scores
    
def readFile(path):
    output = []
    with open(path,'r') as f:
        data = f.read().splitlines()
    f.close()
    for line in data:
        if (line== ""):
            continue
        lineString = line[1:-1]
        temp = lineString.split(" ")
        output.append(map(int,temp))
    return output

def writeFile(scores, strategies):
    n = len(strategies)
    outstring = "Team ,Score ,Strategy\n"
    for i in range(n):
        outstring += str(i+1) + "," 
        outstring += str(scores[i]) + "," 
        outstring += convertStrat(strategies[i])
        outstring += "\n"
    with open(resultsFile, 'w') as f:
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

main()
