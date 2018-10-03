def standaardprijs(afstandKM):
    prijs = afstandKM * 0.80
    if afstandKM > 50:
        prijs = afstandKM * 0.60 + 15
    if afstandKM < 0:
        prijs = 0
    return prijs

print(standaardprijs(100))


def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if weekendrit == True:
        if leeftijd < 12 or leeftijd >= 65:
            prijs = standaardprijs(afstandKM) * 0.65
        else:
            prijs = standaardprijs(afstandKM) * 0.60
    else:
        if leeftijd < 12 or leeftijd >= 65:
            prijs = standaardprijs(afstandKM) * 0.70
        else:
            prijs = standaardprijs(afstandKM)
    return prijs


print(ritprijs(19, False, 100))





