
verseny_adatok = []

try:
    with open("F1-2024dec.csv", encoding="utf-8") as fajl:
        
        for sor in fajl:
            verseny_adatok.append(sor)

except IOError as ex:
    print(f"Fájl megnyitás hiba: {ex}")

#print(verseny_adatok)

    """
    1. Sorozatszámítás/összegzés
    2. Kiválasztás
    3. Megszámolás
    4. Eldöntés 1
        Eldöntés 2
    5.Maximum/minimum kiválasztás
    6. Keresés (lineáris)
    
    7. Szétválogatás
    8. Kiválogatás (külön, helyben)
    9. Unió
    10. Metszet
    
    11. Rendezés
        egyszerű cserés
        buborékos
        minimumkiválasztásos
    """
    
# 1. Mennyi a pontszám átlag?
pontszam = 0
db = len(verseny_adatok)-1
for i in range(1, len(verseny_adatok)):
    sor = verseny_adatok[i].split(",")
    pontszam = pontszam+int(sor[1])
print(f"Pontszámok átlaga: {pontszam/db}")

# 2. Mi a bekért versenyző adatai?
pilota = input("Kérek egy pilótát:")
cv = 1
while verseny_adatok[cv].split(",")[0]!=pilota:
    cv+=1
print(verseny_adatok[cv])

# 3. Hány versenyző teljesített 300 pont felett?
db1 = 0
for i in range(1, len(verseny_adatok)):
    if (int(verseny_adatok[i].split(",")[1]) > 300):
        db1 += 1
print(f"{db1} versenyző teljesített 300 pont felett")

# 4.1 Van-e 0 pontos versenyző?

cv = 1
while cv < len(verseny_adatok) and int(verseny_adatok[cv].split(",")[1])>0:
    cv += 1
if cv <= len(verseny_adatok):
    print("Van 0 pontos versenyző")
else:
    print("Nincs 0 pontos versenyző")

# 4.2 Mindenki szerzett már pontot?

cv = 1
while cv < len(verseny_adatok) and int(verseny_adatok[cv].split(",")[1])>0:
    cv += 1
if cv >= len(verseny_adatok):
    print("Mindenki szerzett pontot")
else:
    print("Nem mindenki szerzett pontot")

# 5. Ki vezeti a szezont?

maxe = int(verseny_adatok[1].split(",")[1])
maxi = 1
for i in range(2, len(verseny_adatok)):
    if int(verseny_adatok[i].split(",")[1]) > maxe:
        maxe = int(verseny_adatok[i].split(",")[1])
        maxi = i
print(f"{verseny_adatok[maxi].split(",")[0]} vezeti a szezont")

# 6. Kinek van 90 pontja?

b = 1
while b < len(verseny_adatok) and int(verseny_adatok[b].split(",")[1]) != 90:
    b += 1
if b < len(verseny_adatok):
    print(f"{verseny_adatok[b].split(",")[0]}-nak/nek van 90 pontja")
else:
    print("Nincs 90 pontos")

# 7. Kik a Mercedes pilótái?

merci = []
db2 = 0
for i in range(1, len(verseny_adatok)):
    if verseny_adatok[i].strip().split(",")[2] == "Mercedes":
        merci.append(verseny_adatok[i].split(",")[0])
        db2 += 1
print(merci)

# 8. Kik a Stake F1 Team Kick Sauber és RB F1 Team pilótái?

dby = 0
dbz = 0
y = []
z = []
for i in range(1, len(verseny_adatok)):
    if verseny_adatok[i].strip().split(",")[2] == "Stake F1 Team Kick Sauber" or verseny_adatok[i].strip().split(",")[2] == "RB F1 Team":
        dby += 1
        y.append(verseny_adatok[i].split(",")[0])
    else:
        dbz += 1
        z.append(verseny_adatok[i].split(",")[0])
print(y, z)

# --------------------------------------------------------------------------------------------------------------------------------------

# 9. Kik 1950 és 2024 top 3-as versenyzők?

verseny_adatok19 = []
verseny_adatok20 = []
try:
    with open("F1_1950-1999.csv", encoding="utf-8") as fajl:
        
        for sor in fajl:
            verseny_adatok19.append(sor)

except IOError as ex:
    print(f"Fájl megnyitás hiba: {ex}")
try:
    with open("F1_2000-2024.csv", encoding="utf-8") as fajl:
        
        for sor in fajl:
            verseny_adatok20.append(sor)

except IOError as ex:
    print(f"Fájl megnyitás hiba: {ex}")
u = []
for i in range(1, len(verseny_adatok19)):
    u.append(verseny_adatok19[i])
for j in range(1, len(verseny_adatok20)):
    u.append(verseny_adatok20)
print(u)

# 10. 