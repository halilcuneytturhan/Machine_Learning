import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split , cross_val_score
from sklearn.tree import DecisionTreeClassifier # Bu sınıfın görevi verileri sınıflara ayırıp 1 veya 0 gibi sonuç verecek
from sklearn.metrics import accuracy_score # bu sınıf da çıktıların doğruluk değerini ölçmeye yarar.



df = pd.read_excel(r'C:\Users\cavus\Desktop\global\makine öğrenmesi\karar_agaci_veri_100.xlsx')


X = df[['Yas','Kan_Basinci','Kolesterol']]
y = df['Hastalik']

# X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=45)

# siniflandirma = DecisionTreeClassifier()
# siniflandirma.fit(X_train, y_train)

# y_pred = siniflandirma.predict(X_test)

# acc = accuracy_score(y_test, y_pred)
# print(f"Modelin doğruluk değeri = {acc:.2f}")

capraz_dogrulama = DecisionTreeClassifier(max_depth=4,min_samples_leaf=4,min_samples_split=9)

siniflandirma = cross_val_score(capraz_dogrulama,X,y, cv=11)
# print(f"Çapraz doğrulama sonucu olarak = {siniflandirma}")
# print(f"Ortalama çapraz doğruluk değeri sonucu = {siniflandirma.mean():.2f}")

capraz_dogrulama.fit(X,y)
# Kullanıcıdan veri alalım

yas = int(input("Lütfen yaşınızı giriniz = "))
kan_basinci = int(input("Lütfen Kan Basıncı değerini giriniz = "))
kolesterol = int(input("Lütfen Kolesterolünüzü giriniz = "))


#Kullanıcıdan alınan veriyi modelin anlayacağı dile çevirme

yeni_veri = pd.DataFrame([[yas,kan_basinci,kolesterol]], columns= ['Yas','Kan_Basinci','Kolesterol'])

tahmin = capraz_dogrulama.predict(yeni_veri)

#Tahmin sonucunu kullanıcıya göster

if (tahmin[0] == 1):
    print("Hastalık var")
else:
    print("Hastalık yok")
    
    