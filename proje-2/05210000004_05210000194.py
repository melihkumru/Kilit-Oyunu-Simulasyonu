def uzerindenatlama(kullanilanList, sonKonum_h, oncekiKonum, oncekiKonum_h, sonKonum, oyuncuChar, oyuncu2Char):
    hamleOyuncu1 = ""
    yanlisVarmi = False
    for rakam, harf in oyuncu2Char:
        if harf == sonKonum_h:
            mekan_r = int(oncekiKonum[0])
            rakip_mr = int(rakam)
            yenimekan = int(sonKonum[0])
            if mekan_r > rakip_mr:
                if yenimekan <= rakip_mr:
                    hamleOyuncu1 = "Rakip karakterin üzerinden geçemezsiniz."
                    yanlisVarmi = True
                    break
            elif mekan_r < rakip_mr:
                if yenimekan >= rakip_mr:
                    hamleOyuncu1 = "Rakip karakterin üzerinden geçemezsiniz."
                    yanlisVarmi = True
                    break
        if rakam == sonKonum[0]:
            mekan_h = kullanilanList.index(oncekiKonum_h)
            rakip_mh = kullanilanList.index(harf)
            yenimekan = kullanilanList.index(sonKonum_h)
            if mekan_h > rakip_mh:
                if yenimekan <= rakip_mh:
                    hamleOyuncu1 = "Rakip karakterin üzerinden geçemezsiniz."
                    yanlisVarmi = True
                    break
            elif mekan_h < rakip_mh:
                if yenimekan >= rakip_mh:
                    hamleOyuncu1 = "Rakip karakterin üzerinden geçemezsiniz."
                    yanlisVarmi = True
                    break

    for rakam, harf in oyuncuChar:
        if harf == sonKonum_h:
            mekan_r = int(oncekiKonum[0])
            kendi_mr = int(rakam)
            yenimekan = int(sonKonum[0])
            if mekan_r > kendi_mr:
                if yenimekan <= kendi_mr:
                    hamleOyuncu1 = "Kendi karakterinizin üzerinden geçemezsiniz."
                    yanlisVarmi = True
                    break
            elif mekan_r < kendi_mr:
                if yenimekan >= kendi_mr:
                    hamleOyuncu1 = "Kendi karakterinizin üzerinden geçemezsiniz."
                    yanlisVarmi = True
                    break
        if rakam == sonKonum[0]:
            mekan_h = kullanilanList.index(oncekiKonum_h)
            kendi_mh = kullanilanList.index(harf)
            yenimekan = kullanilanList.index(sonKonum_h)
            if mekan_h > kendi_mh:
                if yenimekan <= kendi_mh:
                    hamleOyuncu1 = "Kendi karakterinizin üzerinden geçemezsiniz."
                    yanlisVarmi = True
                    break
            elif mekan_h < kendi_mh:
                if yenimekan >= kendi_mh:
                    hamleOyuncu1 = "Kendi karakterinizin üzerinden geçemezsiniz."
                    yanlisVarmi = True
                    break
    if hamleOyuncu1 == "":
        print(hamleOyuncu1, end="")
    else:
        print(hamleOyuncu1)
    return yanlisVarmi


def Koseler(kullanList: list):
    # Bu fonksiyon köşe elemeleri için kullanılır
    maks_sayi = len(kullanList)
    kose1 = ["1A", "2A", "1B"]
    kose2 = [str(1)+kullanList[-1], str(2)+kullanList[-1], str(1)+kullanList[-2]]
    kose3 = [str(maks_sayi)+"A", str(maks_sayi-1)+"A", str(maks_sayi)+"B"]
    kose4 = [str(maks_sayi)+kullanList[-1], str(maks_sayi-1)+kullanList[-1], str(maks_sayi)+kullanList[-2]]
    # Ve en sonda köşe elemelerinin gerçekleşebileceği köşeleri gönderir.
    return [kose1, kose2, kose3, kose4]


