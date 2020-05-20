
def revisar_limpieza(df, df_copy):
    df_2 = df.copy()
    df_2 = df_2.dropna(axis=0, how='all')
    df_2 = df_2.dropna(axis=1, how='all')
    df_2['cantidad_vendidos'] = df_2['cantidad_vendidos'].fillna(0)
    df_2 = df_2.dropna(axis=0)
    
    if not df_2.equals(df_copy):
        print(f'La transformación no fue realizada adecuadamente... Por favor revisa tu procedimiento.\n')
        print(f'DataFrame esperado:\n')
        print(df_2)
        
        print(f'\nDataframe obtenido:\n')
        print(df_copy)
    else:
        print(f'La transformación fue realizada exitosamente... Muchas gracias!')