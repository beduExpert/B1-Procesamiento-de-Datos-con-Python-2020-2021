
def resumen_estadistico(df, df_dropped, mins, maxs, means, medians, stds):
    
    import pandas as pd
    
    error = False
    
    df_dropped_2 = df.drop(columns=['producto'])
    if not df_dropped_2.equals(df_dropped):
        print(f'La columna no-numérica no fue eliminada correctamente... Por favor inténtalo de nuevo')
        error = True
        
    if not df_dropped.min(axis=0).equals(mins):
        print(f'El valor mínimo no fue computado adecuadamente... Por favor inténtalo de nuevo')
        error = True
        
    if not df_dropped.max(axis=0).equals(maxs):
        print(f'El valor máximo no fue computado adecuadamente... Por favor inténtalo de nuevo')
        error = True
        
    if not df_dropped.mean(axis=0).equals(means):
        print(f'El promedio no fue computado adecuadamente... Por favor inténtalo de nuevo')
        error = True
    
    if not df_dropped.median(axis=0).equals(medians):
        print(f'La mediana no fue computada adecuadamente... Por favor inténtalo de nuevo')
        error = True
        
    if not df_dropped.std(axis=0).equals(stds):
        print(f'La desviación estándar no fue computada adecuadamente... Por favor inténtalo de nuevo')
        error = True
    
    if not error:
        rango = maxs - mins
        mins.name = 'Min'
        maxs.name = 'Max'
        rango.name = 'Rango'
        means.name = 'Promedio'
        medians.name = 'Mediana'
        stds.name = 'Std'
        
        resumen = pd.concat([mins, maxs, rango, means, medians, stds], axis=1)
        print(resumen)