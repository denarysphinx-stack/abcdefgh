skore = 0

# muzu napsat takhle = sirka, vyska = 100, 200
while True:
    otazka = input("vyber otazku (1-3) nebo napiš 'konec' pro ukončení: ")
    if otazka == "konec":
        break
    elif otazka == "1":
        answer = input("Je Python programovací jazyk? (ano/ne): ")
        if answer == "ano":
            skore += 10
            print("Správná odpověď! Tvoje skóre je:", skore)
        else:
            skore -= 5
            print("Špatná odpověď. Tvoje skóre je:", skore)
    elif otazka == "2":
        answer = input("Je 2 + 2 rovno 4? (ano/ne): ")
        if answer == "ne":
            skore += 10
            print("Správná odpověď! Tvoje skóre je:", skore)
        else:
            skore -= 5
            print("Špatná odpověď. Tvoje skóre je:", skore)
    elif otazka == "3":
        answer = input("Je Země kulatá? (ano/ne): ")
        if answer == "ano":
            skore += 10
            print("Správná odpověď! Tvoje skóre je:", skore)
        else:
            skore -= 5
            print("Špatná odpověď. Tvoje skóre je:", skore)
    else: 
        print("Neplatná volba. Zkus to znovu.")