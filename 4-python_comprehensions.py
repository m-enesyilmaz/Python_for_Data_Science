"""
Konu başlıkları:

- Comprehensions
List Comprehension
Alıştırmalar

"""

##################################################################################
#                              COMPREHENSION
##################################################################################

# If - Else :

# [ [ifresult] if [condition] else [elseresult] for i in [.....] ]


# If :

# [ [ifresult] for i in [....] if [condition] ]


"""
List comprehension, Python'da kompakt bir şekilde liste oluşturmak için kullanılan bir yapıdır.

"""

# Örnek; bir liste içindeki sayıları negatif ise sıfıra eşitleme, pozitif ise kendilerini koruma
liste = [1, -2, 3, -4, 5, -6]
# [1, 0, 3, 0, 5, 0]

sonuclar = [x if x >= 0 else 0 for x in liste]
print(sonuclar)


# Örnek; bir liste içindeki çift sayıları ikiye bölenlerin karesini, tek sayıları ise üçe bölenlerin karesini içeren bir liste oluşturma:
liste = [3, 8, 27, 10, 9, 12]
# [1.0, 64, 81.0, 100, 9.0, 144]

sonuc = [x**2 if x % 2 == 0 else (x/3)**2 for x in liste]
print(sonuc)


# Bir dize içindeki kelimeleri ters çevirmek
dize = "Machine Learning Summer Camp"
# ['enihcaM', 'gninraeL', 'remmuS', 'pmaC']

ters_kelime = [ kelime[::-1] for kelime in dize.split()]
print(ters_kelime)


# Bir cümle içindeki harflerin büyük harf veya küçük harf olmasına göre ilgili şekilde yeni bir liste oluşturma:
sentence = "dAta sCieNce!"
# ['D', 'a', 'T', 'A', ' ', 'S', 'c', 'I', 'E', 'n', 'C', 'E', '!']

sonuc = [harf.upper() if harf.islower() else harf.lower() for harf in sentence]
print(sonuc)


# Sample
positions = ["goalkeeper","defence","midfielder","forward","winger"]
liste=[]
for x in positions:
    if "e" in x:
        liste.append(x)

liste
# ['goalkeeper', 'defence', 'midfielder', 'winger']


# Sample 2
# 100 'e kadar sayılarda 2 ve 3'e tam kalanlı bölünen sayıları listeme

liste = []
for y in range(100):
    if (y%2 == 0) &  (y%3  == 0):
        liste.append(y)

liste

# List Comprehension
[ y for y in range(100) if (y%2 == 0) &  (y%3  == 0)]


# Sample 3
strings = ["hello", "world", "python", "programming"]
# ['HELLO', 'WORLD', 'PYTHON', 'PROGRAMMING']

uppercase_strings = [word.upper() for word in strings]
print(uppercase_strings)


##################################################################################
#                              LIST COMPREHENSION ALIŞTIRMALAR
##################################################################################


#1 Write a list comprehension that generates a list of all possible substrings of a given string.
string = "myth"
# ['m', 'my', 'myt', 'myth', 'y', 'yt', 'yth', 't', 'th', 'h']

len(string)

sub_string=[]
for i in range(len(string)):
    for j in range(i+1,len(string)+1):
        sub_string.append(string[i:j])

print(sub_string)

# List Comprehenson
sub = [string[i:j] for i in range(len(string)) for j in range(i+1,len(string)+1) ]
print(sub)

# [string[i:j] for i in range(4) for j in range(i+1,5)]

###---------------------------------###

#2 Write a list comprehension that flattens a nested list into a single list.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

single=[]

for flat in nested_list:
    for x in flat:
        single.append(x)

print(single)

# List Comprehension
[x for flat in nested_list for x in flat]

###---------------------------------###

#3 Write a list comprehension that generates a list of all possible combinations of two strings from two given lists.
list1 = ['a', 'b']
list2 = ['x', 'y']
# ['ax', 'ay', 'bx', 'by']

