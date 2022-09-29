from datetime import datetime
print("Niet scheldwoorden schrijven please😡")


#def klant():

mod_dis = False

vandaag = datetime.now()
nu = vandaag.strftime("%m/%d/%Y, %H:%M:%S")

naam = input("Enter je name")
bericht = input("Schrijf pzl")

0
if naam == "" or naam == " ":
    naam = "Anoniem"

if len(bericht) > 140:
    print("Uw opmerking is te lang")
elif mod_dis:
    print("Uw taalgebruik mag niet")
else:
    None
info = (naam + " zei: " + bericht + " op " + nu)
print(info)
file = open("opmerkingen.txt", "a")