def KoseElemesi(sonKonum: str, oyuncuChar: list, oyuncu2Char: list, kullanilanList: list):
    # Bu fonksiyon sayesinde köşe elemesinin olup olmadığını belirliyoruz.
    kose = Koseler(kullanilanList)
    for yanar, zinD, zinY in kose:
        if zinD == sonKonum:
            if zinY in oyuncuChar and yanar in oyuncu2Char:
                return yanar
        elif zinY == sonKonum:
            if zinD in oyuncuChar and yanar in oyuncu2Char:
                return yanar
    return False


def Elenme(sonKonum: str, oyuncuChar: list, oyuncu2Char: list, kullanilanList: list):
    # Bu fonksiyon sayesinde hamle yapıldıktan sonra eleme yapabiliyoruz.
    eleme_adayi = "bos"
    sonKonumR = int(sonKonum[0])
    sonKonumH = sonKonum[1]
    yardimciCharDH, yardimciCharDR, yardimciCharYH, yardimciCharYR, yardimciCharDH2, yardimciCharDR2, yardimciCharYH2, yardimciCharYR2 = "bos", "bos", "bos", "bos", "bos", "bos", "bos", "bos"
    sonK_indeks = 0
    kose = KoseElemesi(sonKonum, oyuncuChar, oyuncu2Char, kullanilanList)

    if kose != False:
        eleme_adayi = kose
    # Bu döngü sayesinde taşı zincirleyip eleme olabileceği durumunda yardımcı karakterin mekanını kontrol ediyoruz.
    for r, h in oyuncuChar:
        h_indeks = kullanilanList.index(h)
        sonK_indeks = kullanilanList.index(sonKonumH)

        if sonKonumR - int(r) == 2 and sonKonumH == h:
            yardimciCharDH, yardimciCharDR = h, int(r)
        elif sonKonumR - int(r) == -2 and sonKonumH == h:
            yardimciCharDH2, yardimciCharDR2 = h, int(r)
        elif h_indeks-sonK_indeks == 2 and sonKonumR == int(r):
            yardimciCharYH, yardimciCharYR = kullanilanList.index(h), r
        elif h_indeks-sonK_indeks == -2 and sonKonumR == int(r):
            yardimciCharYH2, yardimciCharYR2 = kullanilanList.index(h), r

    # Bu döngü sayesinde ise eğer yardımcı çar doğru konumdaysa elenecek taşı döndürüyoruz.
    for r2, h2 in oyuncu2Char:
        h2_indeks = kullanilanList.index(h2)

        if yardimciCharDH2 != "bos":
            if sonKonumR < int(r2) < yardimciCharDR2 and h2 == sonKonumH:
                return r2 + h2
        if yardimciCharDH != "bos":
            if sonKonumR > int(r2) > yardimciCharDR and h2 == sonKonumH:
                return r2 + h2
        if yardimciCharYR2 != "bos":
            if sonK_indeks > h2_indeks > yardimciCharYH2 and yardimciCharYR2 == r2:
                return r2 + h2
        if yardimciCharYR != "bos":
            if sonK_indeks < h2_indeks < yardimciCharYH and yardimciCharYR == r2:
                return r2 + h2
    return eleme_adayi


