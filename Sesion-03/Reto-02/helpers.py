
def crear_histograma_con(datos):
    import seaborn as sns
    import numpy as np
    
    sns.histplot(datos, kde=False, bins=len(np.unique(datos)))
