#PyPoll Project
#1 Find the total number fo votes cast 
import csv
import os
from posixpath import join
#Assign a variable to the file
file_to_load = os.path.join("Resources", "election_results.csv")
#Open elction results and read file
with open(file_to_load) as election_data:
    print(election_data)
#Create a file to save
file_to_save = os.path.join("Analysis", "Election_Analysis.txt")
#Open file_to_save as a text file
with open(file_to_save, "w") as txt_file:
    #List Counties
    txt_file.write("Arapahoe\nDenver\nJefferson")

#Perform analysis

#2 Get a complete list of candidates who received votes
#3 Number of votes poer candidate
#4 Percentage of votes per candidate
#5 The winner of the election based on popular vote