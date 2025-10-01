import io


try:
    with open("F1-2024dec.csv", encoding="utf-8")as fajl:
        pass

except IOError as ex:
    print(f"Fájl megnyitás hiba: {ex}")

   
print("ITT A VÉGE")