podaci_aerodroma = []


def ucitaj_aerodrome():
    file = open("aerodromi.txt", "r")
    sadrzaj = file.readlines()
    file.close()

    for linija in sadrzaj:
        recnik_aerodromi = {}
        reci = linija.split("|")
        sifra_aerodroma = reci[0]
        naziv_aerodroma = reci[1]
        grad = reci[2]
        drzava = reci[3]
        recnik_aerodromi["sifra"] = sifra_aerodroma
        recnik_aerodromi["naziv"] = naziv_aerodroma
        recnik_aerodromi["grad"] = grad
        recnik_aerodromi["drzava"] = drzava.replace('\n', '')
        podaci_aerodroma.append(recnik_aerodromi)

ucitaj_aerodrome()