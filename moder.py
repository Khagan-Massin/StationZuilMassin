# Opent alle relevante bestanden

# open het opmerk bestand in read mode waar alle opmerkingen wachten voordat ze woorden beoordeeld
opmerk = open("Opmerkingen.txt", "r")
# Schrijft Afgekeurd berichten naar Afgekeurd en goedgekeurde berichten naar goed Goedgekeurd
goed = open("Goedgekeurd.txt", "a")
fout = open("Afgekeurd.txt", "a")

#Print (naam, gekozen_station, bericht, tijd) naar het scherm.
#Als de gebruiker "ja" typt woord het naar "Goedgekeurt.txt" geschrijven
#Zo niet word het naar "Afgekeurd.txt" geschrijven

for line in opmerk.readlines():
    print(line)
    response = input("Type 'Ja' om goedtekeuren type 'Nee' om aftekeuren ")
    if response == "Ja" or response == "ja" or response == "jA" or response == "JA":
        print("Goedgekeurd")
        goed.write(line)

    else:
        print("Afgekeurd")
        fout.write(line)


opmerk.close()
goed.close()
fout.close()
