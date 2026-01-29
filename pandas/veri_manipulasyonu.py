import pandas as pd

df = pd.read_excel(r"C:\Users\cavus\Desktop\Pandas\teknolojik_urunler1.xlsx")

# eksik_veriler = df.isnull() # boş satırları True olarak gösterir.
# print(eksik_veriler)


# temiz_df = df.dropna() # Boş satır varsa o satırı tamamen siler
# print(temiz_df)

#!!!!! veri_atanmıs_hali = df.fillna("bos") # değeri olmayan yerleri doldurabiliriz.
# print(veri_atanmıs_hali)


# tip değiştirme adımı
# df['Fiyat (TL)'] = df['Fiyat (TL)'].astype(float)
# print(df['Fiyat (TL)'])



# df.insert(2,'Yeni Sütun',range(1,21))
# print(df.head())




# df.to_excel('yeniveri.xlsx',index=False)
# print("yeni veri eklendi.")


#verileri büyükten kücüge sıralar. False - kücükten büyüge, True büyükten kücüge
# dusuk= df.sort_values(by='Fiyat (TL)',ascending=True)
# print(dusuk)

# düsük sıralama
# dusuk = df.sort_values(by='Fiyat (TL)',ascending=True)
# print(dusuk)

# yüksek sıralama
# yuksek = df.sort_values(by='Fiyat (TL)', ascending=False)
# print(yuksek)


# buyuk = df[df['Fiyat (TL)'] > 5000]
# print(buyuk)


# Tekli Filtreleme
# buyukse_1000den = df[df['Fiyat (TL)'] > 1000]
# print(buyukse_1000den)

# Çoklu filtreleme
filtreleme = df[(df['Fiyat (TL)'] >= 1000) & (df['Kategori'] == 'Akıllı Ev Ürünleri')]
print(filtreleme)



# filtre = df[(df['Fiyat (TL)'] >= 5000) & (df['Kategori'] == 'Mobil Cihazlar')]
# print(filtre)

# Birden fazla sütunu seçmek için kullanılır.
secili = df.loc[:,(['Kategori','Fiyat (TL)'])]
print(secili)

#birden fazla sütun seçmek için
# secili = df.loc[:,(['Ürün Adı', 'Fiyat (TL)','Satış '])]
# print(secili)

ilk10satir = df.iloc[:10,:]
print(ilk10satir)

#:5 -> 5. satıra kadar gösterir, :2 -> 2. sütuna kadar gösterir
# ilk = df.iloc[:5,:2]
# print(ilk)


# sorgu = df.query('Kategori')
# print(sorgu)

#tek index üzerinde sütunda filtreleme yapabiliriz. 
# belirli_cihaz = df[df['Kategori'].isin(['Bilgisayarlar', 'Mobil Cihazlar'])]
# print(belirli_cihaz)


#sayısal değerler de kullanılmaz sadece 1 sütunda istediğimiz filtreyi yapmak için kullanırız.
# ucret = df[df['Kategori'].isin(['Televizyonlar','Bilgisayarlar'])]
# print(ucret)






