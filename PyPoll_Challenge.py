import csv
import os

file_to_load = "C:/Users/tucke/Desktop/Data Analysis Bootcamp/Election_Analysis/resources/election_results.csv"
file_to_save = "C:/Users/tucke/Desktop/Data Analysis Bootcamp/Election_Analysis/analysis/election_analysis.txt"

total_votes = 0

candidate_options = []
candidate_votes = {}

county_options = []
county_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

largest_county = ""
voter_turnout = 0


with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        county_name = row[1]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    for county_name in county_votes:
        number_of_votes = county_votes.get(county_name)
        percent_votes = float(number_of_votes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {percent_votes:.1f}% ({number_of_votes:,})\n"
        )
        print(county_results)

        txt_file.write(county_results)

        if (number_of_votes > voter_turnout):
            voter_turnout = number_of_votes
            largest_county = county_name
            winning_percent_count = percent_votes
    county_winner = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        #f"Winning Vote Count: {voter_turnout:,}\n"
        #f"Winning Percentage: {winning_percent_count:.1f}%\n"
        f"-------------------------\n")
    print(county_winner)

    txt_file.write(county_winner)
    
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

