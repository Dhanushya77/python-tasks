# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

a=int(input('enter frst number:'))
b=int(input('enter scnd number:'))
sum=a+b
product=a*b
if product<=1000:
    print('product is',product)
else:
    print('sum is ',sum)