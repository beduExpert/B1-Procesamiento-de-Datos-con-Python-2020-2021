
def comparar_std(edades, std):
    print(f'== Comparación Desviaciones Estándares ==\n')
    print(f'Esperada: {edades.std()} - Recibida: {std}')
    print(f'Cálculo {"Correcto... Felicidades!" if edades.std() == std else "Incorrecto... Intenta de nuevo"}')