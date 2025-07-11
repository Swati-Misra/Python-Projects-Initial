# This first line is provided for you

hrs = float(input("Enter Hours:"))
rate = float(input ("Enter Rate Per Hour: "))

if hrs<=40:
    pay = hrs * rate
else:
    reghrs=40
    remhours= hrs-40
    ratenew= rate*1.5
    newpay=remhours*ratenew
    pay=(reghrs*rate)+ newpay

print(pay)
