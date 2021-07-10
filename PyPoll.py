# Data to be retrieved
#1. Total votes cast
#2. Complete list of candidates who received votes
#3. Percentage of votes for each candidate
#4. Total number of votes for each candidate
#5. Winner of election based on popular vote

# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable for the file to save and the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Print the header row.
    headers = next(file_reader)
    print(headers)
