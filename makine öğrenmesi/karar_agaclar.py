import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier # Bu sınıfın görevi verileri sınıflara ayırıp 1 veya 0 gibi sonuç verecek
from sklearn.metrics import accuracy_score # bu sınıf da çıktıların doğruluk değerini ölçmeye yarar.

# Veriyi hazırlama : yaş, kan basıncı, kolesterol ve hastalık durumu tespiti

# data = {
#     'Yaş':[25,50,45,30,60],
#     'Kan_basinci': [120,140,130,110,150],
#     'Kolesterol':[180,240,220,160,220],
#     'Hastalik' : [0,1,1,0,1] # 0 -> Hayır, 1 -> Hasta
# }

# df = pd.DataFrame(data)

df = pd.read_excel(r'C:\Users\cavus\Desktop\global\makine öğrenmesi\karar_agaci_veri_100.xlsx')


X = df[['Yas','Kan_Basinci','Kolesterol']]
y = df['Hastalik']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=45)

siniflandirma = DecisionTreeClassifier()
siniflandirma.fit(X_train, y_train)

y_pred = siniflandirma.predict(X_test)

acc = accuracy_score(y_test, y_pred)
# print(f"Modelin doğruluk değeri = {acc}")

# Kullanıcıdan veri alma
yas = int(input("Yaşınızı giriniz = "))
kan_basinci = int(input("Kan basınıcızı giriniz = "))
kolesterol = int(input("Kolesterol seviyesini giriniz = "))



r"""C:\Users\cavus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\sklearn\utils\validation.py:2739: UserWarning: X does not have valid feature names, but DecisionTreeClassifier was fitted with feature names
  warnings.warn(
    Bunun çıkmasının sebebi sklearn kütüphanesi bir df istiyor biz kullanıcıdan aldığımız verileri df ye çevirmemiz gerekiyor o da altta ki satırda mevcut.
"""

# Kullanıcı verisini df ye çevirme
kullanici_verisi = pd.DataFrame([[yas,kan_basinci,kolesterol]], columns= ['Yas','Kan_Basinci','Kolesterol'])

# Tahmin oluştur
# modeli eğitmek icin predict kullanırız.
tahmin = siniflandirma.predict(kullanici_verisi)
sonuc = "Hastalık var" if tahmin[0] == 1 else "Hastalık Yok"
print(f"Tahmin sonucu = {sonuc}")
