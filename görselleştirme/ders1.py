import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


df = pd.read_excel(r'C:\Users\cavus\Desktop\global\pandas\teknolojik_urunler_zamanli.xlsx')

df['Tarih'] = pd.to_datetime(df['Tarih'])
df.set_index('Tarih', inplace=True)

def ekran_temizleme():
    if(os.name == 'nt'):
        os.system ('cls')
    else:
        os.system('clear')




def menu():
    print("Grafik Seçenekleri: ")
    print("1. Satışların zaman içerisindeki değişimi (Çizgi Grafik)")
    print("2. Aylık Toplam Satışlar (Bar Grafik)")
    print("3. Kategorilere Göre Satış Dağılımı (Pasta Grafik)")
    print("4. Fiyat ve satış ilişkisi (Scatter Plot)")
    print("5. Fiyat dağılımı grafiği (Histogram)")
    print("6. Aylık satış miktarları (Çizgi Grafik)")
    print("7. Fiyat kategorisine göre toplam satışlar (Bar Grafik)")
    print("0. Çıkış")

    girilen_deger = input("Seçiminizi yapın= ")

    try:
        #girilen değeri tam sayıya cevirmek icin try bloğu kullandık.
        return int(girilen_deger)
    except ValueError:
        return -1
    


def grafik_secimi(secilen):
    if (secilen == 1):
        df['Satış'].plot(kind='line',xlabel='Fiyat (TL)',ylabel='Satış',title="Satışların zaman içerisindeki değişimi")
        plt.show()
        
    elif (secilen == 2):
        toplam_satis = df.resample('ME')['Satış'].sum().plot(kind='bar',xlabel='Toplam Satış',ylabel='Ay',title="Aylık Toplam Satışlar")
        plt.show()
        
    elif(secilen==3):
        kategori=df.groupby('Kategori')['Satış'].sum().plot(kind='pie',xlabel='Toplam Satış',y='',title="Kategorilere göre Toplam Satışlar")
        plt.show()
        
    elif(secilen==4):
        noktasal = df.plot(kind='scatter',title="Noktasal grafik",x='Fiyat (TL)',y = 'Satış')
        noktasal = np.polyfit(df['Fiyat (TL)'] , df['Satış'], 1)
        p = np.poly1d(noktasal)
        plt.plot(df['Fiyat (TL)'],p(df['Fiyat (TL)']),color = 'red')
        plt.show()
    
    elif(secilen==6):
        aylik_satis = df.resample('ME')['Satış'].sum()
        aylik_satis.plot(kind='line',title="Aylık satış miktarı")
        plt.xlabel("Ay")
        plt.ylabel('Satış miktarı')
        plt.show() 
        
    elif(secilen==7):
        bins = [0,2000,5000,10000,20000,30000]
        # 5 kategori oluşturabilmek için 6 tane sınıra ihtiyacımız vardır.
        labels = ['Düşük','Orta','Yüksek','Çok Yüksek','Lüks'] 
        df['Fiyat Kategorisi'] = pd.cut(df['Fiyat (TL)'], bins = bins, labels=labels)

        # Fiyat kategorisine göre sınıflandırdık ve sonra görselleştirme işlemlerini yapalım
        df.groupby('Fiyat Kategorisi')['Satış'].sum().plot(kind='bar',title='Fiyat kategorisine göre toplam satışlar',xlabel='Fiyat Kategorisi',ylabel='Toplam Satış')
        plt.show()
        
while True:
    ekran_temizleme()
    secim = menu()
    if (secim == 0):
        print('Çıkış yaptınız...')
        break

    elif( 1<= secim <=7 ):
        grafik_secimi(secim)
        
    else:
        print("Lütfen geçerli bir sayı giriniz...")
                






# Satışların zaman içerisinde değişimini gösteren bir çizgi grafiği
# Sayısal değerleri çekmek zorunda burada
# df['Satış'].plot(title="Satışların zaman içindeki değişimi", xlabel="Tarih", ylabel="Satış miktarı")
# plt.show()

# aylik_satis = df.resample('ME')['Satış'].sum()
# aylik_satis.plot(kind='bar',title="Aylık satış miktarı", xlabel='Ay',ylabel='Satış miktarı')
# plt.show()

# pasta grafiğinin kategorilere göre satış dağılımı
# kategorilere_gore_satis = df.groupby('Kategori')['Satış'].sum()
# kategorilere_gore_satis.plot(kind='pie',autopct='%1.1f%%',title='aylık')
# plt.ylabel('')
# plt.show()

# df.plot(kind='scatter',x='Fiyat (TL)',y='Satış', title='Satış')
# plt.show()

# Aylık satışları çizgi grafiği olarak gösteren kod
# aylik_satis = df.resample('ME')['Satış'].sum()
# aylik_satis.plot(kind='line',title="Aylık satış miktarı")
# plt.xlabel("Ay")
# plt.ylabel('Satış miktarı')
# plt.show() 

# Noktasal grafiğe 1 tane line atalım ve alt üst ilişkisini bu şekilde kuralım 

# noktasal = df.plot(kind='scatter',title="Noktasal grafik",x='Fiyat (TL)',y = 'Satış')

# noktasal = np.polyfit(df['Fiyat (TL)'] , df['Satış'], 1)
# p = np.poly1d(noktasal)
# plt.plot(df['Fiyat (TL)'],p(df['Fiyat (TL)']),color = 'red')
# plt.show()

# Fiyatı kategorilerine göre ayıralım.

# bins = [0,2000,5000,10000,20000,30000]
# # 5 kategori oluşturabilmek için 6 tane sınıra ihtiyacımız vardır.
# labels = ['Düşük','Orta','Yüksek','Çok Yüksek','Lüks'] 
# df['Fiyat Kategorisi'] = pd.cut(df['Fiyat (TL)'], bins = bins, labels=labels)

# # Fiyat kategorisine göre sınıflandırdık ve sonra görselleştirme işlemlerini yapalım
# df.groupby('Fiyat Kategorisi')['Satış'].sum().plot(kind='bar',title='Fiyat kategorisine göre toplam satışlar',xlabel='Fiyat Kategorisi',ylabel='Toplam Satış')
# plt.show()