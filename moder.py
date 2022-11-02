#Massin Elotmani
import psycopg2

'''''
Dit script als moderatie en stuurt ook gelijk naar de database.
main.py-->Opmerkingen.csv-->moder.py-->database
'''''
#open een verbinding met de database
verbinding = psycopg2.connect(
    host = "localhost",
    database = "StationZuilMassin",
    user = "postgres",
    password = "HalloSQL1q2"
)

wijzer = verbinding.cursor()

# open opmerkingen.csv in read mode waar alle opmerkingen wachten voordat ze woorden beoordeeld
opmerk = open("Opmerkingen.csv", "r")
"""
Print (naam, gekozen_station, bericht, tijd) naar het scherm.
Als de gebruiker "ja" typt woord het naar "Goedgekeurd.txt" geschreven
Zo niet word het naar "Afgekeurd.csv" geschreven
"""
naam_mod = input("Voer uw naam in")

for line in opmerk.readlines():
    line = line.strip("\n")
    print(line)
    line = line.split("|")

    naam, station, bericht, tijddatum = line

    response = input("Type 'Ja' om goedtekeuren type 'Nee' om aftekeuren ")

    #Pas als de mod Ja of Nee typte breekt hij uit de loop.
    while True:
        if response in ["Ja","ja","jA","JA"]:
            print("Goedgekeurd")
            goedgekeurd = "TRUE"
            break
        elif response in ["Nee","nee","NEE","nEE","NeE","nEe","NEe"]:
            print("Afgekeurd")
            goedgekeurd = "FALSE"
            break
        response = input()

    #Insert het de rij in de database
    wijzer.execute(f"INSERT INTO opmerkingen(naam, station, bericht, goedgekeurd, mod_naam, datetime) "
                   f"VALUES('{naam}', '{station}', '{bericht}', {goedgekeurd},  '{naam_mod}', '{tijddatum}');")

    verbinding.commit()

"""
Wipes Opmerkingen.csv
Voorkomt dat je meer dan een keer een opmerking keurt
"""

opmerk = open("Opmerkingen.csv", "w")
opmerk.write("")

# De verbinding en bestand gesloten.
opmerk.close()
wijzer.close()
verbinding.close()

#Afscheidsbericht
print("\nHeb een fijne dag!")