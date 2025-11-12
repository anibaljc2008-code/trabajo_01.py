# Programa 5: conversión de dólar a guaraníes

# Leer monto en dólares
dolares = float(input("Ingrese el monto en dólares: "))

# Leer cotización del día
cotizacion = float(input("Ingrese la cotización actual del dólar en guaraníes: "))

# Calcular monto en guaraníes
guaranies = dolares * cotizacion

# Mostrar resultado
print(dolares, "dólares equivalen a", guaranies, "guaraníes.")