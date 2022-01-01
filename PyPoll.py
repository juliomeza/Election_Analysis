import csv
import os

# The data we need to retrieve.

# Source Data Path/Filename
file_to_load = os.path.join('Resources', 'election_results.csv')

# Write to File Path/Filename
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Open the file in read mode
with open(file_to_load) as election_data:
    print(election_data)

# Open the file to write data
with open(file_to_save, 'w') as txt_file:
    txt_file.write('Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson')



# 1. The total number of votes
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

