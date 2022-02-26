import time
def hesaplama(tarih="yil", payda=100):
    para = float(input("Yatırmak istediğinizi parayı giriniz: "))
    faiz = float(input("Faiz oranını giriniz :% "))
    tarihSayisi = float(input("Kaç yıl yatırmak istediğinizi giriniz: "))

    getiri = round((para * faiz * tarihSayisi / payda), 2)
    sonuc = round((getiri + para), 2)

    print("{} TL {} faiz oranı ile \n{} {} sürede, ortalama {} getiri getirir ve toplam paranız {} TL olur.".format(round(para), round(faiz), round(tarihSayisi), tarih, round(getiri), round(sonuc)))
def uygulama():
    try:
        programtanitimi = "Bu program faizli paranızın ne kadar olduğunu gösterir."
        print("."*len(programtanitimi), programtanitimi, "."*len(programtanitimi), sep="\n", end="\n\n")

        faizYili = {
            "0":"Aşağıdaki faiz sistemlerinden birini seçiniz:",
            "1": "Günlük faiz hesaplama için 1 tuşuna basınız.",
            "2": "Aylık faiz hesaplama için 2 tuşuna basınız.",
            "3": "Yıllık faiz hesaplama için 3 tuşuna basınız."
        }

        faizTercihi = input("{}\n{}\n{}\n{} \nTercihiniz: ".format(*faizYili.values()))
        if faizTercihi == "1":
            hesaplama("gün", 36500)
        elif faizTercihi == "2":
            hesaplama("ay", 1200)
        elif faizTercihi == "3":
            hesaplama("yıl", 100)
        else:
            print("Lütfen geçerli bir tercih yapınız!")        

    except ZeroDivisionError:
        print("Bir hata oluştu. Lütfen tekrar deneyiniz!")


    finally:
        sayac = 10
        while sayac > 0:
            print("\rSistemden çıkılıyor.. Son {} saniye...".format(sayac), end="")
            time.sleep(1)
            sayac -= 1

uygulama()
