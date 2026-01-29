df = pd.read_excel('teknolojik_urunler_zamanli.xlsx')

df['Tarih'] = pd.to_datetime(df['Tarih'])
print(df.head())