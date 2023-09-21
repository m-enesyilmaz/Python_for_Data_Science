"""
- Fonksiyonlar
- Docstring
- Fonksiyon Okuryazarlığı
- Return#

- Koşullar-Döngüler
- If
- Else & If
- For Döngüsü
- Break & While & Continue
- Enumurate
- Zip
- Lambda & Filter & Reduce

"""

##################################################################################
#                              FUNCTIONS
##################################################################################

# Fonksiyon nedir?

"""
Bir fonksiyon, belirli bir işi gerçekleştirmek için tasarlanmış bir kod bloğudur. 
İçine verilen girdileri alır, bu girdileri işler ve belirli bir çıktıyı üretir.

Programlamada fonksiyonlar da belirli bir görevi yerine getirmek için tasarlanmıştır ve bize istediğimiz sonuçları sunar.


"""


# Parametre nedir? Argüman nedir?

"""
Parametre : Tanımlama esnasındaki temsildir.
Argüman : Parametreyi kullandığımızda argüman olur.

"""

"""
# def function_name(parameters/arguments):
#     statements (function body)
"""

def function_name(parameters,arguments):
    # statements(function_body)
    pass


# Print/Return ?

#######################
# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak
######################

"""
Return yaptığımızda igili objeyi dışarıya çıkarabiliyoruz. Diğer durumda fonksiyondan hiçbir bilgiyi dışarı çıkaramayız.
"""

def calculate_area(length, width):
    return length * width

rectangle_area = calculate_area(10, 5)
print(rectangle_area)


def calculate_area(length, width):
    print(length * width)

rectangle_area = calculate_area(10, 5)
print(rectangle_area)




# Rakamlar arasından ortalamayı hesaplamak
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

sayilar = [85, 90, 92, 88, 95]
average_grade = calculate_average(sayilar)
print(average_grade)

#

def yashesapla(dogumyili):
    return 2023-dogumyili


def emeklilikhesap(dogumyili,isim):
    yas = yashesapla(dogumyili)
    emeklilik = 65- yas
    if emeklilik > 0 :
        print(f'emekliliğe {emeklilik} yıl kaldı')
    else:
        print("Emekli oldunuz")


emeklilikhesap(1989,'Gürkan')


# Yaş, sigorta ve çalışma yılına uygun emeklilik hesap fonksiyonu

def emeklilik_yas_hesabi():
    def emeklilik_yasi(calisma_yili):
        if calisma_yili >= 25:
            return 60
        else:
            return 65

    def uygunluk_durumu(age, insurance, calisma_yili):
        if age >= emeklilik_yasi(calisma_yili) and insurance == True:
            return "Emekli olabilirsiniz."
        else:
            return "Emekli olma şartlarınızı sağlamıyorsunuz."

    return uygunluk_durumu


uygunluk_durumu = emeklilik_yas_hesabi()
age = 34
insurance = True
calisma_yili = 11
result = uygunluk_durumu(age, insurance, calisma_yili)
print(result)


# Bir hesap makinesi fonksiyonu kullanarak, toplama ve çıkarma işlemlerini gerçekleştiren bir hesap makinesi uygulaması

def hesap_makinesi():
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    return add, subtract


toplama, cikarma = hesap_makinesi()
num1 = 10
num2 = 5
toplama_sonucu = toplama(num1, num2)
cikarma_sonucu = cikarma(num1, num2)
print("Toplama Sonucu:", toplama_sonucu)
print("Çıkarma Sonucu:", cikarma_sonucu)


##################################################################################
#                              CONDITIONS
##################################################################################

# IF -ELSE

def sayi_kontrol(sayi):
    if sayi % 2 == 0:
        print(f"{sayi} çift bir sayıdır.")
    else:
        print(f"{sayi} tek bir sayıdır.")

sayi_kontrol(10)

kullanici_sayi = int(input("Bir sayi giriniz:"))
sayi_kontrol(kullanici_sayi)


"""kullanici_sayisi = int(input("Bir sayı girin: "))
sayi_kontrol(kullanici_sayisi)
"""

# For Döngüsü

"""
Python'da for döngüsü, bir iterable (tekrarlanabilir) nesne üzerinde çalışır ve her döngü adımında bir elemana erişir.

for eleman in iterable:

"""


liste = [2, 5, 8, 3, 1, 6]

for sayi in liste:
    print(sayi**2)


# Liste içindeki çift sayıları bulmak
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for sayi in liste:
    if sayi % 2 == 0:
        print(sayi)


# Fonksiyon - For Döngüsü ve If/Else Koşulu
def kontrol_fonksiyonu(sayilar):
    for eleman in sayilar:
        if eleman > 5:
            print(f"{eleman} 5'ten büyüktür.")
        elif eleman < 5:
            print(f"{eleman} 5'ten küçüktür.")
        else:
            print(f"{eleman} 5'e eşittir.")

liste = [2, 5, 8, 3, 1, 6]
kontrol_fonksiyonu(liste)

# Örnekler

