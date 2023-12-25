myList = ["India" , "Qatar" , "Australia", "Russia", "Japan", 45, 42.5, True , "India"]
# can assign multiple datatype in single list
# changes can be done in a list
# repeating elements is allowed
print(type(myList))
print(myList)
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[3])
print(myList[4])
print(myList[5])
print(myList[6])
print(myList[7])
# print(myList[8])

print(myList[1:4])
print(myList[:4])
print(myList[3:])

myList[2] = "China"
print(myList)

myList[5:] = ["Sri Lanka" , "Bhutan" , "Pakistan"]
print(myList)

myList[1:2] = ["Bangladesh" , "Russia", "Punjab"]
print(myList)

myList[1:3] = ["Asia"]
print(myList)


print(len(myList))

myList.insert(3,"Thailand")
print(myList)
myList.append("Switzerland")
print(myList)
herlist = ["apple", "banana", "Guava", "kiwi"]
myList.extend(herlist)
print()
print(myList)
myList.remove("Punjab")
print(myList)
myList.pop(1)
print(myList)
del myList[-1]
print(myList)
print()
print()

# descending
myList.sort(reverse = True)
print(myList)

# ascending
myList.sort()
print(myList)

myList.reverse()
print(myList)

newList = list(myList)
print(newList)

l3 = myList + herlist
print(l3)

# elements are removed but there is still existence of list
myList.clear()
print(myList)

# existence hi khtm ho gyi 
del myList
print(myList)