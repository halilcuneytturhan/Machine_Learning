import pandas as pd
from sklearn.preprocessing import LabelEncoder
#Label encoder verileri 0 ve 1 olarak değiştiriyor.
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns



# Veriyi yükle
df = pd.read_excel(r'C:\Users\cavus\Desktop\global\veri on isleme\veri_on_isleme_ve_ozellik_muhendisligi.xlsx')

# Eksik gelir verilerini ortalama ile doldurma
df.fillna(df['Gelir'].mean(),inplace= True)
# print(df)

le = LabelEncoder()
# df['Cinsiyet'] = le.fit_transform(df['Cinsiyet'])
# print(df)

standart = StandardScaler()
# df[['Yaş','Gelir']] = standart.fit_transform(df[['Yaş','Gelir']])
# print(df)

#Burada da bins içinde 4 adet yazıyorsak 3 adet etiket yazabiliriz 
df['Gelir_Grubu'] = pd.cut(df['Gelir'],bins=[0,3000,5000,7000],labels=['Düşük','Orta','Yüksek'])
# print(df)
# df.drop('ID',axis=1,inplace=True)   
# print(df)
# df.to_excel('Kategorik_Gelir.xlsx',index=False)
# print("Oluşturuldu.")


# Görselleştirme
# plt.figure(figsize=(10,6))
# plt.hist(df['Yaş'], # Yaş kısmı ile tablo oluştur.
#          bins=10, # Bins kısmında da kaç parçaya bölüneceği yazıyor 2 yaparsak 2 grafik, 10 yaparsak 10 grafik
#          color='skyblue' # Color kısmı barın içerisindeki renk
#          ,edgecolor='black' # Dışındaki çizgi
#          )
# plt.xlabel('Yaş')
# plt.ylabel('Frekans')
# plt.title('Yaş Dağılımı')



# 2 meslek grubunu kıyaslayacağımız zaman seaborn kütüphanesi kullanılacak.
plt.figure(figsize=(10,6))
sns.countplot(x='Gelir_Grubu',hue='Yaş',data=df)
plt.xlabel('Gelir Grubu')
plt.ylabel('Cinsiyet')
plt.show()

