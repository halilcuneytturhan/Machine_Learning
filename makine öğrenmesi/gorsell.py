import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score


df = pd.read_excel(r'C:\Users\cavus\Desktop\global\makine öğrenmesi\karar_agaci_veri_100.xlsx')

# Yaş ile hastalık arasındaki ilişkiyi gösterme
plt.figure(figsize=(10,6)) # Veriye şekil vermek için kullanılan boyut ölçüsü
sns.histplot(data=df, # Veri olarak dataframe oluşturduk
             x='Yas', # X olarak yaş aldık
             hue='Hastalik', # Kim var kim yok falan orası için hastalık seçtik
             multiple='stack', # multiple de üst üste yığın olsun diye stack yaptık
             kde=False # Bu görselin içerisinde bir çizgi olmasın diye false dedik kde de
             )
plt.xlabel('Yaş')
plt.title('Hastalık ile yaş arasındaki ilişki')
plt.ylabel('Kişi sayısı')
# plt.show()
 
 
plt.figure(figsize=(10,6))
sns.histplot(data=df, x='Kan_Basinci',hue='Hastalik', multiple='stack',kde=False)
plt.xlabel('Kan Basıncı')
plt.ylabel('Kişi sayısı')
plt.title('Kan Basıncı ile hastalık arasındaki ilişki')
plt.show()




