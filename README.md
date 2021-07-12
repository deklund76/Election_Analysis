# Election_Analysis

## Project Overview
This analysis is a mock election audit of a congressional election for the Colorado Board of Elections using a .csv file of results as a source. The following tasks were performed:

1. Calculated the total number of votes cast.
2. Got a complete list of candidates who received votes.
3. Calculated the total number of votes each candidate received.
4. Calculated the percentage of votes each candidate won.
5. Determined the winner of the election based on the popular vote.
6. Got a complete list of counties involved in the election.
7. Counted vote totals for each county in the congressional district.
8. Determined which county had the highest turnout.

## Election-Audit Results
The Analysis of the election shows that:

* There were 369,711 votes cast in this eleciton
* Jefferson County received 10.5% of the vote and 38,855 votes
* Denver County received 82.8% of the vote and 306,055 votes
* Arapahoe County receieved 6.7% of the vote and 24,801 votes
* The county with the highest turnout was Denver county
* Raymon Anthony Doane received 3.1% of the vote and 11,606 votes
* Charles Casper Stockham received 23.0% of the vote and 85,213 votes
* Diana DeGette won the election, she received 73.8% of the vote and 272,892 votes

## Summary
The Python script used for this audit contained no specific code pertaining to the Colorado election that the script analyzed. This means it can be used on any election data with the same format as the election_results.csv used here. If the county and vote data are present but in a different order, it's just a matter of changing some array indices to match the script to the data. In the case of a ranked-choice election such as the recent mayoral election in New York, the script only requires one more loop and a few conditional statement to be extended for use with ranked choice voting. Here is the Pseudo-Code for such an extension:

initialize "eliminated" array
initialize "fewest votes"

while winner == false:

  fewest votes = 0
  eliminated = ""

  iterate through records counting votes
    for candidate choices in range(columns with ranked choices)
      if candidate not eliminated
        increment candidate's vote count
        break out of for loop

  iterate through candidate dictionary
    if candidate has >50% of votes:
      winner = true
    if candidate's votes < fewest votes:
      fewest votes = candidate's votes
      eliminated = candidate name
    
  eliminated.append(eliminated)
  reset vote totals for candidates to 0
