import pandas as pd

df = pd.read_excel(r"C:\Users\cavus\Desktop\Pandas\teknolojik_urunler.xlsx")

# print(df)
# ortalama_fiyat = df["Fiyat (TL)"].mean() #ortalama fiyat mean fonk.
# print(f"Ortalama Fiyat = {ortalama_fiyat}")


# kategori_bazlı_toplam = df.groupby('Kategori')['Fiyat (TL)'].sum()
# print(f"Ortalama Fiyat {kategori_bazlı_toplam}")

#en cok gelir getiren ürünü bulma
# max_gelir = df.loc[df['Toplam Fiyat (TL)'].idxmax()]
# print(f"En cok gelir getiren ürün {max_gelir}")
# neden loc kullandık cünkü sadece 1 sütun üzerinde calısıcaz o yüzden

# max_gelir_urun = df.loc[df['Toplam Fiyat (TL)'].idxmax()]
# print(f"En cok gelir getiren ürün no = {max_gelir_urun}")

# # alt üst sınırlaması yapma
# fiyat_ust_urunler = df.loc[df['Toplam Fiyat (TL)'] > 4000]
# print(f"Toplam fiyatı 4000'den büyük olanlar = {fiyat_ust_urunler}")

# fiyat_ust_urunler.to_excel('fiyati_4000_yuksek_olanlar.xlsx', index=False)

# print(df['Ürün Adı'])

# kategori = df.loc[df['Kategori']]
# fiyat = df.loc[df['Fiyat']]

# gruplama = df.groupby(('kategori'),('fiyat'))