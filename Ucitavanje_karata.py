podaci_karte = []

def ucitaj_karte():

    file = open("karte.txt", "r")
    sadrzaj = file.readlines()
    file.close()

    for linija in sadrzaj:
        recnik_karte = {}
        reci = linija.split("|")
        recnik_karte["sifra karte"] = reci[0]
        recnik_karte["redni broj kupovine"] = reci[1]
        recnik_karte["sifra leta"] = reci[2]
        recnik_karte["korisnicko ime"] = reci[3]
        recnik_karte["broj telefona"] = reci[4]
        recnik_karte["email"] = reci[5]
        recnik_karte["ime"] = reci[6]
        recnik_karte["prezime"] = reci[7]
        recnik_karte["broj pasosa"] = reci[8]
        recnik_karte["drzavljanstvo"] = reci[9]
        recnik_karte["pol"] = reci[10].replace('\n', '')
        podaci_karte.append(recnik_karte)

ucitaj_karte()

