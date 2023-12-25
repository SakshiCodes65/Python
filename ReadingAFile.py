file = open("Read.txt", "r")
# in read mode: file exist --> open
# in read mode: file donot exist --> error

print(file.read())
print(file.read(3)) 
print(file.readline())
print(file.readline())

for x in file:
    print(x)

print(file.readlines())

file.close()