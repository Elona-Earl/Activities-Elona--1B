name = input("What is your name --> ")
print("Hello",name, "what is your fare")

amount = eval(input("Input your minimum bus fare --->"))

studentfare = input("Are you a student? --->")
if studentfare =='yes'or studentfare == 'YES':
    discount = amount * 0.2
    new_fare = amount - discount
    print("Hi",name)
    print("your dicount is",discount)
    print("your new fare is", new_fare)
else:
    print("sorry you are not eligable for student discount, your fare will be",amount )
