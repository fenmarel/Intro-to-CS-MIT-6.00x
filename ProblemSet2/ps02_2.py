'''
Created on Oct 7, 2012

@author: Jon
'''
balance = 3926
annualInterestRate = 0.20

#paste below this line

minPay = 0
newbalance = 1

while newbalance > 0:
    minPay += 10
    newbalance = balance
    for i in range(12):
        newbalance = (newbalance - minPay) * (1+annualInterestRate/12)

print 'Lowest Payment: ' + str(minPay)