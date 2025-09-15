print ("input 7 numbers")

result = 0  

for i in range(7):
    num = eval(input("Enter your  numbers --->"))
    if num % 2 != 0:   
        result += num

print("The sum of all odd numbers is", result)