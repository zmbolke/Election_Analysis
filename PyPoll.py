#PyPoll Project
#1 Find the total number fo votes cast 

#Add dependancies
import csv
import os
#Assign a variable to the load file
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to the save file
file_to_save = os.path.join("Analysis", "election_analysis.txt")
#Open elction results and read file
with open(file_to_load) as election_data:
    #read file and print data
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    
#Perform analysis


#2 Get a complete list of candidates who received votes
#3 Number of votes poer candidate
#4 Percentage of votes per candidate
#5 The winner of the election based on popular vote