#!/usr/bin/env python
# coding: utf-8

# In[19]:


import csv
import os 


#Loading files and creating variables 

file_to_load = os.path.join(".", "Resources", "election_data.csv")

file_to_output = os.path.join(".", "election_analysis.txt")

total_votes = 0
candidate_votes = {}
candidate_options = []
winning_count = 0
winning_candidate = ""

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    #Reading the Header
    header = next(reader)
    
    
    for row in reader:
        #Adding total votes
        total_votes = total_votes + 1
        
        #Candidate name from rows
        candidate_name = row[2]
        
        
        #Searching for Unique candidates names
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1




        
with open(file_to_output, "w") as txt_file:        
    election_results = (
        f"Election Results\n"
        f"--------------------\n"
        f"Total Votes {total_votes}\n"
        f"--------------------\n"

)

    print(election_results)
    
    txt_file.write(election_results)
    
    #Total votes and percent
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"    
       
        print(voter_output)
        
        txt_file.write(voter_output)
        
    #Winning Candidate    
    winning_candidate_results = (
        f"--------------------\n"
        f"Winner: {winning_candidate}\n"
        f"--------------------\n"
    )
    print(winning_candidate_results)
    
    txt_file.write(winning_candidate_results)
    


# In[ ]:




