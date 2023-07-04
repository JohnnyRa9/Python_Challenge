import os
import csv

vote_counter = 0
candidate_count = {}
Number = 41/100
Election_Result =f"{Number:.0%}"

Election_data = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

#Total number of Votes
with open(Election_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        print(f"\nElection Results\n----------------------------------\n")
        for row in csvreader:
                vote_counter += 1        
        print(f"\nTotal Votes: {vote_counter}\n----------------------------------\n")

#Election results and candidate votes
with open(Election_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        for ID, county, candidate in csvreader:
            if candidate not in candidate_count:
                candidate_count[candidate] = 0
            candidate_count[candidate] += 1

        for candidate, votes in sorted(candidate_count.items(), key=lambda kv: kv[1]):
            Election_Result = (candidate, "{:.2%}".format(candidate_count[candidate] / vote_counter),candidate_count[candidate]) 
            print(Election_Result)

#Winner of the election
winner = max(candidate_count, key=candidate_count.get)

print(f"\n-----------------------\nWinner: {(winner)}!\n-----------------------\n")

#Print output to a text file
output_path = os.path.join("..", 'PyPoll', 'Resources', 'Clean Election Results.txt')
with open(output_path, 'w') as txtfile:
        txtfile.write(f"\nElection Results\n----------------------------------\n")
        txtfile.write(f"\nTotal Votes: {vote_counter}\n----------------------------------\n")
        txtfile.write(f"{Election_Result}")
        txtfile.write(f"\n-----------------------\nWinner: {(winner)}!\n-----------------------\n")