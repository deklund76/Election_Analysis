# Add our dependencies.
import csv, os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Candidate and vote count variables
candidate_options = []
candidate_votes = {}
total_votes = 0

# Create a county list and county votes dictionary.
counties = []
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county and county voter turnout.
highest_turnout_county = ""
highest_county_vote_count = 0
highest_county_turnout = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Read each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes += 1

        # Add candidates to candidate option list
        candidate_name = row[2]

        # Extract the county name from each row.
        county_name = row[1]

        if candidate_name not in candidate_options:
             # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 1
        else:
            candidate_votes[candidate_name] += 1

        # Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in counties:

            # Add the existing county to the list of counties.
            counties.append(county_name)

            # Begin tracking the county's vote count.
            county_votes[county_name] = 1
        else:
            county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    # Print beginnning of County vote summary
    print("\nCounty Votes:\n")

    txt_file.write("\nCounty Votes:\n")

    # Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # Retrieve the county vote count.
        votes = county_votes[county_name]
        # Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print the county results to the terminal.
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n"
        )

        print(county_results)
        # Save the county votes to a text file.
        txt_file.write(county_results)
        # Write an if statement to determine the highest turnout county and get its vote count.
        if (votes > highest_county_vote_count) and (vote_percentage > highest_county_turnout):
            highest_vote_count = votes
            highest_turnout_county = county_name
            highest_county_turnout = vote_percentage

    county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {highest_turnout_county}\n"
        f"-------------------------\n")

    # Print the county with the largest turnout to the terminal.
    print(county_summary)

    # Save the county with the largest turnout to a text file.
    txt_file.write(county_summary)

    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)