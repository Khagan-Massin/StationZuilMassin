opmerk = open("opmerkingen.txt", "r")
goed = open("Goedegekeurt.txt", "a")
for line in opmerk.readlines():
    opmerk = open("opmerkingen.txt", "r")
    goed = open("Goedegekeurt.txt", "a")
    print(line)
    response = input("Type 'Ja' om goedtekeuren type 'Nee' om afteke uren ")
    if response == "Ja" or response == "ja" or response == "jA" or response == "JA":
        print("ok")
        goed.write(line)
        opmerk = open("opmerkingen.txt", "w")
        line.strip("\n")
    else:
        print("niet ok")
opmerk.close()
goed.close()
