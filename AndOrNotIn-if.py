a = -1
b = -5

# using and
if(a>b and a>0):
    print("Level 1 pass")
else:
    print("Level 1 failed")

# using or
if(a>b or a>0):
    print("Level 1 pass")
else:
    print("Level 1 failed")
    
# using not
if(not (a>b)):
    print("Level 1 pass")
else:
    print("Level 1 failed")