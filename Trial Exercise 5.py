largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        inum=int(num)
        if largest is None:
            largest = inum
        elif num > largest:
            largest = inum
        if smallest is None:
            smallest = inum
        elif num < smallest:
            smallest = inum
        print("Maximum", largest)
        print("Minimum", smallest)
        
    except ValueError:
        print("invalid input")
        continue
    

    print("Maximum", largest)
    print("Minimum", smallest)