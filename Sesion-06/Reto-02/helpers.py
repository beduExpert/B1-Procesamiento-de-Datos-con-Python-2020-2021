
def revisar_potencia_de_dos(potencia_de_dos):
    
    import numpy as np
    
    if potencia_de_dos(0) != np.power(2, 0):
        print(f'Error!')
        print(f'Computando 2^0 ... Resultado esperado: {np.power(2, 0)} - Resultado obtenido {potencia_de_dos(0)}')
        return
    
    if potencia_de_dos(2) != np.power(2, 2):
        print(f'Error!')
        print(f'Computando 2^2 ... Resultado esperado: {np.power(2, 2)} - Resultado obtenido {potencia_de_dos(2)}')
        return
    
    if potencia_de_dos(8) != np.power(2, 8):
        print(f'Error!')
        print(f'Computando 2^8 ... Resultado esperado: {np.power(2, 8)} - Resultado obtenido {potencia_de_dos(8)}')
        return
    
    if potencia_de_dos(16) != np.power(2, 16):
        print(f'Error!')
        print(f'Computando 2^16 ... Resultado esperado: {np.power(2, 16)} - Resultado obtenido {potencia_de_dos(16)}')
        return
    
    if potencia_de_dos(56) != np.power(2, 56):
        print(f'Error!')
        print(f'Computando 2^256 ... Resultado esperado: {np.power(2, 256)} - Resultado obtenido {potencia_de_dos(256)}')
        return
        
    print(f'La funcion es correcta!')