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

# Filtrado vectorizado
ventas_dia = Cargar_Csv[Cargar_Csv['date'] == Fecha_Objetivo]

if ventas_dia.empty:
    print("No hay ventas en esa fecha")
else:
    # Métricas vectorizadas
    total_dia = (ventas_dia['quantity'] * ventas_dia['price']).sum()
    total_unidades = ventas_dia['quantity'].sum()

    # Producto más vendido usando groupby
    ventas_por_producto = ventas_dia.groupby("product")["quantity"].sum()
    producto_mas_vendido = ventas_por_producto.idxmax()
    max_cantidad = ventas_por_producto.max()

    print(f'Total de productos vendidos en ({Fecha_Objetivo}): {total_unidades}')
    print(f'Total vendido en ({Fecha_Objetivo}): ${total_dia}')
    print(f'Producto más vendido: {producto_mas_vendido} ({max_cantidad} unidades)')