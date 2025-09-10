print("Welcome to MangaDex Manga Recommender! ")
manga = input("What is your preferred manga you want to read? (action / romance / horror)").lower()
duration = input("How long do you want? (short / medium / long)").lower()
year = input("which year would you like to read? (2000s / 2010s): ").lower()

if manga == 'action':
    if year == '2000s':
        if duration == 'short':
            print("I would recommend you  (Bleach)")
        elif duration == 'medium':
            print("I would recommend you (Samurai Deep Kyo)")
        else:
            print("I would recommend you (One Piece)")
    if year == '2010s':
        if duration == 'short':
            print("I would recommend you (Green Blood)")
        elif duration == 'medium':
            print("I would recommend you (Akame ga Kill!)")
        else:
            print("I would recommend you (Seven Deadly Sins)")


if manga == 'romance':
    if year == '2000s':
        if duration == 'short':
            print("I would recommend you  (Bitter Virgin)")
        elif duration == 'medium':
            print("I would recommend you (Fruit Basket)")
        else:
            print("I would recommend you (Boys over flowers)")
    if year == '2010s':
        if duration == 'short':
            print(" I would recommend you (A Silent Voice)")
        elif duration == 'medium':
            print("I would recommend you (Horimiya)")
        else:
            print("I would recommend you (Domestic Girlfriend)")


if manga == 'horror':
    if year == '2000s':
        if duration == 'short':
            print("I would recommend you (Tokyo Red Hood)")
        elif duration == 'medium':
            print("I would recommend you (Parasyte)")
        else:
            print("I would recommend you (Gantz)")
    if year == '2010s':
        if duration == 'short':
            print("I would recommend you (Ibitsu)")
        elif duration == 'medium':
            print("I would recommend you (Kasane)")
        else:
            print("I would recommend you (Shingeki no Kyojin)")