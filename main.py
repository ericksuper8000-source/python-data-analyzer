from src.load_data import load_data
from datetime import datetime

# Cargar datos
Cargar_Csv = load_data('data/sales.csv')

# Pedir fecha
fecha_input = input('Ingrese la fecha (YYYY-MM-DD): ')

try:
    Fecha_Objetivo = datetime.strptime(fecha_input, "%Y-%m-%d").date() #2025-01-04
except ValueError:
    print("Formato de fecha inválido")
    exit()

Encontrado = False
total_dia = 0
total_prod_vendidos = 0

# Diccionario para acumular ventas por producto
ventas_por_producto = dict({})

for indice, venta in Cargar_Csv.iterrows():

    if venta['date'] == Fecha_Objetivo:
        Encontrado = True

        print(f'Fecha: {venta["date"]}')
        print(f'Producto: {venta["product"]}')
        print(f'Cantidad: {venta["quantity"]}')
        print(f'Precio: {venta["price"]}')
        print('------------------')

        # Acumuladores anteriores
        total_dia += venta["quantity"] * venta["price"]
        total_prod_vendidos += venta["quantity"]

        # Acumulación por producto
        producto = venta["product"]
        cantidad = venta["quantity"]

        if producto in ventas_por_producto:
            ventas_por_producto[producto] += cantidad
        else:
            ventas_por_producto[producto] = cantidad

# Resultados finales
if Encontrado:

    # Buscar producto más vendido
    producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
    max_cantidad = ventas_por_producto[producto_mas_vendido]

    print(f'Total vendido en el día: ${total_dia}')
    print(f'Total productos vendidos en el día: {total_prod_vendidos}')
    print(f'Producto más vendido: {producto_mas_vendido} ({max_cantidad} unidades)')

else:
    print('No hay ventas en esa fecha')