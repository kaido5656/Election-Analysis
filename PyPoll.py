# the data we need to retrieve
#1. the total number of votes cast
#2. a complete list of canidates who recieved votes
#3. the percentage of votes each canidate won
#4. the total number of of votes each canidate won
#5. the winner of the election based on popular vote

import csv
import os
#assign a variable for the load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1initialize a total vote counter
total_votes = 0

#canidate options and votes
canidate_options = []
canidate_votes = {}

#winning canidate and winning count tracker
winning_canidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:
    #read th file object with the reader function
    file_reader = csv.reader(election_data)
    
    #read the header row
    headers = next(file_reader)
    
    #print each row in csv file
    for row in file_reader:
        #2 add to the total vote count
        total_votes += 1


        canidate_name = row[2]

        #if the canidate does not match any existing canidate..
        if canidate_name not in canidate_options:
        #add it to the list of canidates               
             canidate_options.append(canidate_name)

         #begin tracking each canidates vote count
             canidate_votes[canidate_name] = 0
        
        #add a vote to that canidate's coount
        canidate_votes[canidate_name] += 1
    #determine the percentage of votes for each canidate by looping through the counts
    #iterate through the canidate list
    for canidate_name in canidate_votes:

        #retreive vote count of a canidate
        votes = canidate_votes[canidate_name]
        #calculate the percent of votes
        vote_percentage = float(votes) / float(total_votes) *100
        #print the canidate name and percentage of votes
        
        print(f"{canidate_name}: {vote_percentage:.1f}%  ({votes:,})\n")

        #determine winning vote count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winningcount = votes and winningpercent = vote percent
            winning_count = votes
            winning_percentage = vote_percentage
            #and set the winning canidate equal to the canidates name
            winning_canidate = canidate_name

    winning_canidate_summary = (
            f"------------------------\n"
            f"Winner: {winning_canidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"winning Percentage: {winning_percentage:.1f}%\n"
            f"------------------------\n" )
    print(winning_canidate_summary)
#print total votes and canidate list

#print(canidate_votes)
#print(canidate_options)
#print(total_votes)
election_data.close()

#using the with statement open the file as a text file

with open(file_to_save, "w") as txt_file:
    #write some data to the file
    #txt_file.write("Hello World")
    txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")
#close the file
txt_file.close()


