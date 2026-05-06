Pyroom Playground — Online Python IDE.thislist = [1,2,3,4,5,6,7,8,9]

# slices
print(thislist[0])
print(thislist[1])
print(thislist[-1])
print(thislist[-2])
print(thislist[:2])
print(thislist[2:])
print(thislist[1:3])
print(thislist[::2])

# length
print(len(thislist))

# in list
print(1 in thislist)
print(0 in thislist)

# change value
thislist[0] = 99
print(thislist)

# insert
thislist.insert(0, 55)
print(thislist)

# append
thislist.append(33)
print(thislist)

#extend
newlist = [12,13,14]
thislist.extend(newlist)
print(thislist)

#remove
thislist.remove(33)
print(thislist)

mainlist = [0,1,2,3,4,5,6,7,8,9]
#pop
popped = mainlist.pop(1)
print(popped)
print(mainlist)

mainlist.pop(1)
print(mainlist)

#sort
mainlist.sort()
print(mainlist)

#reverse
mainlist.reverse()
print(mainlist)

#copy
copylist = mainlist.copy()
print(copylist)

#clear
mainlist.clear()
print(mainlist)

#join
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)

#multiply
list4 = list1 * 3
print(list4)

#range
list5 = list(range(1,10))
print(list5)

#list comprehension
list6 = [num for num in range(1,10)]
print(list6)

#list comprehension with condition
list7 = [num for num in range(1,10) if num % 2 == 0]
print(list7)

#list comprehension with condition
list8 = [num for num in range(1,10) if num % 2 != 0]
print(list8)

#list comprehension with condition
list9 = [num for num in range(1,10) if num % 2 == 0]
print(list9)

#list comprehension with condition
list10 = [num for num in range(1,10) if num % 2 != 0]
print(list10)

#list comprehension with condition
list11 = [num for num in range(1,10) if num % 2 == 0]
print(list11)



