# Exercise 2: Print the Sum of a Current Number and a Previous number
# Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.


sum=0
crnt_num=0
prev_num=0
for i in range (0,11):
    sum+=i
    crnt_num=i
    print('current number :',crnt_num,'previous number :',prev_num,'sum :',sum)
    prev_num=i