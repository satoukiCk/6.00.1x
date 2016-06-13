balance = 4773
annualInterestRate = 0.2

Btemp = balance
monthlyInterestRate = annualInterestRate / 12
c = 0
while(True):
    c+=1
    fixedPayment = c * 10
    for i in range(1,13):
        monthlyUnpaidBalance = balance - fixedPayment
        balance =  monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    if (balance <=0):
        print "Lowest Payment: ",fixedPayment
        break
    else:
        balance = Btemp

