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



mevcut_bakiye=0
  
  
while True:
  
    print("para yatırmak için :1 para çekmek için :2 mevcut bakiyeyi gözlemlemek için :3 uygulamadan çıkmak için:4 ")
    secim=input("seçim giriniz: ")
 
    if (secim=="1"):
        yatirilacak_miktar=float(input("Yatırılacak miktar: "))
        para_yatir(mevcut_bakiye, yatirilacak_miktar)
        mevcut_bakiye = para_yatir(mevcut_bakiye, yatirilacak_miktar) 
        print("para yatırıldı")
       
    if (secim=="2"):
        cekilecek_miktar=float(input("çekilecek miktarı giriniz"))
        para_cek(mevcut_bakiye,cekilecek_miktar)
        mevcut_bakiye = para_cek(mevcut_bakiye, yatirilacak_miktar) 
     
      
        
        print("para çekildi")
    
    if (secim=="3"):
         print(mevcut_bakiye)
    
    if(secim=="4"):
        break;