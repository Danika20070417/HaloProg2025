"""----------------------------------------------
    EGYSZÁM JÁTÉK
----------------------------------------------"""

import random


# Lista létrehozása
szamok = []

# Kitalálandó számok listájának feltöltése 40 db, random, nem ismétlődő kétjegyű egész számmal
while (len(szamok) != 40):
    szam = random.randint(10, 99)
    
    if szam not in szamok:
        szamok.append(szam)



# Ellenőrzés
print(szamok)


# Változók létrehozása statisztika készítéshez
jatek_szam = 1
nem_talaltDB = 0

# A kitalálandó szám kiválasztása a listából
kitalalando_szam = szamok[random.randint(0, len(szamok))]


# A JÁTÉK ---------------------------------------

jatszol = True

while(jatszol):    
    tipp_sz = input("Tipped? (egész szám): ").strip()
    if(tipp_sz.isdecimal()):
        tipp = int(tipp_sz)
    else:
        print("Egész számmal játsz!")
        continue

    while(tipp != kitalalando_szam):
        nem_talaltDB += 1
        if (tipp == 123):
            pass
        elif (tipp < kitalalando_szam):
            print("A kitalálandó szám nagyobb!")
        elif (tipp > kitalalando_szam):
            print("A kitalálandó szám kisebb!")
        
        tipp_sz = input("Tipped? (egész szám)[Kilépés \'X\' karakterrel]: ").strip()
        
        if(tipp_sz.isdecimal()):
            tipp = int(tipp_sz)
        elif tipp_sz == 'X':
            print(f"{jatek_szam} db kitalálandó szám kitalálásához {nem_talaltDB}* próbálkozott rosszul.")
            exit()
        else:
            print("Egész számmal játsz!")
            tipp = 123
            continue

    print("Kitaláltad a kitalálandó számot!")

    folytatas = input("Akarsz-e még játszani? [I/N]")
    if(folytatas == "N"):
        jatszol = False
        print(f"{jatek_szam} db kitalálandó szám kitalálásához {nem_talaltDB}* próbálkozott rosszul.")
    elif (folytatas == "I"):
        jatek_szam+=1