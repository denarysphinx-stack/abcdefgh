import math
print (f"číslo pi {math.pi}")
print (f"sinus 90° {math.sin(math.pi/2)}")

def bezpecne_deleni(a, b):
    try:
        vysledek = a/b
    except ZeroDivisionError as zde:
        print(f"Chyba: {zde}")
        vysledek = None
    except exception as e:
        zprava = f"nelze delit objekt {a} / {b}: {e}"
        raise exception (zprava)
    finally:
        print("deleni bylo provedeno.")
        print("tento blok se provede vždy.")
    return vysledek
print (bezpecne_deleni(10, 2))
print (bezpecne_deleni(10, 0))
