#Massin Elotmani
import psycopg2
from datetime import datetime

'''''
Dit script als functioneert moderatie en stuurt ook gelijk naar de database.
main.py-->Opmerkingen.csv-->moder.py-->database


Open een verbinding met de database
'''''
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
naam_mod = input("Voer uw naam in ")
mod_email = input("Voer uw Email in ")

"""
Maakt twee exemplaren van alle lijnen in het Opmerkingen.csv
Als een lijn gekeurd is word de lijn van bestand_lijst gehaald.
niet gekeurde lijnen worden terug naar het Opmerkingen.csv geschreven
"""
voor_lines = opmerk.readlines()
bestand_lijst = voor_lines.copy()
for line in voor_lines:

    newline = line.split("|")
    naam, station, bericht, tijddatum = newline
    print(f"\n"
          f"Gebruikersnaam: {naam}\n"
          f"       Station: {station}\n"
          f"       Bericht: {bericht}\n"
          f"            Op: {tijddatum}")

    response = input("Type 'Ja' om goedtekeuren type 'Nee' om aftekeuren ")

    #Pas als de mod Ja of Nee typte breekt hij uit de loop.
    #Als hij stop typte breekt hij uit allebij loops en stopt hij met keuren
    while True:
        if response.lower() == 'ja':
            print("Goedgekeurd")
            goedgekeurd = "TRUE"
            break
        elif response.lower() == 'nee':
            print("Afgekeurd")
            goedgekeurd = "FALSE"
            break
        elif response.lower() == 'stop':
            opmerk = open("Opmerkingen.csv", "w")
            opmerk.writelines(bestand_lijst)
            break
        response = input()

    if response.lower() == 'stop':
        break


#Insert de rij in de database in de opmerkingen table

    wijzer.execute(f"INSERT INTO opmerkingen(naam, station, bericht, goedgekeurd, datetime) "
                   f"VALUES('{naam}', '{station}', '{bericht}', {goedgekeurd}, '{tijddatum}'); ")

    verbinding.commit()

#Geef de tijd van keuring

    vandaag = datetime.now()
    tijd = vandaag.strftime("%m-%d-%Y %H:%M:%S")
    '''''
    Insert moderator info in de mod table
    '''''
    wijzer.execute(f"INSERT INTO moderator(mod_email, mod_naam, keuring_datumtijd) "
                   f"VALUES('{mod_email}', '{naam_mod}', '{tijd}');")

    verbinding.commit()

    bestand_lijst.remove(line)
    '''''
    Als de loop niet breekt (de moderator of dus alles gekeurd)
    '''''
else:
    opmerk = open("Opmerkingen.csv", "w")
    opmerk.truncate(0)
"""
Wipes Opmerkingen.csv
Voorkomt dat je meer dan een keer een opmerking keurt
"""



# De verbinding en bestand gesloten.
opmerk.close()
wijzer.close()
verbinding.close()
#Afscheidsbericht
print("\nHeb een fijne dag!")