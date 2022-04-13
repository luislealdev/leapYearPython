year = int(input("Write the year you want to check: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("It is a leap year")
        else:
            print("It's not a leap year")
    else:
        print("It is a leap year")
else:
    print("It's not a leap year")