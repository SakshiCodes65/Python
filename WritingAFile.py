file = open("Create.txt", "x")

# in x mode : file exist --> error
# in x mode : file donot exist --> create

file = open("Create.txt", "w")

file.write("This is my first line\n")
file.write("This is my second line\n")

file = open("Create.txt", "a")
file.write("Thank you")  # append mtlb uske age likh dega

file = open("Create.txt","w")
file.write("Empty")  # jitna purana hai sab remove kr dega
file.close()
