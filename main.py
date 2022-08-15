# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:08:43 2021

@author: Abdurrahman
"""

isim = ("Ahmet")
isim2 = ("ahmet")
isim.upper()  # >>	AHMET
isim2.upper()  # >>	AHMET
isim.lower()  # >> ahmet
isim2.lower()
isim.islower()  # >>	False
isim2.islower()

isim.replace('a', 'o')
isim2.replace('a', 'E')

# Strip(): karekter dizilerinde kırpma işlemleri için kullanılan strip metoduna

isim_sehir = '  Diy arbakır Şe hri'
isim_sehir.strip()  # >> DiyarbakırŞehri

isim_sehir = 'Diy*ar*b*ak**ırSehri'
# isim_sehir.strip(*) #'DiyarbakırŞehri'


dir(isim_sehir)  # >> Değişkene uygulanabilecek fonksiyonları verir

isim_sehir[0]  # >> D
isim_sehir[1]  # >> i
isim_sehir[0:5]  # >> Diyar		0’ dan 5 e kadar

'a' * 4
5 * 5

# []
# list()

notlar = [90, 80, 70, 50]
type(notlar)
notlar
notlar2 = [[1, 2, 3], [4, 52, 30], [5, 6, 11]]
notlar2[0][1]

liste = ["a", 19.3, 90]
liste = ["a", 19.3, 90, notlar]

type(liste)

# LISTENIN KAÇ ELEMANI VARDIR||||||||||||||||||||||||||||||||||||||
# len(X)
len(liste)
# LISTENIN KAÇ ELEMANI VARDIR||||||||||||||||||||||||||||||||||||||

liste[2]

type(liste[2])
# LISTENIN 0 ELEMANI HANGI VERI TIPINDEDIR||||||||||||||||||||||||||||||||||||||
len(liste[0])
len(liste)

liste2 = [21, 123, 33, 41]
liste3 = ['a', 'b', 'd', 'u', 'r']

# LISTE NASIL SILINMEKTEDIR|||||||||||||||||||||||||||||||||||||

del liste  # iş bittikten sonra listeyi silmek için

# OZET OZET OZET
# LISTE NASIL SILINMEKTEDIR|||||||||||||||||||||||||||||||||||||
# ELEMAN NASIL SILINMEKTEDIR||||||||||||||||||||||||||||||||||||
a = 0
del a
# ELEMAN NASIL SILINMEKTEDIR VE EKLENMEKTEDIR||||||||||||||||||||||||||||||||||||

del notlar[0]
notlar.remove(80)  # 80 ELEMANINI SILDI
notlar.append(80)  # SONA EKLEDI
notlar.append(80, 0)  # YANLIS
notlar.insert(0, 99)  # BAŞA EKLEME İŞLEMİ
notlar.pop(8)  # 8.elemanı silme işlemi
notlar.append(80)
notlar.count(80)  # KAÇ TANE 80 VAR
# ELEMAN NASIL SILINMEKTEDIR VE EKLENMEKTEDIR||||||||||||||||||||||||||||||||||||
notlar.extend('ceyda')  # CEYDA HARF HARF EKLENDI
notlar.sort()  # KÜCÜKTEN BUYUGE DOGRU SIRALAMA
notlar.reverse()  # TERS SIRALAMA
notlar_yedek = notlar.copy()  # NOTLARI YEDEKLEMEK
len(notlar)
notlar[4:]  # BAŞTAN 5.VERI VE SONRASI
notlar[:6]  # ILK 6 'ADET' VERI YANI 0. veri 1.adet
notlar[4:6]  # BAŞTAN 5 'DEN 6. VERIYE KADAR
notlar[-6:]  # SON 6 VERI
notlar[-2:]  # SON IKI VERI (baştan sona sıralama ile)
notlar[:-2]  # SON IKI VERI OLMADAN LISTE
notlar[-6:6]  # sondan 6.veri ile ilkten 6.veri arası
notlar.index(80)  # KAÇINCI INDEXTE KAYITLIDIR?
notlar.index('c')
tuple1 = ("a", "b", "c")  # TUPLE VERILERI DEĞİŞTİRİLEMEZ, TEKRAR TANIM GEREK
tuplea = (5)  # tek veri olursa STRING/INTIGER OLURLAR
type(tuplea)
tuple1[0:2]
yeni = tuple1[0:2]

liste2[:2]
liste3[:4]

liste4 = [liste2, liste3, 123, 12222]

liste4[1][2]

liste_isimler = ["abdullah", "ayse", "selen"]

liste_isimler[0] = liste_isimler[0] + ' bir kral'

liste_isimler[0]

# YADA YADA YADA YADA

liste_isimler[0] = "abdullah bir aslan"

liste_isimler[0]

liste_isimler + ["kemal"]

# EKLENDI AMA ATAMASI YAPILMADI

liste_isimler = liste_isimler + ["kemal"]

# LİSTEDEN ELEMAN SİLME /////////////////////////////////////////////////

del liste_isimler[2]
liste_isimler

# LİSTELER İLE İLGİLİ METHODLARI MERAK
# EDIYORSAK EĞER YAPACAĞIMIZ ŞEY BELLIDIR


dir(liste_isimler)

# DIREKT EKLEDI BENIM TEKRAR ATAMA YAPMAMA
# GEREK KALMADAN BU METHODLA KENDISI EKLEYIP
# ATAMA YAPABILIYOR////////////////////////////////////////////

liste_isimler.append("berkcan")
liste_isimler
type(liste_isimler)

liste_isimler.remove("berkcan")
liste_isimler

liste_isimler.insert(0, "emine")

liste_isimler

liste_isimler[0] = ('fatma')
liste_isimler

# ÜSTTELI METHODU KULLANINCA EKLEDI
# ALTTAKINI KULLANINCA YERLERINI DEGISTIRDI


liste_isimler.insert(2, "baban")
liste_isimler

liste_isimler.insert(4, "hele ninno")
liste_isimler

# LISTE UZUN OLURSA KAÇINCIDA OLDUĞUNU BILMEK ZOOOR

liste_isimler.insert(len(liste_isimler), "deneme")
liste_isimler

# pop BELIRLENEN ELEMANI LISTEDEN SILME

liste_isimler.pop(4)
liste_isimler

liste_yeni = ["selen", "buse", "mine", "selen", "buse"]

# KAÇ TANE OLDUĞUNU SAYDIRMA

liste_yeni.count("selen")

liste_yeni.count("buse")
liste_yeni.count("mine")

# COPY FONKSIYONU YEDEKLEMEK KOPYALAMAK İÇİN


liste_yedek = liste_yeni.copy()
liste_yedek

# EXTEND METHODU, LISTEYE BIRŞEYLER EKLEDI

liste_yeni.extend(["pü", "rezill", "canavar", "22"])
liste_yeni

liste_yeni.append(["e bu da aynı değil mi", "?"])
liste_yeni

# DEĞİLMİŞ ÇÜNKÜ BU YENI BİR LİSTE
# OLUŞTURUP LİSTEYİ LİSTEYE EKLİYOR
# EXTEND İSE DİREKT EKLİYOR !!!!

# YADA BİR SANIYE ?!??

a = len(liste_yeni)  # HATA
liste_yeni.remove(a)  # HATA

# liste_yeni.del(len(liste_yeni)) #HATA

del liste_yeni[len(liste_yeni)]  # HATA

# SÖYLEMEYI UNUTTUM ŞUANDA LISTENIN SON
# ELEMANINI SILMEYE ÇALIŞIYORUM :D :D

del liste_yeni[len(liste_yeni)]  # HATA

del liste_isimler[a]  # HATA
del liste_isimler[10]  # HATA

# DUR LAN NIYE ?!?

len(liste_isimler)  # 10 değil 8 eleman var

# liste


liste_yeni.append("ceyda")
liste_yeni
liste_yeni.remove("ceyda")

# EXTEND EXTEND EXTEND EXTEND EXTEND EXTEND EXTEND EXTEND EXTEND

liste_yedek.extend("eymen")  # HARF HARF YAZDIRDI
liste_yedek

# IKI LISTEYI BIRLEŞTIRMEK İÇİN KULLANILIR

liste_yedek.extend("CAN123", "HA")  # AYNI ANDA IKI TANE EKLETMIYOR
liste_yedek

liste_yedek.extend(["eymen", "Hasan"])  # Listeye ALINCA EKLIYOR
liste_yedek

# APPEND APPEND APPEND APPEND APPEND APPEND APPEND APPEND APPEND


# LISTENIN SONUNA EKLER
liste_yeni.append("ceyda", "HASAN")  # AYNI ANDA IKI TANE EKLETMIYOR
liste_yeni
liste_yeni.append(["ceyda", "HASAN"])  # Listeye alınca LİSTE OLARAK EKLIYOR LISTEYE DAHIL ETMIYOR
liste_yeni

# REMOVE REMOVE REMOVE REMOVE REMOVE REMOVE REMOVE REMOVE REMOVE REMOVE REMOVE REMOVE


liste_yeni.remove("HASAN")  # HASAN LISTEDE YOK DEDI ÇÜNKÜ ELEMAN OLARAK DAHIL DEGIL
liste_yeni

liste_yeni.remove("mine")  # MINE SILINDI
liste_yeni

liste_yeni.remove("rezil", "22")  # REMOVE SADECE TEK DOSYAYI SILER HATASI VERIYOR

del liste_yeni("rezil", "22")  # DEL BU ŞEKİLDE KULLANILAMAZ HATASI

dir(liste_yeni)
liste_yeni.clear("rezil", "22")  # OLMADI
liste_yeni.clear()  # LISTENIN IÇİNI TEMIZLEDI
liste_yeni

# SORT SORT SORT  SORT  SORT  SORT  SORT  SORT  SORT  SORT  SORT  SORT  SORT

sayılar = ['0', '5', '2']  # STRING
sayılar.sort()  # KÜCÜKTEN BUYUGE DOGRU SIRALAMA
sayılar

sayılar2 = [1, 42, 22]  # INT
sayılar2.sort()  # KÜCÜKTEN BUYUGE DOGRU SIRALAMA
sayılar2

type(sayılar[1])  # STRING
type(sayılar2[1])  # INT

# INSERT INSERT INSERT INSERT INSERT INSERT INSERT INSERT INSERT INSERT INSERT INSERT

# BELIRLI BIR NOKTAYA ELEMAN EKLEMEK IÇINDIR

sayılar.insert(2, 31)  # 2.HUCREYE 31 SAYISINI EKLE
sayılar

# POP POP POP POP POP POP POP POP POP POP POP POP POP POP POP POP POP POP POP POP POP

# SILMEK İÇİNDİR


sayılar.pop(0, 1)  # YALNIZCA TEK ARGUMAN OLABILIR HATA
sayılar

sayılar.pop([0, 1])  # BOYLE BIR LISTE YOK HATASI

sayılar.pop(3)  # 3. HUCRE SILINDI
sayılar

# COUNT COUNT COUNT COUNT COUNT COUNT COUNT COUNT COUNT COUNT COUNT COUNT COUNT COUNT COUNT COUNT

# LISTEDE O MADDEDEN KAÇ TANE VAR?


isimler = ("ali", "ali", "buse")
isimler.count("ali")  # 2 TANE

# COPY COPY COPY COPY COPY COPY COPY COPY COPY COPY COPY COPY COPY COPY COPY COPY COPY COPY COPY

# LISTEYI YEDEKLEMEK İÇİNDIR

aaa = isimler.copy()  # ISIMLER LISTE TIPINDE OLMADIĞI İÇİN OLMADI

yedek = sayılar.copy()  # OLDU AYNISINI YEDEK ADINDA YENIDEN KAYDETTI
yedek

# INDEX INDEX INDEX INDEX INDEX INDEX INDEX INDEX INDEX INDEX INDEX INDEX INDEX INDEX INDEX INDEX INDEX

# KAÇINCI INDEXE HUCREYE KAYIT EDILDIĞINI SÖYLÜYOR

liste2.index("33")  # HATA LISTEDE BU YOK

liste2.index('33')  # HATA LISTEDE BU YOK

liste2.index(33)  # 2. INDEXE KAYITLI

# REVERSE REVERSE REVERSE REVERSE REVERSE REVERSE REVERSE REVERSE REVERSE REVERSE REVERSE REVERSE REVERSE

# TERSTEN SIRALIYOR SIRALAMAYI TERSE ÇEVIRIYOR

liste2
liste2.reverse()
liste2

# SORT SORT SORT SORT SORT SORT SORT SORT SORT SORT SORT SORT SORT SORT SORT SORT SORT SORT SORT SORT SORT

# KÜÇÜKTEN BÜYÜĞE DOGRU SIRALADI

liste2.sort()
liste2

# CLEAR LISTENIN İÇİNI TEMIZLIYOR


# TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE
# TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE
# TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE TUPLE

# VERI YAPISI-TUPLE (DEMET) OLUŞTURMA

# 1- KAPSAYICIDIRLAR, FARKLI VERI TIPLERINI KAPSAYABILIRLER
# 2- SIRALIDIR, İÇİNDE İNDEX İŞLEMLERİ YAPILABILIR
# 3- DEĞİŞTİRİLEMEZDIR!!!, LISTELERDE İSE DEĞİŞTİRİLEBİLİRDİ

t = ("1", "2", 3, "Hasan")  # DUZ PARANTEZE ALINARAK YAPILIR

t = "1", "2", 3, "Hasan", [2, 3214, 12, "ASAS"]  # PARANTEZE ALINMADAN OLUŞTURULUR

t = "aslan"
type(t)  # STRING DONDU ÇÜNKÜ TEK ELEMANDA BÖYLE OLUYOR

t = "BUSE",  # Sonuna virgül koyunca TUPLE FORMATINDA KAYDETTİ
type(t)

# VERI YAPISI-TUPLE ELEMAN İŞLEMLERI

t
dir(t)

t = ("Ahmet", "Mehmet", "Can")
t[2]  # LISTELERDEKI GIBI ÇAĞIRILIR

t[2] = 1  # HATA VAR  ATAMA KABUL ETMEZ

# TUPLER BITTI TUPLER BITTI TUPLER BITTI


# SOZLUKLER SOZLUKLER SOZLUKLER


# DERS-1 ve DERS-2

# LİSTELER KAPSAYICI DEĞİŞTİRİLEBİLİR VE SIRALI
# TUPLE LAR KAPSAYICI DEĞİŞTİRİLEMEZ VE SIRALI
# SOZLUKLER KAPSAYICI DEĞİŞTİRİLEBİLİR VE SIRASIZ

# ANAHATAR SOZCUK ANAHTAR DEGER VE KARŞILIKLARI ŞEKLİNDEDİR


# önce key değerleri girilir
sozluk = {"REG": "Regresyon Modeli",
          "LOJ": "LOJISTIK Regresyon",
          "CART": "Classification and Reg"}

# SATIR SATIR F9 a BASARAK ÇALIŞTIRMAZSIN ÇÜNKÜ TEK SATIRDA BİTMİYOR
# ŞAŞIRMAYAYIM DIYE YAZIYORUM, HEPSINI SEÇIP F9 YAP

sozluk

len(sozluk)  # IÇERISINDE KAÇ IFADE VAR

sozluk = {"REG": 10,
          "LOJ": 22,
          "CART": 31}

sozluk

sozluk = {"REG": [10, "HELE NINNO"],
          "LOJ": 22,
          "CART": 31}

dir(sozluk)
# SOZLUK OLUŞTURMA FORMULASYONU

SOZLUK_ADI = {"BIRINCI KEY": "DEGER,LISTE"}

# DERS-3 ve DERS-4
# ÇAĞIRMA İŞLEMLERİNDE KARE PARANTEZLERI UNUTMAYALIM


sozluk[0]  # HATA ALDIK ÇÜNKÜ SOZLUKLER SIRASIZDIR
sozluk["REG"]  # ŞIMDI ALINDI,

SOZLUK_ADI = {"BIRINCI_LO": {"RESTRICK": "111",  # SOZLUK ICINDE SOZLUK
                             "OLO": "2231"}}

SOZLUK_ADI

SOZLUK_ADI["BIRINCI_LO"]["OLO"]  # SOZLUK ICINDEKI SOZLUKTEN ELEMAN SEC

# SOZLUGE EKLEME YAPMAK
# ÇOK KOLAY SADECE KÖŞELİ PARANTEZLE İFADEYİ YAZ
SOZLUK_ADI["GBM"] = "Gradient Boosting Mac"
SOZLUK_ADI
# INT EKLE
SOZLUK_ADI[1] = "Yapay Sinir Ağları"
SOZLUK_ADI
# LISTE EKLE
l = [1, 2, 3]
SOZLUK_ADI[l] = "deneme 1"  # HATA VERDI

# LISTLER KEY DEGERI ATANAMAZ ÇÜNKÜ KEY DEGERLERİ SABIT DEGERLERDIR
# EĞER SABIT DEĞERLER OLMAZSA EKLENEMEZ BU YUZDEN LIST OLMAZ

SOZLUK_ADI[tuple] = "olacak mı?"  # OLDU
SOZLUK_ADI

# SETLER(küme) DERS-1 ve DERS-2
# DERS-1- SET OLUŞTURMA
# OZELLIKLER
# SIRASIZDIRLAR!, INDEXI YOKTUR SOZLUKLER GIBI
# SETLER İÇİNDEKİ DEĞERLER EŞSİZDİR TEKRAR EDEMEZ
# DEĞİŞTİRİLEBİLİRLERDİR
# FARKLI TİPLERİ BARINDIRABİLİRLER


# SET OLUSTURMA
s = set()
s
l = [1, "a", "ali", 123]  # LISTE ILE BIRLEŞTIRME
s = set(l)
s

t = ("d", "hasan")  # BIR TUPLE
type(t)
s = set(t)
s

t2 = ("d", "hasan", "d", "c", "c", "c")  # BIR TUPLE
type(t2)
s = set(t2)  # SADECE TEK BIR DEFA ALDI
s
metin1 = "abdurrahman ekici"  # IÇINDEKI KARAKTERLERI TEK TEK ALDI
type(metin1)
d = set(metin1)
d

set2 = set([1, 2, 2])
set2

len(d)
len(s)

d[0]  # hata setlerde sıra yok

# DERS-2- ELEMAN EKLEME ÇIKARMA

liste1 = ["birinci", "abi", "kardeş", "hasan"]

set1 = set(liste1)

dir(set1)

set1.add("mocuk")  # EKLEME IŞLEM
set1

set.difference("a")  # STR OLMAZ
set.difference(1)  # INT OLMAZ
set.difference(liste1)  # LIST OLMAZ TUPLE OLMAZ

set.difference(set1, s)  # set1' de olup s' de olmayan
set.difference(s, set1)  # s de olup set1 de olmayan

set1.add("ahmet")  # ekle
set1.remove("ahmet")  # sil, yoksa hata verir program durur
set1.discard("ahmet")  # sil, yoksa hataVERME

# DERS-3 SETLERDE FARKLAR

# =============================================================================
#     KLASIK KUME işlemleri
#     difference(): Kümelerin farkları
#     intersection(): İki küme kesişimi yada & işareti
#     union(): İki küme birleşimi
#     symmetric_difference()  ikisinde de olmayanlar
#
# =============================================================================

set1
set2 = set[1, 2, "ali"]  # ☻HATA
set2 = set([1, 2, "ali", "hasan"])

set.difference(set1, set2)  # SET1-SET2
set.difference(set2, set1)  # SET2-SET1
set1.difference(set2)  # SET1-SET2
set2.difference(set1)  # SET2-SET1

set.symmetric_difference(set1, set2)  # SET1,SET2 nin FARK kümesi dışındakiler
set.symmetric_difference(set2, set1)

set1.symmetric_difference(set2)

set1
set2

set1 - set2
set2 - set1

# DERS-4 SETLERDE BIRLEŞIM KESIŞIM


set.intersection(set1, set2)  # KESIŞIM KUMESI
set1.intersection(set2)

set1 & set2  # KESIŞIM KISA YOL
kesisim = set1 & set2

set1.union(set2)  # BIRLEŞIM IŞLEMI
birlesim = set1.union(set2)

set1
set2
set1.intersection_update(set2)  # set1=KESIŞIM ELEMANLARI ARTIK
set1

# DERS-5 SETLERDE SORGU IŞLEMLERI
# =============================================================================
#
# set1.isdisjoint(set2) KESIŞIM KUMESI BOŞ MUDUR?
# set1.issubset(set2)   set1 set2 nin ALT KUMESI midir?
# set1.issuperset(set2) set1 set2 yi KAPSIYOR MU
#
#
# =============================================================================

set1.isdisjoint(set2)

set1 = set([1, 2, 3, "ali", "ahmet"])
set2 = set([1, 2, "ceyda", "selen"])
set3 = set([555, "selma"])

set1.isdisjoint(set2)
set1.isdisjoint(set3)

set1.issubset(set2)

set2.issuperset(set1)

# =============================================================================
# LISTELER            TUPLE            SOZLUK              SETLER
#
# DEĞİŞTİRİLEBİLİR    DEĞİŞTİRİLEMEZ  DEĞİŞTİRİLEBİLİR    DEĞİŞEBİLİR
# SIRALI              SIRALI          SIRASIZ             SIRASIZ+EŞSIZ
# KAPSAYICI           KAPYASICI       KAPSAYICI           KAPSAYICI
#
# =============================================================================
set1 = set([5, 7, 9])
set2 = set([5, 6, 7])
set1.union(set2)
