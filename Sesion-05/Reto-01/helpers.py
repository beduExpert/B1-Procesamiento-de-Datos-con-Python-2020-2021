def obtener_calificaciones(aciertos, porcentajes):
    
    import numpy as np
    
    porcentajes_correcto = np.divide(np.multiply(aciertos, 100), 68)
    if not porcentajes_correcto.equals(porcentajes):
        print(f'Hay algún error en tus cálculos...')
        print(f'¡Por favor intenta de nuevo!')
        return
        
    print(f'== Calificaciones finales ==\n')
    print(f'{("Id del Alumno"):15} | {("Porcentaje de Aciertos"):15}')
    print(f'----------------------------------------')
    for i in range(0, len(porcentajes)):
        print(f'{i:<15} | {np.round(porcentajes[i], 2):<}%')