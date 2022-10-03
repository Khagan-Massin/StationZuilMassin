bestand = open("opmerkingen.txt", "a")
for line in bestand.readlines():
    print(line)
    response= input("Type 'Ja' om goedtekeuren type 'Nee' om aftekeuren ")
    if response == "Ja" or response == "ja" or response == "jA" or response == "JA":
        print("ok")
