import os
import time

print('========================================')
print('PYTHON FUNDAMENTALS INTERACTIVE LEARNER MENU')
time.sleep(1)
print('========================================')

print("This program provides an interactive menu to explore Python fundamentals.")
time.sleep(1)
print("Each topic includes definition, explanation, sample code, and output.")
time.sleep(1)
print("There's also an experiment section for hands-on practice.")
time.sleep(1)
print('========================================')
ign = input("Good day user what is your name---->").title()
time.sleep(1)
print('========================================')
print("Hi,",ign,"\n\tWelcome to the python learning program menu")
time.sleep(1)
print('========================================')
while True:
    yn= input("Would you like to run the program---->(y/n)").lower()
    time.sleep(1)

    if yn =='y':

        while True:
            print("\nSELECT FROM THE FOLLOWING OPTIONS")
            print('A. PRINT STATEMENTS')
            print('B. VARIABLES')
            print('C. OPERATORS')
            print('D. CONDITIONALS')
            print('E. LOOPS')
            print('F. LISTS')
            print('G. FUNCTIONS')
            print('H. EXIT SYSTEM')

            choice = input('SELECT FROM THE FOLLOWING OPTIONS------>').lower()

            if choice == 'a':
                os.system("cls")
                print('=======================================')
                print(f'Hello',ign,'welcome to Print Statement section')
                time.sleep(0.5)
                print('=======================================')
                print('PRINT STATEMENTS')
                time.sleep(0.5)
                print('=======================================')
                while True:
                    print("\nSELECT FROM THE FOLLOWING OPTIONS")
                    print('A. DEFINITION OF PRINT STATEMENT')
                    print('B. FUNCTION OF PRINT STATEMENT')
                    print('C. SAMPLE CODE')
                    print('D. CODE EXPERIMENT SECTION')
                    print('E. RETURN TO MAIN MENU')
                    a_while= input("SELECT FORM THE FOLLOWING OPTIONS------->").lower()
                    if a_while == 'a':
                        print('========================================')
                        print('Definition: The print() function in Python is used to output text or values to the console.')
                        print('========================================')
                        time.sleep(1)
                        continue
                    if a_while == "b":
                        print('========================================')
                        print('Function: It can display strings, numbers, variables, and more. It automatically adds a newline unless specified otherwise.')
                        print('========================================')
                        time.sleep(1)
                        continue
                    if a_while == "c":
                        print('\nSample Code:')
                        time.sleep(1)
                        print('print("Hello, World!")')
                        print('name = "Alice"')
                        print('print(f"Hello, {name}!")')
                        time.sleep(1)
                        print('\nOutput:')
                        print("Hello, World!")
                        name = "Alice"
                        print(f"Hello, {name}!")
                        time.sleep(1)
                        continue
                    if a_while == "d":
                        print('Welcome to the code experiment section!')
                        print('You can enter multi-line Python code here for experimentation.')
                        print('Instructions:')
                        print('- Enter your code line by line.')
                        print('- Type "run" to execute the code you have entered.')
                        print('- Type "clear" to clear the current code without executing.')
                        print('- Type "exit" to return to the main menu.')
                        print('Note: This is for learning purposes only.')
                        print('Only basic codes will run in this program.')
                        print()
                        code_lines = []
                        while True:
                            user_input = input('>>> ')
                            if user_input.lower() == 'exit':
                                break
                            elif user_input.lower() == 'run':
                                if not code_lines:
                                    print('No code to run. Enter some code first.')
                                else:
                                    full_code = '\n'.join(code_lines)
                                    try:
                                        exec(full_code)
                                        print('Code executed successfully.')
                                    except Exception as e:
                                        print(f'Error during execution: {e}')
                                code_lines = []  # Clear after run
                            elif user_input.lower() == 'clear':
                                code_lines = []
                                print('Code cleared.')
                            else:
                                code_lines.append(user_input)
                        continue
                    if a_while == "e":
                        print("RETURNED TO MAIN MENU")
                        time.sleep(1)
                        break

            elif choice == 'b':
                os.system('cls')
                print('=======================================')
                print(f'Hello',ign,'welcome to Variables section')
                time.sleep(0.5)
                print('=======================================')
                print('VARIABLES')
                time.sleep(0.5)
                print('===========================================')
                while True:
                    print("\nSELECT FROM THE FOLLOWING OPTIONS")
                    print('A. DEFINITION OF VARIABLES')
                    print('B. FUNCTION OF VARIABLES')
                    print('C. SAMPLE CODE')
                    print('D. CODE EXPERIMENT SECTION')
                    print('E. RETURN TO MENU')
                    a_while= input("SELECT FORM THE FOLLOWING OPTION------->").lower()
                    if a_while == 'a':
                        print('========================================')
                        print('Definition: A variable in Python is a named storage location that holds a value, which can be changed during program execution.')
                        print('========================================')
                        time.sleep(1)
                        continue
                    if a_while == "b":
                        print('========================================')
                        print('Explanation: Variables are used to store data like numbers, strings, or objects. They must be assigned before use and can hold different data types.')
                        print('========================================')
                        time.sleep(1)
                        continue
                    if a_while == "c":
                        print('\nSample Code:')
                        time.sleep(1)
                        print('x = 10')
                        print('y = "Python"')
                        print('print(x, y)')
                        print('x = 20  # Reassigning')
                        print('print(x)')
                        time.sleep(1)
                        print('\nOutput:')
                        x = 10
                        y = "Python"
                        print(x, y)
                        time.sleep(1)
                        x = 20
                        print(x)
                        time.sleep(1)
                        continue
                    if a_while == "d":
                        print('Welcome to the code experiment section!')
                        print('You can enter multi-line Python code here for experimentation.')
                        print('Instructions:')
                        print('- Enter your code line by line.')
                        print('- Type "run" to execute the code you have entered.')
                        print('- Type "clear" to clear the current code without executing.')
                        print('- Type "exit" to return to the main menu.')
                        print('Note: This is for learning purposes only.')
                        print('Only basic codes will run in this program.')
                        print()
                        code_lines = []
                        while True:
                            user_input = input('>>> ')
                            if user_input.lower() == 'exit':
                                break
                            elif user_input.lower() == 'run':
                                if not code_lines:
                                    print('No code to run. Enter some code first.')
                                else:
                                    full_code = '\n'.join(code_lines)
                                    try:
                                        exec(full_code)
                                        print('Code executed successfully.')
                                    except Exception as e:
                                        print(f'Error during execution: {e}')
                                code_lines = []  # Clear after run
                            elif user_input.lower() == 'clear':
                                code_lines = []
                                print('Code cleared.')
                            else:
                                code_lines.append(user_input)
                        continue
                    if a_while == "e":
                        print("RETURNED TO MAIN MENU")
                        time.sleep(1)
                        break
            elif choice == 'c':
                os.system('cls')
                print('=======================================')
                print(f'Hello',name,'welcome to Operators section')
                time.sleep(0.5)
                print('=======================================')
                print('OPERATORS')
                time.sleep(0.5)
                print('===========================================')
                while True:
                    print("\nSELECT FROM THE FOLLOWING OPTIONS")
                    print('A. DEFINITION OF OPERATORS')
                    print('B. FUNCTION OF OPERATORS')
                    print('C. SAMPLE CODE')
                    print('D. CODE EXPERIMENT SECTION')
                    print('E. RETURN TO MENU')
                    a_while= input("SELECT FORM THE FOLLOWING OPTION------->").lower()
                    if a_while == 'a':
                        print('========================================')
                        print('Definition: Operators in Python are symbols that perform operations on variables and values.')
                        print('========================================')
                        time.sleep(1)
                        continue
                    if a_while == "b":
                        print('========================================')
                        print('Explanation: They include arithmetic (+, -, *, /), comparison (==, !=, <, >), logical (and, or, not), and assignment (=, +=) operators..')
                        print('========================================')
                        time.sleep(1)
                        continue
                    if a_while == "c":
                        print('\nSample Code:')
                        print('a = 5')
                        print('b = 3')
                        print('print(a + b)  # Addition')
                        print('print(a > b)  # Comparison')
                        print('print(a == 5 and b < 4)  # Logical')
                        time.sleep(1)
                        print('\nOutput:')
                        a = 5
                        b = 3
                        print(a + b)
                        print(a > b)
                        print(a == 5 and b < 4)
                        time.sleep(1)
                        continue
                    if a_while == "d":
                        print('Welcome to the code experiment section!')
                        print('You can enter multi-line Python code here for experimentation.')
                        print('Instructions:')
                        print('- Enter your code line by line.')
                        print('- Type "run" to execute the code you have entered.')
                        print('- Type "clear" to clear the current code without executing.')
                        print('- Type "exit" to return to the main menu.')
                        print('Note: This is for learning purposes only.')
                        print('Only basic codes will run in this program.')
                        print()
                        code_lines = []
                        while True:
                            user_input = input('>>> ')
                            if user_input.lower() == 'exit':
                                break
                            elif user_input.lower() == 'run':
                                if not code_lines:
                                    print('No code to run. Enter some code first.')
                                else:
                                    full_code = '\n'.join(code_lines)
                                    try:
                                        exec(full_code)
                                        print('Code executed successfully.')
                                    except Exception as e:
                                        print(f'Error during execution: {e}')
                                code_lines = []  # Clear after run
                            elif user_input.lower() == 'clear':
                                code_lines = []
                                print('Code cleared.')
                            else:
                                code_lines.append(user_input)
                        continue
                    if a_while == "e":
                        print("RETURNED TO MAIN MENU")
                        time.sleep(1)
                        break
            elif choice == 'd':
                os.system('cls')
                print('=======================================')
                print(f'Hello',ign,'welcome to Conditionals section')
                time.sleep(0.5)
                print('=======================================')
                print('CONDITIONALS')
                time.sleep(0.5)
                print('===========================================')
                while True:
                    print("\nSELECT FROM THE FOLLOWING OPTIONS")
                    print('A. DEFINITION OF CONDITIONALS')
                    print('B. FUNCTION OF CONDITIONALS')
                    print('C. SAMPLE CODE')
                    print('D. CODE EXPERIMENT SECTION')
                    print('E. RETURN TO MENU')
                    a_while= input("SELECT FORM THE FOLLOWING OPTION------->").lower()
                    if a_while == 'a':
                        print('========================================')
                        print('Definition: Conditionals in Python allow the program to execute different code blocks based on whether a condition is true or false.')
                        print('========================================')
                        time.sleep(1)
                        continue
                    if a_while == "b":
                        print('========================================')
                        print('Explanation: The if, elif, and else statements are used to control the flow of the program.')
                        print('========================================')
                        time.sleep(1)
                        continue
                    if a_while == "c":
                        print('\nSample Code:')
                        print('age = 18')
                        print('if age >= 18:')
                        print('    print("Adult")')
                        print('else:')
                        print('    print("Minor")')
                        time.sleep(1)
                        print('\nOutput:')
                        time.sleep(1)
                        age = 18
                        if age >= 18:
                            print("Adult")
                        else: 
                            print("Minor")
                        continue
                    if a_while == "d":
                        print('Welcome to the code experiment section!')
                        print('You can enter multi-line Python code here for experimentation.')
                        print('Instructions:')
                        print('- Enter your code line by line.')
                        print('- Type "run" to execute the code you have entered.')
                        print('- Type "clear" to clear the current code without executing.')
                        print('- Type "exit" to return to the main menu.')
                        print('Note: This is for learning purposes only.')
                        print('Only basic codes will run in this program.')
                        print()
                        code_lines = []
                        while True:
                            user_input = input('>>> ')
                            if user_input.lower() == 'exit':
                                break
                            elif user_input.lower() == 'run':
                                if not code_lines:
                                    print('No code to run. Enter some code first.')
                                else:
                                    full_code = '\n'.join(code_lines)
                                    try:
                                        exec(full_code)
                                        print('Code executed successfully.')
                                    except Exception as e:
                                        print(f'Error during execution: {e}')
                                code_lines = []  # Clear after run
                            elif user_input.lower() == 'clear':
                                code_lines = []
                                print('Code cleared.')
                            else:
                                code_lines.append(user_input)
                        continue
                    if a_while == "e":
                        print("RETURNED TO MAIN MENU")
                        time.sleep(1)
                        break
            elif choice == 'e':
                os.system('cls')
                print('=======================================')
                print(f'Hello',name,'welcome to Loops section')
                time.sleep(0.5)
                print('=======================================')
                print('LOOPS')
                time.sleep(0.5)
                print('===========================================')
                while True:
                    print("\nSELECT FROM THE FOLLOWING OPTIONS")
                    print('A. DEFINITION OF LOOPS')
                    print('B. FUNCTION OF LOOPS')
                    print('C. SAMPLE CODE')
                    print('D. CODE EXPERIMENT SECTION')
                    print('E. RETURN TO MENU')
                    a_while= input("SELECT FORM THE FOLLOWING OPTION------->").lower()
                    if a_while == 'a':
                        print('========================================')
                        print('Definition: Loops in Python allow repetitive execution of a block of code.')
                        print('========================================')
                        time.sleep(1)
                        continue
                    if a_while == "b":
                        print('========================================')
                        print('Explanation: Common loops include for (iterating over sequences) and while (based on a condition).')
                        print('========================================')
                        time.sleep(1)
                        continue
                    if a_while == "c":
                        print('\nSample Code (For Loop):')
                        print('for i in range(10):')
                        print('    print(i,"hello world")')
                        time.sleep(1)
                        print('\nSample Code (While Loop):')
                        print('i = 0')
                        print('while i < 6:')
                        print('    print(i)')
                        print('    i += 1')
                        time.sleep(1)
                        print('\nOutput:')
                        print("For Loop:")
                        for i in range(10):
                            print(i,"hello world")
                            time.sleep(1)
                        print("While Loop:")
                        time.sleep(1)
                        i = 0
                        while i < 6:
                            print(i)
                            i += 1
                            time.sleep(1)
                            continue
                    if a_while == "d":
                        print('Welcome to the code experiment section!')
                        print('You can enter multi-line Python code here for experimentation.')
                        print('Instructions:')
                        print('- Enter your code line by line.')
                        print('- Type "run" to execute the code you have entered.')
                        print('- Type "clear" to clear the current code without executing.')
                        print('- Type "exit" to return to the main menu.')
                        print('Note: This is for learning purposes only.')
                        print('Only basic codes will run in this program.')
                        print()
                        code_lines = []
                        while True:
                            user_input = input('>>> ')
                            if user_input.lower() == 'exit':
                                break
                            elif user_input.lower() == 'run':
                                if not code_lines:
                                    print('No code to run. Enter some code first.')
                                else:
                                    full_code = '\n'.join(code_lines)
                                    try:
                                        exec(full_code)
                                        print('Code executed successfully.')
                                    except Exception as e:
                                        print(f'Error during execution: {e}')
                                code_lines = []  # Clear after run
                            elif user_input.lower() == 'clear':
                                code_lines = []
                                print('Code cleared.')
                            else:
                                code_lines.append(user_input)
                        continue
                    if a_while == "e":
                        print("RETURNED TO MAIN MENU")
                        time.sleep(1)
                        break
                
            elif choice == 'f':
                os.system('cls')
                print('=======================================')
                print(f'Hello',ign,'welcome to List section')
                time.sleep(0.5)
                print('=======================================')
                print('LIST')
                time.sleep(0.5)
                print('===========================================')
                while True:
                    print("\nSELECT FROM THE FOLLOWING OPTIONS")
                    print('A. DEFINITION OF LIST')
                    print('B. FUNCTION OF LIST')
                    print('C. SAMPLE CODE')
                    print('D. CODE EXPERIMENT SECTION')
                    print('E. RETURN TO MENU')
                    a_while= input("SELECT FORM THE FOLLOWING OPTION------->").lower()
                    if a_while == 'a':
                        print('========================================')
                        print('Definition: A list in Python is an ordered, mutable collection of items that can hold elements of different data types.')
                        print('========================================')
                        time.sleep(1)
                        continue
                    if a_while == "b":
                        print('========================================')
                        print('Explanation: Lists support indexing, slicing, appending, and other operations for managing sequences of data.')
                        print('========================================')
                        time.sleep(1)
                        continue
                    if a_while == "c":
                        print('\nSample Code:')
                        print('fruits = ["apple", "banana", "cherry"]')
                        print('             #0      #1       #2')
                        time.sleep(1)
                        print('print(fruits[1])  # Indexing')
                        time.sleep(1)
                        print('fruits.append("date")')
                        time.sleep(1)
                        print('print(fruits)')
                        time.sleep(1)
                        print('\nOutput:')
                        fruits = ["apple", "banana", "cherry"]
                        print(fruits[1])
                        fruits.append("date")
                        print(fruits)
                        continue
                    if a_while == "d":
                        print('Welcome to the code experiment section!')
                        print('You can enter multi-line Python code here for experimentation.')
                        print('Instructions:')
                        print('- Enter your code line by line.')
                        print('- Type "run" to execute the code you have entered.')
                        print('- Type "clear" to clear the current code without executing.')
                        print('- Type "exit" to return to the main menu.')
                        print('Note: This is for learning purposes only.')
                        print('Only basic codes will run in this program.')
                        print()
                        code_lines = []
                        while True:
                            user_input = input('>>> ')
                            if user_input.lower() == 'exit':
                                break
                            elif user_input.lower() == 'run':
                                if not code_lines:
                                    print('No code to run. Enter some code first.')
                                else:
                                    full_code = '\n'.join(code_lines)
                                    try:
                                        exec(full_code)
                                        print('Code executed successfully.')
                                    except Exception as e:
                                        print(f'Error during execution: {e}')
                                code_lines = []  # Clear after run
                            elif user_input.lower() == 'clear':
                                code_lines = []
                                print('Code cleared.')
                            else:
                                code_lines.append(user_input)
                        continue
                    if a_while == "e":
                        print("RETURNED TO  MAIN MENU")
                        time.sleep(1)
                        break
            elif choice == 'g':
                os.system('cls')
                print('=======================================')
                print(f'Hello',ign,'welcome to Functions section')
                time.sleep(0.5)
                print('=======================================')
                print('FUNCTIONS')
                time.sleep(0.5)
                print('===========================================')
                while True:
                    print("\nSELECT FROM THE FOLLOWING OPTIONS")
                    print('A. DEFINITION OF FUNCTIONS')
                    print('B. FUNCTION OF FNCTIONS')
                    print('C. SAMPLE CODE')
                    print('D. CODE EXPERIMENT SECTION')
                    print('E. RETURN TO MENU')
                    a_while= input("SELECT FORM THE FOLLOWING OPTION------->").lower()
                    if a_while == 'a':
                        print('========================================')
                        print('Definition: A function in Python is a block of reusable code that performs a specific task and can be called with arguments.')
                        print('========================================')
                        time.sleep(1)
                        continue
                    if a_while == "b":
                        print('========================================')
                        print('Explanation: Functions promote code reusability and modularity. They can return values or perform actions.')
                        print('========================================')
                        time.sleep(1)
                        continue
                    if a_while == "c":
                        print('\nSample Code:')
                        time.sleep(1)
                        print('def greet(name):')
                        print('    return f"Hello, {name}!"')
                        print('print(greet("Alice"))')
                        time.sleep(1)
                        print('\nOutput:')
                        time.sleep(1)
                        def greet(name):
                            return f"Hello, {name}!"
                        print(greet("Alice"))
                        time.sleep(1)
                        continue
                    if a_while == "d":
                        print('Welcome to the code experiment section!')
                        print('You can enter multi-line Python code here for experimentation.')
                        print('Instructions:')
                        print('- Enter your code line by line.')
                        print('- Type "run" to execute the code you have entered.')
                        print('- Type "clear" to clear the current code without executing.')
                        print('- Type "exit" to return to the main menu.')
                        print('Note: This is for learning purposes only.')
                        print('Only basic codes will run in this program.')
                        print()
                        code_lines = []
                        while True:
                            user_input = input('>>> ')
                            if user_input.lower() == 'exit':
                                break
                            elif user_input.lower() == 'run':
                                if not code_lines:
                                    print('No code to run. Enter some code first.')
                                else:
                                    full_code = '\n'.join(code_lines)
                                    try:
                                        exec(full_code)
                                        print('Code executed successfully.')
                                    except Exception as e:
                                        print(f'Error during execution: {e}')
                                code_lines = []  # Clear after run
                            elif user_input.lower() == 'clear':
                                code_lines = []
                                print('Code cleared.')
                            else:
                                code_lines.append(user_input)
                        continue
                    if a_while == "e":
                        print("RETURNED TO  MAIN MENU")
                        time.sleep(1)
                        break
            elif choice == 'h':
                print("=====================================")
                print("SYSTEM EXITED")
                print("Thank you for using my menu\n I hope you learned something from this python learning program")
                time.sleep(0.5)
                print("=====================================")
                break
                
            else:
                print("INVALID CHOICE,PLEASE RE ENTER YOUR CHOICE")
                continue
    else:
        print('========================================')
        print("Program cancelled \n Try it next time")
        print('========================================')
        break            