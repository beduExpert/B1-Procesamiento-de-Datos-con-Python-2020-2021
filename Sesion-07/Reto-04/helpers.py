
def revisar_aplicacion(df_reto_4):
    
    assert 'proportion_of_max_diameter_to_earth' in df_reto_4, 'No existe una columna llamada "proportion_of_max_diameter_to_earth" en el DataFrame'
    assert df_reto_4['proportion_of_max_diameter_to_earth'].equals(df_reto_4['estimated_diameter.meters.estimated_diameter_max'] / 12742000), 'La transformacion no fue realizada adecuadamente'
    
    print(f'La transformación y creación de una nueva columna fue realizada exitosamente!')