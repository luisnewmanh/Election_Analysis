"""
1.Open the data file.
2.Write down the names of all the candidates.
3.Add a vote count for each candidate.
4.Get the total votes for each candidate.
5.Get the total votes cast for the election."""

import csv
#indirect path, impoprt additional method
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    #total number of votes
    total_votes=0
    #name of candidates
    candidates_options=[]
    #create dictonary
    candidate_votes={}
    #winner candidate tracker
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0
    for row in file_reader:
        total_votes=total_votes+1
        if row[2] not in candidates_options:
            candidates_options.append(row[2])
            candidate_votes[row[2]]=0
        candidate_votes[row[2]]=candidate_votes[row[2]]+1
    for candidate in candidates_options:
        vote_percentage=(candidate_votes.get(candidate)/total_votes)*100
        if candidate_votes.get(candidate)>winning_count and vote_percentage>winning_percentage:
            winning_count=candidate_votes.get(candidate)
            winning_percentage=vote_percentage
            winning_candidate=candidate
        print(f"{candidate}: {round(vote_percentage,1)}% ({candidate_votes.get(candidate)})\n")
    print(f"---------------------------\n"
        f"winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {round(winning_percentage,1)}%\n"
        f"---------------------------")
