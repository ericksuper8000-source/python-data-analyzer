from src.load_data import load_data

Ruta_Csv = 'data/sales.csv'

Cargar_Csv = load_data(Ruta_Csv)

print(Cargar_Csv.head())

print (f'-------- Iniciamos aqui --------------')

Fecha_Objetivo = '2025-01-04'

for indice, venta in Cargar_Csv.iterrows():
    Fecha = venta['date']
    Producto = venta['product']
    Cantidad = venta['quantity']
    Precio = venta['price']

    if (Fecha == Fecha_Objetivo):
        print (f'{venta}')