def visualizar_diametros(objetos):
    
    import seaborn as sns
    
    sizes = objetos[['name', 'estimated_diameter.kilometers.estimated_diameter_max']].copy()
    sizes.sort_values('estimated_diameter.kilometers.estimated_diameter_max', ascending=True, inplace=True)
    sns.barplot(sizes['name'], sizes['estimated_diameter.kilometers.estimated_diameter_max'])