
def checar_conversiones(df_reto_1):
    
    import pandas as pd
    import pandas.api.types as ptypes
    
    assert ptypes.is_float_dtype(df_reto_1['relative_velocity.kilometers_per_hour']), 'Cuidado... La columna `relative_velocity.kilometers_per_hour` no es de tipo `float64`'
    assert ptypes.is_datetime64_any_dtype(df_reto_1['close_approach_date']), 'Cuidado... La columna `close_approach_date` no es de tipo `datetime64[ns]`'
    assert ptypes.is_datetime64_any_dtype(df_reto_1['epoch_date_close_approach']), 'Cuidado... La columna `epoch_date_close_approach` no es de tipo `datetime64[ns]'
    
    print(f'¡Éxito! ¡Todas tus conversiones fueron realizadas adecuadamente!')