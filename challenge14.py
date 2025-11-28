import os
import json

print('STUDENT INFORMATION SYSTEM')
print('=============================')

student_record = {}

while True:
    print("SELECT FROM THE FOLLOWING OPTIONS")
    print('A. ADD STUDENT RECORD')
    print('B. PRINT ALL STUDENT RECORD')
    print('C. SEARCH STUDENT RECORD')
    print('D. DELETE STUDENT RECORD')
    print('E. EDIT OR MODIFY STUDENT RECORD')
    print('F.EXPORT STUDENT RECORD')
    print('G. EXIT SYSTEM')

    choice = input('SELECT FROM THE FOLLOWING OPTIONS').lower()

    if choice == 'a':
        os.system("cls")
        print('ADDING STUDENT RECCORD')
        print('===========================')
        

        id_number = eval(input('Please input your STUDENT NUMBER--> '))

        first_name = input('Input your first name --> ').upper()
        second_name = input('Input your second name--> ').upper()
        age = input('Input your age--> ')
        section = input('Input your section--> ').upper()
        course = input('Input your course--> ').upper


        student_record[id_number] = [first_name,second_name,age,section,course]
        print('DATA SAVED SUCCESSFULLY')
        continue
    elif choice == 'b':
        os.system('cls')
        print('PRINTING STUDENT RECORD')
        print('===========================')
        # print(student_record) simple approach

        for i,j in student_record.items():
            print(f"STUDENT ID-{i}, INFORMAION -{j}")

        continue
    elif choice == 'c':
        os.system("cls")
        print("SEARCH STUDENT RECORD")
        search_id = input("Input your student id to search--->").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("RECORD FOUND")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'd':
        os.system("cls")
        print("DELETE STUDENT RECORD")

        search_id= input("Input Student id to search----->")

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("============================")
                print(f"RECORD FOUND FOR ID {search_id}")
                # to print the record for the searched id
                for i in student_record[search_id]:
                    print(f"----{i}")
                print("=======================")
                student_record.pop(search_id)
                print("RECORD DELETED")
            else:
                print("NO RECORD FOUND")
            break   

        continue

    elif choice == 'e':
        os.system('cls')
        print("EDIT OR MODIFY STUDENT RECORD")
        print("===============================")
        search_id=input("Input the student id to search---->")
        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("==============================")
                print("RECORD FOUND FOR ID", search_id)
                # to print record for the searched id
                for i in student_record[search_id]:
                    print(f"---{i}")
                print("===========================")
                # new set of value for the searched id
                first_name = input('Input your first name --> ').upper()
                second_name = input('Input your second name--> ').upper()
                age = input('Input your age--> ')
                section = input('Input your section--> ').upper()
                course = input('Input your course--> ').upper

                student_record[search_id][0]=first_name
                student_record[search_id][1]=second_name
                student_record[search_id][2]=age
                student_record[search_id][3]=section
                student_record[search_id][4]=course
    
                print("DATA UPDATED")
            else:
                print("NO RECORD FOUND")
            break   
        continue
    elif choice == 'f':
        os.system("cls")
        print("EXPORT DATA TO JSON")
        # json javscript object notation

        with open('student_records.json','w') as new_file:
            json.dump(student_record, new_file, indent=4)
        print("\n DATA EXPORTED TO JSON")

        continue

    elif choice == 'g':
        print("SYSTEM EXIT")
        break
    else:
        print("INVALID CHOICE,PLEASE RE ENTER YOUR CHOICE")
        continue


