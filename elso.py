import random


#lista létrehozása
szamok = []

#lista feltöltése 10 db random két jegyű egész számokkal
for i in range(100):
    szam = random.randint(10, 99)
    szamok.append(szam)

#Ellenőrzés
print(szamok)


#EGYSZÁM JÁTÉK
jatek_szam = 0
nem_talalDB = 0

kitalalando_szam = szamok[random.randint(len(szamok))]

