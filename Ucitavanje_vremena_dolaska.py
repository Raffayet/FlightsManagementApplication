avionski_letovi = []
konkretni_avionski_letovi = []
podaci_vreme_dolaska = []

def ucitavanje_avionske_letova():
    global avionski_letovi

    avionski_letovi = []

    file = open("avionski_letovi.txt", "r")
    sadrzaj = file.readlines()
    file.close()

    for linija in sadrzaj:
        reci = linija.split("|")
        broj_leta = reci[0]
        polaziste = reci[1]
        odrediste = reci[2]
        vreme_polaska = reci[3]
        vreme_dolaska = reci[4]
        sletanje_sledeceg_dana = reci[5]
        prevoznik = reci[6]
        dani = reci[7]
        model = reci[8]
        cena = reci[9]

        avionski_letovi.append({"broj leta":broj_leta,"polaziste":polaziste,"odrediste":odrediste,"vreme polaska":vreme_polaska, "vreme dolaska":vreme_dolaska, "sletanje sledeceg dana":
        sletanje_sledeceg_dana, "prevoznik": prevoznik, "dani": dani, "model": model
        ,"cena": cena})

def ispis(r1,r2):
    print(r1)
    print(r2)
    print("-------------------------")

def ucitavanje_konkretnih_letova():
    global konkretni_avionski_letovi

    konkretni_avionski_letovi=[]

    file = open("konkretni_avionski_letovi.txt", "r")
    sadrzaj = file.readlines()
    file.close()

    for linija in sadrzaj:
        reci = linija.split("|")
        sifra_leta = reci[0]
        broj_leta = reci[1]
        datum_polaska = reci[2]
        datum_dolaska = reci[3].replace("\n", "")

        konkretni_avionski_letovi.append({"sifra leta": sifra_leta, "broj leta": broj_leta, "datum polaska": datum_polaska, "datum dolaska": datum_dolaska})


def ucitaj_vreme_dolaska():
    global podaci_vreme_dolaska

    podaci_vreme_dolaska = []

    ucitavanje_avionske_letova()
    ucitavanje_konkretnih_letova()

    for i in avionski_letovi:

        for j in konkretni_avionski_letovi:

            if i["broj leta"] == j["broj leta"]:
                # ispis(i, j)
                broj = i["vreme dolaska"].split(":")
                sati = broj[0]
                minuti = broj[1]

                broj2 = j["datum polaska"].split(".")
                dani = broj2[0]
                meseci = broj2[1]
                godine = broj2[2]

                podaci_vreme_dolaska.append(
                    {"vreme dolaska": i["vreme dolaska"], "sati": sati, "minuti": minuti, "datum dolaska":
                        j["datum dolaska"], "dani": dani, "meseci": meseci, "godine": godine,
                     "broj leta 1": i["broj leta"], "broj leta 2":
                         j["broj leta"], "sifra leta": j["sifra leta"]})

ucitaj_vreme_dolaska()