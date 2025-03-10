import pandas as pd

# Cargar Mexico.csv
df = pd.read_csv('Mexico.csv')

# Ver valores nulos iniciales
print("\nVALORES NULOS ORIGINALES")
print(df.isnull().sum())
print("\nTotal de nulos:", df.isnull().sum().sum())

# Rellenar con valor anterior (ffill)
df_ffill = df.fillna(method='ffill')
print("\nDESPUES DE FFILL")
print(df_ffill.isnull().sum())
print("\nTotal de nulos:", df_ffill.isnull().sum().sum())

# Rellenar con valor siguiente (bfill)
df_bfill = df.fillna(method='bfill')
print("\nDESPUES DE BFILL")
print(df_bfill.isnull().sum())
print("\nTotal de nulos:", df_bfill.isnull().sum().sum())

# Rellenar con texto
df_texto = df.fillna('Sin datos')
print("\nDESPUES DE RELLENAR CON TEXTO")
print(df_texto.isnull().sum())
print("\nTotal de nulos:", df_texto.isnull().sum().sum())

# Rellenar con promedio
df_promedio = df.fillna(df.mean(numeric_only=True))
print("\nDESPUES DE RELLENAR CON PROMEDIO")
print(df_promedio.isnull().sum())
print("\nTotal de nulos:", df_promedio.isnull().sum().sum())

#Rellenar con mediana
df_mediana = df.fillna(df.median(numeric_only=True))
print("\nDESPUES DE RELLENAR CON MEDIANA")
print(df_mediana.isnull().sum())
print("\nTotal de nulos:", df_mediana.isnull().sum().sum())

# Rellenar con constante (cero)
df_constante = df.fillna(0)
print("\DESPUES DE RELLENAR CON CERO")
print(df_constante.isnull().sum())
print("\nTotal de nulos:", df_constante.isnull().sum().sum())
