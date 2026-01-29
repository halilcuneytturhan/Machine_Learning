import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

df = pd.read_excel(r'C:\Users\cavus\Desktop\global\makine öğrenmesi\karar_agaci_veri_100.xlsx')

X = df[['Yas','Kan_Basinci','Kolesterol']]
y = df['Hastalik']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=45)

siniflandirma = DecisionTreeClassifier()
siniflandirma.fit(X_train,y_train)

y_pred = siniflandirma.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(f"Doğruluk değeri = {acc}")




