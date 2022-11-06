#Massin Elotmani
def comment():
    import random
    from datetime import datetime
    #long_station_lijst = ['Aalten', 'Abcoude', 'Akkrum', 'Alkmaar Noord', 'Alkmaar', 'Almelo de Riet', 'Almelo', 'Almere Buiten', 'Almere Centrum', 'Almere Muziekwijk', 'Almere Oostvaarders', 'Almere Parkwijk', 'Almere Poort', 'Alphen aan den Rijn', 'Amersfoort Centraal', 'Amersfoort Schothorst', 'Amersfoort Vathorst', 'Amsterdam Amstel', 'Amsterdam Arena', 'Amsterdam Bijlmer ArenA', 'Amsterdam Centraal', 'Amsterdam Holendrecht', 'Amsterdam Lelylaan', 'Amsterdam Muiderpoort', 'Amsterdam RAI', 'Amsterdam Science Park', 'Amsterdam Sloterdijk', 'Amsterdam Zuid', 'Anna Paulowna', 'Apeldoorn De Maten', 'Apeldoorn Osseveld', 'Apeldoorn', 'Appingedam', 'Arkel', 'Arnemuiden', 'Arnhem Presikhaaf', 'Arnhem Centraal', 'Arnhem Velperpoort', 'Arnhem Zuid', 'Assen', 'Baarn', 'Bad Nieuweschans', 'Baflo', 'Barendrecht', 'Barneveld Centrum', 'Barneveld Noord', 'Barneveld Zuid', 'Bedum', 'Beek-Elsloo', 'Beesd', 'Beilen', 'Bergen op Zoom', 'Best', 'Beverwijk', 'Bilthoven', 'Blerick', 'Bloemendaal', 'Bodegraven', 'Borne', 'Boskoop', 'Boskoop Snijdelwijk', 'Bovenkarspel Flora', 'Bovenkarspel-Grootebroek', 'Boven Hardinxveld', 'Boxmeer', 'Boxtel', 'Breda Prinsenbeek', 'Breda', 'Breukelen', 'Brummen', 'Buitenpost', 'Bunde', 'Bunnik', 'Bussum Zuid', 'Capelle Schollevaar', 'Castricum', 'Chevremont', 'Coevorden', 'Cuijk', 'Culemborg', 'Daarlerveen', 'Dalen', 'Dalfsen', 'De Vink', 'De Westereen', 'Deinum', 'Delden', 'Delft', 'Delft Campus', 'Delfzijl', 'Delfzijl West', 'Den Dolder', 'Den Haag Centraal', 'Den Haag Hollands Spoor', 'Den Haag Laan van NOI', 'Den Haag Mariahoeve', 'Den Haag Moerwijk', 'Den Haag Ypenburg', 'Den Helder', 'Den Helder Zuid', 'Deurne', 'Deventer Colmschate', 'Deventer', 'Didam', 'Diemen', 'Diemen Zuid', 'Dieren', 'Doetinchem De Huet', 'Doetinchem', 'Dordrecht', 'Dordrecht Stadspolders', 'Dordrecht Zuid', 'Driebergen-Zeist', 'Driehuis', 'Dronryp', 'Dronten', 'Duiven', 'Duivendrecht', 'Echt', 'Ede Centrum', 'Ede-Wageningen', 'Eemshaven', 'Eijsden', 'Eindhoven Centraal', 'Eindhoven Stadion', 'Eindhoven Strijp-S', 'Elst', 'Emmen', 'Emmen Zuid', 'Enkhuizen', 'Enschede De Eschmarke', 'Enschede Kennispark', 'Enschede', 'Ermelo', 'Etten-Leur', 'Eygelshoven Markt', 'Eygelshoven', 'Feanwâlden', 'Franeker', 'Gaanderen', 'Geldermalsen', 'Geldrop', 'Geleen Oost', 'Geleen-Lutterade', 'Gilze-Rijen', 'Glanerbrug', 'Goes', 'Goor', 'Gorinchem', 'Gouda Goverwelle', 'Gouda', 'Gramsbergen', 'Grijpskerk', 'Groningen Europapark', 'Groningen Noord', 'Groningen', 'Grou-Jirnsum', 'Haarlem', 'Haarlem Spaarnwoude', 'Halfweg-Zwanenburg', 'Hardenberg', 'Harderwijk', 'Hardinxveld Blauwe Zoom', 'Hardinxveld-Giessendam', 'Haren (NL)', 'Harlingen Haven', 'Harlingen', 'Heemskerk', 'Heemstede-Aerdenhout', 'Heerenveen IJsstadion', 'Heerenveen', 'Heerhugowaard', 'Heerlen de Kissel', 'Heerlen', 'Heerlen Woonboulevard', 'Heeze', 'Heiloo', 'Heino', 'Helmond Brandevoort', 'Helmond Brouwhuis', 'Helmond', "Helmond 't Hout", 'Hemmen-Dodewaard', 'Hengelo Gezondheidspark', 'Hengelo Oost', 'Hengelo', 'Hillegom', 'Hilversum Media Park', 'Hilversum', 'Hilversum Sportpark', 'Hindeloopen', 'Hoensbroek', 'Hoevelaken', 'Hollandsche Rading', 'Holten', 'Hoofddorp', 'Hoogeveen', 'Hoogezand-Sappemeer', 'Hoogkarspel', 'Hoorn Kersenboogerd', 'Hoorn', 'Horst-Sevenum', 'Houten Castellum', 'Houten', 'Houthem-Sint Gerlach', 'Hurdegaryp', 'IJlst', 'Kampen', 'Kampen Zuid', 'Kapelle-Biezelinge', 'Kerkrade Centrum', 'Kesteren', 'Klarenbeek', 'Klimmen-Ransdaal', 'Koog aan de Zaan', 'Koudum-Molkwerum', 'Krabbendijke', 'Krommenie-Assendelft', 'Kropswolde', 'Kruiningen-Yerseke', 'Lage Zwaluwe', 'Landgraaf', 'Lansingerland-Zoetermeer', 'Leerdam', 'Leeuwarden Camminghaburen', 'Leeuwarden', 'Leiden Centraal', 'Leiden Lammenschans', 'Lelystad Centrum', 'Lichtenvoorde-Groenlo', 'Lochem', 'Loppersum', 'Lunteren', 'Maarheeze', 'Maarn', 'Maarssen', 'Maastricht Noord', 'Maastricht', 'Maastricht Randwyck', 'Mantgum', 'Mariënberg', 'Martenshoek', 'Meerssen', 'Meppel', 'Middelburg', 'Mook-Molenhoek', 'Naarden-Bussum', 'Nieuw Amsterdam', 'Nieuwerkerk aan den IJssel', 'Nieuw-Vennep', 'Nijkerk', 'Nijmegen Dukenburg', 'Nijmegen Goffert', 'Nijmegen Heyendaal', 'Nijmegen Lent', 'Nijmegen', 'Nijverdal', 'Nunspeet', 'Nuth', 'Obdam', 'Oisterwijk', 'Oldenzaal', 'Olst', 'Ommen', 'Oosterbeek', 'Opheusden', 'Oss', 'Oss West', 'Oudenbosch', 'Overveen', 'Purmerend Overwhere', 'Purmerend', 'Purmerend Weidevenne', 'Putten', 'Raalte', 'Ravenstein', 'Reuver', 'Rheden', 'Rhenen', 'Rijssen', 'Rijswijk', 'Rilland-Bath', 'Roermond', 'Roodeschool', 'Roosendaal', 'Rosmalen', 'Rotterdam Alexander', 'Rotterdam Blaak', 'Rotterdam Centraal', 'Rotterdam Lombardijen', 'Rotterdam Noord', 'Rotterdam Stadion', 'Rotterdam Zuid', 'Ruurlo', 'Santpoort Noord', 'Santpoort Zuid', 'Sappemeer Oost', 'Sassenheim', 'Sauwerd', 'Schagen', 'Scheemda', 'Schiedam Centrum', 'Schin op Geul', 'Schinnen', 'Schiphol', "'s-Hertogenbosch Oost", "'s-Hertogenbosch", 'Sittard', 'Sliedrecht Baanhoek', 'Sliedrecht', 'Sneek Noord', 'Sneek', 'Soest (Netherlands)', 'Soest Zuid', 'Soestdijk', 'Spaubeek', 'Stavoren', 'Stedum', 'Steenwijk', 'Susteren', 'Swalmen', "'t Harde", 'Tegelen', 'Terborg', 'Tiel Passewaaij', 'Tiel', 'Tilburg', 'Tilburg Reeshof', 'Tilburg Universiteit', 'Twello', 'Uitgeest', 'Uithuizen', 'Uithuizermeeden', 'Usquert', 'Utrecht Centraal', 'Utrecht Leidsche Rijn', 'Utrecht Lunetten', 'Utrecht Maliebaan', 'Utrecht Overvecht', 'Utrecht Terwijde', 'Utrecht Vaartsche Rijn', 'Utrecht Zuilen', 'Valkenburg', 'Varsseveld', 'Veendam', 'Veenendaal Centrum', 'Veenendaal West', 'Veenendaal-De Klomp', 'Velp', 'Venlo', 'Venray', 'Vierlingsbeek', 'Vleuten', 'Vlissingen', 'Vlissingen Souburg', 'Voerendaal', 'Voorburg', 'Voorhout', 'Voorschoten', 'Voorst-Empe', 'Vorden', 'Vriezenveen', 'Vroomshoop', 'Vught', 'Waddinxveen Noord', 'Waddinxveen', 'Waddinxveen Triangel', 'Warffum', 'Weert', 'Weesp', 'Wehl', 'Westervoort', 'Wezep', 'Wierden', 'Wijchen', 'Wijhe', 'Winschoten', 'Winsum', 'Winterswijk', 'Winterswijk West', 'Woerden', 'Wolfheze', 'Wolvega', 'Workum', 'Wormerveer', 'Zaandam Kogerveld', 'Zaandam', 'Zaandijk Zaanse Schans', 'Zaltbommel', 'Zandvoort aan Zee', 'Zetten-Andelst', 'Zevenaar', 'Zevenbergen', 'Zoetermeer Oost', 'Zoetermeer', 'Zuidbroek', 'Zuidhorn', 'Zutphen', 'Zwijndrecht', 'Zwolle', 'Zwolle Stadshagen']
    station_lijst = ['Arnhem', 'Almere', 'Amersfoort', 'Almelo', 'Alkmaar', 'Apeldoorn', 'Assen', 'Amsterdam', 'Boxtel', 'Breda', 'Dordrecht', 'Delft', 'Deventer', 'Enschede','Gouda','Groningen', 'Den Haag', 'Hengelo', 'Haarlem', 'Helmond', 'Hoorn', 'Heerlen', 'Den Bosch', 'Hilversum', 'Leiden', 'Lelystad', 'Leeuwarden', 'Maastricht', 'Nijmegen', 'Oss', 'Roermond', 'Roosendaal', 'Sittard', 'Tilburg', 'Utrecht','Venlo','Vlissingen','Zaandam','Zwolle','Zutphen']
    gekozen_station = (random.choices(station_lijst))[0]



    #Geeft de huidige tijd.
    #Word later achter de reactie geschreven in het csv-bestand
    vandaag = datetime.now()
    tijd = vandaag.strftime("%m-%d-%Y %H:%M:%S")

    #Geeft een bericht aan de opmerking schrijver
    print("Niet scheldwoorden schrijven please😡🙄")

    while True:
        #Laat de gebruiker hun naam en opmerking in te voeren
        naam = input("Enter je name" )
        bericht = input("Schrijf uw opmerking" )

        #Als er geen naam word ingevoerd word de naam "Anoniem"
        if naam == "" or naam == " ":
            naam = "Anoniem"

        #Staat geen berichten langer dan 140 characters.
        if len(bericht) > 140:
            print("Uw opmerking is te lang")
        #Staat geen bericht toe met "|" of "\n"
        elif "|" in bericht or "|" in naam:
            print("Illegal Character\n Do not use '|' or '\\n'")
        #
        else:
            # Laat de gebruiker zien wat hun geschreven heeft.
            print(f"{naam} schreef: '{bericht}' op {tijd} in {gekozen_station}")
            # Schrijft de info (naam, gekozen_station, bericht, tijd) in een CSV-bestand.
            file = open("Opmerkingen.csv", "a")
            raw_info = (f"{naam}|{gekozen_station}|{bericht}|{tijd}\n")
            file.write(raw_info)
            file.close()

if __name__ == "__main__":
    comment()