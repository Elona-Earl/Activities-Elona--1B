for y in range (1, 11, 1):
    for i in range(11,y,-1):
        print(" ", end= " ")
    for x in range (y,0,-1 ):
        print("y",end = " ")
    for z in range (2, y+1):
        print("z", end= " ")
    print()