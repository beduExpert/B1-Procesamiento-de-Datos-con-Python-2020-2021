
def imprimir_proporciones_en_equivalencia_a_porcentajes(proporciones, porcentajes):
    
    print(f'==Proporciones y su equivalencia en porcentajes de 1==\n')
    
    for i in range(len(proporciones)):
        print(f'- {proporciones[i]} es el {int(porcentajes[i])}% de 1.')
        

def imprimir_analisis_estadistico(datos):
    
    def mediana(datos):
        datos_sorted = sorted(datos)
        len_datos = len(datos)
        
        if len_datos % 2 == 0:
            mediana = (datos_sorted[int(len_datos / 2) - 1] + datos_sorted[int(len_datos / 2)]) / 2
        else:
            import math
            mediana = datos_sorted[int(math.floor(len_datos / 2))]
            
        return mediana
    
    print(f'==Análisis estadístico de los datos recibidos==\n')
    print(f'Valor mínimo: {min(datos)}')
    print(f'Valor máximo: {max(datos)}')
    print(f'Rango de valores: {max(datos) - min(datos)}')
    print(f'Promedio: {sum(datos) / len(datos)}')
    print(f'Mediana: {mediana(datos)}')