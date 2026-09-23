# Prueba Ingeniero de Datos Junior
 
## SEPTIEMBRE-2026
## KEVIN CASTIBLANCO
## "SUNSHINE BOUQUET" 

# Utilidades implementadas

- Git - GitHub control de versiones y commits
- SQL Postgrest
- Python 

# Librerias

- Pandas
- Python 3.14.7
- requests
- psycopg2
- Font
- openpyxl

## Descripción
  
Se realiza desarrollo en python para implementar los siguientes puntos:
 
- Consumo de Api e importación de CSV 
- Guardar datos en PostgresSQL
- Normalizar datos y limpiarlos
- Generar tabla a partir de un Join
- Supuestos
- Implementar operaciones escritas directamente en SQL

## API.py

En este entorno se ejecuta el script que consumira una Api en la que indicando el numero de usuario me indicara su ID, Titulo y Contenido de la siguiente dirección https://jsonplaceholder.typicode.com/users/1/posts

# API_2

En este entorno se ejecuta el script que consumira los datos de un CSV, en la que cree una tabla en excel con datos como lo son id, nombre, correo y telefono, ya al consultar los datos en python procedi a realizar el guardado de datos por medio de una conexión a postgresSQL.

##  Normalización de llaves de la prueba con mi cedula 1001050021 generada en "Prueba.by"

- Se tiene los siguientes datos extraidos de las tablas con datos transaccionales (machines.csv y production_orders.csv) ya que presentan datos que pueden ir aumentando su consumo al pasar el tiempo y datos de (downtime.csv y shifts.csv)

DOWNTIME

event_id,
machine_id,
start_time,end_
time,type,reason_
code,order_id

MACHINE

machine_id,
line_id,
machine_type,
install_date

PRODUCTION_ORDERS

order_id,
line_id,
machine_id,
product_id,
start_time,
end_time,
units_produced,
units_defective,
shift_id

SHIFT

shift_id,
start_time
end_time,
supervisor

Para estas colunmas se puede notar que varias tablas tienen relacion (FK) e identificadores unico (PK), se realizara la normalización de la siguiente manera:

DOWNTIME

event_id, (PK)
machine_id,(FK)
start_time,end_
time,type,reason_
code,order_id

MACHINE

machine_id,(PK)
line_id,(FK)
machine_type,
install_date

PRODUCTION_ORDERS

order_id,(PK)
line_id,(FK)
machine_id,(FK)
product_id,
start_time,
end_time,
units_produced,
units_defective,
shift_id(FK)

SHIFT

shift_id,(PK)
start_time
end_time,
supervisor

# Normalizaión en las tablas

Se realiza la normalización de la siguiente manera, emtendiendo que mejora la redundancia y permite la organización de datos en criterios.

Se realiza la creación de una nueva tabla (LINE) ya que tiene relacion con otras tablas y no esta independiente

LINE 
line_id (PK)
machine_id (FK)
Order (FK)

Supuestos:

- Se infieren las llaves de identificador unico (PK) Y foraneas (FK)
- Se realiza la limpieza de en ciertas tablas con la creacion de nueva tabla LINE que lleva relacion con las tablas transaccionales MACHINES Y PRODUCTION.

# JOIN entre tablas

En el "Join.py" se ejecuta el script en donde se visualizara el resultado, en la que se identifica lo siguiente:

- Union de production_orders.csv y shifts.csv
- Columna derivada de units_produced y units_defective(production_orders.csv) 
- Se agrega supervisor

Supuestos:

Se identificara al supervisor que en su turno manifesto mas perdidas de unidades y de hay indigar directamente con el supervisor el por que tantas perdidas.

# Operaciones directamente escritas en SQL 

Estas operaciones seran realizadas en Postgres para inserción, actualización y busquedas con el CSV que cree en "data.svc":

Inserción:
Se gregara un nuevo registro en la tabla users creada en postgresSQL


INSERT INTO users (
	id,
	nombre,
	correo,
	telefono
)
VALUES (
	16,
	'lopez',
	'lopez@gmail.com',
	'31223'
);

Antes de realizar la inserción:

 ![Image Alt](https://github.com/kevin12220/Prueba-Ingeniero-De-Datos/blob/master/Proyect/images/Inicial.png?raw=true)

resultado:






Actualización:

Se actualizará de la tabla "users" el telefono al "id=3", que afectaria a  juan.

UPDATE users
SET telefono = '888888'
WHERE id = 3;



Busquedas:

Se realiza el filtro en la misma tabla users donde muestra los id mayores a 10.





EXTRA:

se convierte a excel la ejecución del script en "Join.py", esto facilita el uso de la información en la que se podra filtrar los supervisores y realizar la suma correspondiente e identificar que supervisor en su turno tuvo mas perdidas de unidades. estro genera unidades_optimas.xlsx

