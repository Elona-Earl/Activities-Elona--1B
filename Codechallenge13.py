statement = True
sum = 0
odd = ""
while statement is True:
    number = eval(input("Input your number (0 to stop) --> "))

    if number % 2 != 0:
        print("The number is odd, put another number")
        sum +=  number
        odd += str(number) + " "
        continue
    elif number == 0 :
        print("The program stops")
        break
    else:
        if number % 2 == 0 :
            print("The number is even, put another number")
            continue
print("The sum of all odd number is", sum)
print("The odd numbers are", odd)