
def revisar_resultados(df_reto_3):
    
    import pandas as np
    import pandas.api.types as pdtypes
    
    assert pdtypes.is_int64_dtype(df_reto_3['is_potentially_hazardous_asteroid']), 'La columna "is_potentially_hazardous_asteroid" no ha sido transformada a tipo numerico'
    assert len(df_reto_3['is_potentially_hazardous_asteroid'].unique()) == 2, 'Hubo un error con la correspondencia de valores booleanos a numéricos. Hay más de dos valores posibles en la columna resultante'
    assert df_reto_3['relative_velocity.kilometers_per_minute'].equals(df_reto_3['relative_velocity.kilometers_per_hour'] / 60), 'La conversión de kilometros por hora a kilómetros por minuto no fue realizada correctamente'
    
    print(f'Todos los procesos fueron realizados exitosamente!')