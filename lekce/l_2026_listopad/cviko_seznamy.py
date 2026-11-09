import math
jmeno = "Petr"
vek = 30
print (f"jmenuji se {jmeno} a je mi {vek} let.")

numbers = [1, 2, 6, 4, 8]
numbers.append(6)
numbers.sort()
print (f"serazeny seznam: {numbers}")
print (f"první prvek seznamu: {numbers[0]}")
print (f"poslední prvek seznamu: {numbers[-1]}")

student = {
    "jmeno": "Lojza",
    "vek": 20,
    "predmety": ["matematika", "informatika"]
}
student ["vek"]=25
student ["jmeno"]="Petr"
student ["predmety"]=["matematika", "informatika", "fyzika"]
print (f"student: {student}")
data = [1, 1, 1, 2, 2, 2, 3, 4, 5]
unique_data = set(data)
print (f"unikatni data: {unique_data}")

for i in range(1, 11):
    if i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

def vypocet_obvodu_telesa(delka, sirka=None):
    if sirka is None:
        sirka = delka
    return 2 * (delka + sirka)

delka = 5
sirka = 3
print (f"obvod obdelniku s delkou {delka} a sirkou {sirka} je {vypocet_obvodu_telesa(delka, sirka)}")