
def verificar_indexaciones(datos_productos, indice, df_productos, pm_sw, p4_final, amd_lt_n, primer_p5, pm_lt_pp, t_pcdr, p3_p6_pd):
    
    import pandas as pd
    
    df_productos_esperado = pd.DataFrame(datos_productos, index=indice)
    if not df_productos_esperado.equals(df_productos):
        print(f'df_productos ha sido creado incorrectamente ... Favor de revisar')
        return
    
    print(f'== Verificación de Indexaciones ==\n')
    verificar_indexacion(df_productos.loc[[3, 5]], pm_sw, 'DataFrame que contenga los productos "Pikame Mucho" y "Stevie Wonder"')
    verificar_indexacion(df_productos.loc[4:], p4_final, 'DataFrame que contenga desde el producto #4 hasta el último')
    verificar_indexacion(df_productos.loc[[7, 4, 6]], amd_lt_n, 'DataFrame que contenga los productos "El AyMeDuele", "Lazarillo de Tormes" y "Needle"')
    verificar_indexacion(df_productos.loc[:5], primer_p5, 'DataFrame que contenga desde el primer producto hasta el producto #5')
    verificar_indexacion(df_productos.loc[[3, 4], ['nombre', 'precio', 'peso']], pm_lt_pp, 'DataFrame que contenga los productos "Pikame Mucho" y "Lazarillo de Tormes", pero sólo con las columnas "nombre", "precio" y "peso"')
    verificar_indexacion(df_productos[['nombre', 'precio', 'capacidad de destrucción retinal']], t_pcdr, "DataFrame que contenga todos los productos pero con sólo las columnas 'nombre', 'precio' y 'capacidad de destrucción retinal'")
    verificar_indexacion(df_productos.loc[3:6, ['nombre', 'precio', 'disponible']], p3_p6_pd, "DataFrame que contenga desde el producto #3 hasta el #6, pero sólo las columnas 'nombre', 'precio' y 'disponible'")
    
def verificar_indexacion(esperada, recibida, descripcion):
    es_correcta = "Correcto" if esperada.equals(recibida) else "Incorrecto"
    respuesta = "Muchas gracias!" if es_correcta == "Correcto" else "Favor de revisar"
    print(f"\n- Descripción de pedido: {descripcion}")
    print(f"El pedido es {es_correcta} ... {respuesta}")