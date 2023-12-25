def func():
    print("This is a function call")

func()
print("Hey")
func()
func()
func()
func()



def sum(x,y):
    print("Sum is : "+ str(x+y))

sum(4,3)
sum(100,299)
sum(100,29)
sum(10,29)



def Intro(name="None"):
    # name = "sakshi"
    print("My name is : "+name)
    
Intro("Sakshi")
Intro("Himani")
Intro()



def func(names):
    for x in names:
        print(x)

names = ["Sakshi","Himani","Neha"]
func(names)



def sum(x,y):
    return x+y

print(sum(4,3))
print(sum(100,299))
print(sum(100,29))
print(sum(10,56))



def family(**members):
    print("Name of father is : "+ members["father"])

family(mother="Ramesh",father="Kumesh")



def family(*members):
    print("4th member of this family is : "+ members[3])

family("beta","father","mother","behn","chachu","chachi")

