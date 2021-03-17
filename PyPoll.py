# the data we need to retrieve
#1. the total number of votes cast
#2. a complete list of canidates who recieved votes
#3. the percentage of votes each canidate won
#4. the total number of of votes each canidate won
#5. the winner of the election based on popular vote

import csv
import os
#assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#create a filename valriable to a direct or indirect path to the the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as election_data:
    #read th file object with the reader function
    file_reader = csv.reader(election_data)
    #print the header row
    headers = next(file_reader)
    print(headers)
#close the file
election_data.close()

#using the with statement open the file as a text file

with open(file_to_save, "w") as txt_file:
    #write some data to the file
    #txt_file.write("Hello World")
    txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")
#close the file
txt_file.close()


