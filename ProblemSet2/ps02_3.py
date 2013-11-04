'''
Created on Oct 7, 2012

@author: Jon
'''
balance = 999999
annualInterestRate = 0.18

#paste below this line

minPay = 0
newbalance = 1
low = balance / 12
high = balance * ((1 + annualInterestRate)**12 / 12)

while abs(newbalance) > 0.01:
    minPay = (low + high) / 2.0
    newbalance = balance
    for i in range(12):
        newbalance = (newbalance - minPay) * (1+annualInterestRate/12)
    if newbalance > 0:
        low = minPay
    elif newbalance < 0:
        high = minPay

print 'Lowest Payment: ' + str(round(minPay, 2))