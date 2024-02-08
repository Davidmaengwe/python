temperature = 13
if temperature > 25:
    print("It is hot")
else:
    print("It is not hot")

# A program that returns the largest number among three numbers
num1 = 45
num2 = 56
num3 = 21
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest   number")
else:
    print(num3, "is the smallest number")

# A program that checks whether a number is even or odd
number = 40
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# A program that checks whether a number is a prime or not
n = 1
n1 = 2
n2 = 3

if n < n1 and n < n2:
    print(n, "is not a prime number")
elif n1 > n and n1 > n2:
    print(n2, "is a prime number")
else:
    print(n2, "is a prime number")


num = 29
if num > 3:
    for i in range(2,num):
        if num % i == 0:
           print(num, "is not a prime number")
           break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
