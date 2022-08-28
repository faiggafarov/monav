meyveler = ["ELMA", "ARMUT", "KİRAZ", "MUZ", "ÇİLEK"]
sebzeler = ["SARIMSAK", "DOMATES", "PATLICAN", "SOĞAN", "PATATES"]
meyve_agirliklar, sebze_agirliklar = [0]*5, [0]*5
monav_meyveler = []
monav_sebzeler = []
a = input("Meyve mi? Sebze mi?(M/S)").upper()
if a == "MEYVE":
    meyve = input("Hangi meyve?").upper()
    if meyve in meyveler:
        meyve_agirlik = int(input("Kaç kilo?"))
        meyve_agirliklar[meyveler.index(meyve)] += meyve_agirlik
        monav_meyveler.append(meyve)
    else:
        print("Aradığınız meyve yok")
elif a == "SEBZE":
    sebze = input("Hangi sebze?").upper()
    if sebze in sebzeler:
        sebze_agirlik = int(input("Kaç kilo?"))
        sebze_agirliklar[sebzeler.index(sebze)] += sebze_agirlik
        monav_sebzeler.append(sebze)
    else:
        print("Aradığınız sebze yok")
else:
    print("Yalnız listedeki meyve ve sebze var")

arzu = input("Başka bir arzunuz varmı?(E/H)").upper()
while arzu == "EVET":
    a = input("Meyve mi? Sebze mi?(M/S)").upper()
    if a == "MEYVE":
        meyve = input("Hangi meyve?").upper()
        if meyve in meyveler:
            meyve_agirlik = int(input("Kaç kilo?"))
            meyve_agirliklar[meyveler.index(meyve)] += meyve_agirlik
            monav_meyveler.append(meyve)
        else:
            print("Aradığınız meyve yok")
    elif a == "SEBZE":
        sebze = input("Hangi sebze?").upper()
        if sebze in sebzeler:
            sebze_agirlik = int(input("Kaç kilo?"))
            sebze_agirliklar[sebzeler.index(sebze)] += sebze_agirlik
            monav_sebzeler.append(sebze)
        else:
            print("Aradığınız sebze yok")
    else:
        print("Yalnız listedeki meyve ve sebze var")
    arzu = input("Manav kısmına geç")

print("\nMonav")
meyve_agirlik_satilan, sebze_agirlik_satilan = [0] * 5, [0] * 5
satilan_meyveler, satilan_sebzeler = [], []
arzu = input("Başka bir arzunuz varmı?(E/H)").upper()
while arzu == "EVET":
    a = input("Meyve mi? Sebze mi?(M/S)").upper()
    to_list = []
    if a == "MEYVE":
        to_list = monav_meyveler
    if a == "SEBZE":
        to_list = monav_sebzeler
    if a == "MEYVE" or a == "SEBZE":
        print("Birini sec:")
    else:
        print("Yalnız meyve ve sebze var")
    for i in to_list:
        print(i)
    if a == "MEYVE":
        meyve = input("Hangi meyve? ")
        if meyve in meyveler:
            meyve_agirlik = float(input("Kaç kilo? "))
            ind = meyveler.index(meyve)
            if meyve_agirliklar[ind] >= meyve_agirlik:
                meyve_agirliklar[ind] -= meyve_agirlik
                meyve_agirlik_satilan[ind] += meyve_agirlik
                satilan_meyveler.append(meyve)
            else:
                print("Tükenmiştir")
            if meyve_agirliklar[ind] < 1:
                monav_meyveler.remove(meyve)
        else:
            print("Öyle meyve yok")
    if a == "SEBZE":
        sebze = input("Hangi sebze? ")
        if sebze in sebzeler:
            sebze_agirlik = float(input("Kaç kilo? "))
            ind = sebze.index(sebze)
            if sebze_agirliklar[ind] >= sebze_agirlik:
                sebze_agirliklar[ind] -= sebze_agirlik
                sebze_agirlik_satilan[ind] += sebze_agirlik
                satilan_sebzeler.append(sebze)
            else:
                print("Tükenmiştir")
            if sebze_agirliklar[ind] < 1:
                monav_sebzeler.remove(sebze)
        else:
            print("Öyle sebze yok")
    arzu = input("Devam? ").upper()

print("Satilan Meyveler: ", satilan_meyveler, meyve_agirlik_satilan)
print("Satilan Sebzeler: ", satilan_sebzeler, sebze_agirlik_satilan)






