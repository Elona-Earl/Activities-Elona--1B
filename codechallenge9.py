print("You have a silly parrot that repeat what you say")
phrase = str(input("What do you want the parrot to say?--> "))
squaks = eval(input("How many times you want the parrot say it? --> "))

for parrot in range(squaks,0,-1):
   print("🦜 Squawk!",phrase,"!!")