def Hamle(oyuncu: str, oyuncuChar: list, oyuncu2Char: list, kullanilanList: list):
    # Oyunun en önemli fonksiyonu
    hamleOyuncu1 = input(f"Oyuncu {oyuncu}, lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedef konumu giriniz: ")
    # Tum hata kontrollerini burada yapiyoruz.
    hatali = True
    while hatali:
        # Doğru veri girişi kontrolü
        try:
            iki_hamle = hamleOyuncu1.split(" ")
            oncekiKonum = iki_hamle[0]
            oncekiKonum_h = oncekiKonum[1].upper()
            sonKonum = iki_hamle[1]
            sonKonum_h = sonKonum[1].upper()
            if not (sonKonum_h in kullanilanList):
                hamleOyuncu1 = input("Lütfen var olan mekan giriniz: ")
                continue
            elif 1 > int(sonKonum[0]) or int(sonKonum[0]) > len(kullanilanList):
                hamleOyuncu1 = input("Lütfen var olan mekan giriniz: ")
                continue
            hata = uzerindenatlama(kullanilanList, sonKonum_h, oncekiKonum, oncekiKonum_h, sonKonum, oyuncuChar, oyuncu2Char)
            if hata:
                hamleOyuncu1 = input(f"Oyuncu {oyuncu}, lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedef konumu giriniz: ")
                continue
            if oncekiKonum[0] != sonKonum[0] and oncekiKonum_h != sonKonum_h:
                hamleOyuncu1 = input("Lutfen yatay veya düşey bir şekilde hareket ediniz!!: ")
                continue
        except IndexError:
            hamleOyuncu1 = input("Lütfen karakterin başlangıç ve son konumlarını giriniz: ")
            continue
        except ValueError:
            hamleOyuncu1 = input("Lütfen önce rakam sonra harf giriniz: ")
            continue
        hatali = False

        iki_hamle = hamleOyuncu1.split(" ")
        oncekiKonum = iki_hamle[0]
        oncekiKonum_h = oncekiKonum[1].upper()
        sonKonum = iki_hamle[1]
        sonKonum_h = sonKonum[1].upper()
        oncekiKonum = oncekiKonum[0]+oncekiKonum_h
        sonKonum = sonKonum[0]+sonKonum_h

        # Yanlis koordinatlara karsi kontrol
        while not oncekiKonum in oyuncuChar:
            print("Lutfen Karakterinizin bulundugu bir konum giriniz!!: ")
            hamleOyuncu1 = input(f"Oyuncu {oyuncu}, lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedef konumu giriniz: ")
            iki_hamle = hamleOyuncu1.split(" ")
            oncekiKonum = iki_hamle[0]
            oncekiKonum_h = oncekiKonum[1].upper()
            sonKonum = iki_hamle[1]
            sonKonum_h = sonKonum[1].upper()
            oncekiKonum = oncekiKonum[0]+oncekiKonum_h
            sonKonum = sonKonum[0] + sonKonum_h

        eleme_adayi = "deneme"
        indeks = oyuncuChar.index(oncekiKonum)
        oyuncuChar[indeks] = sonKonum
        # Eğer elenecek başka karakterler de varsa onları bu şekilde elenecek karakter bitene kadar döngüye sokarak hallediyoruz.
        while eleme_adayi != "bos":
            eleme_adayi = Elenme(sonKonum, oyuncuChar, oyuncu2Char, kullanilanList)
            if eleme_adayi != "bos":
                print(f"{eleme_adayi} konumundaki taş elendi.")
                oyuncu2Char.remove(eleme_adayi)
            hatali = False
    return oyuncuChar


def Ayirici(kullanListe: list):
    ayiriciCizSay = len(kullanListe)*4+5
    ayirici = ["-"]*ayiriciCizSay

    print()
    for ayir in ayirici:
        print(ayir, end="")
    print()
    return ""


def OyunTablosuYazdir(oyuncu1Char: list, oyuncu1, oyuncu2, oyuncu2Char: list, oyunBoyutu: int, kullanListe: list):
    # Burada Tablonun üzerindeki harfleri yazdırmak için
    print("    ", end="")
    for harf in kullanListe:
        print(harf, end="   ")
    # Bu ayirici cizgiler
    Ayirici(kullanListe)
    # Rakam ve karakter bölümünü yazdırmak için
    for num in range(oyunBoyutu):
        numara = str(num+1)
        print(numara, end=" |")

        for sira in kullanListe:
            Mekan = numara+sira
            char = ""

            if Mekan in oyuncu1Char:
                char = oyuncu1
            elif Mekan in oyuncu2Char:
                char = oyuncu2
            if char == "":
                print(" " + char + "  |", end="")
            else:
                print(" " + char + " |", end="")
        print(" ", numara, end="")
        Ayirici(kullanListe)

    print("    ", end="")
    for harf in kullanListe:
        print(harf, end="   ")
    print()


