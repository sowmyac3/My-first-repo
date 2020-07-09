#Given a list [1,5,4,8,11,13,18], print even numbers and their index in the list


#State the list
thislist = [1,5,4,8,11,13,18]

#Setting only index values
thislist.remove(1)
thislist.remove(5)
thislist.remove(11)
thislist.remove(13)

#Setting the index values
x = thislist.index(4)
y = thislist.index(8)
z = thislist.index(18)

#Code that needs to be printed
print("The newlist with even numbers is",thislist)
print( "The index of  4 is",x)
print("The index of 8 is",y)
print("The index of 18 is",z)
