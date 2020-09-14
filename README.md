# Election Analysis
## Overview of Project
The client, a Colorado Board of Elections, wants to complete the election audit for a recent local congressional election.
### Purpose
The purpose of this analysis is to deliver key indicators on the recent election: 

1. Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. Determine the winner of the election based on popular vote

Additionally, the Colorado Board of Elections wants to analyze the elections turnout usining the following parameters:

1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

## Results
### Election Audit
<img src="https://github.com/luisnewmanh/Election_Analysis/blob/master/Resources/Audit_Results.JPG"> 

The analysis of the election shows that:
- There was a total of 369,711 votes casted in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 of the votes 
    - Diana DeGette received 73.8% of the vote and 272,892 of the votes 
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 of the votes
- The winner of the election was:
    - Candidate Diana DeGette, who received 73.8% of the vote and 272,892 of the votes
- The counties that vote in the election were:
    - Jefferson
    - Denver
    - Arapahoe
- The voter turnout for each county was:
    - Jefferson received 10.5% of the vote and 38,855 of the votes
    - Denver received 82.8% of the vote and 306,055 of the votes
    - Arapahoe received 6.7% of the vote and 24,801 of the votes
- The county with highest turnout was:
    - Denver County received 82.8% of the vote and 306,055 of the votes
## Summary
The script to perform the election audit can be used for any other election as long as the provided data set (election_results.csv) has the same format. The sript only open the results file in reading mode assuring that the file will be modified, thus changing the results. One of change to the script that can be done is to analyze the votes per county for each candidate, this can lead to understand the preferences for a particular candidate in a given county. It could be possible to verify if there is a duplicated ballot as an extra layer of security for the election.
