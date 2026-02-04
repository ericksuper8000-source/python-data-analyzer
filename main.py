from src.load_data import load_data

Ruta_Csv = 'data/sales.csv'

Cargar_Csv = load_data(Ruta_Csv)

print(Cargar_Csv.head())

print (f'Todo bien')