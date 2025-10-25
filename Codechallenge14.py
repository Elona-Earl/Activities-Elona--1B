statement = True
list = []
while statement is True:
    anime = input("Enter your peak anime ( enter exit to stop)-->")
    if anime.lower() == 'exit':
        print("You had nice taste there bud")
        break
    list.append(anime)
list_count = len(list)
print("The program exited")
print("Here are the anime you liked:")

for shinn in list:

    print("-", shinn)
    print("Your total anime is", list_count)
