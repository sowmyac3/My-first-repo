#Write a python program to find sum of squares of N natural numbers

n = int(input("please enter a natural number = "))
# Define My Function
def sumsquares(n) : 
   #"Iterate i from 1 and n finding square of i and add to sum" -  
    sum = 0
    for i in range(1, n+1): 
        sum = sum + (i * i) 
    return sum
print(sumsquares(n))
