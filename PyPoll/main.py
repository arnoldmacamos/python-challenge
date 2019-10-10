#------------------------------------------------------------------------------------------------------------------------------- 
# PyBank Script
# Author:         Arnold Macamos
# Date  :         October 09, 2019
# Description:    This is to summarize the voting results
#-------------------------------------------------------------------------------------------------------------------------------   


import os
import csv
import collections

#------------------------------------------------------------------------------------------------------------------------------- 
# This will display the results on the terminal and also export it in an output file
#-------------------------------------------------------------------------------------------------------------------------------   
def output_result(result):

    print(result);
    
    filePath = os.path.join("Output","poll_results.txt")

    with open(filePath,"w") as resultFile:
        resultFile.write(result)
        resultFile.close()
    
    print(f"The above result is also saved in {filePath}")
    
#------------------------------------------------------------------------------------------------------------------------------- 
# This is the starting function of the program
#-------------------------------------------------------------------------------------------------------------------------------          
def run_program():
    filePath = os.path.join("Resources","election_data.csv")
    listElecData = []         #to hold the list of the election data
    #listElecSummary = []      #to hold the summary or election results
    #read the data into the listElecData dictionary list
    with open(filePath) as csvFile:
        reader = csv.DictReader(csvFile)
    
        for row in reader:
            voterID = row["Voter ID"] 
            county = row["County"] 
            candidate = row["Candidate"]
            listElecData.append(
                {
                    "VoterID"   : voterID,
                    "County"    : candidate,
                    "Candidate" : candidate
                }
            )
 
    listElecSummary = collections.Counter([d['Candidate'] for d in listElecData])
    totalVotes = sum(listElecSummary.values())
    winner = max(listElecSummary, key=listElecSummary.get)
    
    #get the list of values from the budgetData dictionary list
 
    print(winner)


#-------------------------------------------------------------------------------------------------------------------------------   
# Start the program
#-------------------------------------------------------------------------------------------------------------------------------   
run_program()
