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

capraz_dogrulama = DecisionTreeClassifier()
siniflandirma = cross_val_score(capraz_dogrulama,X,y, cv=11)
print(f"Çapraz doğrulama sonucu olarak = {siniflandirma}")
print(f"Ortalama çapraz doğruluk değeri sonucu = {siniflandirma.mean():.2f}")


