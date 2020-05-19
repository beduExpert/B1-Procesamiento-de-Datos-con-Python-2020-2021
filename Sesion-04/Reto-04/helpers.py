
def verificar_modificaciones(datos_productos, indice, df_productos, columna_nueva, df_productos_mas_columna_nueva, 
                             precios_descuento, df_productos_descuento, df_productos_sin_precio_ni_peso):
    
    import pandas as pd
    
    df_productos_esperado = pd.DataFrame(datos_productos, index=indice)
    if not df_productos_esperado.equals(df_productos):
        print(f'df_productos ha sido creado incorrectamente ... Favor de revisar')
        return
    
    print(f'== Verificación de Modificaciones ==\n')
    columna_nueva_serie = pd.Series(columna_nueva, index=indice)
    df_productos_mas_columna_nueva_2 = df_productos.copy()
    df_productos_mas_columna_nueva_2['nivel de dolor'] = columna_nueva_serie
    verificar_modificacion(df_productos_mas_columna_nueva_2, df_productos_mas_columna_nueva, 'Agrega por favor columna `columna_nueva` a `df_productos_mas_columna_nueva` con el nombre de columna "nivel de dolor"')
    
    precios_descuento_serie = pd.Series(precios_descuento, index=indice)
    df_productos_descuento_2 = df_productos.copy()
    df_productos_descuento_2['precio'] = precios_descuento_serie
    verificar_modificacion(df_productos_descuento_2, df_productos_descuento, 'Cambia por favor el `DataFrame` `df_productos_descuento` cambiando la columna `precio` por la información contenida en `precios_descuento`')
    
    df_productos_sin_precio_ni_peso_2 = df_productos.drop(columns=['precio', 'peso'])
    verificar_modificacion(df_productos_sin_precio_ni_peso_2, df_productos_sin_precio_ni_peso, 'Elimina por favor las columnas "precio" y "peso"')
    
def verificar_modificacion(esperada, recibida, descripcion):
    es_correcta = "Correcto" if esperada.equals(recibida) else "Incorrecto"
    respuesta = "Muchas gracias!" if es_correcta == "Correcto" else "Favor de revisar"
    print(f"\n- Descripción de pedido: {descripcion}")
    print(f"El pedido es {es_correcta} ... {respuesta}")