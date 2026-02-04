from src.load_data import load_data

Ruta_Csv = 'data/sales.csv'

Cargar_Csv = load_data(Ruta_Csv)

print(Cargar_Csv.head())

Dates = Cargar_Csv['date']

print (f'--------')

print (f'{Dates}')

for elemento in enumerate(Dates):
    print (f'{elemento[1]}')