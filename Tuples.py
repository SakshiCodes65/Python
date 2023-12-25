# list is mutable (changes kr skte hai)
# tuple is ordered and unchangeable 
# different datatypes are allowed in tuple
myTuple = ("India" , "Russia" , "Pakistan", "India",43)
print(type(myTuple))
print(myTuple)
print("Positive indexing")
print(myTuple[0])
print(myTuple[1])
print(myTuple[2])
print(myTuple[3])
print("Negative indexing")
print(myTuple[-1])
print(myTuple[-2])
print(myTuple[-3])
print(myTuple[-4])
print("Slicing")
print(myTuple[1:3])
print(myTuple[:3])
print(myTuple[2:])
print("length of tuple")
print(len(myTuple))

newTuple = ("India")
print(type(newTuple))

newTuple = ("India",)
print(type(newTuple))

# myTuple = ("India" , "Russia" , "Pakistan", "India",43)

# myTuple[3] = "China"
# print(myTuple)

newList = list(myTuple)
newList[3] = "China"  # insert
newList.append("Bhutan")   #append
newList.remove(43)    #remove
myTuple = tuple(newList)
print(myTuple)
# del myTuple
# print(myTuple)

t1 = ("India", "Pakistan","India")
t2 = ("Russia", "China")
t1 += t2   # t1 = t1+t2
print(t1)

print(t1.count("China"))

# (c1,c2,c3)=("America", "Bangladesh", "Sri Lanka")
countries = ("America", "Bangladesh", "Sri Lanka","Pakistan","Japan")
(c1,c2,*c3) = countries
print(c1)
print(c2)
print(c3)

new = countries*2
print(new)