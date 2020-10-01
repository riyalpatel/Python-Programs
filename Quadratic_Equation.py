import cmath
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
delta1 = (b**2)-(4*a*c)
ans1 = (-b + cmath.sqrt(delta1))/(2*a)
print(ans1)
