from src.load_data import load_data
from datetime import datetime

# Cargar datos
Cargar_Csv = load_data('data/sales.csv')

# Pedir fecha
fecha_input = input('Ingrese la fecha (YYYY-MM-DD): ')

try:
    Fecha_Objetivo = datetime.strptime(fecha_input, "%Y-%m-%d").date()
except ValueError:
    print("Formato de fecha inválido")
    exit()

Encontrado = False
Lista_Sumatoria = []

for indice, venta in Cargar_Csv.iterrows():

    if venta['date'] == Fecha_Objetivo:
        Encontrado = True

        print(f'Fecha: {venta["date"]}')
        print(f'Producto: {venta["product"]}')
        print(f'Cantidad: {venta["quantity"]}')
        print(f'Precio: {venta["price"]}')
        print('------------------')

        Total = venta["quantity"] * venta["price"]
        Lista_Sumatoria.append(Total)

# Aqui se realiza la suma
if Encontrado:
    Resultado = sum(Lista_Sumatoria)
    print(f'Total vendido en el día: ${Resultado}')
else:
    print('No hay ventas en esa fecha')