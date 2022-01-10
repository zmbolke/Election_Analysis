# Election_Analysis

# Overview
The purpose of this project is to audit the election results of a colorado based election. The data provided included as CSV file containing votes that specified voting ID, county, and candidate. The tasks performed included: getting the total vote count, the voted for each candidate, the percent vote for each candidate, the vote count per county, the largest number of votes per county, the winner of the election by popular vote, the number of votes the winning candidiate received, and the winning percentage. 

# Resources
Data provided included the election_results.csv
Python version 3.7.6

# Results
-There were a total of 369,711 votes cast.
-There were three counties in colorado: Denver, Jefferson, and Arapahoe.
-A brerakdown of the votes per county in the precinct are as follows:
-Denver: 82.8% (306,055)
-Jefferson: 10.5% (38,855)
-Arapahoe 6.7% (24,801)
-The largest county turnout was Denver with 306,055 votes (82.8% of the total votes).
-The candidates in the race were Charles Casper Stockholm, Dianna DeGette, and Raymon Anthony Doane.
-Votes received by each candidate are as follows:
-Charles Casper Stockham:  23.0% (85,213)
-Diana DeGette:  73.8% (272,892)
-Raymon Anthony Doane:  3.1% (11,606)
-The winner of the election was Diana DeGette with 272,892 votes, or 73.78% of the vote. 

# Election Audit Summary
The script submitted is dynamic and can be adapted to an election with additional candidates and counties since the script creates lists based on the number of candidates and counties in the election. 
First this script could be changed to track an election that needs a minimum percent of the vote to win, not just the majority. This would be done by finding the leading candidate and making sure that the winning percentage is larger than the minimum percentage required to win. 
The second change is that this script could be changed to look at the winning candidate per county by running the vote count on a per county basis.   
