import pandas as pd
from sklearn.preprocessing import LabelEncoder
#Label encoder verileri 0 ve 1 olarak değiştiriyor.

# Veriyi yükle
df = pd.read_excel(r'C:\Users\cavus\Desktop\global\veri on isleme\veri_on_isleme_ve_ozellik_muhendisligi.xlsx')

# Eksik gelir verilerini ortalama ile doldurma
df.fillna(df['Gelir'].mean(),inplace= True)
# print(df)

le = LabelEncoder()
df['Cinsiyet'] = le.fit_transform(df['Cinsiyet'])
print(df)
