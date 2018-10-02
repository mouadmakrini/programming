def kwadraten_som(grondgetallen):
    kwadraten = []
    for getal in grondgetallen:
        if getal >= 0:
           kwadraten.append((getal**2))
    print (sum(kwadraten))
Lijst = [4,5,3,-81]

kwadraten_som(Lijst)
