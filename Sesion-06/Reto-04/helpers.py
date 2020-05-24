
def revisar_dataframe(ventas_dataframe, productos, ventas_enero, ventas_febrero, ventas_marzo, ventas_abril, ventas_mayo,
                      ventas_junio, ventas_julio, ventas_agosto, ventas_septiembre,
                      ventas_octubre, ventas_noviembre, ventas_diciembre):
    
    import pandas as pd
    
    def concatenar_listas_horizontalmente(lista_de_listas, indice):
    
        meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre',
                'diciembre']

        lista_de_series = []
        for i in range(len(lista_de_listas)):
            lista_de_series.append(pd.Series(lista_de_listas[i], index=indice, name=meses[i]))

        dataframe = pd.concat(lista_de_series, axis=1)
        return dataframe
    
    ventas_dataframe_2 = concatenar_listas_horizontalmente([ventas_enero, ventas_febrero, ventas_marzo, ventas_abril, ventas_mayo,
                                                      ventas_junio, ventas_julio, ventas_agosto, ventas_septiembre,
                                                      ventas_octubre, ventas_noviembre, ventas_diciembre], productos)
    ventas_dataframe_2['total_por_producto'] = ventas_dataframe_2.sum(axis=1)
    total_por_mes = ventas_dataframe_2.sum(axis=0)
    total_por_mes.name = 'total_por_mes'
    ventas_dataframe_2 = ventas_dataframe_2.append(total_por_mes)
    
    if ventas_dataframe.equals(ventas_dataframe_2):
        print(f'Felicidades! El procedimiento fue realizado correctamente.')
        import seaborn as sns
        import matplotlib.pyplot as plt
        
        fig, axs = plt.subplots(2, 1, figsize=(8, 12))
        sin_total_por_mes = ventas_dataframe.drop(index='total_por_mes')
        sin_total_por_mes.sort_values('total_por_producto', ascending=False, inplace=True)
        axs[0].set_title('Ventas totales por producto')
        sns.barplot(sin_total_por_mes['total_por_producto'], sin_total_por_mes.index, ax=axs[0])
        
        axs[1].set_title('Ventas totales por mes')
        sin_total_por_producto = ventas_dataframe.drop(columns='total_por_producto')
        sns.barplot(sin_total_por_producto.columns, sin_total_por_producto.loc['total_por_mes'], orient='v', ax=axs[1])
        for item in axs[1].get_xticklabels():
            item.set_rotation(45)
        
    else:
        print(f'Hubo un error!\n')
        print('Dataframe esperado:')
        print(ventas_dataframe_2)
        print('\nDataframe recibido:')
        print(ventas_dataframe)