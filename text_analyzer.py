# Prihlaseni do aplikace.
oddelovac = '-' * 40
print(oddelovac)
# 1.Na začátku přivítá uživatele.
print('Vitej v naši aplikaci. Prosím přihlašte se:')

# 2. Vyžádá si od uživatele přihlašovací jméno a heslo.
jmeno = str(input('Jméno: '))
heslo = str(input('Heslo: '))
uzivatele = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
print(oddelovac)

# 3. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.
if uzivatele.get(jmeno) != heslo:
    print('špátné jméno nebo heslo!!!')
else:
    print('Si přihlášen :)')
    print(oddelovac)

# 4. Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS.
print('Máme 3 texty k analyzovaní.')
vyber = int(input('Prosím vložte číslo od 1 do 3: '))
print(oddelovac)

texts = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad,  
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# Analyzuje text
# 5. Pro vybraný text spočítá následující statistiky:
# a - počet slov,
# b - počet slov začínajících velkým písmenem,
# c - počet slov psaných velkými písmeny,
# d - počet slov psaných malými písmeny,
# e - počet čísel (ne cifer!).

# Úprava textu
text = texts[vyber - 1]
text_o = [slovo.strip(",.") for slovo in text.split()]

# a
slova = len(text_o)
velke_pp = 0
velke_p = 0
male_p = 0
cislice = 0
for znak in text_o:
    # b
    if znak.istitle():
        velke_pp += 1
        continue
    # c
    if znak.isupper():
        velke_p += 1
    # d
    elif znak.islower():
        male_p += 1
    # e
    elif znak.isnumeric():
        cislice += 1

# Vypsání analyzy textu
print(f"V texte se nachází  {slova} slov.")
print(f"Daný text obsahuje {velke_pp} slov začínajících velkým písmenem.")
print(f"Daný text obsahuje  {velke_p} slov psaných velkými písmeny.")
print(f"Daný text obsahuje {male_p} slov psaných malými písmeny.")
print(f"Daný text obsahuje {cislice} čísla.")
print(oddelovac)

# 6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu.
pocet_pismen_slovo = {}
for slovo in text_o:
    pocet_pismen_slovo[len(slovo)] = pocet_pismen_slovo.get(len(slovo), 0) + 1
od_nejmensiho = sorted(pocet_pismen_slovo.keys(), reverse=False)
for klic in od_nejmensiho:
    print(f"{klic} {'*'* pocet_pismen_slovo.get(klic)} {pocet_pismen_slovo.get(klic)}")
print(oddelovac)

# 7. Program spočítá součet všech čísel (ne cifer!) v textu.
cisla = 0
for slovo in text_o:
    if slovo.isnumeric():
       cisla = cisla + int(slovo)
print(f"Když spočítame všechny čísla v textě dostaneme: {str(cisla)}")