balance = 999999
annualInterestRate = 0.18
# T.T confused and referred to someone else's code
BTemp = balance
monthlyInterestRate = annualInterestRate / 12
LowerBound = balance / 12
UpperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0

MonthlyPayment = 0
while abs(balance) >= 0.01:
    balance = BTemp
    MonthlyPayment = (LowerBound + UpperBound) / 2
    for i in range(1, 13):
        monthlyUnpaidBalance = balance - MonthlyPayment
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    if(balance > 0):
        LowerBound = MonthlyPayment
    else:
        UpperBound = MonthlyPayment


print "Lowest Payment: ", round(MonthlyPayment,2)
