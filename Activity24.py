
from Activity
while True :
    print("Code Compiler Program")
    print("a-First program \nb- Second program \n c Third program")
    choice=input("Select from the following option").lower()

    if choice == 'a':
        GreeterPersonName('earl')
        continue
    elif choice =='b':
        GreeterInfo('earl', 'Sariaya','18')
        continue
    elif choice == 'c':
        print("System Exited")
    else:
        print("invalid answer")
        continue