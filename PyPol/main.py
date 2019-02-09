import os
import csv
import sys

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "election_data.csv")

# Export the summary into a text file
sys.stdout = open('PyPoll_Summary.txt', 'w')

# Define the lists that we will use
Candidates_list=[]
Count_votes_per_candidate=[]
Total_candidates_list=[]
Unique_candidates_list=[]
#Votes_list=[]

# Read using CSV module
with open(csvpath, newline='', encoding="utf8") as election_data:
   csvreader = csv.reader(election_data, delimiter=',')

   # Skip the header
   header = next(csvreader)

    #let use the same loop to get the Votes_list and the and the Total_candidates_list
   for row in csvreader:
       # Create the list of all candidates
       Total_candidates_list.append(row[2])
       # Calculate the length of the Total_candidates_list to get the total of Votes 
       length = str(len(Total_candidates_list))
       # also you can create a list named Votes_list and on this loop get the info. but the candidates row has the count
       # as row[0] so for this step is the same use this row to get the length.
       # Votes_list.append(row[0])
       # length = str(len(Votes_list))

   # we will need to get a list of unique candidates,
   # la lista que tenemos de candidatos repite varias veces a los mismos,
   # para poder saber cuantos votos tenemos por candidato necesitamos una lista en donde ellos no se repitan:

   for i in Total_candidates_list:
       if i not in Unique_candidates_list:
           Unique_candidates_list.append(i)

   # Obtain total count of each candidate, with comprehension list method.
   # also you can use for.
   comprehension_list_total_count = [[x,Total_candidates_list.count(x)] for x in set(Total_candidates_list)]

   # Create a dictionary with the comprehension list
   summary_total_candidates = dict((x,Total_candidates_list.count(x)) for x in set(Total_candidates_list))

   # Obtain keys and values from the dictionary
   for key in summary_total_candidates:
       keys = key
   for value in summary_total_candidates.items():
       values = value

   # To obtain the winner we need to know the one that recevied more votes
   # Create a list of candidates and another for the votes. We will use the index of the maximum value in the votes list so we can apply this in the candidates list to know the winner's name
   for row in comprehension_list_total_count:
      Candidates_list.append(row[0])
      Count_votes_per_candidate.append(int(row[1]))

   # Obtain the max value of the list of votes.
   max_increase_value = max(Count_votes_per_candidate)
   max_increase_value_index = Count_votes_per_candidate.index(max_increase_value)
   winner = Candidates_list[max_increase_value_index]

# Print the Summary in an external text file called "PyPoll_Summary.txt" 
print(" ")
print("Election Results")
print("-----------------------")
print(f"Total votes: {length}")
print("-----------------------")

for key, value in summary_total_candidates.items():
   print(f"{key}: {round((int(value)/int(length))*100),3}% ({value})")
print("-----------------------")
print(f"Winner: {winner}")

# Print the Summary in the interactive shell
print(" ",file = sys.stderr)
print("Election Results",file = sys.stderr)
print("-----------------------",file = sys.stderr)
print(f"Total votes: {length}",file = sys.stderr)
print("-----------------------",file = sys.stderr)

for key, value in summary_total_candidates.items():
   print(f"{key}: {round(((int(value)/int(length))*100),1)}% ({value})",file = sys.stderr)
print("-----------------------",file = sys.stderr)
print(f"Winner: {winner}",file = sys.stderr)