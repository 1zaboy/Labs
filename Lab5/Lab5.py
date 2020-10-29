def fibonacci(n):
    if n == 0: return 0
    cur = 1
    if n > 2:
        cur = fibonacci(n-1) + fibonacci(n-2)
    return cur

while True:
    print("----------------------------------------------------------------------------")
    print("1: Output of a specific sequence item")
    print("2: Output all elements of a sequence up to a user-specified element")
    print("3: Does not exceed the value entered by the user")
    print("0: Go out")
    print("\n")

    val = int(input("Enter: "))
    if val == 0:
        break
    if val == 1:
        num = int(input("Enter item: "))
        print(fibonacci(num))
        continue 
    if val == 2:
        num = int(input("Enter item: "))
        for i in range(0, num + 1):
            print(i, ": ", fibonacci(i))
        continue 
    if val == 3:
        num = int(input("Enter item: "))
        for i in range(0, 100000):
            f = fibonacci(i)
            if f >= num:
                break
            print(i, ": ", f)
        continue 
