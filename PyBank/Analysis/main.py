#Importing dependancies
import csv
import os
import statistics as st  

# Function Definition
def Average(list):

   
    return round(st.mean(list), 2) 

# --- define relative path for the input and output files ---
inputfile = os.path.join(r"C:\Users\Robert Odhiambo\OneDrive\Desktop\python-challenge\PyBank\Resources\budget_data.csv")
outputfile = os.path.join(r"C:\Users\Robert Odhiambo\OneDrive\Desktop\python-challenge\PyBank\Analysis\.txt")
# Develop Lists
Dates = []
Profit_Loss = []
Profit_LossChanges = []

# Use the Lists to store values
with open(inputfile, 'r') as budget_data:
    reader = csv.reader(budget_data, delimiter=",")
    
    # Listing for Headers
    Headers = next(reader)

    # Using append
    for row in reader:
        Dates.append(row[0])
        Profit_Loss.append(int(row[1]))

#   Loop Usage
total_Profit_Loss = 0
for i in Profit_Loss:
    total_Profit_Loss = i + total_Profit_Loss

# New List creation
Profit_Loss_Changes = [Profit_Loss[i+1] - Profit_Loss[i] for i in range(0,len(Profit_Loss)-1)]

# Average function usage
AverageChange = Average(Profit_Loss_Changes)

# Zero value creation
Profit_Loss_Changes.insert(0,0)

# Greatest Increase or Decrease values asssignment
Greatest_Increase = 0
Greatest_Decrease = 0
# for loop usage
for i in range(len(Profit_Loss_Changes)-1):
    if Profit_Loss_Changes[i] < Greatest_Decrease:
        Greatest_Decrease = Profit_Loss_Changes[i]

    if Profit_Loss_Changes[i] > Greatest_Increase:
        Greatest_Increase = Profit_Loss_Changes[i]   


#  changes
GI_index = Profit_Loss_Changes.index(Greatest_Increase)
GD_index = Profit_Loss_Changes.index(Greatest_Decrease)

# dates
GI_date = Dates[GI_index]
GD_date = Dates[GD_index]
# Output
Analysis_Output = (f"Financial Analysis\n"
                  f"----------------------------\n"
                  f"Total Months: {len(Dates)}\n"
                  f"Total: ${total_Profit_Loss}\n"
                  f"Average Change: ${AverageChange}\n"
                  f"Greatest Increase in Profits: {GI_date} (${Greatest_Increase})\n"
                  f"Greatest Decrease in Profits: {GD_date} (${Greatest_Decrease})\n"
)

#Out print
print(Analysis_Output)

# Analysis Output
with open(outputfile, 'w') as textfile:
    textfile.write(Analysis_Output)