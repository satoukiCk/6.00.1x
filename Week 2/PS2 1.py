monthlyInterestRate = annualInterestRate / 12
TotalPaid = 0
for i in range(1,13):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance =  monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    TotalPaid += minimumMonthlyPayment
    print "Month" , i
    print "Minimum monthly payment: ", round(minimumMonthlyPayment,2)
    print 'Remaining balance: ',round(balance,2)

print "TotalPaid",round(TotalPaid,2)
print "Remaining balance",round(balance,2)
