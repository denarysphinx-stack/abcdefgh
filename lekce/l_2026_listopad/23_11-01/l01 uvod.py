skore = 0

# muzu napsat takhle = sirka, vyska = 100, 200
while True:
    answer = input("Je Python programovací jazyk? (ano/ne): ")
    if answer == "ano":
        skore += 10
        print("Správná odpověď! Tvoje skóre je:", skore)
    else:
        skore -= 5
        print("Špatná odpověď. Tvoje skóre je:", skore)