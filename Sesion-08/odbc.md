# Conexión a una BDD con `odbc`


#### Objetivos
- Conectarse a una BDD utilizando `odbc`
- Lectura de  una BDD en `odbc`

#### Desarrollo

Para comenzar instalaremos el paquete correspondiente:

```python
!pip install pyodbc
```

Posteriormente agregaremos al inicio de nuestro Notebook la importanción a `pyodbc`.

```python
import pyodbc
```

Para conectarnos con Pandas basta con ingresar las credenciales correspondientes:

```python
# parameters
DB = {'servername': 'host',
      'database': 'database'}

# create the connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + DB['servername'] + ';DATABASE=' + DB['database'] + ';Trusted_Connection=yes')

# query db
sql = """

SELECT top 5 *
FROM data

"""
df = pandas.read_sql(sql, conn)
df.head()
```

En el código anterior usamos **SQL Server** sin embargo, en la [documentación](https://github.com/mkleehammer/pyodbc/wiki) podrás encontrar información para conectarte a cualquier gestor.