import pandas as pd
 Matias1507-patch-1

# Leer archivo CSV

df = pd.read_csv("datos/ventas.csv")

# Crear columna total

df["total"] = df["cantidad"] * df["precio"]

# Calcular ventas totales

ventas_totales = df["total"].sum()

# Producto más vendido

producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

# Mostrar resultados

print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)
=======
import matplotlib.pyplot as plt

# 1. Leer los datos del archivo CSV que creamos
try:
    df = pd.read_csv('datos/ventas.csv')
    print("Datos cargados correctamente.")
except FileNotFoundError:
    print("Error: No se encontró el archivo ventas.csv en la carpeta datos.")
    exit()

# 2. Calcular la columna Total (Cantidad * Precio)
df['total'] = df['cantidad'] * df['precio']

# 3. Mostrar un resumen básico por pantalla
print("\n--- RESUMEN DE VENTAS ---")
print(df)

total_general = df['total'].sum()
print(f"\nVenta Total General: ${total_general}")

# 4. Agrupar por producto para ver cuál vendió más
resumen_productos = df.groupby('producto')['total'].sum()

# 5. Generar y guardar el gráfico de barras requerido por el TP
plt.figure(figsize=(8, 5))
resumen_productos.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Total de Ventas por Producto (Año 2026)')
plt.xlabel('Producto')
plt.ylabel('Ingresos ($)')
plt.xticks(rotation=0)
plt.tight_layout()

# Guardamos el gráfico en la carpeta de resultados
plt.savefig('resultados/grafico_ventas.png')
print("\nGráfico generado con éxito en 'resultados/grafico_ventas.png'.")
 main
