"""----------------------------------------------
    EGYSZÁM JÁTÉK
----------------------------------------------"""

import random


# Lista létrehozása
szamok = []

# Kitalálandó számok listájának feltöltése 40 db, random, nem ismétlődő kétjegyű egész számmal
while len(szamok) != 40:
    szam = random.randint(10, 99)
    
    if szam not in szamok:
        szamok.append(szam)

# Ellenőrzés
print(szamok)


# Változók létrehozása statisztika készítéshez
jatek_szam = 0
nem_talaldDB = 0

# A kitalálandó szám kiválasztása a listából
kitalalando_szam = szamok[random.randint(0, len(szamok))]


# A JÁTÉK ---------------------------------------
kitalalando_szam = 12

jatszol = True

while(jatszol):    
    tipp_sz = input("Tipped? (egész szám): ").strip()
    if(tipp_sz.isdecimal()):
        tipp = int(tipp_sz)
    else:
        print("Egész számmal játsz!")
        continue

    while(tipp != kitalalando_szam):
        
        if (tipp < kitalalando_szam):
            print("A kitalálandó szám nagyobb!")
        else:
            print("A kitalálandó szám kisebb!")
        
        tipp_sz = input("Tipped? (egész szám): ").strip()
        if(tipp_sz.isdecimal()):
            tipp = int(tipp_sz)
        else:
            print("Egész számmal játsz!")
            continue

    print("Kitaláltad a kitalálandó számot!")

    folytatas = input("Akarsz-e még játszani? [I/N]")
    if(folytatas == "N"):
        jatszol = False