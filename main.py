from src.load_data import load_data
from datetime import datetime

# Cargar datos
Cargar_Csv = load_data('data/sales.csv')

# Pedir fecha al usuario
fecha_input = input('Ingrese la fecha (YYYY-MM-DD): ') # 2025-01-04

try:
    Fecha_Objetivo = datetime.strptime(fecha_input, "%Y-%m-%d").date()
except ValueError:
    print("Formato de fecha inválido")
    exit()

# Buscar ventas
Encontrado = False

for indice, venta in Cargar_Csv.iterrows():

    if venta['date'] == Fecha_Objetivo:
        Encontrado = True

        print(f'Fecha: {venta["date"]}')
        print(f'Producto: {venta["product"]}')
        print(f'Cantidad: {venta["quantity"]}')
        print(f'Precio: {venta["price"]}')
        print('------------------')

# Caso donde no hubo coincidencias
if not Encontrado:
    print('No hay ventas en esa fecha')