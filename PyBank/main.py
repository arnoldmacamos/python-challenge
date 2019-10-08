"""
PyBank Script
Author:         Arnold Macamos
Date:           October 07, 2019
Description:    This is to analyze the financial records of a company
"""


import os
import csv

filePath = os.path.join("Resources","budget_data.csv")
listBudgetData = []         #to hold the list of the budget data

#read the data into the budgetData dictionary list
with open(filePath) as csvFile:
    reader = csv.DictReader(csvFile)
    prevProfitLoss = 0                           #to keep track of the previous profit/loss to compute for the profit/loss change
    currProfitLoss = 0
    for row in reader:
        budgDate = row["Date"]                   #budget date
        budgProfLoss = int(row["Profit/Losses"]) #profit/losses
        if(prevProfitLoss == 0):
            currProfitLoss = 0
        else:
            currProfitLoss = budgProfLoss
        listBudgetData.append(
            {
                "Date"              : budgDate,
                "ProfitOrLosses"    : budgProfLoss,
                "ProfLossChange"    : (currProfitLoss - prevProfitLoss)
            }
        )
        prevProfitLoss = budgProfLoss

#get the list of values from the budgetData dictionary list
listProfLossesChange = [x["ProfLossChange"] for x in listBudgetData]
listProfLosses = [x["ProfitOrLosses"] for x in listBudgetData]

greatestIncProfLosses = max(listProfLossesChange)
greatestIncDate = [x["Date"] for x in listBudgetData if x["ProfLossChange"] == greatestIncProfLosses][0]

greatestDecProfLosses = min(listProfLossesChange)
greatestDecDate = [x["Date"] for x in listBudgetData if x["ProfLossChange"] == greatestDecProfLosses][0]

totalMonths = len(listProfLosses)
totalProfLosses = sum(listProfLosses)
averageChange = sum(listProfLossesChange)/(totalMonths - 1)

#Display Results
print("Financial Analysis")
print("---------------------------------------")
print(f"Total Months:   {totalMonths}")
print(f"Total:          {totalProfLosses}")
print(f"Average Change: {averageChange}")
print(f"Greatest Increase in Profits: {greatestIncDate} {greatestIncProfLosses}")
print(f"Greatest Decrease in Profits: {greatestDecDate} {greatestDecProfLosses}")
