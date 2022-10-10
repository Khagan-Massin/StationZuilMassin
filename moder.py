opmerk = open("opmerkingen.txt", "r")
goed = open("Goedegekeurt.txt", "a")
fout = open("niet_goed.txt", "a")
for line in opmerk.readlines():
    opmerk = open("opmerkingen.txt", "r")
    goed = open("Goedegekeurt.txt", "a")
    fout = open("niet_goed.txt", "a")
    print(line)
    response = input("Type 'Ja' om goedtekeuren type 'Nee' om afteke uren ")
    if response == "Ja" or response == "ja" or response == "jA" or response == "JA":
        print("ok")
        line = line.strip("\n")
        goed.write(line)

    else:
        print("niet")
        line = line.strip("\n")
        fout.write(line)



opmerk.close()
goed.close()
fout.close()
