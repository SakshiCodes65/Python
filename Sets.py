# Unordered
# No duplicates
# Unindexed
# different datatypes
# Unchangeable  (can add and remove but cant assign)
mySet = {"Apple" ,  True, 1, "Banana" , "Apple" , 43 , 65.23, 0 , False}
print(type(mySet))
print(mySet)
# print(mySet[0])
print(len(mySet))
newSet = set(("Apple","Banana","Guava"))
print(newSet)

mySet.add("Kiwi")
print(mySet)

set1 = {"India" , "Pakistan"}
set2 = {"Qatar" , "China"}
set1.update(set2)  # update me list tuple dictionary set kuch b add kr skte ho
print(set1)

# donot throws error
# mySet.discard("India")
# print(mySet)

# Throws an error when no matching element found
# mySet.remove("India") 
# print(mySet)

x = mySet.pop()
print(mySet)
print(x)

mySet.clear()
print(mySet)

# del mySet
# print(mySet)

s1 = {1,2,3,4,4}
s2 = {3,4,5,6,6}
s3 = s1.union(s2)  # koi b element 2 bar print ni hoga
print(s3)

s4 = s1.intersection(s2)  # jitne common elements the dono sets me sirf whi print krega
print(s4)

s1.intersection_update(s2)
print(s1)

t1 = {9,8,7,6}
t2 = {7,6,5,4}
z = t1.symmetric_difference(t2)  # prints olny and only uncommon elements || removes common elements
print(z)

t1.symmetric_difference_update(t2)
print(t1)