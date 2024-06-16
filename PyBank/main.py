import os
import csv


def fin_analysis(df):
    dates = [str(row[0]) for row in budget_data]
    prof_loss = [int(row[1]) for row in budget_data]

    #total number of months included in the dataset
    count_months = len(dates)

    #net total amount of Profit/Losses over the entire period
    net_PL = sum(prof_loss)
       
    #changes in Profit/Losses over the entire period, and then the average of those changes
    def average(list):
        length = len(list)
        avg = round(sum(list)/length, ndigits=2)
        return avg

    #greatest increase in profits (date and amount) over the entire period
    max_profit = max(prof_loss)
    ind = prof_loss.index(max_profit)
    date_max_prof = dates[ind]
    
    #greatest decrease in profits (date and amount) over the entire period
    min_profit = min(prof_loss)
    ind = prof_loss.index(min_profit)
    date_min_prof = dates[ind]


    #print results to console
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {count_months}")
    print(f"Total: ${net_PL}")
    print(f"Average Change: ${average(prof_loss)}")
    print(f"Greatest Increase in Profits: {date_max_prof} (${max_profit})")
    print(f"Greatest Decrease in Profits: {date_min_prof} (${min_profit})\n\n")


    #define file to write output to
    file1 = open("Output/Financial Analysis.txt", "w")

    #list of strings for output
    L = ["Financial Analysis\n",
         "-------------------------\n",
         f"Total Months: {count_months}\n",
         f"Total: ${net_PL}\n",
         f"Average Change: ${average(prof_loss)}\n",
         f"Greatest Increase in Profits: {date_max_prof} (${max_profit})\n"
         f"Greatest Decrease in Profits: {date_min_prof} (${min_profit})\n",
         "-------------------------"]
    
    #write string to output file
    file1.writelines(L)
    file1.close()

#open election_data.csv file and run fin_analysis() with data
csv_loc = os.path.join('Resources', 'budget_data.csv')

with open(csv_loc) as file:
    reader = csv.reader(file, delimiter=",")
    next(reader, None)  
    
    budget_data = [date for date in reader]
    
    fin_analysis(budget_data)