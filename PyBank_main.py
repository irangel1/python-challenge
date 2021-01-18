import csv
import os

# path for data
csvpath = os.path.join("python-challenge/PyBank/Resources/budget_data.csv")
csvpath_results = ("python-challenge/PyBank/Analysis/budget_data.txt")

# Variables definition
total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
profit_loss_change = 0
max_increase = ["",0]
max_decrease = ["",9999999]

profit_loss_changes = []

#Open file
with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)

    #loop to find total months and profit losses
    for row in reader:
        total_months = total_months + 1
        total_profit_loss = total_profit_loss + int(row["Profit/Losses"])
        print(row)

        #Check changes
        profit_loss_change = int(row["Profit/Losses"]) - prev_profit_loss
        print(profit_loss_change)

        #Reset the value of prev_profit_loss to the complte row
        prev_profit_loss =int(row["Profit/Losses"])
        print(prev_profit_loss)

        #Find max increase and drecrease
        if (profit_loss_change > max_increase[1]):
            max_increase[1]=profit_loss_change
            max_increase[0]=row["Date"]

        if(profit_loss_change < max_decrease[1]):
            max_decrease[1] = profit_loss_change
            max_decrease[0] = row["Date"]
        
        #Add to the profit_loss_changes list
        profit_loss_changes.append(int(row["Profit/Losses"]))

    #Obtain profit average
    profit_loss_avg = sum(profit_loss_changes)/len(profit_loss_changes)

    #Print results
    print("Financial Analysis")
    print("___________________________")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(total_profit_loss))
    print("Average Change: " + "$" + str(round(profit_loss_avg,2)
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")")
    print("Greatest Decrease: " + str(max_decrease[0] + " ($" + str(max_decrease[1]+ ")")

#Output in txt
with open(csvpath_results,"w") as txt_file:
    text_file.write("Total Months: " + str(total_months))
    txt_file.write("⁄n")
    txt_file.write("Total: " + str(total_profit_loss))
    txt_file.write("⁄n")
    txt_file.write("Average Change: " + profit_loss_avg)
    txt_file.write("⁄n")
    txt_file.write("Greatest Increase: " + str(max_increase[0]) + " ($" + str(max_increase[1)]) + ")")
    txt_file.write("⁄n")
    txt_file.write("Greatest Decrease: " + str(max_decrease[0]) + " ($" + str(max_decrease[1)]) + ")")



