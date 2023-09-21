"""
Konu başlıkları:

- Working Settings
- Pycharm
- Virtual Environment
- Package Management

- Data Structures

"""

##################################################################################
# WORKING ENVIRONMENT SETTINGS - ANACONDA- PYCHARM
##################################################################################

# Anaconda nedir?
"""
Anaconda, Python tabanlı bir veri bilimi platformudur ve birçok popüler Python paketini ve aracını içerir.
Paket yöneticisi olan conda ve kullanıcı dostu bir grafiksel kullanıcı arayüzü olan Anaconda Navigator ile birlikte,
veri bilimcileri ve geliştiricileri için güçlü bir geliştirme ve analiz ortamı sağlar.
"""

# Pycharm nedir?
"""
IDE(Integrated Development Environment)
Python programlama dili için özel olarak tasarlanmış bir entegre geliştirme ortamıdır (IDE). 
PyCharm, Python projelerini oluşturmanız, düzenlemeniz, hata ayıklamanız, test etmeniz ve dağıtmanız için bir dizi araç ve özellik sunar.
"""

# Virtual Environment neden oluşturuyoruz?
"""
İzole bir çalışma ortamı oluşturmak için "sanal ortam" oluşturmaktayız.
"""

"""
Sanal ortamlar birbirinden farklı kütüphane ve versiyonlar içerisinde projeler birbirini etkilemeden çalışma imkanı
sağlamaktadır.
"""

# Virtual ortam(Sanal ortam) araçları nelerdir?
"""
venv, virtualenv, pipenv, conda
"""

# Package Management(paket yönetim) toollarına neden ihtiyacımız bulunmaktadır?
"""
Tools that manage the dependency management work of libraries/packages.
"""

# Package management tools? Conda ve pip arasındaki ilişki nedir?
"""
pip, pipenv, conda
"""

"""
Conda, hem paket yönetimi hem de sanal ortam yönetimi yapmaktadır.
pip, paket yönetimi yapmaktadır.
"""

"""
venv ve virtualenv paket yönetim aracı olarak pip kullanır.
conda ve pipenv hem paket yönetimi hem virtual env yönetimi yapabilmektedir.
"""

# Virtual environment ve package management

# Sanal ortamların listelenmesi:
# conda env list

# Sanal ortam oluşturma:
# conda create –n myenv

# Sanal ortamı aktif etme:
# conda activate myenv

# Yüklü paketlerin listelenmesi:
# conda list

# Paket yükleme:
# conda install numpy

# Aynı anda birden fazla paket yükleme:
# conda install numpy scipy pandas

# Paket silme:
# conda remove package_name

# Belirli bir versiyona göre paket yükleme:
# conda install numpy=1.20.1

# Paket yükseltme:
# conda upgrade numpy

# Tüm paketlerin yükseltilmesi:
# conda upgrade –all

# pip: pypi (python package index) paket yönetim aracı

# Paket yükleme:
# pip install pandas

###############################################
# eğer ortam deeğişkenlerini birisine aktarmak istersek yapmamız gereken:
# conda env export > environment.yaml

# örneğin başka bir bilgisayarda bu environment i tekrar oluşturmak istedik:
# conda env create -f environment.yaml


##################################################################################
# DATA STRUCTURES ( VERI YAPILARI)
##################################################################################

# Veri yapıları nelerdir?

"""
# Sayılar
# Strings
# List
# Dictionary
# Tuple
# Set
"""


# SAYILAR
# int
x = 10
type(x)

# float
y = 20.3
type(y)

# complex
z = 3j + 5
type(z)

t = 1j + 10
type(t)


# STRING
x = "DATA SCIENCE"
type(x)

y = "Data\t Science"


# BOOLEAN
True
False
type(False)

10 % 5 == 3 % 3

type(10 % 5 == 3 % 3)

10 / 5 == 6 // 3


# LIST
"""
Değiştirilebilir

Sıralıdır.

Index işlemi yapılabilir.

Kapsayıcıdır.

"""

l= ["Data",1,"python",1.2,"machine learning",2.4]
type(l)

# check methods?
dir(l)

# eleman ekleme
l.append("chatgpt")
print(l)

# l.append(4,"comprehension")

# eleman çıkarma
l.pop(2)
print(l)

# indexleme
l[2] = "chatgpt"
print(l)


## Yorumlama ##
b = ["String",1,2,"Python",(0,1,2)]

b[-2]
b[-6]
b.pop(-1)
print(b)


# DICT
"""
Değiştirilebilir

Sırasızdır

Kapsayıcıdır.

"""

d = {"Captain America: The First Avenger": 2011,
     "Avengers": 2012,
     "Avengers:Ultron Age": 2015,
     "Avengers:Infinity War":2018,
     "Avengers:End Game":2019}

print(d)

d.keys()
d.values()

# Key Sorgulama
"Avengers" in d

# Value Değiştirmek
d["Avengers"] = 2014

# Value Erişmek
d.values()

# Key-Value Değerini Güncellemek
d.update({"Captain America: The First Avenger": 2010})
print(d)

# Son eleman silmek
d.popitem()

dir(d)


# TUPLE
"""
Değiştirilemez

Sıralıdır

Kapsayıcıdır.

"""

t = ("Machine Learning", "Data Science","Data Analyst","Data Engineer")
type(t)


# Indexleme yapılabilir mi?
t[0]= "Machine"


coral = ('blue coral', 'staghorn coral','pillar coral', 'elkhorn coral','black coral')
print(coral)
coral[-4:-2]

# Yukarıdaki tuple içerisinde "black coral" nesnesini siliniz ve tekrardan tuple olarak gösteriniz.

"""
c = list(coral)
c.pop(4)
c = tuple(c)
print(c)

"""


# SET
"""
Değiştirilebilir

Sırasız + Eşsizdir.

Kapsayıcıdır.

"""

s = {"Python", "Machine Learning", "Data Science","Python","Machine Learning"}
type(s)
print(s)

# Indexleme yapılabilir mi?
s[1]


# tuple ---
x = {42, 'foo', (1, 2, 3), 3.14159}

# list
y = {42, 'foo', [1, 2, 3], 3.14159}

# dictionary
z = {1,2, {'a': 1, 'b': 2},5}


#######################
# difference(): İki kümenin farkı
#######################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

# set1'de olup set2'de olmayanlar.
set1.difference(set2)
set1 - set2

# set2'de olup set1'de olmayanlar.
set2.difference(set1)
set2 - set1


#######################
# isdisjoint(): İki kümenin kesişimi boş mu?
#######################

set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set1.isdisjoint(set2)
set2.isdisjoint(set1)

#######################
# intersection(): İki kümenin kesişimi
#######################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)

set1 & set2


#######################
# union(): İki kümenin birleşimi
#######################

set1.union(set2)
set2.union(set1)


####################################################################################
#                       DATA STRUCTURE ALIŞTIRMALAR
# ##################################################################################


# 1) Write a line of code that creates a list containing the first 10 Fibonacci numbers.
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

fibonacci = [0,1]

while len(fibonacci)<10:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
print(fibonacci)


# 2) Write a line of code that counts the number of unique characters in a string.
string = "hello world"
# 8
unique_char = len(set(string))
print(unique_char)

# 3) Write a line of code that finds the second smallest element in a list.
my_list = [5, 3, 1, 4, 2,12,0,-4]
# 0

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

