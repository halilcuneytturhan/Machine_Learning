import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\cavus\Desktop\Pandas\teknolojik_urunler.xlsx")

df['Tarih'] = pd.to_datetime(np.random.choice(pd.date_range('2024-01-01','2024-12-31'),size=len(df)))
print(df.head())

df.to_excel('teknolojik_urunler_zamanli.xlsx',index=False)
print("Veriler dosyaya aktarıldı.")