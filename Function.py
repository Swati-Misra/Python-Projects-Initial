def computepay(h, r):
    if h<=40:
        pay = h * r
    else:
        reghrs=40
        remhours= h-40
        ratenew= r*1.5
        newpay=remhours*ratenew
        pay=(reghrs*r)+ newpay
        return pay

hrs = float(input("Enter Hours: "))
rate = float(input ("Enter Rate Per Hour: "))
p = computepay(hrs, rate)
print("Pay", p)