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
    #name of counties
    counties_names=[]
    #create dictonaries candidates and votes
    candidate_votes={}
    county_votes={}
    #winner candidate and largest county tracker
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0
    largest_turnout=""
    winning_county=0
    #vote count
    for row in file_reader:
        total_votes=total_votes+1
        if row[2] not in candidates_options:
            candidates_options.append(row[2])
            candidate_votes[row[2]]=0
        candidate_votes[row[2]]=candidate_votes[row[2]]+1
        if row[1] not in counties_names:
            counties_names.append(row[1])
            county_votes[row[1]]=0
        county_votes[row[1]]=county_votes[row[1]]+1
    #print results and save them into analysis.txt
    with open(file_to_save,"w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"---------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"---------------------------\n\n")
        print(election_results, end="")
        txt_file.write(election_results)
        print("County Votes:")
        txt_file.write("County Votes:\n")
        for county in counties_names:
            county_percentage=(county_votes.get(county)/total_votes)*100
            county_results=(f"{county}: {round(county_percentage,1)}% ({county_votes.get(county)})\n")
            print(county_results, end="")
            txt_file.write(county_results)
            if county_votes.get(county)>winning_county:
                largest_turnout=county
        greatest_turnout=(
            f"\n"
            f"""---------------------------
Largest County Turnout: {largest_turnout}
---------------------------\n\n"""
        )
        print(greatest_turnout)
        txt_file.write(greatest_turnout)
        for candidate in candidates_options:
            vote_percentage=(candidate_votes.get(candidate)/total_votes)*100
            candidate_results=(f"{candidate}: {round(vote_percentage,1)}% ({candidate_votes.get(candidate)})\n\n")
            print(candidate_results, end="")
            txt_file.write(candidate_results)
            if candidate_votes.get(candidate)>winning_count and vote_percentage>winning_percentage:
                winning_count=candidate_votes.get(candidate)
                winning_percentage=vote_percentage
                winning_candidate=candidate        
        winning_summary=(f"---------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count}\n"
            f"Winning Percentage: {round(winning_percentage,1)}%\n"
            f"---------------------------")
        print(winning_summary, end="")
        txt_file.write(winning_summary)
        #faltan comas en votos y error en turnout debe ser denver