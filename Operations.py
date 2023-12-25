x = 45
y = 5
# simple arithmetic operation
print("Arithmetic operation")
print(x+y)  # 50
print(x-y)  # 40
print(x*y)  # 225
print(x**y) # 184528125
print(x%y)  # 0 (remainder)
print(x/y)  # 9.45 (Quotient)
print(x//y) # 9 

print("Assignement operator")
#assignement operator
a = 5  
print(a)
a += 100 # a = a+100
print(a)
a -= 100 # a = a+100
a *= 100 # a = a*100
a /= 100 # a = a/100

print("Comparison operator")
print(2==2)
print(2==4)
print(2>4)
print(2>=4)
print(2<4)
print(2<=4)
print(2!=3)

print("Logical Operator")
# and or not
print(4>2 and 10>1)   # (T and T)  --> T
print(14>2 and 1>10)  # (T and F)  --> F
print(3>7 and 10<2)   # (F and F)  --> F

print(4>2 or 10>1)   # (T or T)  --> T
print(14>2 or 1>10)  # (T or F)  --> T
print(3>7 or 10<2)   # (F or F)  --> F

print(not(10>5))

print()

a = 5
b = 5
c = 10

print(a is b)  # True 
print(a is not c) # True
print(a is not b) # False

y = "Hey there i am using whatsapp"
z = "sakshi"
k = "am"
print(z in y)  # False
print(k in y)  # True
