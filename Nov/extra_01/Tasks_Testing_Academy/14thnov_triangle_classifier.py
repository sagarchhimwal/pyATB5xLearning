# Triangle classifier

int1 = int(input("Enter number 1: "))
int2 = int(input("Enter number 2: "))
int3 = int(input("Enter number 3: "))

if int1 == int2 == int3:
    print("Triangle is equilateral")
elif int1 == int2 or int2 == int3 or int1 == int3 :
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")

