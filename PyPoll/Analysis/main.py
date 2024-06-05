#Importing dependancies
import csv
import os

# Using 3 decimal points
def fixPercent(num):
    num = "{:.3%}".format(num)
    return num

# Path for data retrieval
inputfile = os.path.join( r"C:\Users\Robert Odhiambo\OneDrive\Desktop\python-challenge\PyPoll\Resources\election_data.csv")
outputfile = os.path.join(r"C:\Users\Robert Odhiambo\OneDrive\Desktop\python-challenge\PyPoll\Analysis\.txt")

# Lists creation
UniqueCandidates = []
VoteCounts = []
VotePercent = []
TotalVotes = 0
WinnerCount = 0

# Reading the file
with open(inputfile, 'r') as electiondata:
    reader = csv.reader(electiondata, delimiter=",")

    # list for headers
    Headers = next(reader)

    # loop statement

    for row in reader:
        TotalVotes += 1
    
        # Applying the if statement to pick candidates appropriately
        if row[2] not in UniqueCandidates:

            #Use of append
            UniqueCandidates.append(row[2])
            VoteCounts.append(1)

        else:

            CandidateIndex = UniqueCandidates.index(row[2])
            VoteCounts[CandidateIndex] += 1
        

# Votes Calculation
for i in range(len(VoteCounts)):
    VotePercent.append(VoteCounts[i] / TotalVotes)

# Basis for the Winner
for i in range(len(VoteCounts)):

    # Votes validation
    if VoteCounts[i] > WinnerCount:
        
        # Further Votes Validation
        WinnerCount = VoteCounts[i]

        #Winner updates
        Winner = UniqueCandidates[i]

#Output
with open(outputfile, 'w') as textfile:
    textfile.write(f"Election Results\n"
                   f"----------------------------\n"
                   f"Total Votes: {TotalVotes}\n"
                   f"----------------------------\n"
                   )

    # Winner loop
    for i in range(len(UniqueCandidates)):
        textfile.write(f"{UniqueCandidates[i]}: {fixPercent(VotePercent[i])} ({VoteCounts[i]})\n")

    textfile.write(f"----------------------------\n"
                   f"Winner: {Winner}\n"
                   f"----------------------------\n"
                  )

# Print out
with open (outputfile, 'r') as analysis:
    contents = analysis.read()
    print(contents)