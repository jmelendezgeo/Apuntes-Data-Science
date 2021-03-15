
<div align="center">
    <h1>SQL y MySQL</h1>
    <img src="https://imgur.com/0r5s3Rl.png" width="">
</div>

## Introducción al documento

Este documento corresponde a un fork a los apuntes originales escritos por [Franco Manca](https://github.com/francomanca93) del curso de platzi SQL y mySQL.

El contenido de este documento es **teorico - practico** del [Curso de SQL y MySQL](https://platzi.com/cursos/sql-mysql/) y busca ser una guía para futuros trabajos. El mismo está dictado por [Alberto Alcocer](https://twitter.com/beco), Desarrollador Independiente. El curso es de [Platzi](https://platzi.com).

Con el curso de SQL se conocerá el lenguaje de consulta estructurada que te permité consultar de manera estructurada la información insertada en la base de datos. Elabora tablas, cruza, elimina, modifica y consulta información. Se aprenderá las funciones de MySQL como gestor de base de datos con el que podrás crear aplicaciones para ejecutar dichas funciones.

## Objetivos del documento

- Crear bases de datos
- Cruzar información para la obtención de resultados
- Consulta información en la bases de datos

## Tabla de contenido
- [Curso de SQL y MySQL](#curso-de-sql-y-mysql)
  - [Introducción al Curso de SQL y MySQL](#introducción-al-curso-de-sql-y-mysql)
    - [Introduccioón al curso](#introduccioón-al-curso)
    - [Instalación local de un RDBMS (Ubuntu)](#instalación-local-de-un-rdbms-ubuntu)
    - [La consola de MySQL](#la-consola-de-mysql)
    - [¿Qué es una base de datos?](#qué-es-una-base-de-datos)
  - [CREATE](#create)
    - [Motores de bases de datos](#motores-de-bases-de-datos)
    - [Comando CREATE](#comando-create)
    - [Tipos de columnas / Creación de la tabla books](#tipos-de-columnas--creación-de-la-tabla-books)
      - [Tipos de datos para columnas mas comunes](#tipos-de-datos-para-columnas-mas-comunes)
      - [Creación de la tabla books](#creación-de-la-tabla-books)
    - [Tipos de columnas / Creación de la tabla authors](#tipos-de-columnas--creación-de-la-tabla-authors)
      - [Tips/Recomendaciones](#tipsrecomendaciones)
      - [Comandos sql](#comandos-sql)
      - [Creación de la tabla authors](#creación-de-la-tabla-authors)
    - [Tipos de columnas usados | Creación de la tabla clientes](#tipos-de-columnas-usados--creación-de-la-tabla-clientes)
      - [Tipos de datos usados | columnas de buena práctica](#tipos-de-datos-usados--columnas-de-buena-práctica)
      - [Creación de la tabla clientes](#creación-de-la-tabla-clientes)
    - [DESAFIO | Creación de tabla operations](#desafio--creación-de-tabla-operations)
  - [INSERT](#insert)
    - [Comando INSERT](#comando-insert)
    - [Comando on duplicate key](#comando-on-duplicate-key)
    - [Inserción de datos usando queries anidados](#inserción-de-datos-usando-queries-anidados)
  - [Bash y archivos SQL](#bash-y-archivos-sql)
  - [SELECT](#select)
    - [Su majestad el SELECT | Comandos básicos](#su-majestad-el-select--comandos-básicos)
    - [Comando JOIN](#comando-join)
    - [Left JOIN](#left-join)
    - [Tipos de JOIN | Resumen](#tipos-de-join--resumen)
      - [1. Inner Join](#1-inner-join)
      - [2. Left Join](#2-left-join)
      - [3. Right Join](#3-right-join)
      - [4. Outer Join](#4-outer-join)
      - [5. Left excluding join](#5-left-excluding-join)
      - [6. Right Excluding join](#6-right-excluding-join)
      - [7. Outer excluding join](#7-outer-excluding-join)
      - [Resumen](#resumen)
    - [Casos de Negocios](#casos-de-negocios)
      - [DICTINCT](#dictinct)
      - [COUNT | GROUP BY | ORDER BY | NOT IN | IN](#count--group-by--order-by--not-in--in)
      - [AVG() AS promedio | STDDEV() AS desviacion_estandar](#avg-as-promedio--stddev-as-desviacion_estandar)
      - [MAX() y MIN()](#max-y-min)
      - [CONCAT() | TO_DAY() | NOW() | Realizando un reporte](#concat--to_day--now--realizando-un-reporte)
    - [Comandos UPDATE, DELETE y TRUNCATE](#comandos-update-delete-y-truncate)
  - [Consultas en MySQL](#consultas-en-mysql)
    - [Super QUERIES](#super-queries)
    - [Comando mysqldump](#comando-mysqldump)

# Curso de SQL y MySQL

## Introducción al Curso de SQL y MySQL

### Introduccioón al curso

La diferencia entre SQL y MySQL:

- [SQL](https://es.wikipedia.org/wiki/SQL) (Structured Query Language; lenguaje de consulta estructurada) es un lenguaje de dominio específico utilizado en programación, diseñado para administrar, y recuperar información de sistemas de gestión de bases de datos relacionales. Una de sus principales características es el manejo del álgebra y el cálculo relacional para efectuar consultas con el fin de recuperar, de forma sencilla, información de bases de datos, así como realizar cambios en ellas.

- [MySQL](https://www.mysql.com/) es un sistema de administración de bases de datos (Database Management System, DBMS) o también llamado motor de bases de datos.

Existen muchos tipos de bases de datos, desde un simple archivo hasta sistemas relacionales orientados a objetos. MySQL, como base de datos relacional, utiliza múltiples tablas para almacenar y organizar la información.

Fue escrito en C y C++ y se integra perfectamente con los lenguajes de programación más usados en todo el mundo.

![que_es_mysql](https://imgur.com/JgDLdW2.png)

> NOTA: En el curso sólo se utilizará la consola para hacer consultas.

### Instalación local de un RDBMS (Ubuntu)

[Instalacción de MySQL 5.7 en Ubuntu 20.04](https://computingforgeeks.com/how-to-install-mysql-on-ubuntu-focal/)

### La consola de MySQL

La forma de conectarnos a nuestro servidor MySQL a través de nuestra terminal es:

```shell
$ mysql -h <dirección_de_nuestro_servidor> -u <usuario> -p -P <puerto>
Enter password: <aquí introducirías tu password>?
```

En un principio, luego de instalar mysql, no podrás conectarte con algun usuario. La manera de entrar por defecto a mysql sin que te pida usuario o contraseña es a través de: 

```shell
sudo mysql
```
Dentro del entorno de mysql, debes hacer un cambio de la password nativa de mysql por una password que elijas. Debe cumplir con unas especificaciones según el nivel de validación de seguridad (Low, Medium o Hard). 


Comandos usados en esta sección:

- `show databases;` -> lista las bases de datos que tiene el servidor

- `use [name_database];`-> selecciona o se conecta a la base de datos a trabajar

- `show tables;` -> muestra las tablas que contiene la base de datos

- `select database();` -> muestra cual es la base de datos que tenemos seleccionada o en la que se esta trabajando.

> Todos los comandos deben de terminar con “;”.

### ¿Qué es una base de datos?

Se llama **base de datos**, o también banco de datos, a un conjunto de información perteneciente a un mismo contexto, ordenada de modo sistemático para su posterior recuperación, análisis y/o transformación.

Es un lugar donde podemos ir almacenando datos puntuales de cualquier cantidad de cosas para después operar sobre esos datos y convertirlos en información. Esa información convertirla en operaciones de negocio y las operaciones de negocio convertirlas en dinero, crecimiento sabiduría lo que sea. **TODO RESIDE EN LOS DATOS Y CÓMO OPERAMOS SOBRE LOS DATOS**.

> “Una base de datos es una conglomeración genérica de datos”.

## CREATE

### Motores de bases de datos

> Los **Motores de Bases de Datos**, son programas específicos, dedicados a servir de intermediarios entre las **bases de datos** y las **aplicaciones** que las utilizan como función principal, cada uno de estos cumple una tarea especifica, que van desde **crear** la Base de Datos hasta administrar el **uso y acceso** a esta.

> Un **motor SQL** es un tipo de software que recopila e interpreta comandos SQL para que se puedan realizar las operaciones apropiadas en la base de datos relacional.

Dos tipos de tablas por defecto en MySQL:

- **MyISAM**: directa, sencilla, más rápida y las transacciones son completamente uno a uno. Sus caracteristicas son:

  - Bloqueo de tabla
  - Aumento del rendimiento si nuestra aplicación realiza un elevado número de consultas “Select”.
  - Las tablas pueden llegar a dar problemas en la recuperación de datos.
  - Permite hacer búsquedas full-text
  - Menor consumo memoria RAM
  - Mayor velocidad en general a la hora de recuperar datos.
  - Ausencia de características de atomicidad ya que no tiene que hacer comprobaciones de la integridad referencial, ni bloquear las tablas para realizar las operaciones, esto nos lleva como los anteriores puntos a una mayor velocidad.

- **InnoDB**: nueva, recuperable en caso de falla de disco duro pero es un poco más lenta.

  - Bloqueo de registros
  - Soporte de transacciones
  - Rendimiento
  - Concurrencia
  - Confiabilidad
  - Permite hacer búsquedas full-text (mysql >= 5.6)

> En la vida real usamos las tablas con dos propósitos:
>La estrategia aqui es que hablaremos de dos propositos para nuestra base de datos: Catalogo y Operacion. Donde, por ejemplo, las de catalogo creceran en un orden lento (puede ser listado de usuario) que no es comparable con el crecimiento de una base de datos de prestamos de libros de una biblioteca. Se esperaria que diariamente se realizaran muchos prestamos de libros, a mayor velocidad, que el crecimiento de nuevos usuarios
> - **Catalogo**: crecerá en un orden lento, según las necesidades de la propia BD. (Listado de Usuarios, InnoDB)
> - **Operación**: se enfocan a lectura, mayor acceso a disco duro. (Prestamos de libros, MyISAM).

**InnoDB y MyISAM**

Supongamos que vamos a construir un blog sobre autos deportivos. Vamos a tener **usuarios** que publican posts, cada uno perteneciente a una **categoría** y con una o muchas **etiquetas**. Además, pueden escribir **comentarios** en cada artículo. Cada cosa remarcada es lo que llamamos _entidad_, la cual posee _atributos_ que la caracterizan y _relaciones_ con algunas otras. En MySQL nosotros llamamos a las entidades **tablas** y a las bases de datos que alojan estas entidades **esquemas**. Donde nos centraremos es que en las tablas a veces se reciben muchos registros en un tiempo corto pero tambien muchas consultas en segundos. Por ejemplo, todas las semanas se registran nuevos usuarios per cada dia se leen más de 10000 veces los posts del sitio.

* ¿Vamos a escribir datos muy seguido?
* ¿Necesitamos hacer consultas constantemente?
* ¿Es importante cumplir con ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad)?

Todo esto debe ser respondido antes de crear la estructura de cada entidad. Una vez que lo hayamos hecho es hora de escoger el engine correcto para construir nuestras tablas 

* InnoDB es el rey de la escritura. Es un motor diseñado para fortalecer la Atomicidad, Consistencia, Aislamiento y Durabilidad en una base de datos. ¿Vamos a hacer uso de las sentencias _INSERT_ y _UPDATE_? InnoDB.
* MyISAM es el rey de la lectura. Si estamos hablando de velocidad para hacer consultas, el claro ganador es MyISAM. Nuestro blog recibira miles y miles de vistas todos los dias, seria un desastre que nuestro esquema tardara mas de lo esperado en responder a nuestro backend. Por ende, como vamos a reproducir multiples sentencias _SELECT_, MyISAM deberia formar parte del core de nuesta tabla 



### Comando CREATE

Primero debemos crear una base de datos. 
Podemos usar 

```sql
CREATE DATABASE nombre_database;
);
```
Esto nos creara la database. Sin embargo, podriamos blindar la sentencia al decirle "Crea la base de datos si no existe". Esto se hace porque, de existir la base de datos, nos dice _Query OK_ y nos muestra un warning indicando que la base de datos ya existe. Si intentamos crear una base de datos sin esto, nos devolverá un error porque la base de datos ya existe.

```sql
CREATE DATABASE IF NOT EXISTS nombre_database;
```



```sql
CREATE TABLE IF NOT EXISTS nombre_tabla_en_plural (
    ...nombre_de_columnas...
);
```




### Tipos de columnas / Creación de la tabla books

**Tips**

* Es recomendable que al momento de nombrar tablas lo hagamos en plural: book:books por convención
* Por convención (Buena práctica importante que ahorra muchos dolores de cabeza) toda tabla necesita un id. Una forma única de relacionarse. Es una manera Universal de referirnos a una unica tupla (porque p.e hay libros que se llaman igual pero tienen diferentes autores). Idealmente que tenga un autoincrement si son enteros.



#### Tipos de datos para columnas mas comunes

- `NOT NULL` permite que un campo no pueda estar sin completar, es distinto `NULO` a `EMPTY`.
- `INTEGER UNSIGNED` permite que no existan signos, de forma que los numeros siempre seran positivos.

>DATO IMPORTANTE: mysql no detecta cuando los datos de `AUTO_INCREMENT` han sido borrados, por tanto seguira con el ultimo dato que guardo.

- `DEFAULT [valor por defecto]`: Si no introducimos ningun dato, mySQl automaticamente le dara al campo el valor de `DEFAULT`.
- La diferencia entre `CHAR` y `VARCHAR` es que en el primer tipo de dato se asigna un valor en memoria por defecto dependiendo el tamaño de espacios que sean asignados, en cambio, `VARCHAR` va llenando esos campos en memoria conforme se tengan los datos en el campo.
- `COMMENT`: Comentario a la columna que solo es visible para quien este manejando la base de datos
- Para imagenes asignamos `VARCHAR`.

> NOTA: no se guarda la imagen como tal, guardamos el url del origen de la imagen. No se guardan archivos binarios en la base de datos relacional, nunca guardar una imagen, pero si una referencia.

- `FLOAT` es utilizado para calculos precisos, `DOUBLE` puede ser aplicado de forma simple a los precios de una libreria (en este caso). FLOAT maneja 6 decimales de precision.
- `DOUBLE` (espacios que podremos llenar, espacios asignados para numeros decimales). Por ejemplo DOUBLE (6,2) es 4 numeros antes de la coma y dos decimales.
- `TEXT` permite agregar texto, grandes cantidades de caracteres.
- `TINYINT` Es un número entero con o sin signo. Con signo el rango de valores válidos va desde -128 a 127. Sin signo, el rango de valores es de 0 a 255. `TINYINT(1)` = BOOL (0 o 1), también llamado bandera.
- `TINYTEXT`, `TEXT`, `BIGTEXT`: Textos de diferente cantidad de espacios soportados, de menor a mayor respectivamente.

#### Creación de la tabla books

```sql
CREATE TABLE IF NOT EXISTS books (
    `book_id` INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `author_id` INTEGER UNSIGNED,
    `title` VARCHAR(100) NOT NULL,
    `year` INTEGER UNSIGNED NOT NULL DEFAULT 1900,
    language VARCHAR(2) NOT NULL DEFAULT 'es' COMMENT 'ISO 639-1 Language',
    `cover_url` VARCHAR(500),
    `price` DOUBLE(6,2) NOT NULL DEFAULT 10.0,
    `sellable` TINYINT(1) DEFAULT 1,
    `copies` INTEGER NOT NULL DEFAULT 1,
    `description` TEXT
);
```


### Tipos de columnas / Creación de la tabla authors

#### Tips/Recomendaciones

- La tablas de bases datos necesitan una `PRIMARY KEY` osea un “id” para **identificar los registros**.

> **Es buena práctica**: MySQL permite minúsculas y mayúsculas en el nombre de tablas y sentencias sql, pero es recomendable colocar en mayúsculas las sentencias(palabras reservadas) sql y todo lo relaciona con lo propio de MySQL y en minúscula el nombre de tablas y columnas (lo relacionado a nosotros).

- Como la relación entre tablas es lógica y se realiza mediante los id, en la tabla en donde se referencia la columna debe ser del mismo tipo de datos.

- **El error vs Warnings**: la diferencia entre estos dos es que el error rompe cualquier flujo de trabajo que tengamos en nuestra aplicación mientras que el warnnigs nos muestra una advertencia que no rompe el flujo de trabajo workflow.

- Cuando queremos usar una palabra reservada del lenguaje como nombre de alguna columna lo colocamos encerrado entre comillas de acento ejemplo: year (que es una palabra reservada). Ojo en la diferencia: No son comillas dobles "", comillas simples '' y comillas de acento ``

#### Comandos sql

> TENER **MUCHO CUIDADO** CON EL SIGUIENTE COMANDO **`DROP`**, **PODEMOS PERDER MUCHO TIEMPO/DINERO** SI LO HACEMOS POR ERROR. **VERIFICAR SIEMPRE**.

- `DROP TABLE name_table;` borra la estructura de la tabla de bases de datos y su contenido.

```sql
/*Eliminar una tabla*/
DROP TABLE `authors`;
```

- `DESCRIBE name_table;` muestra la estructura de nuestra tabla. Nos muestra las columnas: field, type, Null, Key, Default, Extra.

```sql
/*describe el contenido (columnas) de la tabla books*/
DESCRIBE `books`;
```

- `DESC name_table;` es un acrónimo de `DESCRIBE` que realiza la misma función de describir la estructura de la tabla.

- `SHOW FULL COLUMNS FROM name_table;` Esta función describe la estructura de la bases de datos incluyendo más información cómo: field, Type, Collation, Null, Key, Default, Extra, Privileges, comment.

```sql
SHOW FULL COLUMNS FROM `books`;
```

#### Creación de la tabla authors

```sql
CREATE TABLE IF NOT EXISTS authors(
    `author_id` INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL, 
    `nationality` VARCHAR(3)
);
```

### Tipos de columnas usados | Creación de la tabla clientes

#### Tipos de datos usados | columnas de buena práctica

- El no colocar `AUTO_INCREMENT` a la columna que es PRIMARY KEY simplemente vuelve el proceso de asignar id a una forma manual o se puede asignar desde otra capa de negocios. Depende mucho de los gustos. Sin embargo, que esto parta desde la base de datos puede ahorrar problemas y mejora compatibilidades.

- `UNIQUE`, la columna que tenga el constraint **unique** garantiza que el valor que se guarda en esa columna sea único. Esto podria funcionar por ejemplo si solamente aceptamos 1 cliente por correo.

- `TIMESTAMP` Está basado en el número **epoch** que es el **1 enero de 1970** hasta la fecha y es donde se determina el inicio de las computadoras. Es un número entero que se guarda en segundos y permite hacer operaciones sobre él. Es muy eficiente a la hora de hacer calculos y cualquier lenguaje puede luego transformarlo en un formato deseado como, por ejemplo 'yyyy-mm-dd hh:mm:ss'

- `DATETIME` Este tipo de dato puede guardar cualquier valor de tipo fecha sin restricción. Incluso anterior a nuestra era. Por eso las fechas de nacimiento de usuarios debe utilizar este valor para garantizar que podemos registrarlos con la fecha adecuada (por si nacieron antes de 1970).

> TIMESTAMP vs DATETIME: hay que resaltar que:
> 1. `TIMESTAMP` “NO PUEDE HACER TODO LO DE `DATETIME` pero `DATETIME` SÍ PUEDE HACERLO DE UN `TIMESTAMP`”.
> 2. `DATETIME` no está guardado en segundos y no es tan eficiente para hacer cálculos.

- `active`

Es buena práctica no eliminar registros de una bases de datos es por ello que se crea una columna como active que es un valor booleano. Dicho valor sirve para para decir si el registro está activo o no.

- `created_at` y `updated_at`

Es buena práctica tener una columna que permite saber el momento exacto en el que se crea un registro o se actualiza. Este tipo de dato se comporta más como una meta-información y nos puede ayudar, por ejemplo, a cuántos usuarios fueron creados en una fecha en específico, saber cuando una tupla se actualizó, etc.

- `created_at`

Es una columna de buena práctica que permite saber cuando se creó un registro. Está utilizará un conjunto de propiedades llamada entre ella se colocará `DEFAULT CURRENT_TIMESTAMP` . Cuando se realiza un insert sí el valor de esta columna viene vacío colocará en la tupla el valor de la fecha en que se creó de manera automática. Tambien vamos a querer que se actualice un `update_at` con la hora en el que hacemos una actualizacion al registro.

#### Creación de la tabla clientes

```sql
CREATE TABLE clients(
    `client_id` INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `email` VARCHAR(100) NOT NULL UNIQUE,
    `birthdate` DATETIME,
    `gender` ENUM('M', 'F', 'ND') NOT NULL,
    `active` TINYINT(1) NOT NULL DEFAULT 1,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;
```

### DESAFIO | Creación de tabla operations

```sql
CREATE TABLE IF NOT EXISTS operations(
    `operation_id` INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `book_id` INTEGER UNSIGNED NOT NULL,
    `client_id` INTEGER UNSIGNED NOT NULL,
    `operation_type` ENUM('B', 'R', 'S') NOT NULL COMMENT 'B=BORROWED, R=RETURNED, S=SOLD',
    /*[prestado(operacion no finializada), devuelto(oper finalizada) o vendido(oper finalizada)],*/
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP 
        ON UPDATE CURRENT_TIMESTAMP,
    `finished` TINYINT(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

## INSERT

### Comando INSERT

> Buenas prácticas:
> 1. Tener una buen modelo de bases de datos y un buen modelo de negocio que evite la duplicidad de información ya que esto nos ahorra el tiempo de procesamiento, ahorra en espacio. Por ejemplo, creamos una tabla de autores porque puede darse el caso que varios libros tengan el mismo autor y , de esta forma, no escribimos el nombre del mismo autor varias veces.
> 2. Realizar inserciones de 50 registros máximo. Esto no es necesariamente obligatorio pero funciona muy bien y esto se hace porque sí hay algún problema en la inserción sólo se pierde datos de 50 a 50.

Formas de insertar:

1. 
```sql
/*Existe varias formas de hacer insert, según las
versiones de mysql que tengamos instalados estas son
algunas de ellas*/
INSERT INTO  authors (author_id,name,nationality) VALUES (NULL,'Juan Rulfo','MEX');
INSERT INTO  authors (name,nationality) VALUES (NULL,'Gabriel García Máquez','COL');
INSERT INTO  authors VALUES (NULL,'Juan Gabriel Vasquez','COL');
```
2. 
```sql
/*otra forma, que sí funciona*/
INSERT INTO  `authors` (name,nationality)
    VALUES  ('Juan Rulfo','MEX'),
            ('Gabriel García Máquez','COL'),
            ('Juan Gabriel Vasquez','COL'),
            ('Julio Cortázar','COL'),
            ('Isabelle Allende','CHI'),
            ('Octavio Paz','MEX'),
            ('Juan Carlos Onetti','URU');
```
3.
```sql
/*o si sabemos que hay un id que no existe podemos insertarlos juntos con su  id*/
INSERT INTO  `authors` (author_id,name,nationality)
    VALUES ('16','Pablo Neruda','MEX');


```

### Comando on duplicate key

`ON DUPLICATE KEY` sirve para insertar un dato que ya esta creado pero queremos actualizar un atributo de ese dato por uno nuevo.

```sql
INSERT INTO `clients`(name, email, birthdate, gender, active)
VALUES ('Pedro Sanchez','Pedro.78522059J@random.names','1992-01-31','M', 0)
ON DUPLICATE KEY UPDATE active = VALUES(active)
```

Opciones:

1. `ON DUPLICATE KEY IGNORE ALL` esto indica que si hay algun error, lo va a ignorar y va a correr la sentencia.

> **NUNCA UTILIZAR, EVITAR A TODA COSTA.**
> Los errores están ahi para algo, sin embargo la recomendación es NUNCA usar IGNORE ALL en una sentencia SQL de MYSQL.

2. `ON DUPLICATE KEY UPDATE active = VALUES(active)` para cambiarle el valor de activo, de 1 a 0. Esta sentencia con la palabra UPDATE nos permite actualizar la información por alguna otra. Hay hos formas de hacer esto:

  - `ON DUPLICATE KEY UPDATE active = 0;`
  - `ON DUPLICATE KEY UPDATE active = VALUES(active);`

3. `ON DUPLICATE KEY UPDATE SET email=''` Esto nos esta indicando que, en el valor duplicado, hagamos un update. En este caso el valor duplicado seria el email y pedimos que se cambie por vacío

### Inserción de datos usando queries anidados

Tenemos un archivo CVS con la siguiente información

```text
El laberinto de la Soledad | Octavio Paz | 1955
Vuelta al laberinto de la Soledad | Octavio Paz | 1960
```

Vemos que nuestro csv esta en formato Libro, autor, año. Pero si recordamos nuestra base de datos tienen una tabla para libros y otra para autores. Si queremos insertar el libro, ¿Como añadimos el author_id si tenemos es el nombre?

Mediante un script de Python podemos obtener estos datos e ir iterando para las insercciones, pero el problema surge en que nuestra tabla de books tenemos solo el title y el year, el nombre del autor lo tenemos en otra tabla llamada authors.

Supongamos que insertamos un libro, pero como el autor es de tipo integer por referencia lógica a la tabla authors, en un primer momento tenemos que hacer un select a la tabla authors, fijarse que id tiene el autor en cuestión y regresar a insertar el registro

```sql
INSERT INTO books (title, author_id) VALUES ('El laberinto de la Soledad', 6);
```

Sin embargo al usar INSERT con SELECT anidados, podemos saltarnos el paso de hacer el select previo a la tabla de autores y colocarlo internamente en la consulta de insercción. Para el campo author_id, su valor lo obtengo de una subconsulta, de ahí que este entre parentesis, para que se haga primero:

```sql
INSERT INTO books (title, author_id, year)
VALUES ('Vuelta al laberinto de la Soledad',
(SELECT author_id FROM authors WHERE name = 'Octavio Paz'),
1960);
```

Esto hará que, al ingresar el registro del author_id, se haga una subconsulta y se busque en la tabla de authores el id del autor cuyo nombre es 'Octavio Paz'. Esto es potente y funciona. 

> Las consultas anidadas deben tratarse con cudiado porque eleva la complejidad del algoritmo y el timpo de ejecución (Puede elevarlo al cuadrado o duplicarlo). Lo ideal sería hacer ese proceso de limpieza en una capa previa a la base de datos, en algun lenguaje de programacion, y luego insertar la información correctamente según la estructuras de las tablas en la base de datos




## Bash y archivos SQL

Se pueden traer grandes bases de datos sin tener que cargar todo manualmente desde la terminal bash directamente. Lo que hacemos es ir a la carpeta contenedora de los archivos desde la terminal y con el siguiente comando traemos los archivos sql:

1. Crear base de datos desde cero:

```shell
mysql -u root -p < all_schema.sql
```

2. Traer todos los datos a la base de datos creada.

```shell
mysql -u root -p -D proyecto_platzi < all_data.sql
```

Shell lo que hara sera pasar todo el archivo a sql por lo que tiene que estar correctamente estructurado. Por ejemplo, debe incluso contener el comando "Use nombre_database" para que sql sepa sobre cual base de datos ejecutar las sentencias.


## SELECT

### Su majestad el SELECT | Comandos básicos

- Traer toda la informacion de una tabla: 
```sql
SELECT * FROM clients;
```

- Traer solo una columna especifica (en este caso la columna “name”):

```sql
SELECT name FROM clients;
```

- Traer varias columnas especificas (en este caso la columna “name” y “gender”):

```sql
SELECT name, email, gender FROM clients;
```

- Limitar el numero de resultados (en este caso maximo 10 resultados):

```sql
SELECT name, email, gender FROM clients LIMIT 10;
```
> LIMIT siempre va al final de select.

- Condicionar los resultados a una caracteristica (en este caso todos los resultados que tengan gender con el valor “M”):

```sql
SELECT name, email, gender FROM clients WHERE gender='M';
```

- Listar el año de nacimientos de los clientes, con la función YEAR()

```sql
SELECT YEAR(birthdate) FROM clients;
```
> Ya los manejadores de bases de datos tienen integradas un monton de funciones. Por ejemplo, esta es una funcion que recibe informacion en formato date y extrae el año.


- Mostrar el año actual

```sql
SELECT YEAR(NOW());
```

- Listar los 10 primeros resultados de las edades de los clientes (estos resultados no tienen un orden en particular). Vemos que aqui ya estamos haciendo calculos sencillos.

```sql
SELECT YEAR(NOW()) - YEAR(birthdate) FROM clients LIMIT 10;
```

- Listar nombre y edad de los 10 primeros clientes

```sql
SELECT name, YEAR(NOW()) - YEAR(birthdate) FROM clients LIMIT 10;
```

- Listar clientes que coincidan con el nombre de "Saave". En este caso estamos usando funciones que actúan como condiciones. Al añadir el %Saave% decimos que no importa que haya antes o despues, queremos uno que incluya la cadena Saave en su nombre. 

```sql
SELECT * FROM clients WHERE name LIKE '%Saave%';
```
En este caso retorna toda la informacion de 'Pablo Saaveda'

- Utilizar funciones para obtener datos especificos (en este caso todas las Mujeres que en su nombre tengan la cadena “Lop”), usando alias para nombrar la función como 'edad':

```sql
SELECT name, email, YEAR(NOW()) - YEAR(birthdate) AS edad, gender
FROM clients
WHERE gender='F'
    AND name LIKE '%Lop%';
```

### Comando JOIN

Algunos de los JOIN's usados en la clase fueron:

- Listar todos los autores con ID entre 1 y 5 con los filtro mayor y menor igual

```sql
SELECT * FROM authors WHERE author_id > 0 AND author_id <= 5;
```

- Listar todos los autores con ID entre 1 y 5 con el filtro BETWEEN

```sql
SELECT * FROM authors WHERE author_id BETWEEN 1 AND 5;
```

- Listar los libros con filtro de author_id entre 1 y 5

```sql
SELECT book_id, author_id, title FROM books WHERE author_id BETWEEN 1 AND 5;
```

- Listar nombre y titulo de libros mediante el JOIN de las tablas books y authors

```sql
SELECT b.book_id, a.name, a.author_id, b.title
FROM books AS b
JOIN authors AS a
  ON a.author_id = b.author_id
WHERE a.author_id BETWEEN 1 AND 5;
```

- Listar transactions con detalle de nombre, titulo y tipo. Con los filtro genero = F y tipo = Vendido. Haciendo join entre transactions, books y clients.

```sql
SELECT c.name, b.title, t.type
FROM transactions AS t
JOIN books AS b
  ON t.book_id = b.book_id
JOIN clients AS c
  ON t.client_id = c.client_id
WHERE c.gender = 'F'
  AND t.type = 'sell';
```

- Listar transactions con detalle de nombre, titulo, autoor y tipo. Con los filtro genero = M y de tipo = Vendido y Devuelto. Haciendo join entre transactions, books, clients y authors.

```sql
SELECT c.name, b.title, a.name AS 'author of book', t.type
FROM transactions AS t
JOIN books AS b
  ON t.book_id = b.book_id
JOIN clients AS c
  ON t.client_id = c.client_id
JOIN authors AS a
  ON b.author_id = a.author_id
WHERE c.gender = 'M'
  AND t.type IN ('sell', 'lend');
```

- JOIN y order by (por defecto es ASC)

```sql
SELECT a.author_id, a.name AS 'author name', a.nationality, b.title AS 'title of book'
FROM authors AS a
JOIN books AS b
  ON b.author_id = a.author_id
WHERE a.author_id BETWEEN 1 AND 5
ORDER BY a.author_id DESC;
```

### Left JOIN

En la sección se vio el uso de INNER JOIN, en esta sección veremos el uso de LEFT JOIN.

- Uso del JOIN implícito

```sql
SELECT b.title, a.name
FROM authors AS a, books AS b
WHERE a.author_id = b.author_id
LIMIT 10;
```

- Uso del JOIN explícito

```sql
SELECT b.title, a.name
FROM books AS b
INNER JOIN authors AS a
  ON a.author_id = b.author_id
LIMIT 10;
```

Ambos casos son iguales, pero el segundo se puede leer claramente mas rapido.

- LEFT JOIN para traer datos incluso que no existen, como el caso del author_id = 4 que no tene ningún libro registrado. Esto va a traer la tabla pivote (en este caso la de autores) con la informacion de la otra tabla.

```sql
SELECT a.author_id, a.name AS 'author name', a.nationality, b.title AS 'title of book'
FROM authors AS a
LEFT JOIN books AS b
  ON b.author_id = a.author_id
WHERE a.author_id BETWEEN 1 AND 5
ORDER BY a.author_id;
```

Salida:

```txt
+-----------+--------------------+-------------+---------------------------------------+
| author_id | author name        | nationality | title of book                         |
+-----------+--------------------+-------------+---------------------------------------+
|         1 | Sam Altman         | USA         | The Startup Playbook                  |
|         1 | Sam Altman         | USA         | The Startup Playbook                  |
|         2 | Freddy Vega        | COL         | NULL                                  |
|         3 | Arthur Conan Doyle | GBR         | Estudio en escarlata                  |
|         3 | Arthur Conan Doyle | GBR         | The - Vol I Complete Sherlock Holmes  |
|         3 | Arthur Conan Doyle | GBR         | The - Vol II Complete Sherlock Holmes |
|         4 | Chuck Palahniuk    | USA         | NULL                                  |
|         5 | Juan Rulfo         | MEX         | El llano en llamas                    |
+-----------+--------------------+-------------+---------------------------------------+
8 rows in set (0.00 sec)
```

- Contar número de libros que tiene un autor. Con COUNT() usamos una funcion para contar las entradas. Para poder utilizarla correctamente en este caso, es necesario tener un GROUP BY (agrupado por un criterio) sobre algun parametro. En este caso podriamos agrupar por el nombre del autor pero siempre que se pueda utilizar un id (author_id) deberiamos usarlo en lugar a cualquier cadena de caracteres que podria repetirse (tal vez hay autores distintos pero que se llaman igual).

> Siempre que trabajemos con funciones como Sum(), Count(),Avg(),Max(),Min() debemos agregar la funcion GROUP cuando en el SELECT incluyamos otra columna para mostrar aparte de la funcion de agrupamiento de otra columna. Si no, solo mostrara el primer resultado de la funcion

```sql
SELECT a.author_id, a.name AS 'author name', a.nationality, COUNT(b.book_id)
FROM authors AS a
LEFT JOIN books AS b
  ON b.author_id = a.author_id
WHERE a.author_id BETWEEN 1 AND 5
GROUP BY a.author_id
ORDER BY a.author_id;
```

Salida:

```txt
+-----------+--------------------+-------------+------------------+
| author_id | author name        | nationality | COUNT(b.book_id) |
+-----------+--------------------+-------------+------------------+
|         1 | Sam Altman         | USA         |                2 |
|         2 | Freddy Vega        | COL         |                0 |
|         3 | Arthur Conan Doyle | GBR         |                3 |
|         4 | Chuck Palahniuk    | USA         |                0 |
|         5 | Juan Rulfo         | MEX         |                1 |
+-----------+--------------------+-------------+------------------+
5 rows in set (0.00 sec)
```

### Tipos de JOIN | Resumen

En las secciones anterior estuvimos hablando de dos tipos de joins, **inner y left**, que podemos usar cuando estemos trabajando con consultas a nuestras bases de datos.

Existen diferentes formas en las que se pueden unir las tablas en nuestras consultas y de acuerdo con esta unión se va a mostrar información, y es importante siempre tener clara esta relación.

En esta sección verémos gráficamente 7 diferentes tipos de uniones que puedes realizar.

Usar correctamente estas uniones puede reducir el tiempo de ejecución de tus consultas y mejorar el rendimiento de tus aplicaciones.

Cuando hacemos uniones en las consultas para seleccionar información, estamos trabajando con tablas, estas tablas podemos verlas como conjuntos de información, de forma que podemos asimilar los joins entre tablas como uniones e intersecciones entre conjuntos.

Supongamos que contamos con dos conjuntos, el conjunto A y el conjunto B, o, la tabla A y la tabla B. Sobre estos conjuntos veamos cuál es el resultado si aplicamos diferentes tipos de join.

#### 1. Inner Join

Esta es la forma mas fácil de seleccionar información de diferentes tablas, es tal vez la que mas usas a diario en tu trabajo con bases de datos. Esta union retorna todas las filas de la tabla A que coinciden en la tabla B. Es decir aquellas que están en la tabla A Y en la tabla B, si lo vemos en conjuntos la intersección entre la tabla A y la B.

![inner_join](https://imgur.com/0UYpY7R.png)

Esto lo podemos implementar de esta forma cuando estemos escribiendo las consultas:

```sql
SELECT <columna_1> , <columna_2>,  <columna_3> ... <columna_n> 
FROM Tabla_A AS A
INNER JOIN Tabla_B AS B
  ON A.pk = B.pk
```

#### 2. Left Join

Esta consulta retorna todas las filas que están en la tabla A y ademas si hay coincidencias de filas en la tabla B también va a traer esas filas.

![left_join](https://imgur.com/kSClrnI.png)

Esto lo podemos implementar de esta forma cuando estemos escribiendo las consultas:

```SQL
SELECT <columna_1> , <columna_2>,  <columna_3> ... <columna_n>
FROM Tabla_A AS A
LEFT JOIN Tabla_B AS B
  ON A.pk = B.pk
```

#### 3. Right Join

Esta consulta retorna todas las filas de la tabla B y ademas si hay filas en la tabla A que coinciden también va a traer estas filas de la tabla A.

![right_join](https://imgur.com/3NxcbZF.png)

Esto lo podemos implementar de esta forma cuando estemos escribiendo las consultas:

```sql
SELECT <columna_1> , <columna_2>,  <columna_3> ... <columna_n>
FROM Tabla_A AS A
RIGHT JOIN Tabla_B AS B
  ON A.pk = B.pk
```

#### 4. Outer Join

Este join retorna TODAS las filas de las dos tablas. Hace la union entre las filas que coinciden entre la tabla A y la tabla B.

![outer_join](https://imgur.com/YzeWIiR.png)

Esto lo podemos implementar de esta forma cuando estemos escribiendo las consultas:

```sql
SELECT <columna_1> , <columna_2>,  <columna_3> ... <columna_n>
FROM Tabla_A AS A
FULL OUTER JOIN Tabla_B AS B
  ON A.pk = B.pk
```

#### 5. Left excluding join

Esta consulta retorna todas las filas de la tabla de la izquierda, es decir la tabla A que no tienen ninguna coincidencia con la tabla de la derecha, es decir la tabla B.

![left_excluding_join](https://imgur.com/IzBm6Qt.png)

Esto lo podemos implementar de esta forma cuando estemos escribiendo las consultas:

```sql
SELECT <columna_1> , <columna_2>,  <columna_3> ... <columna_n>
FROM Tabla_A AS A
LEFT JOIN Tabla_B AS B
  ON A.pk = B.pk
WHERE B.pk IS NULL
```

#### 6. Right Excluding join

Esta consulta retorna todas las filas de la tabla de la derecha, es decir la tabla B que no tienen coincidencias en la tabla de la izquierda, es decir la tabla A.

![right_Excluding_join](https://imgur.com/BdsPDB2.png)

Esto lo podemos implementar de esta forma cuando estemos escribiendo las consultas:

```sql
SELECT <columna_1> , <columna_2>,  <columna_3> ... <columna_n>
FROM Tabla_A AS A
RIGHT JOIN Tabla_B AS B
  ON A.pk = B.pk
WHERE A.pk IS NULL
```

#### 7. Outer excluding join

Esta consulta retorna todas las filas de la tabla de la izquierda, tabla A, y todas las filas de la tabla de la derecha, tabla B que no coinciden.

![outer_excluding_join](https://imgur.com/JgWdifp.png)

Esto lo podemos implementar de esta forma cuando estemos escribiendo las consultas:

```sql
SELECT <select_list>
FROM Table_A AS A
FULL OUTER JOIN Table_B AS B
  ON A.Key = B.Key
WHERE A.Key IS NULL OR B.Key IS NULL
```

#### Resumen

![simples_join](https://imgur.com/gShbqsw.png)

![join_command_1](https://imgur.com/hy5ybTz.png)

![join_command_2](https://imgur.com/6W8q7Vb.png)

![join_command_3](https://imgur.com/K0UvZM2.png)

![join_command_4](https://imgur.com/Os3DvYq.png)

Más informacion: En esta [cheat sheet](https://learnsql.com/blog/sql-join-cheat-sheet/joins-cheat-sheet-a4.pdf)

### Casos de Negocios

En cada caso de negocio utilizaremos algunas funciones y atributos particulares de mysql para realizar los casos de negocios correspondientes. Los casos de negocios corresponden a preguntas que nosotros nos podemos hacer, la respuesta a las preguntas la podemos encontrar haciendo queries correctas a la base de datos, obteniendo la informacion que nosotros queremos.

#### DICTINCT

1. ¿Que nacionalidades hay?

```sql
-- Me va a traer todos los valores de las columnas que encuentre.
SELECT nationality FROM authors;

-- Me traerá las diferentes nacionalidades unicamente
SELECT DISTINCT nationality FROM authors;

-- Si lo pasamos el parametro ORDER BY lo ordenará
SELECT DISTINCT nationality FROM authors ORDER BY nationality;
```

```sql

mysql> SELECT DISTINCT nationality FROM authors ORDER BY nationality;
+-------------+
| nationality |
+-------------+
| NULL        |
| AUS         |
| AUT         |
| COL         |
| DEU         |
| ENG         |
| ESP         |
| FRA         |
| GBR         |
| IND         |
| JAP         |
| MEX         |
| RUS         |
| SWE         |
| USA         |
+-------------+
15 rows in set (0.00 sec)
```

#### COUNT | GROUP BY | ORDER BY | NOT IN | IN

2. ¿Cuantos escritores hay de cada nacionalidad?

```sql
-- Cuantos escritores hay por cada nacionalidad ordenados de mayor a menor cantidad
SELECT nationality , COUNT(author_id) TOTAL
FROM authors
GROUP BY nationality
ORDER BY TOTAL DESC;

+-------------+-------+
| nationality | TOTAL |
+-------------+-------+
| NULL        |    71 |
| USA         |    27 |
| ENG         |    10 |
| IND         |     6 |
| RUS         |     4 |
| FRA         |     3 |
| SWE         |     2 |
| AUT         |     2 |
| MEX         |     1 |
| JAP         |     1 |
| ESP         |     1 |
| DEU         |     1 |
| COL         |     1 |
| GBR         |     1 |
| AUS         |     1 |
+-------------+-------+
15 rows in set (0.00 sec)


-- Igual que la query anterior pero le agregamos un segundo orden que es por nacionalidad
SELECT nationality , COUNT(author_id) TOTAL
FROM authors
GROUP BY nationality
ORDER BY TOTAL DESC, nationality ASC;

+-------------+-------+
| nationality | TOTAL |
+-------------+-------+
| NULL        |    71 |
| USA         |    27 |
| ENG         |    10 |
| IND         |     6 |
| RUS         |     4 |
| FRA         |     3 |
| AUT         |     2 |
| SWE         |     2 |
| AUS         |     1 |
| COL         |     1 |
| DEU         |     1 |
| ESP         |     1 |
| GBR         |     1 |
| JAP         |     1 |
| MEX         |     1 |
+-------------+-------+
15 rows in set (0.00 sec)


-- Sacamos los valores nulos
SELECT nationality , COUNT(author_id) TOTAL
FROM authors
WHERE nationality IS NOT NULL
GROUP BY nationality
ORDER BY TOTAL DESC, nationality;

+-------------+-------+
| nationality | TOTAL |
+-------------+-------+
| USA         |    27 |
| ENG         |    10 |
| IND         |     6 |
| RUS         |     4 |
| FRA         |     3 |
| AUT         |     2 |
| SWE         |     2 |
| AUS         |     1 |
| COL         |     1 |
| DEU         |     1 |
| ESP         |     1 |
| GBR         |     1 |
| JAP         |     1 |
| MEX         |     1 |
+-------------+-------+
14 rows in set (0.01 sec)


-- Si no queremos los valores nullos ni los de Rusia, por ejemplo
SELECT nationality , COUNT(author_id) TOTAL
FROM authors
WHERE nationality IS NOT NULL
  AND nationality NOT IN('RUS')
GROUP BY nationality
ORDER BY TOTAL DESC, nationality;

+-------------+-------+
| nationality | TOTAL |
+-------------+-------+
| USA         |    27 |
| ENG         |    10 |
| IND         |     6 |
| FRA         |     3 |
| AUT         |     2 |
| SWE         |     2 |
| AUS         |     1 |
| COL         |     1 |
| DEU         |     1 |
| ESP         |     1 |
| GBR         |     1 |
| JAP         |     1 |
| MEX         |     1 |
+-------------+-------+
13 rows in set (0.00 sec)


-- Igual que antes pero ahora tampcoo queremos a Austria
SELECT nationality , COUNT(author_id) TOTAL
FROM authors
WHERE nationality NOT IN ('RUS', 'AUT')
GROUP BY  nationality
ORDER BY TOTAL DESC, nationality;

+-------------+-------+
| nationality | TOTAL |
+-------------+-------+
| USA         |    27 |
| ENG         |    10 |
| IND         |     6 |
| FRA         |     3 |
| SWE         |     2 |
| AUS         |     1 |
| COL         |     1 |
| DEU         |     1 |
| ESP         |     1 |
| GBR         |     1 |
| JAP         |     1 |
| MEX         |     1 |
+-------------+-------+
12 rows in set (0.00 sec)


-- ¿Y si queremos solo a algunos paises puntuales? Eliminamos el NOT y usamos solo el IN.
SELECT nationality , COUNT(author_id) TOTAL
FROM authors
WHERE nationality IN ('RUS', 'AUT')
GROUP BY  nationality
ORDER BY TOTAL DESC, nationality;

+-------------+-------+
| nationality | TOTAL |
+-------------+-------+
| RUS         |     4 |
| AUT         |     2 |
+-------------+-------+
2 rows in set (0.00 sec)


```

3. ¿Cuantos libros hay de cada nacionalidad?

```sql
SELECT authors.nationality, COUNT(books.book_id) TOTAL
FROM authors
INNER JOIN books
WHERE authors.author_id = books.author_id
GROUP BY authors.nationality
ORDER BY TOTAL DESC;

+-------------+-------+
| nationality | TOTAL |
+-------------+-------+
| NULL        |   100 |
| USA         |    36 |
| ENG         |    16 |
| SWE         |    11 |
| RUS         |     9 |
| IND         |     8 |
| AUT         |     4 |
| FRA         |     3 |
| GBR         |     3 |
| AUS         |     2 |
| MEX         |     1 |
| ESP         |     1 |
| DEU         |     1 |
| JAP         |     1 |
+-------------+-------+
14 rows in set (0.00 sec)


```

#### AVG() AS promedio | STDDEV() AS desviacion_estandar 

4. ¿Cuál es el promedio/desviación estándar del precio de libros?

```sql
SELECT a.nationality,  
      AVG(b.price) AS promedio,
      STDDEV(b.price) AS std
FROM books AS b
JOIN authors AS a
  ON a.author_id = b.author_id
GROUP BY a.nationality
ORDER BY promedio DESC;

+-------------+-----------+--------------------+
| nationality | promedio  | std                |
+-------------+-----------+--------------------+
| ENG         | 19.316875 |  5.822852306591247 |
| NULL        | 18.151400 |  6.267859127325693 |
| RUS         | 17.065556 |  4.747806771110475 |
| IND         | 16.923750 |  4.226635593175736 |
| FRA         | 16.900000 |  4.931531202375181 |
| GBR         | 16.666667 |  8.289886743630591 |
| AUS         | 15.820000 | 0.5199999999999996 |
| USA         | 15.727500 | 4.2106600003905434 |
| SWE         | 15.696364 | 1.2190254880419302 |
| ESP         | 15.200000 |                  0 |
| AUT         | 14.545000 | 1.9411530078795958 |
| JAP         | 12.300000 |                  0 |
| DEU         | 10.200000 |                  0 |
| MEX         | 10.000000 |                  0 |
+-------------+-----------+--------------------+
14 rows in set (0.00 sec)

```


5. ¿Cuál es el promedio/desviación estándar de la cantidad de autores por nacionalidad?

```sql
-- Agrupar por la columna pivot.
SELECT a.nationality,
      COUNT(b.book_id) as libros,
      AVG(b.price) as prom,
      STDDEV(b.price) as std
FROM books as b
JOIN authors as a
   ON a.author_id = b.author_id
GROUP BY  nationality
ORDER BY libros DESC;

+-------------+--------+-----------+--------------------+
| nationality | libros | prom      | std                |
+-------------+--------+-----------+--------------------+
| NULL        |    100 | 18.151400 |  6.267859127325693 |
| USA         |     36 | 15.727500 | 4.2106600003905434 |
| ENG         |     16 | 19.316875 |  5.822852306591247 |
| SWE         |     11 | 15.696364 | 1.2190254880419302 |
| RUS         |      9 | 17.065556 |  4.747806771110475 |
| IND         |      8 | 16.923750 |  4.226635593175736 |
| AUT         |      4 | 14.545000 | 1.9411530078795958 |
| FRA         |      3 | 16.900000 |  4.931531202375181 |
| GBR         |      3 | 16.666667 |  8.289886743630591 |
| AUS         |      2 | 15.820000 | 0.5199999999999996 |
| ESP         |      1 | 15.200000 |                  0 |
| MEX         |      1 | 10.000000 |                  0 |
| JAP         |      1 | 12.300000 |                  0 |
| DEU         |      1 | 10.200000 |                  0 |
+-------------+--------+-----------+--------------------+
14 rows in set (0.00 sec)

```

#### MAX() y MIN()

6. ¿Cuál es el precio máximo y mínimo de un libro?

```sql

SELECT a.nationality, MAX(b.price), MIN(b.price)
FROM books AS b
JOIN authors AS a
  ON a.author_id = b.author_id
GROUP BY a.nationality;

+-------------+--------------+--------------+
| nationality | MAX(b.price) | MIN(b.price) |
+-------------+--------------+--------------+
| NULL        |        45.40 |         8.60 |
| AUS         |        16.34 |        15.30 |
| AUT         |        15.98 |        11.20 |
| DEU         |        10.20 |        10.20 |
| ENG         |        28.70 |        10.60 |
| ESP         |        15.20 |        15.20 |
| FRA         |        22.50 |        10.50 |
| GBR         |        23.50 |         5.00 |
| IND         |        23.60 |        10.50 |
| JAP         |        12.30 |        12.30 |
| MEX         |        10.00 |        10.00 |
| RUS         |        26.34 |        10.99 |
| SWE         |        18.58 |        15.00 |
| USA         |        27.00 |        10.00 |
+-------------+--------------+--------------+
14 rows in set (0.00 sec)

```

#### CONCAT() | TO_DAY() | NOW() | Realizando un reporte

7. ¿Cómo quedaría el reporte de préstamos?

- Usamos CONCAT() para agregar una segunda columna a una primer columna.
- TO_DAY(): Es una función que me dice cuantos dias han pasado desde el dia 00-00-0000 (Inicio del calendario gregoriano) hasta la fecha si se requiere con NOW().
- Usamos en este caso TO_DAY() para saber hace cuanto se alquilo tal libro.

```sql

SELECT c.name,
      t.type,
      b.title,
      CONCAT(a.name, "(", a. nationality, ")") as author,
      TO_DAYS(NOW()) - TO_DAYS(t.created_at) AS ago
FROM transactions AS t
LEFT JOIN clients AS c
  ON c.client_id = t.client_id
LEFT JOIN books AS b
  ON b.book_id = t.book_id
LEFT JOIN authors AS a
  ON b.author_id = a.author_id;

+-----------------------+--------+-------------------------------------+-------------------------+------+
| name                  | type   | title                               | author                  | ago  |
+-----------------------+--------+-------------------------------------+-------------------------+------+
| Maria Teresa Castillo | sell   | El llano en llamas                  | Juan Rulfo(MEX)         |   24 |
| Luis Saez             | lend   | Talesof Mystery and Imagination     | Edgar Allen Poe(USA)    |   24 |
| Jose Maria Bermudez   | sell   | Estudio en escarlata                | Arthur Conan Doyle(GBR) |   24 |
| Rafael Galvez         | sell   | The Startup Playbook                | Sam Altman(USA)         |   24 |
| Antonia Giron         | lend   | El llano en llamas                  | Juan Rulfo(MEX)         |   24 |
| Antonia Giron         | return | El llano en llamas                  | Juan Rulfo(MEX)         |   24 |
| Juana Maria Lopez     | sell   | Vol39 No. 1 Social Choice & Welfare | NULL                    |   24 |
+-----------------------+--------+-------------------------------------+-------------------------+------+
7 rows in set (0.00 sec)


```

### Comandos UPDATE, DELETE y TRUNCATE

**Tips**:

- Los datos no deberían borrarse, siempre y cuando se respete el acuerdo con el usuario final.
- **SIEMPRE** usar **WHERE** con comandos **UPDATE** o **DELETE**.
- Al hacer **UPDATE** o **DELETE** usar **LIMIT** para limitar el impacto del comando si algo saliese mal. Por ejemplo, si por alguna condicion que no consideramos se corresponde a 3 registros con el limit podriamos garantizar que solo se borraria 1

Comandos:

- `DELETE`: elimina información. Usamos el delete from table para ese tipo de acciones, es un DML ( lenguaje de manipulación de datos) por tanto admite parámetros usando condiciones, es decir soporta la clausula WHERE además que te devuelve el numero de archivos afectados en la operación y puedes incluso usar el LIMIT. recuerden que el DELETE borra registros 1 por 1 además que la tabla recuerda el valor AUTO_INCREMENT en caso la hayas vaciado.
- `UPDATE`: actualiza información en una tabla.
- `TRUNCATE`: elimina el contenido de una tabla por completo. Es decir, la vacía. En TRUNCATE lo que se realiza es destruir la tabla y luego recrearla ya que es un DLL (lenguaje de definición de datos), lo que lo hace más rápido y no devuelve registros afectados.

**Código**:
La estructura comun de un DELETE (recordando que **siempre** debemos ser lo mas especificos posibles) es la siguiente:

```sql
DELETE 
FROM tabla
WHERE
  [columna = valor, ...] (Idealmente que sean ids)
LIMIT
  [condiciones]
```


La estructura comun de un UPDATE sería la siguiente:

```sql
UPDATE tabla
SET 
  [columna = valor, ...]
WHERE
  [condiciones]
LIMIT
  [valor]
```


```sql
-- Ejemplos de Delete y Update

DELETE FROM authors WHERE author_id = 161 LIMIT 1;

----------------------------
mysql> select count(*) from authors;
+----------+
| count(*) |
+----------+
|      132 |
+----------+
1 row in set (0.00 sec)

mysql> delete from authors where author_id = 161 limit 1;
Query OK, 1 row affected (0.00 sec)

mysql> select count(*) from authors;
+----------+
| count(*) |
+----------+
|      131 |
+----------+
1 row in set (0.00 sec)

---------------------------------

-- Selecciono las columnas que se muentras de la tabla clients donde active sea diferente de 1 (ó = 0)
SELECT client_id, name FROM clients WHERE active <> 1;

-- Actualizo el client_id 80 a un active = 0
UPDATE clients SET active = 0 WHERE client_id = 80 LIMIT 1;

-- Actualizo el mail del client_id 7
UPDATE clients
SET
    email = 'javier@gmail.com'
WHERE
    client_id = 7
LIMIT 1;

--Desactivar clientes con ID especifica o apellido lopez

UPDATE clients
SET
    active = 0
WHERE
    client_id IN (1,6,8,27)
    OR name like '%Lopez%';

-- Buscar con ID y Lopez

SELECT client_id, name
FROM clients
WHERE
    client_id IN (1,6,8,27)
    OR name like '%Lopez%';

-- Utilizando TRUNCATE eliminamos los datos de la table dejando la estructura de la misma unicamente.
TRUNCATE transactions;
```

* ALTER es a las columnas lo que UPDATE es a las filas
* DROP es a las columnas lo que DELETE es a las filas

> El truncate elimina una tabla, y la crea de nuevo por lo que el resultado es que ahora tienes la tabla vacía. Si quisieras eliminar una tabla con su informacion y estructura puede usarse **DROP** tabla



## Consultas en MySQL

### Super QUERIES

Con **super QUERIES** lo que buscamos es darle inteligencia a las columnas.

```sql
-- SUM(), para sumar cada valor(1) en una tupla
SELECT
  COUNT(book_id),
  SUM(IF(year < 1950, 1, 0)) AS `<1950`,
  SUM(IF(year >= 1950 AND year < 1990, 1, 0)) AS `<1990`,
  SUM(IF(year >= 1990 AND year < 2000, 1, 0)) AS `<2000`,
  SUM(IF(year >= 2000, 1, 0)) AS `<hoy`
FROM books;

+----------------+-------+-------+-------+------+
| COUNT(book_id) | <1950 | <1990 | <2000 | <hoy |
+----------------+-------+-------+-------+------+
|            197 |   186 |     1 |     8 |    2 |
+----------------+-------+-------+-------+------+
1 row in set (0.00 sec)


-- Agrupar el query anterior y mostrar su nacionalidad
SELECT
  nationality,
  COUNT(book_id),
  SUM(IF(year < 1950, 1, 0)) AS `<1950`,
  SUM(IF(year >= 1950 AND year < 1990, 1, 0)) AS `<1990`,
  SUM(IF(year >= 1990 AND year < 2000, 1, 0)) AS `<2000`,
  SUM(IF(year >= 2000, 1, 0)) AS `<hoy`
FROM books AS b
JOIN authors AS a
  ON a.author_id = b.author_id
WHERE a.nationality IS NOT NULL
GROUP BY nationality;

+-------------+----------------+-------+-------+-------+------+
| nationality | COUNT(book_id) | <1950 | <1990 | <2000 | <hoy |
+-------------+----------------+-------+-------+-------+------+
| AUS         |              2 |     2 |     0 |     0 |    0 |
| AUT         |              4 |     4 |     0 |     0 |    0 |
| DEU         |              1 |     1 |     0 |     0 |    0 |
| ESP         |              1 |     1 |     0 |     0 |    0 |
| FRA         |              3 |     3 |     0 |     0 |    0 |
| GBR         |             19 |    19 |     0 |     0 |    0 |
| IND         |              8 |     8 |     0 |     0 |    0 |
| JAP         |              1 |     1 |     0 |     0 |    0 |
| MEX         |              1 |     0 |     1 |     0 |    0 |
| RUS         |              9 |     9 |     0 |     0 |    0 |
| SWE         |             11 |     3 |     0 |     8 |    0 |
| USA         |             36 |    34 |     0 |     0 |    2 |
+-------------+----------------+-------+-------+-------+------+
12 rows in set (0.00 sec)

```
Consultas tan elaboradas como esta y que pueden llegar a ser muy repetidas conviene guardaralas en una vista.
Las vistas generan tablas a partir de las sentencias de SQL, y pueden ejecutarse a partir de su nombre unicamente.

```sql
-- Con esto puedes crear la vista que quedará guardada.
CREATE VIEW books_nationality_year AS
    SELECT a.nationality, COUNT(book_id) AS 'Total', 
        SUM(IF(year < 1950, 1, 0)) as `< 1950`,  
        SUM(IF(year < 1990 and year >= 1950, 1, 0)) as `< 1990`, 
        SUM(IF(year < 2000 and year >= 1990, 1, 0)) as `< 2000`, 
        SUM(IF(year >= 2000, 1, 0)) as `hoy`
    FROM books as b
    JOIN authors as a 
    ON b.author_id = a.author_id
    WHERE a.nationality IS NOT NULL
    GROUP BY nationality;
-- Con esto ejecutas la vista
SELECT * FROM books_nationality_year;
```




### Comando mysqldump


Otras sentencias utiles que podriamos utilizar podrian ser:

* Añadir una nueva columna: Añade la columna birthyear luego de name en la tabla authors
```sql
ALTER TABLE authors ADD COLUMN birthyear integer default 1930 after name;
```
* Modificar la columna creada: Hace modificaciones a la columna birthyear: ahora es tipo year y el default es 1920
```sql
ALTER TABLE authors MODIFY COLUMN birthyear year default 1920;
```
* Eliminar la columna:
```sql
ALTER TABLE DROP COLUMN birthyear;
```
* Mostrar solo algunas tablas
```sql
show tables like '%i%'
```

El comando mysqldump se utiliza para respaldar tu base de datos. Puedes respaldar la informacion (como crear un txt con todo lo de la base de datos.).


> “El esquema se versiona, los datos se respaldan”

- El comando `mysqldump -u root -p nombre_de_base_de_datos` podeos ejecutarlo en la terminal y te arrastra todo el **schema y los datos de la base de datos**. Esto te va a imprimir todo lo que necesitarias para generar de nuevo tu base de datos. Incluso incluye los comandos para eliminar si ya existe y luego crearla de nuevo con la informacion

 Si lo hacemos de la siguiente manera: `mysqldump -u root -p nombre_de_base_de_datos > base_de_datos_completa.sql` podemos guardar la base de datos en un archivo.
  
- El comando `mysqldump -u root -p -d nombre_de_base_de_datos > esquema.sql` te permite crear un documento con solo el **schema de la BD** (La creacion de las tablas pero sin los datos en la tabla)

Nota: Recordar que para los dos comandos anteriores deben realizarse en una terminal fuera de la BD y estar ubicados en el directorio donde se desea guardar el archivo.

## Comandos mas comunes del curso

Les dejo los comandos más utilizados en el curso:

* SHOW databases; - muestra las bases de datos existentes.
* USE database_name; - selecciona una base de datos específica.
* SHOW tables; - muestras las tablas de la base de datos.
*SELECT database(); - me muestra el nombre de la base de datos seleccionada.
* CREATE database database_name; - crea una nueva base de datos.
* CREATE DATABASE IF NOT EXISTS database_name; - crea una base de datos si no existe.
* SHOW warnings; - muestra las advertencias.
* DROP table table_name; - Elimina permanentemente una tabla.
* DESCRIBE table_name; - Nos indica las columnas que tenemos en una tabla.
* SHOW FULL COLUMNS FROM table_name; - es parecido al comando DESCRIBE pero muestra mas datos.
* INSERT INTO table_name(columns) VALUES(values); - inserta una tupla.
* ON DUPLICATE KEY IGNORE ALL - esta sentencia ignora las resticciones al insertar una tupla
con un valor repetido y que esta restringido en una columna con UNIQUE (Nota: nunca utilizarlo).
* ON DUPLICATE KEY UPDATE column = VALUES(value) - al insertar una tupla con un campo duplicado
actualiza un el valor de un campo específico con un nuevo valor tomado de los datos insertados.
* SELECT * FROM table_name WHERE column_value = 1\G - en lugar de cerrar la sentencia con ;
se utiliza \G, lo cual muestra los datos de una manera mas legible.
* mysql -u root -p < all_schema.sql - con este comando podemos ejecutar un script SQL inmediatamente
despues de acceder a la base de datos.
* mysql -u root -p -D database_name < all_schema.sql - este comando es parecido al anterior solo
que con la bandera -D indicamos el nombre de la base de datos sobre la que queremos ejecutar el script.
* SELECT YEAR(NOW()); - esta sentencia me muestra el año de la fecha actual utilizando las funciones YEAR() y NOW().
* SELECT * FROM table_name WHERE column_value like ‘%value%’; - esta sentencia nos muestra las tuplas que en un
campo específico contengan un valor, el wildcard % indica que no nos importa que valor existan antes o despues del
dato que especificamos.
* SELECT COUNT(*) FROM table_name; - devuelve el número de tuplas de una tabla.
* SELECT * FROM table_name WHERE column_value BETWEEN value AND value; - nos devuelve las tuplas que se encuentren
en medio de los valores indicados.
* DELETE FROM table_name WHERE column_value = value; - elimina una tupla de una tabla.
* UPDATE table_name SET [column_value = value, …] WHERE column_value = value; - actualiza una tupla de una tabla.
* TRUNCATE table_name; - borra todo el contenido de una tabla.
* mysqldump -u user -p database_name > esquema.sql - guarda el esquema de una base de datos con todo y datos en un
archivo sql.
* mysqldump -u user -p -d database_name es parecido al comando anterior solo que aquí no se guardan los datos.
