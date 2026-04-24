def para_cek(mevcut_bakiye, cekilecek_miktar):
    if mevcut_bakiye < 0:
        return "Mevcut bakiye geçersiz"
    if cekilecek_miktar <= 0:
        return "Geçersiz miktar"
    if cekilecek_miktar > mevcut_bakiye:
        return "Yetersiz bakiye"
    return mevcut_bakiye - cekilecek_miktar


def para_yatir(mevcut_bakiye, yatirilacak_miktar):
    if mevcut_bakiye < 0:
        return "Mevcut bakiye geçersiz"
    if yatirilacak_miktar <= 0:
        return "Geçersiz miktar"
    return mevcut_bakiye + yatirilacak_miktar


def kullanici_ekle(kullanicilar, yeni_ad):
    kullanicilar[yeni_ad] = {"bakiye": 0, "islemler": []}
    print(f"{yeni_ad} eklendi")


kullanicilar = {}
aktif_kullanici = None

while True:
    
    if aktif_kullanici is None:
        ad = input("Kullanıcı adınız: ")
        if ad in kullanicilar:
            print(f"Hoşgeldin {ad}")
        else:
            kullanicilar[ad] = {"bakiye": 0, "islemler": []}
            print(f"Yeni hesap oluşturuldu: {ad}")
        aktif_kullanici = ad
        continue
    
    print(f"\n--- MENÜ ({aktif_kullanici}) ---")
    print("1: Para yatır")
    print("2: Para çek")
    print("3: Bakiye göster")
    print("4: İşlem geçmişi")
    print("5: Yeni kullanıcı oluştur")
    print("6: Kullanıcı değiştir")
    print("7: Çıkış")
    
    secim = input("Seçim: ")
    
    if secim == "1":
        try:
            yatirilacak_miktar = float(input("Yatırılacak miktar: "))
        except ValueError:
            print("Geçerli bir sayı giriniz!")
            continue
        
        sonuc = para_yatir(kullanicilar[aktif_kullanici]["bakiye"], yatirilacak_miktar)
        
        if isinstance(sonuc, str):
            print(sonuc)
        else:
            kullanicilar[aktif_kullanici]["bakiye"] = sonuc
            print("Para yatırıldı")
            kullanicilar[aktif_kullanici]["islemler"].append(f"{yatirilacak_miktar} TL yatırıldı")
    
    elif secim == "2":
        try:
            cekilecek_miktar = float(input("Çekilecek miktar: "))
        except ValueError:
            print("Geçerli bir sayı giriniz!")
            continue
        
        sonuc = para_cek(kullanicilar[aktif_kullanici]["bakiye"], cekilecek_miktar)
        
        if isinstance(sonuc, str):
            print(sonuc)
        else:
            kullanicilar[aktif_kullanici]["bakiye"] = sonuc
            print("Para çekildi")
            kullanicilar[aktif_kullanici]["islemler"].append(f"{cekilecek_miktar} TL çekildi")
    
    elif secim == "3":
        print(f"Mevcut bakiye: {kullanicilar[aktif_kullanici]['bakiye']} TL")
    
    elif secim == "4":
        if len(kullanicilar[aktif_kullanici]["islemler"]) == 0:
            print("Henüz işlem yok")
        else:
            for islem in kullanicilar[aktif_kullanici]["islemler"]:
                print(islem)
    
    elif secim == "5":
        yeni_ad = input("Yeni kullanıcı adı: ")
        if yeni_ad in kullanicilar:
            print("Bu kullanıcı zaten var!")
        else:
            kullanici_ekle(kullanicilar, yeni_ad)
    
    elif secim == "6":
        aktif_kullanici = None
        continue
    
    elif secim == "7":
        print(f"Hoşçakal {aktif_kullanici}!")
        break
    
    else:
        print("Geçersiz seçim!")