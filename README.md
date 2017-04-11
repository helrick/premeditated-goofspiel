# premeditated-goofspiel

Files and programs associated with running a Premeditated Goofspiel Tournament

To run a tournament with n human teams:
1) Number the teams from 1-n
2) Put their strategies in the vector form [1 2 3 etc.] 
3) One team's strategy per line
4) Run the Goofspiel.py file
5) The results will be stored in the .csv file Results.csv
6) Repeat steps 2-4 for as many iterations of the tournament as required, 
   Copy and save the scores from Results.csv to prevent loss of data

To simulate a tournament with agents, using a modified genetic algorithm 
to change their strategies:
1) Run the 'genStrategies.py' file
2) Run the 'runTournament.py' file 
(best overscore score for one round against all other agents  will be printed)
3) The results will be stored in the .csv file GeneticResults.csv
(the default is to run 200 iterations of the genetic algorithm)
 




