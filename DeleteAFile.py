import os

# if exists--> Delete
# if not --> error

if(os.path.exists("Delete.txt")):
    os.remove("Delete.txt")
    print("File deleted")
else:
    print("File does not exist")