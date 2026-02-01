import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler



df = pd.read_excel(r"C:\Users\cavus\Desktop\global\veri on isleme\veri_on_isleme_ve_ozellik_muhendisligi.xlsx")

# print(df)

# Cinsiyet ve gelirleri ortalama değer ile doldurma

df.fillna(df['Gelir'].mean(),inplace=True)

#Cinsiyet ve meslek sütunlarını sayısal hale getirelim.

le = LabelEncoder()
df['Cinsiyet'] = le.fit_transform(df['Cinsiyet'])
df['Meslek'] = le.fit_transform(df['Meslek'])
# print(df)

#Girdi ve çıktı değerleri
x = df[['Yaş','Meslek','Cinsiyet']] # girdi
y = df['Gelir'] # çıktı

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# Ölçeklendirme
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train) # Train verileri hem fit olur hem de transforum yapılır.
x_test = scaler.transform(x_test) # Test verilerinde fit kullanılmaz.


# Modeli oluştur ve eğit
model = LinearRegression()
model.fit(x_train,y_train)

# Modeli test etmek
acc = model.score(x_test,y_test)
print(f"Modelin doğruluk oranı = {acc*100:.2f}%")


# Daha karmaşık bir model kullan
rf_model = RandomForestRegressor(n_estimators=80,random_state=1)
rf_model.fit(x_train,y_train)

rf_acc = rf_model.score(x_test,y_test)
print(f"RF Modelinin doğruluk oran = {rf_acc*100:.2f}%")






# Kullanıcıdan veri alalım
yas = int(input('Lütfen yaşınızı giriniz= '))
meslek = input('Lütfen mesleğinizi giriniz = ').capitalize()
cinsiyet = input('Lütfen cinsiyetinizi giriniz (Erkek - Kadın) = ').capitalize()

# # Kullanıcıdan alınan mesleği kodlayalım. (Label encoding)
meslek_kod = le.transform([meslek])[0]

if cinsiyet == 'Erkek':
    cinsiyet_kod =1
elif cinsiyet == 'Kadın':
    cinsiyet_kod = 0
else:
    raise ValueError('Geçersiz işlem')


yeni_veri = pd.DataFrame([[yas,meslek_kod,cinsiyet_kod]], columns=['Yaş', 'Meslek','Cinsiyet'])
yeni_veri_scaled = scaler.transform(yeni_veri)
tahmin = rf_model.predict(yeni_veri_scaled)
print(f"Ortlama maaş tahmini = {tahmin[0]:.2f} TL")






