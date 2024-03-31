# Python Program to Find the Factorial of a Number
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
num=int(input("Enter a number: "))
result=factorial(num)
print(f"The factorial of {num} is {result}.")

# Python Program to Print the Fibonacci sequence.
# 0 1 1 2 3 5 8
a=0
b=1
count=0
num=int(input("Enter a number:"))
print("The fibonacci series is-")
while count<num:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    count+=1
    
# Python Program to Convert Decimal to Binary, Octal and Hexadecimal
decimal=int(input("Enter a decimal number: "))
binary=bin(decimal)
octal=oct(decimal)
hexa=hex(decimal)
print(f"{decimal} in binary is {binary}")
print(f"{decimal} in octal is {octal}")
print(f"{decimal} in hexadecimal is {hexa}")