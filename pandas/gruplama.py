import pandas as pd

df = pd.read_excel(r"C:\Users\cavus\Desktop\Pandas\teknolojik_urunler.xlsx")

# gruplama = df.groupby('Kategori')
# print(gruplama)

# Gruplamaya göre kategori
# grup = df.groupby('Kategori')['Fiyat (TL)']
# print(grup)


# Burası da birden fazla gruplama yapacağımız zaman .agg kullanıyoruz.
# toplama_ve_ortalamaya_gore_satis = df.groupby('Kategori').agg(
#     {
#         'Satış':'sum',
#         'Fiyat (TL)':'mean'
#     }
# )
# print(toplama_ve_ortalamaya_gore_satis) 


# EN PAHALI VE EN UCUZ ÜRÜNLER
# en_pahali_urun = df.loc[df.groupby('Kategori')['Fiyat (TL)'].idxmax()]
# print(f"En Pahalı ürünler {en_pahali_urun}")

# en_ucuz_urun = df.loc[df.groupby('Kategori')['Fiyat (TL)'].idxmin()]
# print(f"En Ucuz ürünler {en_ucuz_urun}")


#Burası önemli bilmek gerekiyor.
# ust_duzey_gruplama = df.groupby('Kategori').filter(lambda x:x['Satış'].sum() > 50)
# print(ust_duzey_gruplama)





