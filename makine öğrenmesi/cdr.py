import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#veriyi hazırlama

data = {
    'Ev_Buyuklugu' : [120,250,175,300,220],
    'Oda_Sayisi' : [3,5,4,6,4],
    'Fiyat':[2400000,5000000,3500000,6000000,4400000]
}

df = pd.DataFrame(data)
# Burayı bir dataframe haline getirdik.
X = df[['Ev_Buyuklugu','Oda_Sayisi']] #girdi - # Burada tablo halindedir. Burayı bir bütün olarak alıyor -Başlık ve diğer girdiler dahil.
y = df['Fiyat'] #çıktı - # Burada dizi halinde

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=45)

# Modeli Oluşturma ve eğitme

model = LinearRegression() #Bunu yapacaksın
model.fit(X_train, y_train) #Eğitilmiş veriler var burada


# Burası kodun düzgün çalışıp çalışılmayacağını test eder.

# y_pred = model.predict(X_test) #Eğitilmiş bir modeli kullanacağız burada (X_test verisini y_pred'e at, doğruluğunu göstermek için)
# Kodun doğruluk oranını ölçer. 0'a yakın en doğrudur.
# Hata hesaplama, ne kadar az o kadar iyi sonuç
# Verinin tutarlı olduğunu öğrendik ve artık kullanmamıza gerek yok çünkü veri hatası 0 alıyor.

# mse = mean_squared_error(y_test,y_pred)
# rmse = np.sqrt(mse) #karekökünü alır hatayı daha anlamlı hale getirir.
# print(f"Ortalama kare hatası(mse) = {rmse}")


# ev_buyuklugu = float(input("Lütfen evin büyüklüğünü (m²) girin = "))

# tahmini_fiyat = model.predict([[ev_buyuklugu]]) # Çift parantez kullanmamızın sebebi burada
# #Model eğitilirken [] 1 tane olması tek boyut yani bir dizi olarak görür [[]] 2 tane olması tek sayı değil tablo olarak algılamasını sağlar.


# print(f"Bu evin tahmini fiyatı = {tahmini_fiyat[0]:.2f} TL ") #Birden fazla index olsaydı 1 yazsak çalışırdı.
ev_buyuklugu = float(input("Lütfen evin büyüklüğünü (m²) girin = "))
oda_sayisi = int(input("Lütfen oda sayısı giriniz= "))

tahmini_fiyat = model.predict([[ev_buyuklugu,oda_sayisi]])
print(f"Bu evin tahmini fiyatı = {tahmini_fiyat[0]:.2f}")




