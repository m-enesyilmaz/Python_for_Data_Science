###############################################
# PYTHON İLE VERİ ANALİZİ (DATA ANALYSIS WITH PYTHON)
###############################################
# - Pandas

#############################################
# PANDAS
#############################################

# Pandas Series
# Veri Okuma (Reading Data)
# Veriye Hızlı Bakış (Quick Look at Data)
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# Apply ve Lambda
# Birleştirme (Join) İşlemleri

#############################################
# Pandas Series
#############################################
import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
type(s)
s.index
s.dtype
s.size
s.ndim  # pandas serileri tek boyutludur ve index bilgileri vardır
s.values
type(s.values)  # numpy array e döndüğünü gördük
s.head(3)
s.tail(3)


#############################################
# Veri Okuma (Reading Data)
#############################################

df = pd.read_csv("datasets/advertising.csv")
df.head()
# pandas cheatsheet


#############################################
# Veriye Hızlı Bakış (Quick Look at Data)
#############################################
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()
df["sex"].head()
df["sex"].value_counts()


#############################################
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
#############################################

df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13]
df.drop(0, axis=0).head()

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)

# df = df.drop(delete_indexes, axis=0)
# df.drop(delete_indexes, axis=0, inplace=True)


#######################
# Değişkeni Indexe Çevirmek
#######################

df["age"].head()
df.age.head()

df.index = df["age"]

df.drop("age", axis=1).head()  # axis=1 sütunlardan yap işlemi demek

df.drop("age", axis=1, inplace=True)
df.head()


#######################
# Indexi Değişkene Çevirmek
#######################

df.index

df["age"] = df.index
# bir dataframe'in içerisine yeni bir değişken eklemek istersek üstteki gibi yapabiliriz
df.head()
df.drop("age", axis=1, inplace=True)

df.reset_index().head()
df = df.reset_index()
df.head()


#######################
# Değişkenler Üzerinde İşlemler
#######################

pd.set_option('display.max_columns', None)  # tüm datasetini sınırlandırma oldan göster demek
df = sns.load_dataset("titanic")
df.head()

"age" in df

df["age"].head()
df.age.head()  # değişken seçme bu iki türlüde yapılabilir

df["age"].head()
type(df["age"].head())  # bu şekilde bir pandas serisi olarak kalacaktır


df[["age"]].head()  # eğer dataframe olarak kalmasını istiyorsanız bu şekilde kullanılması gerekmekte
type(df[["age"]].head())

df[["age", "alive"]]

col_names = ["age", "adult_male", "alive"]
df[col_names]

df["age2"] = df["age"]**2
df["age3"] = df["age"] / df["age2"]

df.drop("age3", axis=1).head()

df.drop(col_names, axis=1).head()

df.loc[:, ~df.columns.str.contains("age")].head()


#######################
# iloc & loc
#######################

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# iloc: integer based selection
df.iloc[0:3] # index bilgisi vererek seçme işlemi yapar
df.iloc[0, 0]

# loc: label based selection
df.loc[0:3]  # mutlak olarak isimlendirmenin kendisini seçiyor
# yani iloc da e kadar seçiyor loc da label kendisini de seçiyor


df.iloc[0:3, 0:3]
# df.iloc[0:3, "age"] --> bu hata veriyor mesela sebebi ise iloc integer base
df.loc[0:3, "age"]

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]


#######################
# Koşullu Seçim (Conditional Selection)
#######################

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()
df[df["age"] > 50]["age"].count()

df.loc[df["age"] > 50, ["age", "class"]].head()  # burada  bir koşul ve iki sütun seçtik

df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()
# üstteki gibi birden fazla koşul giriyorsa paratez içinde koşulu göndermek gerekiyor
df["embark_town"].value_counts()

df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]]

df_new["embark_town"].value_counts()


#############################################
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
#############################################

# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()
# - pivot table

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df["age"].mean()

df.groupby("sex")["age"].mean()  # bunun açılımı  şu demek:
# df dataframe'ni cinsiyete göre grupla daha sonra yaş değişkeninin  ortalamasını al

df.groupby("sex").agg({"age": "mean"})
df.groupby("sex").agg({"age": ["mean", "sum"]})

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})


df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                                        "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                                                 "survived": "mean"})


df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                                                 "survived": "mean",
                                                 "sex": "count"})


#######################
# Pivot table
#######################

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived", "sex", "embarked")

df.pivot_table("survived", "sex", ["embarked", "class"])

df.head()

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])
# geneldee sayısal değişkeni hangi hangi kategorilere bölmek istersek cut'ı kullanıyoruz
# ama elimizdeki sayısal değişkeni tanımıyorum çeyreklik değerlerine gör bölünsün istiyorsak qcut kullanıyoruz

df.pivot_table("survived", "sex", ["new_age", "class"])

pd.set_option('display.width', 500)


#############################################
# Apply ve Lambda
#############################################

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

df.head()

df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# df.loc[:, ["age","age2","age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.head()


#############################################
# Birleştirme (Join) İşlemleri
#############################################

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2])  # concat iki dataframe i alt alta birleştiriyor, axis =1 dersek yan yana

pd.concat([df1, df2], ignore_index=True)


#######################
# Merge ile Birleştirme İşlemleri
#######################

df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
pd.merge(df1, df2, on="employees")

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz.
df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4)
# ortak olanlar üzerinden işlem yapıyor

