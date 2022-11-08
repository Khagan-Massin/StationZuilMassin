#Massin Elotmani
def comment():
    import random
    from datetime import datetime
    station_lijst = ['Arnhem', 'Almere', 'Amersfoort', 'Almelo', 'Alkmaar', 'Apeldoorn', 'Assen', 'Amsterdam', 'Boxtel', 'Breda', 'Dordrecht', 'Delft', 'Deventer', 'Enschede','Gouda','Groningen', 'Den Haag', 'Hengelo', 'Haarlem', 'Helmond', 'Hoorn', 'Heerlen', 'Den Bosch', 'Hilversum', 'Leiden', 'Lelystad', 'Leeuwarden', 'Maastricht', 'Nijmegen', 'Oss', 'Roermond', 'Roosendaal', 'Sittard', 'Tilburg', 'Utrecht','Venlo','Vlissingen','Zaandam','Zwolle','Zutphen']

    #Geeft de huidige tijd.
    #Word later achter de reactie geschreven in het csv-bestand
    vandaag = datetime.now()
    tijd = vandaag.strftime("%m-%d-%Y %H:%M:%S")

    while True:
        #Laat de gebruiker hun naam en opmerking in te voeren
        naam = input("Voer uw naam je naam ")
        bericht = input("Schrijf uw opmerking ")

        #Als er geen naam word ingevoerd word de naam "Anoniem"
        if naam == "" or naam == " ":
            naam = "Anoniem"

        #Staat geen berichten langer dan 140 characters.
        if len(bericht) > 140:
            print("Uw opmerking is te lang")
        #Staat geen bericht toe met "|" of "\n"
        elif "|" in bericht or "|" in naam:
            print("Illegal Character\n Do not use '|' or '\\n'")
        # Staat geen aanhalingstekens vanwege problemen met SQL
        elif "'" in bericht or "'" in naam:
            print("Illegal Character\n Do not use ' or '\\n'")
        #
        else:
            #Kiest een willekeurige station in Nederland
            gekozen_station = random.choice(station_lijst)
            # Laat de gebruiker zien wat hun geschreven heeft.
            print(f"{naam} schreef: '{bericht}' op {tijd} in {gekozen_station}")
            # Schrijft de info (naam, gekozen_station, bericht, tijd) in een CSV-bestand.
            file = open("Opmerkingen.csv", "a")
            raw_info = (f"{naam}|{gekozen_station}|{bericht}|{tijd}\n")
            file.write(raw_info)
            file.close()

if __name__ == "__main__":
    comment()