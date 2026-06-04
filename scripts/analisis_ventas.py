import pandas as pd
import matplotlib.pyplot as plt

# Cargo los datos del csv
df = pd.read_csv('datos/ventas.csv')

# Calculo el total multiplicando cantidad por precio
df['total'] = df['cantidad'] * df['precio']

# Print para ver que todo cargó bien en la consola
print("--- RESUMEN DE VENTAS ---")
print(df)

total_general = df['total'].sum()
print(f"\nVenta Total General: ${total_general}")

# Agrupo por producto para el gráfico
resumen_productos = df.groupby('producto')['total'].sum()

# Armo el gráfico de barras
plt.figure()
resumen_productos.plot(kind='bar')
plt.title('Total de Ventas por Producto (Año 2026)')
plt.xlabel('Producto')
plt.ylabel('Ingresos ($)')

# Guardo el gráfico en la carpeta de resultados
plt.savefig('resultados/grafico_ventas.png')
print("\nGráfico guardado en resultados/grafico_ventas.png")
