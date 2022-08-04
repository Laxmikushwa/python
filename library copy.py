fine=int(input("enter the fine="))
expectedday=int(input("enter the expectedday="))
returnedday=int(input("enter the returnedday="))
days=expectedday-returnedday
days=returnedday-expectedday
if returnedday<expectedday:
    print("no fine")
else:
    print(fine*days)
expectedmonth=int(input("enter the expectedmonth="))
returnedmonth=int(input("enter the returnedmonth="))
month=12
month=expectedmonth-returnedmonth
month=returnedmonth-expectedmonth
if returnedmonth<expectedmonth:
    print("no fine")
else:
    print(fine*month)
fine=10000
expectedyear=int(input("enter the expectdyear"))
returnedyear=int(input("enter the returnedyear"))
year=expectedyear-returnedyear
year=returnedyear-expectedyear
if returnedyear<expectedyear:
    print("no fine")
else:
    print(fine*year)


