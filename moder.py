import psycopg2

verbinding = psycopg2.connect(
    host = "localhost",
    database = "StationZuilMassin",
    user = "postgres",
    password = "HalloSQL1q2"
)

wijzer = verbinding.cursor()

# open het opmerk bestand in read mode waar alle opmerkingen wachten voordat ze woorden beoordeeld
opmerk = open("Opmerkingen.csv", "r")

#Print (naam, gekozen_station, bericht, tijd) naar het scherm.
#Als de gebruiker "ja" typt woord het naar "Goedgekeurt.txt" geschrijven
#Zo niet word het naar "Afgekeurd.csv" geschrijven

naam_mod = input("Voer uw naam in")

for line in opmerk.readlines():
    line = line.strip("\n")
    line = line.split("|")
    print(line)

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

    insertdb = (f"INSERT INTO opmerkingen(naam, station, bericht, goedgekeurd, mod_naam, datetime) Values('{naam}', '{station}', '{bericht}', {goedgekeurd},  '{naam_mod}', '{tijddatum}');")
    print(insertdb)
    wijzer.execute(insertdb)

# Wipes Opmerkingen.csv
opmerk = open("Opmerkingen.csv", "w")
opmerk.write("")



opmerk.close()
wijzer.close()
verbinding.close()