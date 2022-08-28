manav_meyve=list()
manav_sebze=list()
musteri=list()
ELMA=0
ARMUT=0
MUZ=0
KIRAZ=0
CILEK=0
PATLICAN=0
DOMATES=0
BIBER=0
KABAK=0
PATATES=0

print("****** HALE HOŞGELDİNİZ *******")
while True:
    secim=input("Meyve mi Sebze mi?(M/S) Çıkış için Q:").upper()
    if secim=="M":
        #region While
        while True:
            meyve=int(input("1-Elma\n2-Armut\n3-Muz\n4-Kiraz\n5-Cilek\n6-Ana Menü\n\tSeçiminiz:"))
            if meyve==1:
                if "ELMA" not in manav_meyve:
                    manav_meyve.append("ELMA")
                ELMA+=int(input("Kaç kilo istersiniz?"))
            elif meyve==2:
                if "ARMUT" not in manav_meyve:
                    manav_meyve.append("ARMUT")
                ARMUT += int(input("Kaç kilo istersiniz?"))
            elif meyve==3:
                if "MUZ" not in manav_meyve:
                    manav_meyve.append("MUZ")
                MUZ += int(input("Kaç kilo istersiniz?"))
            elif meyve==4:
                if "KIRAZ" not in manav_meyve:
                    manav_meyve.append("KIRAZ")
                KIRAZ += int(input("Kaç kilo istersiniz?"))
            elif meyve==5:
                if "CILEK" not in manav_meyve:
                    manav_meyve.append("CILEK")
                CILEK += int(input("Kaç kilo istersiniz?"))
            elif meyve == 6:
                print("Ana Menüye Yönlendiriliyorsunuz...")
                import time
                time.sleep(3)
                break
            else:
                print("Hatalı Meyve Seçimi!!")
        #endregion
        #region Stabil
        # meyve = int(input("1-Elma\n2-Armut\n3-Muz\n4-Kiraz\n5-Cilek\n\tSeçiminiz:"))
        # if meyve == 1:
        #     pass
        # elif meyve == 2:
        #     pass
        # elif meyve == 3:
        #     pass
        # elif meyve == 4:
        #     pass
        # elif meyve == 5:
        #     pass
        # else:
        #     print("Hatalı Meyve Seçimi!!")
        # cevap=input("Başka Bir Arzunuz Var Mı? (E/H)").upper()
        # if cevap=="E":
        #     continue
        # else:
        #     break
        #endregion
    elif secim=="S":
        while True:
            sebze = int(input("1-PATLICAN\n2-DOMATES\n3-BIBER\n4-KABAK\n5-PATATES\n6-Ana Menü\n\tSeçiminiz:"))
            if sebze == 1:
                if "PATLICAN" not in manav_sebze:
                    manav_sebze.append("PATLICAN")
                PATLICAN += int(input("Kaç kilo istersiniz?"))
            elif sebze == 2:
                if "DOMATES" not in manav_sebze:
                    manav_sebze.append("DOMATES")
                DOMATES += int(input("Kaç kilo istersiniz?"))
            elif sebze == 3:
                if "BIBER" not in manav_sebze:
                    manav_sebze.append("BIBER")
                BIBER += int(input("Kaç kilo istersiniz?"))
            elif sebze == 4:
                if "KABAK" not in manav_sebze:
                    manav_sebze.append("KABAK")
                KABAK += int(input("Kaç kilo istersiniz?"))
            elif sebze == 5:
                if "PATATES" not in manav_sebze:
                    manav_sebze.append("PATATES")
                PATATES += int(input("Kaç kilo istersiniz?"))
            elif sebze == 6:
                print("Ana Menüye Yönlendiriliyorsunuz...")
                import time

                time.sleep(3)
                break
            else:
                print("Hatalı Sebze Seçimi!!")

    elif secim=="Q":
        print("Yine Bekleriz...")
        import time
        time.sleep(3)
        break
    else:
        print("Hatalı Seçim!!")



