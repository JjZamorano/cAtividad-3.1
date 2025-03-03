import pandas as pd
import numpy as np

#mediana
def replace_numeric_median(df):
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    for col in numeric_columns:
        df[col] = df[col].fillna(df[col].median())
    return df

#forward fill
def replace_object_ffill(df):
    object_columns = df.select_dtypes(include=['object', 'datetime64', 'category']).columns
    for col in object_columns:
        df[col] = df[col].ffill()
    return df

#backward fill
def replace_object_bfill(df):
    object_columns = df.select_dtypes(include=['object', 'datetime64', 'category']).columns
    for col in object_columns:
        df[col] = df[col].bfill()
    return df

#reemplazar nulos con string especifico
def replace_object_string(df, string_value="NO_DATA"):
    object_columns = df.select_dtypes(include=['object', 'datetime64', 'category']).columns
    for col in object_columns:
        df[col] = df[col].fillna(string_value)
    return df

#reemplazar nulos
def replace_numeric_constant(df, constant=0):
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    for col in numeric_columns:
        df[col] = df[col].fillna(constant)
    return df

#Funcion menu
def main():
    #carga de dato
    df = pd.read_csv('Ventas_totales.csv')
    
    #guardar resultados
    df_median = replace_numeric_median(df.copy())
    df_median.to_csv('ventas_median.csv', index=False)
    print("Archivo ventas_median.csv")
    
    df_ffill = replace_object_ffill(df.copy())
    df_ffill.to_csv('ventas_ffill.csv', index=False)
    print("Archivo ventas_ffill.csv")
    
    df_bfill = replace_object_bfill(df.copy())
    df_bfill.to_csv('ventas_bfill.csv', index=False)
    print("Archivo ventas_bfill.csv")
    
    df_string = replace_object_string(df.copy(), "SIN_DATOS")
    df_string.to_csv('ventas_string.csv', index=False)
    print("Archivo ventas_string.csv")
    
    df_constant = replace_numeric_constant(df.copy(), -999)
    df_constant.to_csv('ventas_constant.csv', index=False)
    print("Archivo ventas_constant.csv")

#registro
if __name__ == "__main__":
    main()


