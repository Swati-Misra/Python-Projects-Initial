num=0
tot=0
while True :
    sval=input("Enter a number: ")
    if sval=="done":
        break
    try:
        fval=float(sval)
    except:
        print("invalid input")
        continue
   #print(fval)
    num=num+1
    tot=tot+fval
#print("all done")
print(tot,num,tot/num)