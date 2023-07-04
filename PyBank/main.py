import os
import csv

#List to store values
Months_counter = 0
minVal = [] 
maxVal = []
xs = []

Budget_data = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#Total number of months
with open(Budget_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        print(f"\nFinancial Analysis\n----------------------------------\n")
        for row in csvreader:
                Months_counter += 1        
        print(f"Total Months: {Months_counter}")

#Net total of Profit/Losses over entire period
with open(Budget_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        Net_total = sum(float(row[1]) for row in csvreader)
        print (f"Total: ${Net_total}")

#getting the month with the maximum increase
with open(Budget_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        for row in csvreader:
                maxVal = max(csvreader, key=lambda row: int(row[1]))
        print(f"The greatest increase is: {maxVal}")

#getting the month with the maximum decrease
with open(Budget_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        minVal = min(csvreader, key=lambda row: int(row[1]))
        print(f"The greatest decrease is: {minVal}")

#Calculating the average
with open(Budget_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)        
        for row in csvreader:
                x = int(row[1])
                xs.append(x)
        Average = round(sum(xs) / len(xs))
        print(f"Average Change: {Average}")

output_path = os.path.join("..", 'PyBank', 'Resources', 'Clean budget.txt')
with open(output_path, 'w') as txtfile:
        txtfile.write(f"\nFinancial Analysis\n----------------------------------\n")
        txtfile.write(f"\nTotal Months: {Months_counter}\n")
        txtfile.write(f"\nTotal: ${Net_total}\n")
        txtfile.write(f"\nThe greatest increase is: {maxVal}\n")
        txtfile.write(f"\nThe greatest decrease is: {minVal}\n")
        txtfile.write(f"\nAverage Change: {Average}\n")
