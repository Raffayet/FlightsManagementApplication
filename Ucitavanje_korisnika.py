podaci_korisnici = []

def ucitaj_korisnike():

    file = open("korisnici.txt", "r")
    sadrzaj = file.readlines()
    file.close()

    for linija in sadrzaj:
        recnik_korisnici = {}
        reci = linija.split("|")
        recnik_korisnici["korisnicko ime"] = reci[0]
        recnik_korisnici["sifra"] = reci[1]
        recnik_korisnici["ime"] = reci[2]
        recnik_korisnici["prezime"] = reci[3]
        recnik_korisnici["uloga"] = reci[4].replace('\n', '')
        if len(reci) == 10:
            recnik_korisnici["broj pasosa"] = reci[5]
            recnik_korisnici["drzavljanstvo"] = reci[6]
            recnik_korisnici["broj telefona"] = reci[7]
            recnik_korisnici["email"] = reci[8]
            recnik_korisnici["pol"] = reci[9].replace('\n', '')
        podaci_korisnici.append(recnik_korisnici)

ucitaj_korisnike()

