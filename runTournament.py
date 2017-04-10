#

def main():
    import Goofspiel
    import geneticGoofspiel
    clearFile()
    bestOverall = 0
    for i in range(200):
        Goofspiel.main()
        bestScore = geneticGoofspiel.main()
        if(bestOverall < bestScore):
            bestOverall = bestScore
        writeFile(i)
    print("Best Overall Score: " + str(bestOverall))

def clearFile():
    f = open("GeneticResults.csv","w")
    f.write("")

def writeFile(num):
    temp = open("Results.csv")
    f = open("GeneticResults.csv","a")
    f.write("Iteration: " + str(num+1) + "\n")
    f.write(temp.read())

if __name__ == "__main__":
    main()