def oyna():
    istek = True
    while istek:
        oyuncu1 = input("1. oyuncuyu temsil etmek için bir karakter giriniz: ")
        while not oyuncu1.isalnum():
            oyuncu1 = input("1. oyuncuyu temsil etmek için boş karakter giremezsiniz: ")
        oyuncu2 = input("2. oyuncuyu temsil etmek için bir karakter giriniz: ")

        while not oyuncu2.isalnum():
            oyuncu2 = input("2. oyuncuyu temsil etmek için boş karakter giremezsiniz: ")

        oyunBoyutu = (input("Başlangıç oyun alanı boyutu belirleyin [4-8]: "))
        while True:
            try:
                oyunBoyutu = int(oyunBoyutu)
                if not oyunBoyutu in [4, 5, 6, 7, 8]:
                    oyunBoyutu = (input("Lütfen 4 ile 8 aralığında giriniz: "))
                    continue
            except:
                oyunBoyutu = (input("Lütfen 4 ile 8 aralığında rakam giriniz: "))
                continue
            break
        HarfListesi = [["A", "B", "C", "D"], ["A", "B", "C", "D", "E"], ["A", "B", "C", "D", "E", "F"], ["A", "B", "C", "D", "E", "F", "G"], ["A", "B", "C", "D", "E", "F", "G", "H"]]
        kullanListe = HarfListesi[oyunBoyutu-4]
        oyuncu1Char = []
        oyuncu2Char = []

        for num in kullanListe:
            # Başlangıç pozisyonunda karakterlerin konumu
            numara = "1"
            oyuncu1Mekan = numara + num
            oyuncu1Char.append(oyuncu1Mekan)
            numara = str(oyunBoyutu)
            oyuncu2Mekan = numara + num
            oyuncu2Char.append(oyuncu2Mekan)

        OyunTablosuYazdir(oyuncu1Char, oyuncu1, oyuncu2, oyuncu2Char, oyunBoyutu, kullanListe)
        oyun_modu = True
        oyun_sayisi = 1

        while oyun_modu:
            char_sayi_1 = len(oyuncu1Char)
            char_sayi_2 = len(oyuncu2Char)
            oyuncu_sirasi = oyun_sayisi % 2
            # Bir karakter kalan taraf kaybediyor.
            if char_sayi_1 <= 1:
                print(f"Oyun bitti,{oyuncu2} oyuncusu kazandı.")
                break
            elif char_sayi_2 <= 1:
                print(f"Oyun bitti,{oyuncu1} oyuncusu kazandı.")
                break
            if oyuncu_sirasi == 1:
                oyuncu1Char = Hamle(oyuncu1, oyuncu1Char, oyuncu2Char, kullanListe)
                OyunTablosuYazdir(oyuncu1Char, oyuncu1, oyuncu2, oyuncu2Char, oyunBoyutu, kullanListe)
            else:
                oyuncu2Char = Hamle(oyuncu2, oyuncu2Char, oyuncu1Char, kullanListe)
                OyunTablosuYazdir(oyuncu1Char, oyuncu1, oyuncu2, oyuncu2Char, oyunBoyutu, kullanListe)
            oyun_sayisi += 1

        sorgu = input("Tekrar oynamak istermisiniz (e/E;h/H): ")
        while not sorgu in ["e", "E", "h", "H"]:
            sorgu = input("Lutfen dogru harfi giriniz: ")
        if sorgu in ["h", "H"]:
            istek = False


oyna()
