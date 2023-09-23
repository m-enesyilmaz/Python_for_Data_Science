#########################################################
# Pandas ve Kural Tabanlı Sınıflandırma Alıştırmalar
#########################################################

#######################
# Alıştırma 1
#######################

import seaborn as sns
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
df = sns.load_dataset('titanic')
df.head()
# sns.get_dataset_names()


# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
df['sex'].value_counts()

male = df['sex'].value_counts()['male']
male


# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
df.nunique()


# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
df['pclass'] # series
df.pclass # series
df[['pclass']] # dataframe

df['pclass'].nunique()
df.pclass.unique()


# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
df[['pclass', "parch"]].nunique()


# Görev 6: embarked değişkeninin tipini kontrol ediniz.
# Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.

# * Az sayıda unique değerden oluşan string tipinde bir değişken var ise
# veri tipini category olarak değiştirmek bellek avantajı ve işlem hızı sağlar.
df['embarked'].dtype

df.info()
df.head()

df['embarked'] = df['embarked'].astype('category')


# Görev 7: embarked değeri C olanların tüm bilgilerini gösteriniz.
df[df['embarked'] == 'C'].head()
df.head()


# Görev 8: embarked değeri S olmayanların tüm bilgilerini gösteriniz.
df[df['embarked'] != 'S']
df[~(df['embarked'] == 'S')]


# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
df[(df['age'] < 30) & (df['sex'] == 'female')].head()


# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
df[(df['fare'] > 500) | (df['age'] > 70)].head()


# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
df.isnull().sum()
df.isna().sum()

df.isnull()

int(True + True)

df.shape[0]


# Görev 12: who değişkenini dataframe’den çıkarınız.
df.head()
df.drop('who', axis=1, inplace=True)


# Görev 13: deck değişkenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
df['deck'].fillna(df['deck'].mode()[0], inplace=True)

df['deck'].value_counts().index[0]

df.isnull().sum()


# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
df['age'] = df['age'].fillna(df['age'].median())


# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
df.groupby(['pclass', "sex"]).agg({'survived': ['sum', 'count', 'mean']})
# df.groupby(['pclass', "sex"])['survived'].mean()


# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz.
# (apply ve lambda yapılarını kullanınız)
df['age_flag'] = df['age'].apply(lambda x: 1 if x < 30 else 0)
df.head()

df[df.embark_town.isnull()]


# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
df = sns.load_dataset('tips')
df.head()


# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
df.groupby('time').agg({'total_bill': ['sum', 'min', 'max', 'mean', 'count']})

# df.groupby("time")["total_bill"].agg(["sum","min","max","mean"])


# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
df.groupby(['day','time']).agg({'total_bill': ['sum', 'min', 'max', 'mean', 'count']})


# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
df_female_lunch = df[(df['time'] == 'Lunch') & (df['sex'] == 'Female')]
df_female_lunch.groupby('day').agg({'total_bill': ['sum', 'min', 'max', 'mean', 'count'],
                                    'tip': ['sum', 'min', 'max', 'mean', 'count']})


# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
df.loc[(df['size'] < 3) & (df['total_bill'] > 10), 'total_bill'].mean()


# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz.
# Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
df['total_bill_tip_sum'] = df['tip'] + df['total_bill']
df.head()


# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız
# ve ilk 30 kişiyi yeni bir dataframe'e atayınız
df_top30 = df.sort_values(by='total_bill_tip_sum', ascending=False).head(30)
df_top30

# df.sort_values(by='total_bill_tip_sum', ascending=False).iloc[:30]


#######################
# Alıştırma 2
#######################

#############################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
#############################################

#############################################
# İş Problemi
#############################################
# Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak seviye tabanlı (level based) yeni müşteri tanımları (persona)
# oluşturmak ve bu yeni müşteri tanımlarına göre segmentler oluşturup bu segmentlere göre yeni gelebilecek müşterilerin şirkete
# ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.

# Örneğin: Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek kullanıcının ortalama ne kadar kazandırabileceği belirlenmek isteniyor.


#############################################
# Veri Seti Hikayesi
#############################################
# Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu ürünleri satın alan kullanıcıların bazı
# demografik bilgilerini barındırmaktadır. Veri seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı tablo
# tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir kullanıcı birden fazla alışveriş yapmış olabilir.

# Price: Müşterinin harcama tutarı
# Source: Müşterinin bağlandığı cihaz türü
# Sex: Müşterinin cinsiyeti
# Country: Müşterinin ülkesi
# Age: Müşterinin yaşı

################# Uygulama Öncesi #####################

#    PRICE   SOURCE   SEX COUNTRY  AGE
# 0     39  android  male     bra   17
# 1     39  android  male     bra   17
# 2     49  android  male     bra   17
# 3     29  android  male     tur   17
# 4     49  android  male     tur   17

################# Uygulama Sonrası #####################

#       customers_level_based        PRICE SEGMENT
# 0   BRA_ANDROID_FEMALE_0_18  1139.800000       A
# 1  BRA_ANDROID_FEMALE_19_23  1070.600000       A
# 2  BRA_ANDROID_FEMALE_24_30   508.142857       A
# 3  BRA_ANDROID_FEMALE_31_40   233.166667       C
# 4  BRA_ANDROID_FEMALE_41_66   236.666667       C


#############################################
# PROJE GÖREVLERİ
#############################################

#############################################
# GÖREV 1: Aşağıdaki soruları yanıtlayınız.
#############################################
import pandas as pd

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
df = pd.read_csv('datasets/persona.csv')

df.info()
df.head()
df.tail()
df.describe().T
df.shape
df.columns
df.index
df.isnull().values.any()


# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?
df['SOURCE'].unique()
df['SOURCE'].value_counts()


