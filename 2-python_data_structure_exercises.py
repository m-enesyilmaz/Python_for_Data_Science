####################################################################################
#                       DATA STRUCTURE ALIŞTIRMALAR
# ##################################################################################

## GÖREV 1: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. 
# Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
text = "The goal is to turn data into information, and information into insight."
text.upper().replace(","," ").replace("."," ").split()

###---------------------------------###

## GÖREV 2: Verilen liste için aşağıdaki görevleri yapınız.
lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
lst[0]
lst[10]

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.
data_list = lst[0:4]
data_list

# Adım 4: Sekizinci index'teki elemanı silin.
lst.pop(8)
lst

# Adım 5: Yeni bir eleman ekleyin.
lst.append(101)
lst

# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.
lst.insert(8, "N")
lst

###---------------------------------###

## GÖREV 3: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}

# Adım 1: Key değerlerine erişiniz.
dict.keys()

# Adım 2: Value'lara erişiniz.
dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict.update({"Daisy": ["England",13]})
dict
dict.get("Daisy")

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict.update({"Ahmet": ["Turkey", 24]})
dict
dict.items()

# Adım 5: Antonio'yu dictionary'den siliniz.
dict.pop("Antonio")
dict

###---------------------------------###

## GÖREV 4: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
# Liste elemanlarına tek tek erişmeniz gerekmektedir.
# Her bir elemanın çift veya tek olma durumunu kontrol etmek için % yapısını kullanabilirsiniz.
l = [2,13,18,93,22]

def func(list):

    cift_list = []
    tek_list = []

    for i in list:
        if i % 2 == 0:
            cift_list.append(i)
        else:
            tek_list.append(i)

    return cift_list, tek_list


cift,tek = func(l)


#List comp. çözümü:
def func(list):
    cift_list = [x for x in list if x % 2 == 0]
    tek_list = [x for x in list if x % 2 != 0]

    return cift_list, tek_list

cift, tek = func(l)

###---------------------------------###

## GÖREV 5: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for i,x in enumerate(ogrenciler):
    if i<3:
        i += 1
        print("Mühendislik Fakültesi",i,". öğrenci: ",x)
    else:
        i -= 2
        print("Tıp Fakültesi",i,". öğrenci: ",x)

###---------------------------------###

## GÖREV 6: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. 
#           Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
  print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")

###---------------------------------###

## GÖREV 7: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
# Kapsayıp kapsamadığını kontrol etmek için issuperset() metodunu,farklı ve ortak elemanlar için ise intersection ve difference metodlarını kullanınız.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume(set1,set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

kume(kume1,kume2)

###---------------------------------###


###        Alıştırmalar Devam       ###
# 1) Write a line of code that creates a list containing the first 10 Fibonacci numbers.
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

fibonacci = [0,1]

while len(fibonacci)<10:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
print(fibonacci)


# 2) Write a line of code that counts the number of unique characters in a string.
string = "hello world"

unique_char = len(set(string))
print(unique_char)


# 3) Write a line of code that finds the second smallest element in a list.
my_list = [5, 3, 1, 4, 2,12,0,-4]

sorted(set(my_list))[1]
list(set(my_list))[1]


# 4) Write a line of code that creates a tuple containing the squares of numbers from 1 to 5.
#(1, 4, 9, 16, 25)

tuple([x**2 for x in range(1,6)])


# 5) Write a line of code that removes duplicates from a list and converts it into a tuple.
my_list = [1, 2, 3, 2, 4, 5, 3, 1]
# (1, 2, 3, 4, 5)

tuple(set(my_list))
sorted(set(my_list))