[ x + y for x in list1 for y in list2]

###---------------------------------###

#4 Write a list comprehension that generates a list of prime numbers up to a given number n.
# [2, 3, 5, 7, 11, 13, 17, 19]

n = 20

def is_prime(number):
    if number < 2:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

prime_sayılar = []
for number in range(2,n+1):
    if is_prime(number):
        prime_sayılar.append(number)

print(prime_sayılar)


[number for number in range(2,n+1) if is_prime(number)]

#Alternative Solution for List Comprehension
n=20
[number for number in range(2,n+1) if all(number % i != 0 for i in range(2,int(number**0.5)+1))]

###---------------------------------###

#5 Write a list comprehension that finds all numbers in a given list that are divisible by the sum of their digits.
numbers = [12, 23, 34, 45, 56, 67, 78, 89, 90]
# [12, 45, 90]

result = [num for num in numbers if num % sum(int(digit) for digit in str(num)) == 0]
print(result)

###---------------------------------###

#6 Extracting even-length words from a list of strings:
strings = ["apple", "banana", "orange", "kiwi", "grape"]
# ['banana', 'orange', 'kiwi']

even_length_words = [word for word in strings if len(word) % 2 == 0]
print(even_length_words)

###---------------------------------###

#7 A listesindeki elemanları for döngüsü kullanarak B listesine taşımak
A = [20, 35, 48, 50, 23]
B = []
# [20, 35, 48, 50, 23]

for eleman in A:
    B.append(eleman)

A.clear()

print("A listesi:", A)
print("B listesi:", B)


def transform(liste1,liste2):
    for eleman in liste1:
        liste2.append(eleman)

    liste1.clear()
    return liste1,liste2

liste1,liste2 = transform(A,B)

###---------------------------------###

#8 unique elemanları döndüren fonksiyonu yazınız.
no_unique_list = [1,1,1,2,2,2,3,5,5,5,7,7,7,9,9,9]
# [1, 2, 3, 5, 7, 9]

def no_unique(i):
    liste = list(set(i))

    return liste

no_unique(no_unique_list)

###---------------------------------###

#9 Bir sayı listesi alıp bu listenin içindeki tüm elemanları toplayan fonksiyonu yazınız.
sampleList = [15,25,40,55,60]
# Liste Elemanlarının Toplamı: 195

def sum(sayi_listesi):
    toplam = 0
    for eleman in sayi_listesi:
        toplam += eleman
    return toplam

sampleList = [15, 25, 40, 55, 60]
toplam = sum(sampleList)
print("Liste Elemanlarının Toplamı:", toplam)

###---------------------------------###

#10 For döngüsü kullanarak faktöriyel hesabını yazınız.
def faktoriyel(n):
    faktoriyeller = [1]
    for i in range(1, n+1):
        faktoriyel = faktoriyeller[-1] * i
        faktoriyeller.append(faktoriyel)
    return faktoriyeller

n = 5
faktoriyeller = faktoriyel(n)
print(faktoriyeller)

###---------------------------------###

#11 For döngüsü kullanarak girilen sayının faktöriyel hesabını yazan fonksiyonu yazınız
def faktoriyel_hesapla(n):
    faktoriyel = 1
    if n < 0:
        return "Negatif sayıların faktöriyeli tanımsızdır."
    elif n == 0:
        return 1
    else:
        for i in range(1, n+1):
            faktoriyel *= i
        return faktoriyel

sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))
faktoriyel = faktoriyel_hesapla(sayi)
print("Faktöriyel:", faktoriyel)

###---------------------------------###

#12 players listesinde kelime uzunluğu 6'den küçük olanları getiren listeyi tanımla
players = ["messi","ronaldo","benzema","mbappe","haaland"]

liste= []
for i in players:
    if len(i)< 6:
        liste.append(i)

liste

goat = [i for i in players if len(i)< 6]
print(goat)


