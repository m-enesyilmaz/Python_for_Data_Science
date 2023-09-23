###############################################
# PYTHON İLE VERİ ANALİZİ (DATA ANALYSIS WITH PYTHON)
###############################################
# - NumPy

#############################################
# NUMPY
#############################################

# Neden NumPy? (Why Numpy?)
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
# Yeniden Şekillendirme (Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
# Matematiksel İşlemler (Mathematical Operations)

"""
numpy'ı list'lerden ayıran önemli iki nokta;
1. verimli veri saklama (hızlı)
2. vektörel işlemler (yüksek seviyeden)
kısaca özetleyecek olursak:
numpy içerisinde bir veri tutarken fixtype adını verdiği sabitlenmiş tipte tutarak
listelere kıyasla çok daha hızlı bir şekilde işlem yapma imkanı sağlar.
bir diğeri örneğin döngü yazmaya gerek olmadan array seviyesinde çok basit işlemlerle
normalde daha fazla çaba gerektiren işlemleri gerçekleştirmeyi sağlar.
"""

#############################################
# Neden NumPy?
#############################################
import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b


#############################################
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
#############################################

# numpy ın veri tipi array
np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))
np.zeros(10, dtype=int)
np.random.randint(0, 10, size=10)
np.random.normal(10, 4, (3, 4))


#############################################
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
#############################################

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)
a.ndim
a.shape
a.size
a.dtype


#############################################
# Yeniden Şekillendirme (Reshaping)
#############################################

np.random.randint(1, 10, size=9)
np.random.randint(1, 10, size=9).reshape(3, 3)

ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)


#############################################
# Index Seçimi (Index Selection)
#############################################

a = np.random.randint(10, size=10)
a[0]
a[0:5]  # sol taraf dahil, sağ taraf hariç
a[0] = 999

m = np.random.randint(10, size=(3, 5))

m[0, 0]  # m[satır, sütun]
m[1, 1]
m[2, 3]

m[2, 3] = 999

m[2, 3] = 2.9  # numpy fixtype (tek bir tip) olduğu için genele göre uyumlu tutar

m[:, 0]  # bütün satırlar 0. sütun demek
m[1, :]
m[0:2, 0:3]  # satırda 0'dan 2 ye kadar git, sütunda 0'dan 3 e kadar git


#############################################
# Fancy Index
#############################################

v = np.arange(0, 30, 3) # 0'dan 30'a kadar 3'er 3'er artan array oluştur demek
v[1]
v[4]

catch = [1, 2, 3]

v[catch]  # index bilgilerini tek seçim yapıyormuşcasına ilgili arrayden getir dedik


#############################################
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
#############################################

v = np.array([1, 2, 3, 4, 5])

#######################
# Klasik döngü ile
#######################
ab = []
for i in v:
    if i < 3:
        ab.append(i)

#######################
# Numpy ile
#######################
v < 3  # bu sorguyu array in bütün elemanlarına gitti yaptı
# eğer bir array'in içerisinden koşullu elaman seçmek istiyorsak bu şekilde yapabiliriz
v[v < 3]
v[v > 3]
v[v != 3]
v[v == 3]
v[v >= 3]


#############################################
# Matematiksel İşlemler (Mathematical Operations)
#############################################

v = np.array([1, 2, 3, 4, 5])

v / 5
v * 5 / 10
v ** 2
v - 1

np.subtract(v, 1)
np.add(v, 1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)
v = np.subtract(v, 1)


#######################
# NumPy ile İki Bilinmeyenli Denklem Çözümü
#######################

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])

np.linalg.solve(a, b)