# Soru 3: Kaç unique PRICE vardır?
df.PRICE.nunique()


# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
df.PRICE.value_counts()


# Soru 5: Hangi ülkeden kaçar tane satış olmuş?
df.COUNTRY.value_counts()


# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?
df.groupby('COUNTRY').agg({'PRICE': 'sum'})
# df.groupby('COUNTRY')['PRICE'].sum()


# Soru 7: SOURCE türlerine göre göre satış sayıları nedir?
df.SOURCE.value_counts()


# Soru 8: Ülkelere göre PRICE ortalamaları nedir?
df.groupby('COUNTRY').agg({'PRICE': 'mean'})


# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
df.groupby(['SOURCE']).agg({'PRICE': 'mean'})


# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
df.groupby(['SOURCE', 'COUNTRY']).agg({'PRICE': 'mean'})


#############################################
# GÖREV 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
#############################################

agg_df = df.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE']).agg({'PRICE': 'mean'})


#############################################
# GÖREV 3: Çıktıyı PRICE'a göre sıralayınız.
#############################################
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE'a uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.

agg_df.sort_values('PRICE', ascending=False)

len(agg_df.columns)


#############################################
# GÖREV 4: Indekste yer alan isimleri değişken ismine çeviriniz.
#############################################
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# İpucu: reset_index()
# agg_df.reset_index(inplace=True)

agg_df = agg_df.reset_index()
agg_df.columns


#############################################
# GÖREV 5: AGE değişkenini kategorik değişkene çeviriniz ve agg_df'e ekleyiniz.
#############################################
# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici olacağını düşündüğünüz şekilde oluşturunuz.
# Örneğin: '0_18', '19_23', '24_30', '31_40', '41_70'

# AGE değişkeninin nerelerden bölüneceğini belirtelim:

my_bins = [0, 18, 23, 30, 40, agg_df['AGE'].max()]

# Bölünen noktalara karşılık isimlendirmelerin ne olacağını ifade edelim:

mylabels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(agg_df['AGE'].max())]
# mylabels = ['0_18', '19_23', '24_30', '31_40', f'41_{agg_df["AGE"].max()}']

# age'i bölelim:
pd.cut(agg_df['AGE'], bins=my_bins, labels=mylabels)

agg_df['AGE_CAT'] = pd.cut(agg_df['AGE'], bins=my_bins, labels=mylabels)
agg_df.head()


#############################################
# GÖREV 6: Yeni level based müşterileri tanımlayınız ve veri setine değişken olarak ekleyiniz.
#############################################
# customers_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.
# Dikkat!
# list comp ile customers_level_based değerleri oluşturulduktan sonra bu değerlerin tekilleştirilmesi gerekmektedir.
# Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18
# Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.
agg_df.drop(['AGE', 'PRICE'], axis=1).values

liste = ['A', 'B', 'C']
'-'.join(liste)

agg_df["CUSTOMERS_LEVEL_BASED"] = ["_".join(i).upper() for i in agg_df.drop(['AGE', 'PRICE'], axis=1).values]
agg_df

# ["{}_{}_{}_{}".format(x.upper(),y.upper(),z.upper(),k) for x,y,z,k in zip(agg_df["COUNTRY"],agg_df["SOURCE"],agg_df["SEX"],agg_df["AGE_CAT"])]

# agg_cols=["COUNTRY","SOURCE","SEX","AGE_CAT"]

# [col[0].upper()+"_"+col[1].upper()+"_"+col[2].upper()+"_"+col[3].upper() for col in agg_df[agg_cols].values ]

# agg_df['COUNTRY'].astype(str) + "_" + \
# agg_df['SOURCE'].astype(str) + "_" + \
# agg_df['SEX'].astype(str) + "_" + \
# agg_df['AGE_CAT'].astype(str)

# Gereksiz değişkenleri çıkaralım:
agg_df.head()
agg_df = agg_df[['CUSTOMERS_LEVEL_BASED', 'PRICE']]

agg_df = agg_df.groupby('CUSTOMERS_LEVEL_BASED')['PRICE'].mean().reset_index()

###
# # Amacımıza bir adım daha yaklaştık.
# Burada ufak bir problem var. Birçok aynı segment olacak.
# örneğin USA_ANDROID_MALE_0_18 segmentinden birçok sayıda olabilir.
# kontrol edelim:

# Bu sebeple segmentlere göre groupby yaptıktan sonra price ortalamalarını almalı ve segmentleri tekilleştirmeliyiz.


#############################################
# GÖREV 7: Yeni müşterileri (USA_ANDROID_MALE_0_18) segmentlere ayırınız.
#############################################
# PRICE'a göre segmentlere ayırınız,
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz,
# segmentleri betimleyiniz,

[23, 27, 34, 34, 35, 39, 41, 48]

agg_df['SEGMENT'] = pd.qcut(agg_df.PRICE, q=4, labels=['D', 'C', 'B','A'])
agg_df.head()

agg_df.groupby('SEGMENT').agg({'PRICE': 'mean'}).reset_index()

agg_df['PRICE'].corr()


#############################################
# GÖREV 8: Yeni gelen müşterileri sınıflandırınız ne kadar gelir getirebileceğini tahmin ediniz.
#############################################
# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
new_user = 'TUR_ANDROID_FEMALE_31_40'
agg_df[agg_df['CUSTOMERS_LEVEL_BASED'] == new_user]


# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente ve ortalama ne kadar gelir kazandırması beklenir?
new_user = 'FRA_IOS_FEMALE_31_40'
agg_df[agg_df['CUSTOMERS_LEVEL_BASED'] == new_user]
agg_df[agg_df['CUSTOMERS_LEVEL_BASED'] == 'BRA_ANDROID_FEMALE_0_18']

df[['PRICE', 'AGE']].corr()

