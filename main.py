#Massin Elotmani
from datetime import datetime

vandaag = datetime.now()
tijd = vandaag.strftime("%m/%d/%Y %H:%M:%S")


print("Niet scheldwoorden schrijven please😡")

naam = input("Enter je name")
bericht = input("Schrijf uw bericht")

if naam == "" or naam == " ":
    naam = "Anoniem"

if len(bericht) > 140:
    print("Uw opmerking is te lang")

else:
    format_info = (naam + " schreef: " + "'" + bericht + "'" + " op " + tijd)
    print(format_info)

    file = open("opmerkingen.txt", "a")
    raw_info = naam + ", '" + bericht + "', " + tijd + "\n"
    file.write(raw_info)
    file.close()
