import math as M

def f(x):
    return M.log(x)

def f1(x):
    return 1/x

def f2(x):
    return -1/x**2

def f3(x):
    return 2/x**3

def f4(x):
    return -6/x**4

def f5(x):
    return 24/x**5


"""MAIN"""



print("valores iniciales")
x0 = 1
x1 = 2.5

y0 = f(x0)

print("x0 =",x0)
print("x1 =",x1)

print("f(x0) = ",y0)
print("f(x1) = ?")

h = x1-x0
print("h =",h)

#SERIE DE TAYLOR
yi = float(y0) #-62

#derivadas de x0
fd = [f1(x0),f2(x0),f3(x0),f4(x0),f5(x0)]

print()
print("#","\t","|","f(x)","\t","|","Rn")
print("-"*30)
for i in range(5):
    Rn = fd[i]*(h**(i+1)/M.factorial(i+1))
    print(i,"\t","|",yi,"\t","|",Rn)
    yi = yi+Rn
    
    

    
