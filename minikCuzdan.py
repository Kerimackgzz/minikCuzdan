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


mevcut_bakiye = 0
islem_listesi = []
kullanici_adi = input("Hoşgeldiniz! Kullanıcı adınız: ")
print(f"Merhaba {kullanici_adi}!")

while True:
    print("\n--- MENÜ ---")
    print("1: Para yatır")
    print("2: Para çek")
    print("3: Bakiye göster")
    print("4: İşlem geçmişi")
    print("5: Çıkış")
    
    secim = input("Seçim: ")
    
    if secim == "1":
        try:
            yatirilacak_miktar = float(input("Yatırılacak miktar: "))
        except ValueError:
            print("Geçerli bir sayı giriniz!")
            continue
        
        sonuc = para_yatir(mevcut_bakiye, yatirilacak_miktar)
        
        if isinstance(sonuc, str):
            print(sonuc)
        else:
            mevcut_bakiye = sonuc
            print("Para yatırıldı")
            islem_listesi.append(f"{yatirilacak_miktar} TL yatırıldı")
    
    elif secim == "2":
        try:
            cekilecek_miktar = float(input("Çekilecek miktar: "))
        except ValueError:
            print("Geçerli bir sayı giriniz!")
            continue
        
        sonuc = para_cek(mevcut_bakiye, cekilecek_miktar)
        
        if isinstance(sonuc, str):
            print(sonuc)
        else:
            mevcut_bakiye = sonuc
            print("Para çekildi")
            islem_listesi.append(f"{cekilecek_miktar} TL çekildi")
    
    elif secim == "3":
        print(f"Mevcut bakiye: {mevcut_bakiye} TL")
    
    elif secim == "4":
        if len(islem_listesi) == 0:
            print("Henüz işlem yok")
        else:
            for islem in islem_listesi:
                print(islem)
    
    elif secim == "5":
        print(f"Hoşçakal {kullanici_adi}!")
        break
    
    else:
        print("Geçersiz seçim!")