#Made by bibi100101.
#Bubble sort, not very efficient. May look dirty. Comments in Polish and English.

import random

#Polski: Generuje listę z losową długością i numerami.
#English: Generates list with random lenght and numbers.
MojaLista = []
for i in range(0, random.randint(10, 100)):
    MojaLista.append(random.randint(1, 1000))

#Translation: List before:
print("Lista Wczesniej: ",MojaLista) 

def Sort(Lista):
    while True:
        #Polish: Przechodzi przez każdą liczbę w liscie. Jeżeli numer w liscie jest większy niż następny numer, zamienia miejsca
        # liczb i zwiększa licznik. W przeciwnym razie kontynuuje. Jeżeli licznik jest 0 to znaczy, że nic się nie zmieniło i
        # zwraca wysortowaną listę.
        
        #English: Goes trough every number in list. If number in list is greater then number after, swaps and inrement
        # counter(Licznik). Otherwise continues. If counter is 0 that means no change and returns sorted list.
        
        Licznik = 0
        for i in range(0,len(Lista)-1):
            if Lista[i] > Lista[i + 1]:
                Lista[i], Lista[i + 1] = Lista[i + 1], Lista[i]
                Licznik =+ 1
            else:
                continue
        if Licznik == 0:
            return(Lista)

#Translation: List after
print("\nLista pozniej: ", Sort(MojaLista))
