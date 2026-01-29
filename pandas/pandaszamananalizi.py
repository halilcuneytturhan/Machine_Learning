import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\cavus\Desktop\global\pandas\teknolojik_urunler_zamanli.xlsx")

df['Tarih'] = pd.to_datetime(df['Tarih'])
# print(df.head())
print(df['Tarih'])


#indexlemeee ( cok önemlii!!! )

#burada ürün no'ya göre sıralama işlemi yapılıyor.
df.set_index('Tarih', inplace=True)
# print(df)

#burada da tarihe göre sıralama yapıldı.
df = df.sort_index()
# print(d

# 1. En yüksek satış yapılan ay ve o ayda en çok satılan ürünler

aylik_satis = df.resample('ME')['Satış'].sum()
max_ay = aylik_satis.idxmax()
max_satis_ay = aylik_satis.max()
max_satis_ay_urunler = df[df.index.to_series().between(max_ay - pd.offsets.MonthBegin(1),max_ay)]
print(f"En yüksek satış yapılan ay= {max_ay} - Toplam satış= {max_satis_ay}")
print('O ay en çok satılan ürünler; ')
print(max_satis_ay_urunler[['Ürün Adı','Satış']])


# 2. en düşük satış yapılan ürün ve o ayda en az satılan ürünler

# aylik_satis = df.resample('ME')['Satış'].sum()
# min_ay = aylik_satis.idxmin()
# min_satis_ay = aylik_satis.min()
# min_satis_ay_urunler = df[df.index.to_series().between(min_ay - pd.offsets.MonthBegin(1), min_ay)]
# print(f"En düşük satış yapılan ay= {min_ay} - Toplam satış= {min_satis_ay}")
# print('O ay en az satılan ürünler; ')
# print(min_satis_ay_urunler[['Ürün Adı','Satış']])

# 3. En fazla satış yapılan gün ve o gün satılan ürün

# gunluk_satis = df.resample('D')['Satış'].sum()
# max_gun = gunluk_satis.idxmax()

# max_gun_satis = gunluk_satis.max()
# max_gun_satis_urun = df.loc[max_gun]
# print(f"En düşük satış yapılan ay= {max_gun} - Toplam satış= {max_gun_satis}")
# print('O ay en az satılan ürünler; ')
# print(max_gun_satis_urun[['Ürün Adı','Satış']])


# 4. Haftalık en fazla satış yapılan ürünler

# haftalik_satis = df.resample('W')['Satış'].sum()
# max_hafta = haftalik_satis.idxmax()

# max_hafta_satis = haftalik_satis.max()
# max_hafta_satis_urun = df[df.index.to_series().between(max_hafta - pd.offsets.Week(1), max_hafta)]

# print(f"En düşük satış yapılan hafta= {max_hafta} - Toplam satış= {max_hafta_satis}")
# print('O ay en az satılan ürünler; ')
# print(max_hafta_satis_urun[['Ürün Adı','Satış']])


# En yüksek toplam fiyatın olduğu ay ve o ay da satılan ürünler

# max_ay = df.resample('ME')['Toplam Fiyat (TL)'].sum()
# max_ay_fiyat = max_ay.idxmax()
# max_ay_satis = max_ay.max()
# max_ay_satis_urun = df[df.index.to_series().between(max_ay_fiyat - pd.offsets.MonthBegin(1), max_ay_fiyat)]
# print(f"En çok satış yapılan ay = {max_ay_fiyat}\n Toplam Satış = {max_ay_satis}")









