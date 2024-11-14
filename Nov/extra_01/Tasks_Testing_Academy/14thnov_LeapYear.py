#Leap Year
# That consist of 366 days



Year = int(input("Enter a year to checkits a leap year or not ? "))

if Year % 400 == 0 or (Year % 4 == 0 and Year % 100 != 0 ):
    print(f'{Year} is a leap year')
else:
    print(f'{Year} is not a leap year')