#PyPoll Project
#1 Find the total number fo votes cast 
#Add dependancies
import csv
import os

#Assign a variable to the load file
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to the save file
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#set total votes equal to 0 
total_votes = 0
#create list of candidates
candidate_options = []
#create dictionary to track votes
candidate_votes = {}

#Open elction results and read file
with open(file_to_load) as election_data:
    #read file and print data
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    #Loop through rows
    for row in file_reader:
        #add up votes
        total_votes += 1
        #Candidate names
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            #add candidates to the list
            candidate_options.append(candidate_name)
            #set vote count for each candidate to 0
            candidate_votes[candidate_name] = 0
        #add up votes for each candidate 
        candidate_votes[candidate_name] += 1
    #PRINT vote percentage for each candidate   
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: received {vote_percentage}% of the vote.")


