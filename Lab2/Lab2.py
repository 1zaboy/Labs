import math

print("Lab 2. Performed by Vlad Kolosov.")
print()

#x = input("input x: ")
#y = input("input y: ")
#z = input("input z: ")

x = 182.5
y = 18.225
z = -0.03298

print("X: ", x)
print("Y: ", y)
print("Z: ", z)

f1 = math.fabs(math.pow(x, y/x)-math.pow(y/x,1/3))

f2 = (y-x)*((math.cos(y)-z/(y-x))/(1+math.pow(y-x, 2)))

result = f1 + f2

print("Result: ", result)

