#!/usr/bin/env python
# coding: utf-8

# In[32]:


import csv
import os

# Loading files and setting the outputs 

file_to_load = os.path.join(".", "Resources", "budget_data.csv")

file_to_output = os.path.join(".", "budget_analysis.txt")

total_months = 0
total_net = 0
net_change_list = []
greatest = ["", 0]
least = ["", 99999999999999]


# Read the csv & convert to a list
with open(file_to_load) as financial_data:
    
    reader = csv.reader(financial_data)
    
    #Header row
    
    header = next(reader)
    
    first_row = next(reader)
    
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    total_months += 1
    
    
    for row in reader:
        
        #Calculate the total
        total_months += 1
        total_net += int(row[1])
        
        
        #Net Change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        
        
        #Calculate the greatest increase
        if(net_change > greatest[1]):
            greatest[0] = row[0]
            greatest[1] = net_change
        
        
        #Calculate the greatest decrease
        if(net_change < least[1]):
            least[0] = row[0]
            least[1] = net_change
        
        
net_monthly_average = sum(net_change_list)/ len(net_change_list)      
        
    
output = (
    f"Financial Analysis\n"
    f"------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change ${net_monthly_average:.2f}\n"
    f"Greatest Increase in Profits: {greatest[0]} (${greatest[1]})\n"
    f"Greatest Decrease in Profits: {least[0]} (${least[1]})\n" 
    
)

print(output)
    
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
    
   
 


# In[ ]:




