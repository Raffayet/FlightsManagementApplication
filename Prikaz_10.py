import datetime

trenutni_dan = datetime.datetime.now()

file = open("aerodromi.txt", "r")
sadrzaj = file.readlines()
aerodromi = {}

for linija in sadrzaj:
    reci = linija.split("|")
    sifra_aerodroma = reci[0]
    naziv_aerodroma = reci[1]
    grad = reci[2]
    drzava = reci[3]
    aerodromi[str(sifra_aerodroma)] = grad
file.close()

lista_cena = []
konacna_lista_cena = []


def ucitavanje_cena():

    file1 = open("avionski_letovi.txt", "r")
    file2 = open("konkretni_avionski_letovi.txt", "r")
    sadrzaj_avionskih_letova = file1.readlines()
    sadrzaj_konkretnih_avionskih_letova = file2.readlines()
    file1.close()
    file2.close()

    for line in sadrzaj_avionskih_letova:
        words = line.split("|")
        broj_leta = words[0]
        cena = words[9].replace('\n', "")

        for linee in sadrzaj_konkretnih_avionskih_letova:
            wordss = linee.split("|")
            broj_konkretnog_leta = wordss[1]
            datum_poletanja = wordss[2]
            broj = datum_poletanja.split(".")
            dan = broj[0]
            mesec = broj[1]
            godina = broj[2]
            dan_leta = datetime.datetime(int(godina), int(mesec), int(dan))

            if broj_leta == broj_konkretnog_leta and dan_leta > trenutni_dan:
                lista_cena.append(cena)


def sortiranje_cena():

    ucitavanje_cena()
    for i in range(len(lista_cena)):

        for j in range(len(lista_cena) - 1):

            if lista_cena[j] < lista_cena[j + 1]:

                x = lista_cena[j]
                lista_cena[j] = lista_cena[j + 1]
                lista_cena[j + 1] = x


def skracivanje_liste():

    zeljeni_broj_cena = 10
    sortiranje_cena()
    del lista_cena[:len(lista_cena) - zeljeni_broj_cena]

def konacna_lista():

    skracivanje_liste()
    for broj in lista_cena:

        if broj not in konacna_lista_cena:

            konacna_lista_cena.append(broj)
    return konacna_lista_cena


def prikaz_10_najjeftinijih():

    konacna_lista()

    file1 = open("avionski_letovi.txt", "r")
    file2 = open("konkretni_avionski_letovi.txt", "r")
    sadrzaj1 = file1.readlines()
    sadrzaj2 = file2.readlines()

    print(
        "| SIFRA LETA | POLAZISNI GRAD | ODREDISNI GRAD | VREME POLETANJA | VREME SLETANJA | "
        "PREVOZNIK | DATUM POLETANJA | MODEL AVIONA | CENA |")
    print(135 * "_")

    for i in konacna_lista_cena:

        for linija in sadrzaj1:
            reci = linija.split("|")
            broj_leta = reci[0]
            polazisni_aerodrom = reci[1]
            odredisni_aerodrom = reci[2]
            vreme_poletanja = reci[3]
            vreme_sletanja = reci[4]
            sletanje_sledeceg_dana = reci[5]
            prevoznik = reci[6]
            dani = reci[7]
            model_aviona = reci[8]
            cena = reci[9]

            for linija in sadrzaj2:
                reci = linija.split("|")
                sifra_konkretnog_leta = reci[0]
                broj_konkretnog_leta = reci[1]
                datum_poletanja = reci[2]
                datum_sletanja = reci[3]
                broj = datum_poletanja.split(".")
                dan = broj[0]
                mesec = broj[1]
                godina = broj[2]
                dan_leta = datetime.datetime(int(godina), int(mesec), int(dan))

                if dan_leta > trenutni_dan and broj_konkretnog_leta == broj_leta and int(cena) == int(i):
                    print("{0:^14}{1:^16}{2:^19}{3:^15}{4:^20}{5:^10}{6:^19}{7:^15}{8:^6}".format(sifra_konkretnog_leta,
                    aerodromi[str(polazisni_aerodrom)], aerodromi[str(odredisni_aerodrom)], vreme_poletanja, vreme_sletanja,
                    prevoznik, datum_poletanja, model_aviona, cena))
                    print(135 * "_")

    file1.close()
    file2.close()
