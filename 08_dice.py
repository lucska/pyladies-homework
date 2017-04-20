# -*- coding: UTF-8 -*-
# Napiš program, který simuluje tuto hru:
# První hráč hází kostkou (t.j. vybírají se náhodná čísla od 1 do 6), dokud nepadne šestka. Potom hází další hráč,
# dokud nepadne šestka i jemu. Potom hází hráč třetí, a nakonec čtvrtý. Vyhrává ten, kdo na hození šestky
# potřeboval nejvíc hodů. (V případě shody vyhraje ten, kdo házel dřív.)
# Program by měl vypisovat všechny hody, a nakonec napsat, kdo vyhrál.

from random import randrange
i = 1
j = 1
k = 1

def hod_kostkou ():
    "Hazí kostkou náhodná čísla 1 až 6, když padne 6 přestane házet"
    cislo = randrange (1,7)
    print (cislo)
    return cislo

print ("Hází první hráč!")
hod = hod_kostkou ()
while hod !=6:
    hod = hod_kostkou ()
    i = i+1
print ("Počet hodů je: ", i)

print ("Hází druhý hráč!")
hod = hod_kostkou ()
while hod !=6:
    hod = hod_kostkou ()
    j = j+1
print ("Počet hodů je: ", j)

print ("Hází třetí hráč!")
hod = hod_kostkou ()
while hod !=6:
    hod = hod_kostkou ()
    k = k+1
print ("Počet hodů je: ", k)

def vyhodnoceni():
    if i < j and i < k:
        print ("Vyhrál první hráč")
    elif j < i and j < k:
        print ("Vyhrál druhý hráč")
    elif k < i and k < j:
        print ("Vyhrál třetí hráč")
    elif i == j or i == k:
        print ("Stejný výsledek. Vyhrál první hráč, protože házel první")
    elif j == k:
        print ("Stejný výsledek. Vyhrál druhý hráč, protože házel dřív")
vyhodnoceni ()
