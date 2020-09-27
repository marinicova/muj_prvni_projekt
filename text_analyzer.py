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

oddelovac = '-' * 60
print(oddelovac)
print('Vitej v naši aplikaci. Prosím přihlašte se:')

jmeno = input('Jméno: ')
heslo = input('Heslo: ')
uzivatele = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
print(oddelovac)

if uzivatele.get(jmeno) != heslo:
    print('špátné jméno nebo heslo!!!')
    print(oddelovac)
    exit()
else:
    print('Si přihlášen :)')
    print(oddelovac)

print('Máme 3 texty k analyzování.')
vyber = int(input('Prosím vložte číslo od 1 do 3: '))
print(oddelovac)

text = texts[vyber - 1]
text_o = [slovo.strip(",.") for slovo in text.split()]

slova = len(text_o)
velke_pp = 0
velke_p = 0
male_p = 0
cislice = 0

for slovo in text_o:

    if slovo.istitle():
        velke_pp += 1

    elif slovo.isupper():
        velke_p += 1

    elif slovo.islower():
        male_p += 1

    elif slovo.isnumeric():
        cislice += 1

print(f"V texte se nachází {slova} slov.")
print(f"Daný text obsahuje {velke_pp} slov začínajících velkým písmenem.")
print(f"Daný text obsahuje {velke_p} slov psaných velkými písmeny.")
print(f"Daný text obsahuje {male_p} slov psaných malými písmeny.")
print(f"Daný text obsahuje {cislice} čísla.")
print(oddelovac)

delka_slovo = {}
for slovo in text_o:
    delka_slovo[len(slovo)] = delka_slovo.get(len(slovo), 0) + 1

for klic in sorted(delka_slovo.keys()):
    print(f"{klic} {'*'* delka_slovo.get(klic)} {delka_slovo.get(klic)}")
print(oddelovac)

cisla = sum([int(slovo) for slovo in text_o if slovo.isnumeric()])
print(f"Když spočítame všechny čísla v textě dostaneme: {str(cisla)}")
print(oddelovac)
