# Opent alle relevante bestanden

# open het opmerk bestand in read mode waar alle opmerkingen wachten voordat ze woorden beoordeeld
opmerk = open("Opmerkingen.txt", "r")
# Schrijft Afgekeurd berichten naar Afgekeurd en goedgekeurde berichten naar goed Goedgekeurd
goed = open("Goedgekeurd.txt", "a")
fout = open("Afgekeurd.txt", "a")

#Print (naam, gekozen_station, bericht, tijd) naar het scherm.
#Als de gebruiker "ja" typt woord het naar "Goedgekeurt.txt" geschrijven
#Zo niet word het naar "Afgekeurd.txt" geschrijven

naam_mod = input("Voer uw naam in")

for line in opmerk.readlines():
    print(line)
    response = input("Type 'Ja' om goedtekeuren type 'Nee' om aftekeuren ")

    #Pas als de mod Ja of Nee typte breekt hij uit de loop.
    while True:
        if response in ["Ja","ja","jA","JA"]:
            print("Goedgekeurd")
            line = line.strip("\n")
            goed.write(f"{line}|{naam_mod}\n")
            break
        elif response in ["Nee","nee","NEE","nEE","NeE","nEe","NEe"]:
            print("Afgekeurd")
            line = line.strip("\n")
            fout.write(f"{line}|{naam_mod}\n")
            break
        response = input()

opmerk.close()
goed.close()
fout.close()
