import os
import csv

def election_results(df):
    ballot_id = [str(row[0]) for row in votes]
    county = [str(row[1]) for row in votes]
    candidate = [str(row[2]) for row in votes]


    #define file to write output to
    file2 = open("Output/Election Results.txt", "w")
    L = ["Election Results\n",
         "-------------------------\n"]
    file2.writelines(L)
    file2.close() 
    
    #print to console
    print("Election Results")
    print("-------------------------")


    #total number of votes cast
    count_votes = len(set(ballot_id))

    #print total votes to console
    print(f"Total Votes: {count_votes}")
    print("-------------------------")

    #add output to Election Results.txt file
    file2 = open("Output/Election Results.txt", "a")
    L = [f"Total Votes: {count_votes}\n",
         "-------------------------\n"]
    file2.writelines(L)
    file2.close()
  
    
    #list of candidates who recieved votes
    candidates = list(set(candidate))

    #calculate percent votes and count of votes for each candidate that received a vote
    percent_votes = []
    count_votes = []    
    for i in range(len(candidates)):
        count = 0

        #total number of votes each candidate won
        for j in range(len(candidate)):
            if candidate[j]==candidates[i]:
                count += 1
        
        #percentage of votes each candidate won
        p_vote = round(count/len(candidate)*100, ndigits = 2)
        
        #add counts and percents to list
        percent_votes.append(p_vote)
        count_votes.append(count)

        #print candidate results to console
        print(f"{candidates[i]}: {p_vote}% ({count})")

        #add output to Election Results.txt file
        file2 = open("Output/Election Results.txt","a")
        file2.write(f"{candidates[i]}: {p_vote}% ({count})\n")
        file2.close()


    #Winner of the election based on popular vote
    id = percent_votes.index(max(percent_votes))
    winner = candidates[id]

    #print winner to console
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    #add output to Election Results.txt file
    file2 = open("Output/Election Results.txt", "a")
    L = ["-------------------------\n",
         f"Winner: {winner}\n",
         "-------------------------\n"]
    file2.writelines(L)
    file2.close()


#open election_data.csv file and run electioin_results() with data
csv_loc = os.path.join('Resources','election_data.csv')

with open(csv_loc) as file:
    reader = csv.reader(file, delimiter=",")
    next(reader, None)

    votes = [row for row in reader]

    election_results(votes)