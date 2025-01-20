class Convert:
    def __init__(self, line):
        aksjdh = line.strip().split(";")
        if aksjdh[1] == "k":
            self.kerdes = aksjdh[2]
            self.valaszok = []
        elif aksjdh[1] == "v":
            try:
                pont = int(aksjdh[3])
            except ValueError:
                print(f"Hiba: a pont értéke nem szám a következő válasznál: {aksjdh[2]}")
                pont = 0
            self.valaszok.append({"valasz": aksjdh[2], "pont": pont})

kerdesek = []
current_kerdes_valasz = None

f = open('kerdesek.csv', 'r', encoding='utf-8')
for i in f:
        parts = i.strip().split(";")
        if parts[1] == "k":
            if current_kerdes_valasz:
                kerdesek.append(current_kerdes_valasz)
            current_kerdes_valasz = Convert(i)
        elif parts[1] == "v" and current_kerdes_valasz:
            try:
                pont = int(parts[3])
            except ValueError:
                pont = 0
            current_kerdes_valasz.valaszok.append({"valasz": parts[2], "pont": pont})

if current_kerdes_valasz:
    kerdesek.append(current_kerdes_valasz)
f.close()

pontszam = 0
question_number = 1

for i in kerdesek:
    print(f"{question_number}. Kérdés: {i.kerdes}\n")

    for idx, valasz in enumerate(i.valaszok, 1):
        print(f"{idx}) {valasz['valasz']}")

    valasz_szam = int(input("\nVálassz egy számot (1, 2 vagy 3): "))

    while valasz_szam not in [1, 2, 3]:
        print("Hiba: csak 1, 2 vagy 3 válaszok közül választhatsz.")
        valasz_szam = int(input("\nVálassz egy számot (1, 2 vagy 3): "))

    pontszam += int(i.valaszok[valasz_szam - 1]["pont"])

    question_number += 1

print(f"Pontszám: {pontszam}")
if 21 >= pontszam >= 13:
    print("Gratulálunk, te tudod, hogy kell igazán egészségesen élni. Ami nagyon fontos, hogy továbbra is figyelj oda a megfelelő hidratálásra és a rostbevitelre. Ha még nem próbáltad, akkor itt az ideje kipróbálni az alternatív fehérje megoldásokat is. Szuper egészséges és finom tud lenni. Egyre vigyázz, azért ne hajtsd túl magad. ;)")
elif 30 >= pontszam >= 22:
    print("Jó úton jársz, de még van mit javítani az étkezéseden. Figyelj a rost és a megfelelő fehérje bevitelre (hal, pulyka vagy csirke legyen a fő és a hüvelyes zöldségek). Nézz utána a mediterrán étrendnek, a tested meg fogja hálálni. A nassolást, amennyire lehet, mellőzd. A nyugodt alváshoz pedig elengedhetetlen a jó környezet, a sötét szoba. Nyugi, nincs szörny az ágy alatt. ;)")
elif 39 >= pontszam >= 31:
    print("Ajjaj, nagy a baj. Nem figyelsz az étkezésedre. Ha ezen nem változtatsz, komoly egészségügyi következményei is lehetnek (mint a cukorbetegség, a magas vérnyomás vagy a korai csontritkulás).")