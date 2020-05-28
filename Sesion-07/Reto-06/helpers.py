
def corroborar_hallazgos(velocidad_en_kilometros_por_segundo_de_objeto_mas_lento, medida_de_diametro_mas_grande):
    
    assert velocidad_en_kilometros_por_segundo_de_objeto_mas_lento == 0.681436673, 'Ésa no es la velocidad en kilómetros por segundo del objeto más lento'
    assert medida_de_diametro_mas_grande == 6516.883821679, 'Ése no es el diámetro más grande medido en nuestro dataset'
    
    print('Tus hallazgos son correctos! Bien hecho!')