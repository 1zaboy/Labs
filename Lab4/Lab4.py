import random
print("Lab 4. Performed by Vlad Kolosov.")
print("Try to Guess the Number")
print("You need to guess a number between 0 and 100")
print("\n")


while True:
    print("----------------------------------------------------------")
    ranVal1 = int(input("Start rand value: "))
    ranVal2 = int(input("Stop rand value: "))
    maxCountTry = int(input("Max count try: "))
    print("\n")

    randomValue = random.randint(ranVal1, ranVal2)

    userValue = ""
    isTrueValue = False 
    countTry = 0

    for index in range(0, maxCountTry):
        userValue = input("Enter value: ")
        if userValue.isdigit() == False:
           print("You need enter value")
           continue
        countTry = countTry + 1
        userValue = int(userValue)
        if userValue == randomValue:
            isTrueValue = True 
            break
        elif countTry >= maxCountTry: 
            break
        elif userValue > randomValue:
            print("<")
            continue
        elif userValue < randomValue:
            print(">")
            continue

    if isTrueValue:
        print("\n")
        print("Congratulations, you guessed the number!")
        print("Number: ", randomValue)
        print("Count try: ", countTry)
        print("\n")
    else:
        print("Game Over")

    isNext = bool(int(input("Want to replay the game? 1(true) or 0(false): ")))
    if isNext == False:
        break
    print("\n")

