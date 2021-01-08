def checar_subconjuntos(df_february, df_hazardous, df_bigger_than_1000):
    
    import pandas as pd

    assert (df_hazardous['is_potentially_hazardous_asteroid'] == 0).sum() == 0, 'Algunos records en `df_hazardous` pertenecen a objetos donde is_potentially_hazardous_asteroid es `False`'
    assert (df_hazardous['is_potentially_hazardous_asteroid'] == 1).sum() > 0, 'No hay ningun record en `df_hazardous` donde is_potentially_hazardous_asteroid sea `True`'
    
    assert (df_bigger_than_1000['estimated_diameter.meters.estimated_diameter_max'] <= 1000).sum() == 0, 'Algunos records en `df_bigger_than_1000` pertenecen a objetos con diámetro menor a 1000 metros'
    assert (df_bigger_than_1000['estimated_diameter.meters.estimated_diameter_max'] > 1000).sum() > 0, 'No hay ningún record en `df_bigger_than_1000` que pertenezca a objetos con diámetro mayor a 1000 metros'
    
    february = pd.to_datetime('1995-02-01', format='%Y-%m-%d').timestamp() * 1000
    march = pd.to_datetime('1995-03-01', format='%Y-%m-%d').timestamp() * 1000 
    
    assert (df_february['epoch_date_close_approach'] < february).sum() == 0, 'Algunos records de `df_february` pertenecen a meses anteriores a Febrero de 1995'
    assert (df_february['epoch_date_close_approach'] >= march).sum() == 0, 'Algunos records de `df_february` pertenecen a meses posteriores a Febrero de 1995'
    
    print('Todos tus subconjuntos son correctos. ¡Gran trabajo!')