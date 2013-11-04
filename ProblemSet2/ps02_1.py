'''
Created on Oct 7, 2012

@author: Jon
'''
balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

#paste below this line

totalPay = 0

for i in range(12):
    print 'Month: ' + str(i + 1)
    minPay = monthlyPaymentRate * balance
    print 'Minimum monthly payment: ' + str(round(minPay, 2))
    balance = (balance - minPay) * (1+annualInterestRate/12)
    print 'Remaining balance: ' + str(round(balance, 2))
    totalPay += minPay
    
print 'Total Paid: ' + str(round(totalPay, 2))
print 'Remaining balance: ' + str(round(balance, 2))