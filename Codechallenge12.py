for y in range (1,7,1):
    for i in range(7, y, -1):
        print(" ", end = ' ')
    for x in range (y, 0, -1):
        print("*", end= " ")
    for z  in range(2,y+1):
        print("@", end = " ")
    print()