import math

print("Lab 3. Performed by Vlad Kolosov.")
print()

def Task2Fun1(x):
    return x * 2

def Task2Fun2(x):
    return x * 2

def Task2Fun3(x):
    return x / 3

def Task1():
    a = int(input("input a: "))
    b = int(input("input b: "))
    c = int(input("input c: "))

    D = b ** 2 - (4 * a * c)
    if D < 0:
        print("Корней нет")
        return

    res1 = (-b - math.sqrt(D)) / (2 * a)
    res2 = (-b + math.sqrt(D)) / (2 * a)

    print("Первый корень: ", res1)
    print("Второй корень: ", res2)

def Task2():
    a = int(input("input a: "))
    b = int(input("input b: "))
    z = int(input("input z: "))

    x = 0
    if z <= 0:
        x = z ** 2 + 1
    if z > 0:
        x = math.sqrt(z)

    print("Выберете функцию")
    print("1: 2x")
    print("2: x2")
    print("3: x/3")

    f = int(input("input c: "))
    fx = 0
    if f == 1:
        fx = Task2Fun1(x)  
    if f == 2:
        fx = Task2Fun2(x)  
    if f == 3:
        fx = Task2Fun3(x)  
    f1 = (b * fx) / (math.cos(x))
    f2 = a * math.log10(abs(math.tan(x / 2)))
    print("Результат: ", f1 + f2)


print("1: Отсновное задание")
print("2: Индивидуальное задание")

a = int(input("Выберите цифру: "))
if(a == 1):
    Task1()
if(a == 2):
    Task2()
