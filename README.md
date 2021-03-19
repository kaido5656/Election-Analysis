# Election-Analysis
### Overview of the Election Audit
  The purpose for this exercise was to assist Tom and Seth in retrieving voting data from a CSV file using Python. In the original code the data retrieved valuable information regarding each canidates total votes, percentage of votes, total votes cast and ultimatly the winner of the election with regards to the data provided. However, the data was missing some information regarding votes spread by county and their respective percentage of votes cast. To provide more information on the counties, I was tasked with refactoring the code to add more insight to the county data.
  
#### Election-Audit Results :


1. 369,711 votes were cast in this congressional election

2. County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

3. Largest County Turnout : Denver

4. Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
5. Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%

##### The data above was recieved by the following code:
```
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

    #save the results to our text file
    with open(file_to_save, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"------------------------\n"
            f"Total votes :{total_votes:,}\n"
            f"------------------------\n" )
        print(election_results, end="")
        #save the final vote count to the text file
        txt_file.write(election_results)
        #determine the percentage of votes for each canidate by looping through the counts
        #iterate through the canidate list
        for canidate_name in canidate_votes:

            #retreive vote count of a canidate
            votes = canidate_votes[canidate_name]
            #calculate the percent of votes
            vote_percentage = float(votes) / float(total_votes) *100
            #print the canidate name and percentage of votes
            
            canidate_results = (f"{canidate_name}: {vote_percentage:.1f}%  ({votes:,})\n")
            print(canidate_results)
            txt_file.write(canidate_results)
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
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"------------------------\n" )
        print(winning_canidate_summary)
        #saved the winning canidates results to the text file
        txt_file.write(winning_canidate_summary)

```
### Election-Audit Summary
  The above data was gathered using a python script gatering data from a CSV file and with some refactoring could adequately utilized in future elections. The script would be able to pull any number of canidate names, total votes cast, percentage of votes per canidate and county, and much more if needed to be tailored to handle additional data. For example this code could be modified further to provide a spread of canidate votes per county so that each canidate can see how well they faired in any particular county, this data could then be utilized for future campaign efforts. An another example of the above code being formatted for future use could be for a sales like enviroment, in which most of the code would function the same however the variables could be changed to reflect productsbeing tracked and sold.
