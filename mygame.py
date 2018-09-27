import random
import time
def start():
    while True:
        print("Oyuna yeni başlıyoruz..")
        print("Önünde üç kapı var")
        print("Bunların birisi sayısal diğeri sözel sorular soruyor")
        print("3. ise direk kaybettiriyor")
        print("OYUN BAŞLIYOR....")
        time.sleep(3)
        print("Kapı seçiliyor...")
        time.sleep(2)
        secim = random.randint(0,3)
        
        
        if secim == 1:
            print("Sayisal kapı seçildi")
            sayisal()
        elif secim==2:
            print("Sözel kapı seçildi")
            sozel()
        elif secim==3:
            print("Oyunu başlamadan kaybettin :-))))) ")
            print("Oyun yeniden başlıyor")
            start()
        else:
            print("Bir hata oluştu..")

def sayisal():
    #sayisal sorular soracak
    print("Sayısal kapısı açıldı")
    for x in range(0,4):
        ilk_sayi=random.randint(0,9)
        ikinci_sayi=random.randint(0,9)
        sonuc=ilk_sayi*ikinci_sayi
        print(f"{ilk_sayi} ile {ikinci_sayi}'nin çarpımı nedir" )
        giris=int(input(">>> "))

        if giris==sonuc:
            print(f"{giris} doğru")
            x=1+x
        else:
            print(f"{giris} yanlış")
            
            
        
    

    


def sozel():
    #Sozel sorular soracak
    print("Sözel kapısı açıldı")

    Cumhuriyet_ilani="29Ekim1923"
    Anayasa_kabulu="20Nisan1924"
    Lozan_imzalanmasi="25Temmuz1923"
    Meclisin_Kurulusu="23Nisan1920"
     
    
    

    sorular = ['Cumhuriyet ne zaman kuruldu?', 'Anayasa ne zaman kabul edildi?', 'Lozan ne zaman imzalandı?','Meclis na zaman kuruldu?']
    cevaplar = [Cumhuriyet_ilani,Anayasa_kabulu,Lozan_imzalanmasi,Meclisin_Kurulusu]
    """for q, a in zip(questions, answers):
        print('{0} {1}.'.format(q, a))"""
    index=random.randint(0,3)
    for i in range(2):
        print(sorular[index])
        cevap=input(">>")
        yer = cevaplar.index(cevap)
        if yer==index:
            print("Cevap doğru")
            i=i+1
        else:
            print("Yanlış Cevap")
       
            
        
        
    
    
   
    
    

    

    
    



sozel()
            
        
