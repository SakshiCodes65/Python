a = 100
b = -5

# nested if
if(a>b):
    print("Level 1 pass")
    print("A is greater than B")
    if(a>0):
        print("Level 2 pass")
        print("A is greater than 0")
    else:
        print("Level 2 failed")
        print("A is not greater than 0")

