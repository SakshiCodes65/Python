# multiple ways of creating a string
str1 = "sakshi is best"
str2 = 'sakshi is best'
str3 = '''sakshicodes is youtube channel'''

# indexing of a string
x = "hello"
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
# print(x[5])  throws error

# string slicing
y = "sakshiCodes is a youtube channel , Thank you"
print(y[3:6])  # [jahan se start karna hai  : jahan tak chahiye]
print(y[:6])
print(y[6:])
print(y[-5:-2])

print(len(y))
print(y.upper())
print(y)
print(y.lower())
print(y.strip())
y_modified = y.replace("youtube" , "YT")
print(y_modified)
print(y.split(","))
print(y.find("youtube"))
print(y.capitalize())
print(y.count("a"))
print(y.endswith("sakshi"))

x = "Sakshi"
y = "Codes"
print(x+" "+y)

name = "sakshi"
sen = "My name is " + name
print(sen)

name = "sakshi"
city = "patiala"
state = "punjab"
sen = "My name is {} i live in {} that is in {}" 
print(sen.format(name,city,state))