for i in range(1,11):
    for j in range(1,11):
        carpim=i*j
        print(f'{i} x {j} = {carpim}')
    print("----")

# Çarpım Tablosu
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 1 x 6 = 6
# 1 x 7 = 7
# 1 x 8 = 8
# 1 x 9 = 9
# 1 x 10 = 10
# --------------------

"""
for i in range(1, 11):
    for j in range(1, 11):
        carpim = i * j
        print(f"{i} x {j} = {carpim}")
    print("--------------------")
"""




# Üçgen Sayılar
# [1,3,6,10,15,21]

for i in range(1,7):
    ucgen_sayi = (i*(i+1))//2
    print(ucgen_sayi)

n = int(input("Kaç terimli üçgen sayısı bulmak istersin?"))


"""
n = int(input("Kaç terimli üçgen sayılarını bulmak istiyorsunuz? "))

for i in range(1, n + 1):
    ucgen = (i * (i + 1)) // 2
    print(ucgen)
"""

# Palindromik Sayılar
# 22
# 33
# 44
# 55
# 66
# 77
# 88
# 99

"""
baslangic = int(input("Başlangıç sayısını girin: "))
bitis = int(input("Bitiş sayısını girin: "))

for sayi in range(baslangic, bitis + 1):
    sayi_str = str(sayi)
    ters_str = sayi_str[::-1]
    if sayi_str == ters_str:
        print(sayi)
"""

sayi_str = str(212)
sayi_str[::-1]

212

basla = int(input("Başlangıç sayısını seçiniz:"))
bitis = int(input("Bitiş sayısını seçiniz"))

for sayi in range(10,250):
    sayi_str = str(sayi)
    ters_str = sayi_str[::-1]
    if sayi_str == ters_str:
        print(sayi)

for sayi in range(basla, bitis):
    sayi_str = str(sayi)
    ters_str = sayi_str[::-1]
    if sayi_str == ters_str:
        print(sayi)


# Break - Continue - While

# break?


# continue
"""
Döngüyü atla
"""

# while

"""
break ifadesi bir döngüyü tamamen sonlandırmak için kullanılırken, 
continue ifadesi bir döngü adımını atlayarak bir sonraki adıma geçmek için kullanılır. 
while döngüsü ise belirli bir koşul sağlandığı sürece döngüyü tekrarlar.

"""

# Sample 1
i = 1
toplam = 0
while i <= 10:
    if i == 6:
        i += 1
        continue
    toplam += i
    i += 1
print("Toplam:", toplam)


# Sample 2
toplam = 0
while True:
    sayi = int(input("Bir sayı girin: "))
    if sayi < 0:
        break
    toplam += sayi
print("Toplam:", toplam)

""""
while döngüsü sonsuz bir döngü olarak başlıyor (while True). Kullanıcıdan sürekli olarak bir sayı girmesini istiyoruz
"""


# Enumerate : Otomatik Index ile for loop

"""
enumerate() fonksiyonu, bir iterable (tekrarlanabilir) nesne üzerinde indeksleriyle birlikte 
döngü yapmayı sağlayan bir Python fonksiyonudur. 

enumerate(iterable, start=0)

"""


players = ["modric","kross","iniesta","xavi"]

for i in players:
    print(i)


for index, person in enumerate(players):
    print(index+1 ,person)



# Sample
kelimeler = input("Kelime listesini girin (virgülle ayırın): ").split(",")

for indeks, kelime in enumerate(kelimeler,1):
    print(indeks, kelime.strip())


#######################
#  Lambda
#######################

# lambda arguments : expression

kare = lambda x: x ** 2
print(kare(4))


carpimlar = []
for i in range(1, 6):
    carpimlar.append((lambda x: x * i)(2))
print(carpimlar)

"""
lambda ifadesi, basit veya tek seferlik kullanımlar için hızlı bir şekilde bir fonksiyon tanımlamak için kullanılır. 
Genellikle, kısa ve basit fonksiyonları belirli bir ifade veya işlem için kullanırken tercih edilir. 
"""


def func(n):
  return lambda a : a ** n

square = func(2)
print(square(7))


"""
map() fonksiyonu ile bu fonksiyonları bir iterable üzerinde uygulayarak yeni bir iterable oluşturuyoruz. 
Benzer şekilde, filter() fonksiyonu ile de belirli bir koşulu sağlayan elemanları bir iterable'dan filtreleyebiliyoruz.

map() fonksiyonu, bir iterasyon yapısı üzerinde belirli bir işlemi uygulayarak yeni bir iterasyon yapısı oluştururken, 
filter() fonksiyonu belirli bir koşulu sağlayan elemanları seçerek yeni bir iterasyon yapısı oluşturur.

"""
# Sample 1
liste1 = [1, 2, 3, 4, 5]
liste2 = [10, 20, 30, 40, 50]

toplam = list(map(lambda x, y: x + y, liste1, liste2))
print(toplam)


# Sample 2
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tekler = list(filter(lambda x: x % 2 != 0,liste))
print(tekler)
