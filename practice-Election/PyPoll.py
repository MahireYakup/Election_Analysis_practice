# Open the data file.
import csv
from email import header
import os
#from pathlib import Path 
#election_data=Path("election_results.csv")
#with open("election_data", 'r') as electiondatafile:
    #electiondatareader= csv.reader(electiondatafile, delimiter=',')
    #print(electiondatareader[10])
    #print(election_data.mode)
file_to_load=os.path.join("Resources","election_results.csv")
with open(file_to_load) as election_data_file:
    print(election_data_file)
file_to_save=os.path.join("Analysis","election_data_analysis.txt")
with open(file_to_save, 'w') as election_data_analysis:
    election_data_analysis=open(file_to_save, 'w')
    election_data_analysis.write("Arapahoe, ")
    election_data_analysis.write("Denver, ")
    election_data_analysis.write("Jefferson")
    election_data_analysis.write("\n-------\n")
    election_data_analysis.write("Arapahoe1, Denver1, Jefferson1\n")
    election_data_analysis.write("Arapahoe\n Denver\n Jefferson\n")
    
    #print(election_data_analysis)
with open(file_to_load) as election_data_file:
    print(election_data_file)
    file_reader=csv.reader(election_data_file)
    #for row in file_reader:
            #print(len(row))
    headers=next(file_reader)
    print(headers)
    election_data_file.close()

# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.