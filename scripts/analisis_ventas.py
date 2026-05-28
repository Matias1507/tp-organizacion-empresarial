import pandas as pd

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
