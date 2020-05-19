
def revisar_indexaciones(gastos_serie, gastos_D_G, gastos_A_E, gastos_B_F_H,
                         gastos_principio_a_E, gastos_D_a_G, gastos_C_a_final):
    
    print(f'== Revisión de Indexaciones ==\n')
    revisar_indexacion(gastos_serie.loc[['D', 'G']], gastos_D_G, 'División D y G')
    revisar_indexacion(gastos_serie.loc[['A', 'E']], gastos_A_E, 'División A y E')
    revisar_indexacion(gastos_serie.loc[['B', 'F', 'H']], gastos_B_F_H, 'División B, F y H')
    revisar_indexacion(gastos_serie.loc[:'E'], gastos_principio_a_E, 'desde primera División a E')
    revisar_indexacion(gastos_serie.loc['D':'G'], gastos_D_a_G, 'División D y G')
    revisar_indexacion(gastos_serie.loc['C':], gastos_C_a_final, 'División C a última División')
    
def revisar_indexacion(esperada, recibida, nombre):
    es_correcta = 'Correcta' if esperada.equals(recibida) else 'Incorrecta'
    print(f'{(f"- Indexación {nombre}: {es_correcta}"):55} | Cantidad esperada: ${sum(esperada)} MXN - Cantidad recibida: ${sum(recibida)} MXN')