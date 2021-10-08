podaci_vreme_polaska = []

def ucitaj_vreme_polaska():
    global  podaci_vreme_polaska

    file = open("avionski_letovi.txt", "r")
    sadrzaj = file.readlines()
    file.close()

    file2 = open("konkretni_avionski_letovi.txt", "r")
    sadrzaj2 = file2.readlines()
    file2.close()

    for linija in sadrzaj:
        recnik_vreme_polaska = {}
        reci = linija.split("|")
        recnik_vreme_polaska["vreme polaska"] = reci[3]
        broj = recnik_vreme_polaska["vreme polaska"].split(":")
        sati = int(broj[0])
        minuti = int(broj[1])
        recnik_vreme_polaska["sati"] = sati
        recnik_vreme_polaska["minuti"] = minuti
        broj_leta = reci[0]

        for linija2 in sadrzaj2:
            reci2 = linija2.split("|")
            broj_konkretnog_leta = reci2[1]
            if broj_leta == broj_konkretnog_leta:

                recnik_vreme_polaska["datum polaska"] = reci2[2]
                broj2 = reci2[3].split(".")
                dani = broj2[0]
                meseci = broj2[1]
                godine = broj2[2]
                recnik_vreme_polaska["dani"] = dani
                recnik_vreme_polaska["meseci"] = meseci
                recnik_vreme_polaska["godine"] = godine

                podaci_vreme_polaska.append(recnik_vreme_polaska)

ucitaj_vreme_polaska()