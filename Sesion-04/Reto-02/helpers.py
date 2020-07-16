
def revisar_indexaciones(gastos_serie, gastos_D_G, gastos_A_E, gastos_B_F_H,
                         gastos_principio_a_E, gastos_D_a_G, gastos_C_a_final):
    
    print(f'== Revisión de Indexaciones ==\n')
    print(f"{'Indexación':30} | {'Resultado':15} | {'Suma esperada ':15} | {'Suma recibida ':15}")
    print("-"*85)
    revisar_indexacion(gastos_serie.loc[['D', 'G']], gastos_D_G, 'División D y G')
    revisar_indexacion(gastos_serie.loc[['A', 'E']], gastos_A_E, 'División A y E')
    revisar_indexacion(gastos_serie.loc[['B', 'F', 'H']], gastos_B_F_H, 'División B, F y H')
    revisar_indexacion(gastos_serie.loc[:'E'], gastos_principio_a_E, 'Desde primera División a E')
    revisar_indexacion(gastos_serie.loc['D':'G'], gastos_D_a_G, 'División D y G')
    revisar_indexacion(gastos_serie.loc['C':], gastos_C_a_final, 'División C a última División')

def formatear_precio(precio):
    return f"${precio} MXN"
    
def revisar_indexacion(esperada, recibida, nombre):
    es_correcta = 'Correcta' if esperada.equals(recibida) else 'Incorrecta'
    suma_esperada = formatear_precio(sum(esperada))
    suma_recibida = formatear_precio(sum(recibida))
    print(f"{nombre:30} | {es_correcta:15} | {suma_esperada:15} | {suma_recibida:15}")