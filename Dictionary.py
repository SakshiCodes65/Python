# ordered
# changeable
# no duplicates (in terms of key)

myDict = {"Key":"Value" , "Name":"Sakshi" , "Age":19 , "DOB":2004 , "DOB" : 2005 , "DOB2" : 2005}
print(type(myDict))
print(myDict)
print(len(myDict))

print(myDict["Name"])  # error if doesnt exist
print(myDict.get("Sakshi")) # returns none if doesnt exist
print(myDict.keys())
print(myDict.values())
print(myDict.items())

myDict["Name"] = "Sakshi goyal"
myDict["Channel Name"] = "SakshiCodes"
myDict.update({"Age" : 20})
myDict.pop("DOB2")
# X = myDict.popitem()  # removes latest added element or any item 
# print(X)
# myDict.clear()
# del myDict
print(myDict)

newDict = myDict.copy()
print(newDict)

