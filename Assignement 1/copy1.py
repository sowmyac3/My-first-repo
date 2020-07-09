#Python Program To Find The Factorial Of A Number provided by the user

# To take input from the user
num = int(input("Enter a number:    "))
factorial = 1
#Check if the number is positive, negative, and zero
#Note:(negative number's do not have factorial)
#Note: The factorial of 0 is always 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range (1, num + 1):
        factorial = factorial*i
    print("The factorial of" + " " + str(num) + " is " + str(factorial))
