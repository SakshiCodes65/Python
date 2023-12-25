# lambda Arguements : Expression

sum = lambda x : x+5
print(sum(3))

mul = lambda x,y : x*y
print(mul(4,5))



def plus(x):
    return lambda y : x+y

ans = plus(6)  # lambda y : 6 + y

print(ans(5))