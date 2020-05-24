
def test_lista_de_strings_a_lista_de_floats(lista_de_strings_a_lista_de_floats):
    
    import numpy as np
    
    errores = 0
    
    lista_1_original = ['1', '2', '3', '4', '5']
    lista_1_esperada = [1.0, 2.0, 3.0, 4.0, 5.0]
    lista_1_obtenida = lista_de_strings_a_lista_de_floats(lista_1_original)
    if lista_1_obtenida != lista_1_esperada:
        print(f'Error!\n')
        print(f'- Lista original: {lista_1_original}')
        print(f'- Lista esperada: {lista_1_esperada}')
        print(f'- Lista recibida: {lista_1_obtenida}')
        print('\n')
        errores += 1
        
    lista_2_original = []
    lista_2_esperada = []
    lista_2_obtenida = lista_de_strings_a_lista_de_floats(lista_2_original)
    if lista_2_obtenida != lista_2_esperada:
        print(f'Error!\n')
        print(f'- Lista original: {lista_2_original}')
        print(f'- Lista esperada: {lista_2_esperada}')
        print(f'- Lista recibida: {lista_2_obtenida}')
        print('\n')
        errores += 1
        
    lista_3_original = ['1.2', '33', '55.5', 'f', '78']
    lista_3_esperada = [1.2, 33.0, 55.5, np.nan, 78.0]
    lista_3_obtenida = lista_de_strings_a_lista_de_floats(lista_3_original)
    if lista_3_obtenida != lista_3_esperada:
        print(f'Error!\n')
        print(f'- Lista original: {lista_3_original}')
        print(f'- Lista esperada: {lista_3_esperada}')
        print(f'- Lista recibida: {lista_3_obtenida}')
        print('\n')
        errores += 1
        
    lista_4_original = ['f', 'g', 't', 'e', 'r']
    lista_4_esperada = [np.nan, np.nan, np.nan, np.nan, np.nan]
    lista_4_obtenida = lista_de_strings_a_lista_de_floats(lista_4_original)
    if lista_4_obtenida != lista_4_esperada:
        print(f'Error!\n')
        print(f'- Lista original: {lista_4_original}')
        print(f'- Lista esperada: {lista_4_esperada}')
        print(f'- Lista recibida: {lista_4_obtenida}')
        print('\n')
        errores += 1
        
    lista_5_original = ['f', '4.4', 't', '6.6', 'r', '9.9']
    lista_5_esperada = [np.nan, 4.4, np.nan, 6.6, np.nan, 9.9]
    lista_5_obtenida = lista_de_strings_a_lista_de_floats(lista_5_original)
    if lista_5_obtenida != lista_5_esperada:
        print(f'Error!\n')
        print(f'- Lista original: {lista_5_original}')
        print(f'- Lista esperada: {lista_5_esperada}')
        print(f'- Lista recibida: {lista_5_obtenida}')
        print('\n')
        errores += 1
        
    if errores > 0:
        return
    
    print(f'Todo funciona correctamente!')