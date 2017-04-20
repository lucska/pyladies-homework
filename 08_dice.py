# -*- coding: UTF-8 -*-
# Napiš program, který simuluje tuto hru:
# První hráč hází kostkou (t.j. vybírají se náhodná čísla od 1 do 6), dokud nepadne šestka. Potom hází další hráč,
# dokud nepadne šestka i jemu. Potom hází hráč třetí, a nakonec čtvrtý. Vyhrává ten, kdo na hození šestky
# potřeboval nejvíc hodů. (V případě shody vyhraje ten, kdo házel dřív.)
# Program by měl vypisovat všechny hody, a nakonec napsat, kdo vyhrál.

#nastin...
while hod != 6:
    hod = hod_kostkou()
    # do whilu dat dalsí přiklad, pocitadlo

def hod_kostkou():
    return random (6) ##dopracovat
