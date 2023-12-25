i = 1  #initialization is imp
while(i<=10):  # condition is imp
    print(i)
    i = i + 1    # increment / decrement

print()

j = 10
while(j>0):
    print(j) 
    if(j==8):
        break
    j = j - 1 
else:
    print("Process is ended")

print()
j = 11
while(j>0):
    j = j - 1 
    if(j==8):
        continue
    print(j) 