print("****** MANAVA HOŞGELDİNİZ *******")
while True:
    secim = input("Meyve mi Sebze mi?(M/S) Çıkış için Q:").upper()
    if secim=="M":
        if len(manav_meyve)==0:
            print("Meyvelerimiz Tükenmiştir :(")
            continue
        i=1
        for m in manav_meyve:
            print(f"{i}-{m}")
            i+=1
        meyve=input("Hangi Meyve?").upper()
        if meyve in manav_meyve:
            if meyve=="ELMA":
                kilo=int(input("Kaç Kilo İstersiniz?"))
                if kilo<=ELMA:
                    ELMA-=kilo
                    if meyve not in musteri:
                        musteri.append(meyve)
                    if ELMA==0:
                        manav_meyve.remove(meyve)
                else:
                    print(f"{meyve} elimizde mevcut olan kilo:{ELMA}")
            elif meyve == "ARMUT":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= ARMUT:
                    ARMUT -= kilo
                    if meyve not in musteri:
                        musteri.append(meyve)
                    if ARMUT == 0:
                        manav_meyve.remove(meyve)
                else:
                    print(f"{meyve} elimizde mevcut olan kilo:{ARMUT}")
            elif meyve == "MUZ":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= MUZ:
                    MUZ -= kilo
                    if meyve not in musteri:
                        musteri.append(meyve)
                    if MUZ == 0:
                        manav_meyve.remove(meyve)
                else:
                    print(f"{meyve} elimizde mevcut olan kilo:{MUZ}")
            elif meyve == "KIRAZ":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= KIRAZ:
                    KIRAZ -= kilo
                    if meyve not in musteri:
                        musteri.append(meyve)
                    if KIRAZ == 0:
                        manav_meyve.remove(meyve)
                else:
                    print(f"{meyve} elimizde mevcut olan kilo:{KIRAZ}")

            elif meyve == "CILEK":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= CILEK:
                    CILEK -= kilo
                    if meyve not in musteri:
                        musteri.append(meyve)
                    if CILEK == 0:
                        manav_meyve.remove(meyve)
                else:
                    print(f"{meyve} elimizde mevcut olan kilo:{CILEK}")
        else:
            print("Olmayan Meyve Girişi!!")

    elif secim=="S":
        if len(manav_sebze) == 0:
            print("Sebzelerimiz Tükenmiştir :(")
            continue
        i = 1
        for m in manav_sebze:
            print(f"{i}-{m}")
            i += 1
        sebze = input("Hangi Sebze?").upper()
        if sebze in manav_sebze:
            if sebze == "PATLICAN":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= PATLICAN:
                    PATLICAN -= kilo
                    if sebze not in musteri:
                        musteri.append(sebze)
                    if PATLICAN == 0:
                        manav_sebze.remove(sebze)
                else:
                    print(f"{sebze} elimizde mevcut olan kilo:{PATLICAN}")
            elif sebze == "DOMATES":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= DOMATES:
                    DOMATES -= kilo
                    if sebze not in musteri:
                        musteri.append(sebze)
                    if DOMATES == 0:
                        manav_sebze.remove(sebze)
                else:
                    print(f"{sebze} elimizde mevcut olan kilo:{DOMATES}")
            elif sebze == "BIBER":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= BIBER:
                    BIBER -= kilo
                    if sebze not in musteri:
                        musteri.append(sebze)
                    if BIBER == 0:
                        manav_sebze.remove(sebze)
                else:
                    print(f"{sebze} elimizde mevcut olan kilo:{BIBER}")
            elif sebze == "PATATES":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= PATATES:
                    PATATES -= kilo
                    if sebze not in musteri:
                        musteri.append(sebze)
                    if PATATES == 0:
                        manav_sebze.remove(sebze)
                else:
                    print(f"{sebze} elimizde mevcut olan kilo:{PATATES}")

            elif sebze == "KABAK":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= KABAK:
                    KABAK -= kilo
                    if sebze not in musteri:
                        musteri.append(sebze)
                    if KABAK == 0:
                        manav_sebze.remove(sebze)
                else:
                    print(f"{sebze} elimizde mevcut olan kilo:{KABAK}")
        else:
            print("Olmayan Sebze Girişi!!")
    elif secim == "Q":
        print("Yine Bekleriz...")
        import time
        time.sleep(3)
        break
    else:
        print("Hatalı Seçim!!")


print(musteri)


###########
# EXE Dosyası Yapma
# pip install pyinstaller


## FULL EXE
# pyinstaller Manav_Otomasyonu.py


## SINGLE EXE
# pyinstaller --onefile Manav_Otomasyonu.py






