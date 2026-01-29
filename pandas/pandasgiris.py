import pandas as pd

# s = pd.Series([10,20,30,40], index = ["a","b","c","d"])
# print(s)

data = {
    "Fiyat" : [45,85,45,25],
    "Satış Adedi" : [5,6,7,2],
    "Kategori" : ["Roman","Bilim","Çocuk","Tarih"]
}

df = pd.DataFrame(data)
# print(df)
# print(df.head()) # İlk satırları gösterir.
# print(df.info()) # Bilgi verir.
# print(df.describe()) # Sayısal veriler hakkında bilgi verir. 
# print(df[['Fiyat','Kategori']]) # Kaç tane veri kullanacaksak o kadar kareli parantez atacağız.

# filtre = df[df['Fiyat'] > 50 ]
# print(filtre)

df['Toplam Fiyat'] = (df['Satış Adedi'] * df['Fiyat'])
print(df['Toplam Fiyat'])

# df = df.drop('Kategori', axis=1)
# print(df)




df['Kategori'] = ["Roman","Bilim","Çocuk","Tarih"]
print(df)