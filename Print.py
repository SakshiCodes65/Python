# int
x = 45
# float
y = 45.2
# string
z = 'sakshi'
m = "himani"

# diff between print() and print("")
print("x")
print(x)

print(y)
print(z)
print(m)

# multi value assignment
v, a, b = 23, 34, 45
print(v)
print(a)
print(b)

# knowing the type of variable
print(type(x))
print(type(y))
print(type(z))

# typecasting a variable here we are typecasting an integer 45 to string "45"
word = str(45)
print(type(word))

# how to print multi values in single line using ,
print(x,y)
print(y,z)
#plus value in both numeric value will add them
print(x+y)
# print(y+z) this will give you an error because number cant be added in a string
print(z+m)  #this will concatenate them
print(z+" "+m)  #this will concatenate them with a space
