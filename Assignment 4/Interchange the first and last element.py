# Given a list [12,35,9,56,34] , interchange first and last element in the list


thislist = ['12','35','9','56','34']

#change first and last element
temp = thislist[0]
thislist[0] = thislist[4]
thislist[4]= temp

#Print The NewList
print(thislist)
