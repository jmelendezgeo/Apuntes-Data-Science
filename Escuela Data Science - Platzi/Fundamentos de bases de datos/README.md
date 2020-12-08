
![badge](src/badge.webp)

# Fundamentos de Bases de Datos

El contenido de este documento esta basado en el curso del mismo nombre dictado por Javier Morales en [Platzi](https://platzi.com/r/jrmelendezm_/).
Estas notas son un Fork a partir de las notas de [Rusbel Bermudez](https://github.com/rb-one)

## Indice

- [Fundamentos de Bases de Datos](#fundamentos-de-bases-de-datos)
  - [Indice](#indice)
  - [Modulo 1. Bienvenida conceptos básicos y contexto histórico de las Bases de Datos](#modulo-1-bienvenida-conceptos-básicos-y-contexto-histórico-de-las-bases-de-datos)
    - [Clase 1Expert Session: resuelve tus dudas sobre las bases de datos](#clase-1expert-session-resuelve-tus-dudas-sobre-las-bases-de-datos)
    - [Clase 2 Bienvenida conceptos básicos y contexto histórico de las Bases de Datos](#clase-2-bienvenida-conceptos-básicos-y-contexto-histórico-de-las-bases-de-datos)
      - [Tipos de bases de datos](#tipos-de-bases-de-datos)
      - [Servicios](#servicios)
  - [Modulo 2. Introducción a las bases de datos relacionales](#modulo-2-introducción-a-las-bases-de-datos-relacionales)
    - [Clase 3 Historia de las RDB (relational data bases)](#clase-3-historia-de-las-rdb-relational-data-bases)
    - [Clase 4 Entidades y atributos](#clase-4-entidades-y-atributos)
      - [Atributos](#atributos)
      - [Entidades](#entidades)
      - [Clase 5 Entidades de Platzi Blog](#clase-5-entidades-de-platzi-blog)
    - [Clase 6 Relaciones](#clase-6-relaciones)
      - [Cardinalidad: 1 a 1](#cardinalidad-1-a-1)
      - [Cardinalidad: 0 a 1](#cardinalidad-0-a-1)
      - [Cardinalidad: 1 a N (1 a muchos)](#cardinalidad-1-a-n-1-a-muchos)
      - [Cardinalidad: 0 a N](#cardinalidad-0-a-n)
    - [Clase 7 Multiples muchos](#clase-7-multiples-muchos)
    - [Clase 8 Diagrama ER](#clase-8-diagrama-er)
    - [Clase 9 Diagrama Físico: tipos de datos y constraints](#clase-9-diagrama-físico-tipos-de-datos-y-constraints)
      - [Tipos de dato](#tipos-de-dato)
      - [Constraints (Restricciones)](#constraints-restricciones)
    - [Clase 10 Diagrama Físico: normalizacion](#clase-10-diagrama-físico-normalizacion)
    - [Clase 11 Diagrama Físico: normalizando Platziblog](#clase-11-diagrama-físico-normalizando-platziblog)
      - [Diagram Entidad Relacion](#diagram-entidad-relacion)
      - [Diagrama fisico Paso 1](#diagrama-fisico-paso-1)
      - [Diagrama fisico Paso 2](#diagrama-fisico-paso-2)
      - [Diagrama fisico Paso 3](#diagrama-fisico-paso-3)
    - [Clase 12 Formas normales en DB relacionales](#clase-12-formas-normales-en-db-relacionales)
      - [Primera Forma Normal (1FN)](#primera-forma-normal-1fn)
      - [Segunda Forma Normal (2FN)](#segunda-forma-normal-2fn)
      - [Tercera Forma Normal (3FN)](#tercera-forma-normal-3fn)
      - [Cuarta Forma Normal (4FN)](#cuarta-forma-normal-4fn)
  - [Modulo 3 RDBMS (MySQL) o cómo hacer lo anterior de manera práctica](#modulo-3-rdbms-mysql-o-cómo-hacer-lo-anterior-de-manera-práctica)
    - [Clase 13 RDB Qué](#clase-13-rdb-qué)
    - [Clase 14 Instalación local de un RDBMS (Windows)](#clase-14-instalación-local-de-un-rdbms-windows)
    - [Clase 15  Instalación local de un RDBMS (Mac)](#clase-15-instalación-local-de-un-rdbms-mac)
    - [Clase 16 Instalación local de un RDBMS (Ubuntu)](#clase-16-instalación-local-de-un-rdbms-ubuntu)
    - [Clase 17 Clientes Graficos](#clase-17-clientes-graficos)
    - [Clase 18 Servicios administrados](#clase-18-servicios-administrados)
  - [Modulo 4 SQL hasta en la sopa](#modulo-4-sql-hasta-en-la-sopa)
    - [Clase 19 Historia de SQL](#clase-19-historia-de-sql)
    - [Clase 20 DDL create](#clase-20-ddl-create)
    - [Clase 21 CREATE VIEW y DDL ALTER](#clase-21-create-view-y-ddl-alter)
      - [Create view](#create-view)
      - [Alter Table](#alter-table)
      - [Drop Column Borrando una columna](#drop-column-borrando-una-columna)
    - [Clase 22 DDL drop](#clase-22-ddl-drop)
    - [Clase 23 DML](#clase-23-dml)
      - [Insert](#insert)
      - [Update](#update)
      - [Delete](#delete)
      - [Select](#select)
    - [Clase 24 Que tan standard es SQL](#clase-24-que-tan-standard-es-sql)
    - [Clase 25 Creando Platziblog: tablas independientes](#clase-25-creando-platziblog-tablas-independientes)
    - [Clase 26 Creando Platziblog: tablas dependientes](#clase-26-creando-platziblog-tablas-dependientes)
    - [Clase 27 Creando Platziblog: tablas transitivas](#clase-27-creando-platziblog-tablas-transitivas)
      - [Reverse Engineer](#reverse-engineer)
    - [Clase 28 Por qué las consultas son tan importantes](#clase-28-por-qué-las-consultas-son-tan-importantes)
    - [Clase 29 Estructura básica de un Query](#clase-29-estructura-básica-de-un-query)
      - [Primer Consulta](#primer-consulta)
    - [Clase 30 SELECT](#clase-30-select)
    - [Clase 31 FROM](#clase-31-from)
    - [Clase 32 Utilizando la sentencia FROM](#clase-32-utilizando-la-sentencia-from)
    - [Clase 33 WHERE](#clase-33-where)
    - [Clase 34 Utilizando la sentencia WHERE nulo y no nulo](#clase-34-utilizando-la-sentencia-where-nulo-y-no-nulo)
    - [Clase 35 GROUP BY](#clase-35-group-by)
    - [Clase 36 ORDER BY y HAVING](#clase-36-order-by-y-having)
    - [Clase 37 El interminable agujero de conejo (Nested queries)](#clase-37-el-interminable-agujero-de-conejo-nested-queries)
    - [Clase 38 Como convertir una pregunta en un query SQL](#clase-38-como-convertir-una-pregunta-en-un-query-sql)
      - [De pregunta a Query](#de-pregunta-a-query)
    - [Clase 39 Preguntandole a la base de datos](#clase-39-preguntandole-a-la-base-de-datos)
    - [Clase 40 Consultando PlatziBlog](#clase-40-consultando-platziblog)
  - [Modulo 4 Introduccion a la bases de datos NO relacionales](#modulo-4-introduccion-a-la-bases-de-datos-no-relacionales)
    - [Clase 41 Que son y cuales son los tipos de bases de datos no relacionales](#clase-41-que-son-y-cuales-son-los-tipos-de-bases-de-datos-no-relacionales)
      - [Tipos de bases de datos no relacionales:](#tipos-de-bases-de-datos-no-relacionales)
    - [Clase 42 Servicios administrados y jerarquía de datos](#clase-42-servicios-administrados-y-jerarquía-de-datos)
  - [Modulo 5 Manejo de modelos de datos en bases de datos no relacionales](#modulo-5-manejo-de-modelos-de-datos-en-bases-de-datos-no-relacionales)
    - [Clase 43 Top level collection con Firebase](#clase-43-top-level-collection-con-firebase)
    - [Clase 44 Creando y borrando documentos en Firestore](#clase-44-creando-y-borrando-documentos-en-firestore)
    - [Clase 45 Colecciones vs subcolecciones](#clase-45-colecciones-vs-subcolecciones)
    - [Clase 46 Recreando Platziblog](#clase-46-recreando-platziblog)
    - [Clase 47 Construyendo Platziblog en Firestore](#clase-47-construyendo-platziblog-en-firestore)
    - [Clase 48 Proyecto final: transformando tu proyecto en una db no relacional](#clase-48-proyecto-final-transformando-tu-proyecto-en-una-db-no-relacional)
      - [Regla 1. Piensa en la vista de tu aplicación](#regla-1-piensa-en-la-vista-de-tu-aplicación)
  - [Modulo 6 Bases de datos en la vida real](#modulo-6-bases-de-datos-en-la-vida-real)
    - [Clase 49 Bases de datos en la vida real](#clase-49-bases-de-datos-en-la-vida-real)
    - [Clase 50 Big Data](#clase-50-big-data)
    - [Clase 51 Data warehouse](#clase-51-data-warehouse)
    - [Clase 52 Data mining](#clase-52-data-mining)
    - [Clase 53 ETL](#clase-53-etl)
    - [Clase 54 Business intelligence](#clase-54-business-intelligence)
    - [Clase 55 Machine Learning](#clase-55-machine-learning)
    - [Clase 56 Data Science](#clase-56-data-science)
    - [Clase 57 Por que aprender bases de datos hoy](#clase-57-por-que-aprender-bases-de-datos-hoy)
  - [Bonus](#bonus)
    - [Clase 58 Bases de datos relacionales vs no relacionales](#clase-58-bases-de-datos-relacionales-vs-no-relacionales)

## Modulo 1. Bienvenida conceptos básicos y contexto histórico de las Bases de Datos

### Clase 1Expert Session: resuelve tus dudas sobre las bases de datos

### Clase 2 Bienvenida conceptos básicos y contexto histórico de las Bases de Datos

Tu profesor será Israel Vázquez, senior web developer en San Francisco, seminarista de bases de datos y entusiasta data engineering.
El almacenamiento en la nube tiene un gran pro comparada con los otros métodos de almacenamiento ya que es accesible desde cualquier parte del mundo. Además es centralizada y puede ser usada por varias personas al mismo tiempo. 

Las bases de datos entran cuando hacemos la transición a medios digitales.Surgen para complementar la arquitectura de Von Neumann. Este describe una arquitectura de diseño para un computador digital electrónico con partes que constan de una unidad de procesamiento que contiene una unidad aritmético lógica y registros del procesador, una unidad de control que contiene un registro de instrucciones y un contador de programa, una memoria para almacenar tanto datos como instrucciones, almacenamiento masivo externo, y mecanismos de entrada y salida.

La intencion era tener la capacidad de almacenar información más allá de la memoria RAM para poder acceder a ella una vez que, por ejemplo, se reiniciara el computador

#### Tipos de bases de datos

Se han dividido historicamente en dos ramas:

**Relacionales:** En la industria hay varias compañías dedicadas a ser manejadoras de bases de datos relacionales como SQL Server, Oracle, **MariaDB**, entre otras.
**No relacionales**: Todavía están avanzando y existen ejemplos muy distintos como cassandra, elasticsearch, neo4j, MongoDB, entre otras.

#### Servicios

**Auto administrados:** Es la base de datos que instalas tú y te encargas de actualizaciones, mantenimiento, etc.
**Administrados:** Servicios que ofrecen las nubes modernas como Amazon, Google, Azure; y no debes preocuparte por mantenimiento o actualizaciones.


## Modulo 2. Introducción a las bases de datos relacionales

### Clase 3 Historia de las RDB (relational data bases)

Las bases de datos surgen de la necesidad de conservar la información más allá de lo que existe en la memoria RAM.

Primero, las bases de datos basadas en archivos eran datos guardados en texto plano (como archivos .txt o separados por comas), fáciles de guardar pero muy difíciles de consultar y por la necesidad de mejorar esto nacen las bases de datos relacionales. Surgió la necesidad de tener algo un poco más estructurado, de allí nacen las bases de datos relacionales. **Su inventor Edgar Codd** dejó ciertas reglas para asegurarse de que toda la filosofía de las bases de datos no se perdiera, estandarizando el proceso, **Codd invento el algebra relacional**

(Contenido adicional)
Bases de datos relacionales (RBD)

Es importante que sea fácil de guardar y extraer, anteriormente se usaban bases de datos basadas en archivos, el cuál era texto plano fácil de guardar, pero difícil de extraer, por esto se inventaron las bases de datos relacionales. En 1990 Codd se preocupó porque los sistemas de gestión de bases de datos (SGBD) que decían ser relacionales, no lo eran. En la práctica es difícil cumplir las 12 pero, un SGBD es más relacional cuantas más reglas cumpla

Las Reglas y mandamientos de Edgar Frank Ted Codd

**Regla 0:** Regla de fundación.
a) Cualquier sistema que se proclame como relacional, debe ser capaz de gestionar sus bases de datos enteramente mediante sus capacidades relacionales.

**Regla 1:** Regla de la información.
a) Todos los datos deben estar almacenados en las tablas
b) Esas tablas deben cumplir las premisas del modelo relacional
c) No puede haber información a la que accedemos por otra vía

**Regla 2:** Regla del acceso garantizado.
a) Cualquier dato es accesible sabiendo la clave de su fila y el nombre de su columna o atributo
b) Si a un dato no podemos acceder de esta forma, no estamos usando un modelo relacional

**Regla 3:** Regla del tratamiento sistemático de valores nulos.
a) Esos valores pueden dar significado a la columna que los contiene
b) El SGBD debe tener la capacidad de manejar valores nulos
c) El SGBD reconocerá este valor diferenciándolo de cualquier otro
d) El SGBD deberá aplicársele la lógica apropiada
e) Es un valor independiente del tipo de datos de la columna

**Regla 4:** Catálogo dinámico en línea basado en el modelo relacional.
a) El catálogo en línea es el diccionario de datos
b) El diccionario de datos se debe de poder consultar usando las mismas técnicas que para los datos
c) Los metadatos, por tanto, se organizan también en tablas relacionales
d) Si SELECT es una instrucción que consulta datos, también será la que consulta los metadatos

**Regla 5:** Regla comprensiva del sublenguaje de los datos completo.
a) Al menos tiene que existir un lenguaje capaz de hacer todas las funciones del SGBD
b) No puede haber funciones fuera de ese lenguaje
c) Puede haber otros lenguajes en el SGBD para hacer ciertas tareas
d) Pero esas tareas también se deben poder hacer con el “lenguaje completo”

**Regla 6:** Regla de actualización de vistas.
a) Las vistas tienen que mostrar información actualizada
b) No puede haber diferencias entre los datos de las vistas y los datos de las tablas base

**Regla 7:** Alto nivel de inserción, actualización, y cancelación.
a) La idea es que el lenguaje que maneja la base de datos sea muy humano
b) Eso implica que las operaciones del lenguaje de manipulación de los datos (DML) trabajen con conjuntos de filas a la vez
c) Para modificar, eliminar o añadir datos, no hará falta programar de la forma en la que lo hacen los lenguajes de tercera generación como C o Java

**Regla 8:** Independencia física de los datos.
a) Cambios en la física de la BD no afecta a las aplicaciones ni a los esquemas lógicos
b) El acceso a las tablas (elemento lógico) no cambia porque la física de la base de datos cambie

**Regla 9:** Independencias lógicas de los datos.
a) Cambios en el esquema lógico (tablas) de la BD no afectan al resto de esquemas
b) Si cambiamos nombres de tabla, o de columna o modificamos información de las filas, las aplicaciones (esquema externo) no se ven afectadas
c) Es más difícil de conseguir

**Regla 10:** Independencia de la integridad.
a) Las reglas de integridad (restricciones) deben de ser gestionadas y almacenadas por el SGBD

**Regla 11:** Independencia de la distribución.
a) Que la base de datos se almacene o gestione de forma distribuida en varios servidores, no afecta al uso de esta ni a la programación de las aplicaciones de usuario
b) El esquema lógico es el mismo independientemente de si la BD es distribuida o no

**Regla 12:** La regla de la no subversión.
a) La base de datos no permitirá que exista un lenguaje o forma de acceso, que permita saltarse las reglas anteriores.

### Clase 4 Entidades y atributos

Una **entidad** es algo similar a un objeto (programación orientada a objetos) y representa algo en el mundo real, incluso algo abstracto. Tienen atributos que son las cosas que los hacen ser una entidad, se diagraman dentro de cuadrados  y **por convención se ponen en plural**.

#### Atributos

Los atributos se representan con óvalos, los que tienen multiples valores llevan dobles óvalos, también existen atributos compuestos, los atributos especiales son óvalos con linea punteada.

Por ejemplo, vemos los atributos de las laptops. Una laptop tiene una pantalla, color, año, modelo y metodo de entrada. El numero de serie como es un atributo especifico de cada laptop, único, se coloca subrayado. Una laptop puede tener varios discos duros, por lo que es un atributo multiple. La antiguedad es un atributo especial porque no se obtiene como los demás, se obtiene a partir del año de la laptop, por eso se coloca en lineas espaciadas. Esta notación se conoce como **Notación Chen**

Los **atributos compuestos** son aquellos que tienen atributos ellos mismos.

Los **atributos llave** son aquellos que identifican a la entidad y no pueden ser repetidos, se diagraman con underline. Existen:

- Naturales: Son inherentes al objeto como el número de serie
- Clave artificial: No es inherente al objeto y se asigna de manera arbitraria

![src/Atributos-rdb.png](src/Atributos-rdb.png)

#### Entidades

**Entidad Fuerte:** No depende de ninguna entidad para existir

**Entidades débiles:** No pueden existir sin una entidad fuerte y se representan con un cuadrado con doble línea.

- Identidades débiles por identidad: No se diferencian entre sí más que por la clave de su identidad fuerte.
- Identidades débiles por existencia: Se les asigna una clave propia.

![src/entidades_debiles.png](src/entidades_debiles.png)

![src/entidades_debiles_2.png](src/entidades_debiles_2.png)

Las entidades debiles pueden serlo por dos motivos:

**Por identidad:** No se diferencian entre si mas que por la clave de su entidad fuerte (clave isbn).

**Por existencia:** Usando llave asignada por nosotros (un id).

En nuestro ejemplo, vemos que tenemos entidades debiles (los ejemplares) que indican en que pasillo se encuentran y que edicion son (primera edicion o tercera edicion). No podriamos tener ejemplares sin antes tener un libro, por eso son identidades debiles. Para poder diferenciarlas (ya que por ejemplo hay varios pasillo1/ primera edicion) tendriamos que enlazarlas a su libro correspondiente (por identidad) o asignandoles un id particular (por existencia). El asignarles un ID particular sigue implicando que sean débiles conceptualmente.

#### Clase 5 Entidades de Platzi Blog

Nuestro proyecto será un manejador de Blogpost. Es un contexto familiar y nos representará retos muy interesantes.

- Primer paso: Identificar las entidades (abstracciones del mundo real). Esto se conoce como diagramas de ER. En el, vamos a poner todas las posibles entidades que vamos a manejar y sus atributos. Por ejemplo, en nuestro blog tendremos Post, usuarios, comentarios y categorias.

![src/entidades_platziblog.png](src/entidades_platziblog.png)

- Segundo paso: Pensar en los atributos.

![src/entidades_platziblog_2.png](src/entidades_platziblog_2.png)

![src/entidades_platziblog_3.png](src/entidades_platziblog_3.png)


Comentarios: 
  * Fecha de publicación
  * Id del usuario
  * Id del comentario
  
Categorias:
 * Nombre de categoría
 * Id de categoría


Algunas herramientas para hacer diagramas de entidad-relación serían:
* [lucidchart](https://www.lucidchart.com/)
* [Draw.io](https://app.diagrams.net/)

### Clase 6 Relaciones

Las **relaciones** nos permiten ligar o unir nuestras diferentes entidades y se representan con rombos. Por convención se definen a través de verbos.Por ejemplo, un jugador **pertenece** a un equipo, laptops **tiene** disco duro, 

![src/relaciones.png](src/relaciones.png)




Las relaciones tienen una propiedad llamada **cardinalidad** y tiene que ver con números. Cuántos de un lado pertenecen a cuántos del otro lado:

Cardinalidad: 1 a 1
Cardinalidad: 0 a 1
Cardinalidad: 1 a N
Cardinalidad: 0 a N

#### Cardinalidad: 1 a 1

![src/cardinalidad_1_1.png](src/cardinalidad_1_1.png)

1 persona - **tiene** - 1 dato_contacto
1 dato_contacto - **tiene** - 1 persona.

La simbología de las dos rayitas implica que es relación 1 a 1 estricta.

#### Cardinalidad: 0 a 1

Algunos autores la denominan 1 a 1 opcional.
En el ejemplo una sesión tiene un usuario, pero no necesariamente esta loggeado todo  el tiempo. La cardinalidad es opcional, se representa con la misma linea anterior pero punteada

![src/cardinalidad_0_1.png](src/cardinalidad_0_1.png)

#### Cardinalidad: 1 a N (1 a muchos)

Una persona tiene N automóviles, pero 1 automóvil solo tiene 1 dueño. En este caso tenemos una cardinaldiad de 1 a N con un conector que significa 1 y del otro lado una linea que se parte (p.e en tres) para indicar que son muchos. 

![src/cardinalidad_1_N.png](src/cardinalidad_1_N.png)

#### Cardinalidad: 0 a N

Por ejemplo, un paciente en un hospital. Algunos lo consideran 1 a N opcional. Por ejemplo, un paciente siempre esta asignado a una o varias habitaciones en un hospital pero las habitaciones no necesariamente deben tener pacientes. Pueden estar vacias.

![src/33333333333333333333333333333333333333333333333333333333333333333333.png](src/cardinalidad_0_N.png)

### Clase 7 Multiples muchos

Este tipo de cardinalidad es muy interesante por ello su clase aparte,se vera cuando veamos los campos clave.

Cardinalidad: N a N. Por ejemplo, un alumno **pertenece** a una o varias clases. A su vez, una clase puede tener varios alumnos. 

### Clase 8 Diagrama ER

Un diagrama es como un mapa y nos ayuda a entender cuáles son las entidades con las que vamos a trabajar, cuáles son sus relaciones y qué papel van a jugar en las aplicaciones de la base de datos.

Un usuario puede escribir muchos posts. Tambien, un usuario escribe muchos ocmentarios, Los post tienen comentarios. Una categoria engloba a varios post. Los posts pueden tener muchas etiquetas y a su vez una etiqueta puede tener varios posts.

![src/diagrama_ER.png](src/diagrama_ER.png)

### Clase 9 Diagrama Físico: tipos de datos y constraints

Para llevar a la práctica un diagrama debemos ir más allá y darle detalle con parámetros como:

#### Tipos de dato

**- Texto:**
  -CHAR(n): Permite almacenar cadenas y caracteres. De memoria fija
  -VARCHAR(n): Reserva un espacio minimo de memoria variable para almacenar cadenas y caracteres con limite de 255 caracteres.
  -TEXT: En los casos en los que se superen los 255 caracteres; permite guardar mas contenido de texto.


**- Números:**:
  -INTEGER: Numero sin punto decimal.
  -BIGINT: Declarar un numero muy grande.
  -SMALLINT: Declara un numero pequeño (ventajas por eficiencia)
  -DECIMAL(n,s): Declara numeros decimales, primero se añade el numero entero (n) y luego el decimal (s)
  -NUMERIC(n,s)

**- Fecha/hora:**: 
  -DATE: Indica fecha: Año-mes-día 
  -TIME: Indica la hora
  -DATETIME: Contiene fecha y hora
  -TIMESTAMP: Contiene fecha y hora. Se utiliza en "rangos"

**- Lógicos:** 
  -BOOLEAN

Nota:

Char(8) reserva 8 espacios en memoria de forma fija, Varchar(8) hace lo mismo pero crece (1,2,3...8) de manera dinámica conforme los requieres.

#### Constraints (Restricciones)

Significa que vamos a añadir reglas a nuestra base de datos.

**- NOT NULL:** Se asegura que la columna no tenga valores nulos. Cuando metes valores en una tabla, el valor por defecto es el null ( nulo). Si añades este constraint, por ejemplo, a una casilla de _nombre_, cuando intenten enviarte una base de datos con nombre vacío, la base de datos enviara un error. Esto ayuda a definir los datos obligatorios del sistema

**- UNIQUE:** Se asegura que cada valor en la columna no se repita. Por ejemplo, el email (que nadie tenga el mismo email dos veces).

**- PRIMARY KEY:** Es una combinación de NOT NULL y UNIQUE. Esto se utilza mucho; los conocidos Campos Llave para llevar el id de cosas, por ejemplo. Nos ayudara posteriormente a hacer union entre una tabla y otra o relaciones entre entidades (Lo hacemos un indice)

**- FOREIGN KEY:** Identifica de manera única una tupla en otra tabla. Se utiliza cuando queremos usar otra tabla, es la otra parte de Primary Key. Cuando queremos juntar dos tablas, la primary key de la otra tabla se añade como Foreign Key para ligarlos

**- CHECK:** Se asegura que el valor en la columna cumpla una condición dada. Nos permite definir la regla que queramos. 

**- DEFAULT:** Coloca un valor por defecto cuando no hay un valor especificado. Por ejemplo, el valor por defecto sería null pero se puede configurar a que, por ejemplo, sea 0. 

**- INDEX:** Se crea por columna para permitir búsquedas más rápidas. Tiene la desventaja de que tiene que reindexar los registros cada vez que añades un nuevo registro, lo que vuelve muy lenta la operación de la bd a medida que el proyecto crece. Por ejemplo, es contraproducente cuando tenemos una tabla en la que metemos registro pero no leemos seguido.

### Clase 10 Diagrama Físico: normalizacion

### ¿Por qué se normalizan las bases de datos?

    * Evitar la redundancia de los datos.
    * Disminuir problemas de actualización de los datos en las tablas.
    * Proteger la integridad de los datos.
    * Facilitar el acceso e interpretación de los datos.
    * Reducir el tiempo y complejidad de revisión de las bases de datos.
    * Optimizar el espacio de almacenamiento.
    Prevenir borrados indeseados de datos.



La normalización como su nombre lo indica nos ayuda a dejar todo de una forma normal. Esto obedece a las 12 reglas de Codd y nos permiten separar componentes en la base de datos:

Las formas normales son reglas que utilizamos para normalizar la información.

![src/diagrama_fisico_sin_normalizar.png](src/diagrama_fisico_sin_normalizar.png)

**Primera forma normal (1FN):** Esta FN nos ayuda a eliminar los valores repetidos y no atómicos dentro de una base de datos.

Formalmente, una tabla está en primera forma normal si:

    * Todos los atributos son atómicos. Un atributo es atómico si los elementos del dominio son simples e indivisibles.
    * No debe existir variación en el número de columnas.
    * Los campos no clave deben identificarse por la clave (dependencia funcional).
    * Debe existir una independencia del orden tanto de las filas como de las columnas; es decir, si los datos cambian de orden no deben cambiar sus significados.

Se traduce básicamente a que si tenemos campos compuestos como por ejemplo “nombre_completo” que en realidad contiene varios datos distintos, en este caso podría ser “nombre”, “apellido_paterno”, “apellido_materno”, etc.

También debemos asegurarnos que las columnas son las mismas para todos los registros, que no haya registros con columnas de más o de menos.

Todos los campos que no se consideran clave deben depender de manera única por el o los campos que si son clave.

Los campos deben ser tales que si reordenamos los registros o reordenamos las columnas, cada dato no pierda el significado.


En nuestra tabla sin normalizar vemos que hay campos repetidos. Tenemos _materia 1_ y _materia 2_ aunque ambas sean _materias_

![src/diagrama_fisico_1N.png](src/diagrama_fisico_1N.png)


**Segunda forma normal (2FN):** Esta FN nos ayuda a diferenciar los datos en diversas entidades.

Formalmente, una tabla está en segunda forma normal si:

    * Está en 1FN
    * Sí los atributos que no forman parte de ninguna clave dependen de forma completa de la clave principal. Es decir, que no existen dependencias parciales.
    * Todos los atributos que no son clave principal deben depender únicamente de la clave principal.

Lo anterior quiere decir que sí tenemos datos que pertenecen a diversas entidades, cada entidad debe tener un campo clave separado. Por ejemplo:

Una vez que separamos nuestra tabla, vemos que ahora tenemos la informacion del alumno dos veces. Esto no debería ser así; por lo que separaremos la tabla de alumnos de la tabla de materias. Con esto nos sacamos los renglones repetidos. Esto tiene sentido pues materia y alumno no deberian considerarse una misma entidad; conceptualmente son dos cosas diferentes. Alumnos y materias se considerarian cardinalidad N:N

![src/diagrama_fisico_2N.png](src/diagrama_fisico_2N.png)

**Tercera forma normal (3FN):** Esta FN nos ayuda a separar conceptualmente las entidades que no son dependientes.

Formalmente, una tabla está en tercera forma normal si:

  * Se encuentra en 2FN
  * No existe ninguna dependencia funcional transitiva en los atributos que no son clave

Esta FN se traduce en que aquellos datos que no pertenecen a la entidad deben tener una independencia de las demás y debe tener un campo clave propio. Continuando con el ejemplo anterior, al aplicar la 3FN separamos la tabla alumnos ya que contiene datos de los cursos en ella quedando de la siguiente manera.

En este caso, lo mejor sería separar los cursos. A pesar de que no se repetian había una cardinalidad 1 a 1 entre alumnos y cursos, son entidades separadas. Nuestros alumnos no tienen ligadas las maestrias o los cursos. Las maestrias pueden tener mas de un alumno por lo que podria considerarse una entidad.

![src/diagrama_fisico_3N.png](src/diagrama_fisico_3N.png)

**Cuarta forma normal (4FN):** Esta FN nos trata de atomizar los datos multivaluados de manera que no tengamos datos repetidos entre rows.

Formalmente, una tabla está en cuarta forma normal si:

   * Se encuentra en 3FN
   * Los campos multivaluados se identifican por una clave única

Esta FN trata de eliminar registros duplicados en una entidad, es decir que cada registro tenga un contenido único y de necesitar repetir la data en los resultados se realiza a través de claves foráneas.

Aplicado al ejemplo anterior la tabla materia se independiza y se relaciona con el alumno a través de una tabla transitiva o pivote, de tal manera que si cambiamos el nombre de la materia solamente hay que cambiarla una vez y se propagara a cualquier referencia que haya de ella.
Esto implica que separaremos las materias nuevamente, porque en la versión anterior igual teniamos repetido el nombre MySQL y Python; no podemos permitirnos esto. Esta vez separamos materias. Luego tendremos una tabla que dira materias por alumno que se encargara de ligar los contenidos de las tablas; se incluye un id artificial y enlazamos los ids de los alumnos con los ids de las materias. Cuando estamos creando una BBDD, si las entidades se relacionan a su cardinalidad N:M automaticamente se crea una nueva tabla como forma de relación.

![src/diagrama_fisico_4N.png](src/diagrama_fisico_4N.png)

A pesar de que tenemos los mismos datos, esto nos ayuda hacer uniones que en inicio no teniamos pensado. Podemos incluir nuevos alumnos o nuevas materias y añadirlas a los alumnos. Nos permite mucha flexbilidad y garantiza que a lo largo de la base de datos no haya estados repetidos. Nos permitira tambien hacer Querys complejos

### Clase 11 Diagrama Físico: normalizando Platziblog

#### Diagram Entidad Relacion

Ahora que tenemos nuestras entidades y relaciones, como se muestra en el siguiente diagrama, debemos normalizar nuestro blog.

![src/diagrama_ER.png](src/diagrama_ER.png)

#### Diagrama fisico Paso 1

Generar los campos básicos de cada entidad.

Por ejemplo, Usuario:
-ID: Debe tener un ID que será una PrimaryKey, Unico de cada usuario y no se puede repetir
- Login, psw, nickname: Para ingresar debe tener un login (Not null) y una contraseña (not null). Ademas, cada usuario necesita un nickname para poder ser reconocido en la pagina. Cada usuario se registra con un email unico (not null y unique)


![src/Diagrama_Fisico_paso_1.png](src/diagrama_fisico_paso_1.png)

#### Diagrama fisico Paso 2

Genera las relaciones entre cada entidad y asigna PK y FK. Como regla, en una relación 1:N se añade la clave del que tiene 1. Por ejemplo, Un usuario puede tener muchos post, por lo que en post el id del usuario se debe añadir como FK.

![src/diagrama_fisico_paso_2.png](src/diagrama_fisico_paso_2.png)

#### Diagrama fisico Paso 3

![src/diagrama_fisico_paso_2_N_N.png](src/diagrama_fisico_paso_2_N_N.png)

Para manejar las relaciones muchos a muchos, es necesario generar una tabla intermedia de esta manera. Esta tabla va a relacionar los posts con las etiquetas y tiene las llaves de ambos registros.

![src/diagrama_fisico_paso_3_N_N.png](src/diagrama_fisico_paso_3_N_N.png)

Observa que post_id y etiqueta_id usan llaves compuestas para hacer combinaciones únicas, o podemos generar también la forma anterior con un id. Una clave compuesta es cuando se tiene un campo ID pero no es un solo campo, este campo esta formado por dos campos (el id de post y el id de las etiquetas). Por ejemplo, si se tiene el post 1 con la etiqueta 2, el post 1 con la etiqueta 3, la combinación debe ser única. Esta es una práctica que se utiliza, sin embargo tambien puede añadirse una nueva clave id de esta tabla post-etiquetas.

### Clase 12 Formas normales en DB relacionales

La normalización en las bases de datos relacionales es uno de esos temas que, por un lado es sumamente importante y por el otro suena algo esotérico. Vamos a tratar de entender las formas normales (FN) de una manera simple para que puedas aplicarlas en tus proyectos profesionales.

#### Primera Forma Normal (1FN)

Esta FN nos ayuda a eliminar los valores repetidos y no atómicos dentro de una base de datos.

Formalmente, una tabla está en primera forma normal si:

- Todos los atributos son atómicos. Un atributo es atómico si los elementos del dominio son simples e indivisibles.
- No debe existir variación en el número de columnas.
- Los campos no clave deben identificarse por la clave (dependencia funcional).
- Debe existir una independencia del orden tanto de las filas como de las columnas; es decir, si los datos cambian de orden no deben cambiar sus significados.

Se traduce básicamente a que si tenemos campos compuestos como por ejemplo “nombre_completo” que en realidad contiene varios datos distintos, en este caso podría ser “nombre”, “apellido_paterno”, “apellido_materno”, etc.

Se traduce básicamente a que si tenemos campos compuestos como por ejemplo “nombre_completo” que en realidad contiene varios datos distintos, en este caso podría ser “nombre”, “apellido_paterno”, “apellido_materno”, etc.

Los campos deben ser tales que si reordenamos los registros o reordenamos las columnas, cada dato no pierda el significado.

#### Segunda Forma Normal (2FN)

Esta FN nos ayuda a diferenciar los datos en diversas entidades.

Formalmente, una tabla está en segunda forma normal si:

- Está en 1FN
- Sí los atributos que no forman parte de ninguna clave dependen de forma completa de la clave principal. Es decir, que no existen dependencias parciales.
- Todos los atributos que no son clave principal deben depender únicamente de la clave principal.

Lo anterior quiere decir que sí tenemos datos que pertenecen a diversas entidades, cada entidad debe tener un campo clave separado. Por ejemplo:

![diagrama_fisico_1N.png](src/diagrama_fisico_1N.png)

En la tabla anterior tenemos por lo menos dos entidades que debemos separar para que cada uno dependa de manera única de su campo llave o ID. En este caso las entidades son alumnos por un lado y materias por el otro, ya que una materia. En el ejemplo anterior, quedaría de la siguiente manera:

![diagrama_fisico_2N.png](src/diagrama_fisico_2N.png)

#### Tercera Forma Normal (3FN)

Esta FN nos ayuda a separar conceptualmente las entidades que no son dependientes.

Formalmente, una tabla está en tercera forma normal si:

Se encuentra en 2FN
No existe ninguna dependencia funcional transitiva en los atributos que no son clave

Esta FN se traduce en que aquellos datos que no pertenecen a la entidad deben tener una independencia de las demás y debe tener un campo clave propio. Continuando con el ejemplo anterior, al aplicar la 3FN separamos la tabla alumnos ya que contiene datos de los cursos en ella quedando de la siguiente manera.

![diagrama_fisico_3N.png](src/diagrama_fisico_3N.png)

#### Cuarta Forma Normal (4FN)

Esta FN nos **trata de atomizar los datos multivaluados** de manera que no tengamos datos repetidos entre rows.

Formalmente, una tabla está en cuarta forma normal si:

- Se encuentra en 3FN
- Los campos multivaluados se identifican por una clave única

Esta FN trata de eliminar registros duplicados en una entidad, es decir que cada registro tenga un contenido único y de necesitar repetir la data en los resultados se realiza a través de claves foráneas.

Aplicado al ejemplo anterior la tabla materia se independiza y se relaciona con el alumno a través de una tabla transitiva o pivote, de tal manera que si cambiamos el nombre de la materia solamente hay que cambiarla una vez y se propagara a cualquier referencia que haya de ella.

![diagrama_fisico_4N](src/diagrama_fisico_4N.png)

De esta manera, aunque parezca que la información se multiplicó, en realidad la descompusimos o normalizamos de manera que a un sistema le sea fácil de reconocer y mantener la consistencia de los datos.

Algunos autores precisan una 5FN que hace referencia a que después de realizar esta normalización a través de uniones (JOIN) permita regresar a la data original de la cual partió.

## Modulo 3 RDBMS (MySQL) o cómo hacer lo anterior de manera práctica

### Clase 13 RDB Qué

**RDBMS** significa Relational Database Management System o sistema manejador de bases de datos relacionales. Es un programa que se encarga de seguir las reglas de Codd y se puede utilizar de manera programática.

### Clase 14 Instalación local de un RDBMS (Windows)

Hay dos maneras de acceder a manejadores de bases de datos:

- Instalar en máquina local un administrador de bases relacional.
-Tener ambientes de desarrollo especiales o servicios cloud.

En este curso usaremos MySQL porque tiene un impacto histórico siendo muy utilizado y además es software libre y gratuito. La versión 5.6.43 es compatible con la mayoría de aplicaciones y frameworks.

- Root es el usuario principal que tendrá todos los permisos y por lo tanto en ambientes de producción hay que tener mucho cuidado al configurarlo.

Link
<https://dev.mysql.com/downloads/windows/installer/5.6.html>

Procedimiento:

- Descargamos e instalamos como es usual en windows
- En el instalador seleccionamos la opción custom
- Instalamos MySQL Server la version 64bts
- Instalamos MySQL Workbench (ignoramos lo demás)

![Instalador_mysql_1](src/Instalador_mysql_1.png)
![Instalador_mysql_2](src/Instalador_mysql_2.png)
![Instalador_mysql_3](src/Instalador_mysql_3.png)

### Clase 15  Instalación local de un RDBMS (Mac)

La instalación es similar al todos los instaladores en mac, descarga el archivo .dmg

<https://dev.mysql.com/downloads/workbench/>

Para macOS debes descargar workbench aparte.

<https://dev.mysql.com/downloads/mysql/5.7.html>

### Clase 16 Instalación local de un RDBMS (Ubuntu)

Visita la dirección de descarga de la versión de comunidad de MySql
<https://dev.mysql.com/downloads/mysql/5.7.html#downloads>

Dirígete a la sección de selección de descargas y selecciona tu distribución de Linux. En nuestro caso Ubuntu y selecciona posteriormente la versión que estás utilizando actualmente, en nuestro caso 18.04 de 64 bits.

Los pasos son similares a los otros sistemas, descarga el paquete .deb, también puedes instalar desde la consola

sudo apt-get install mysql-server

### Clase 17 Clientes Graficos

Observamos el preview y pasos para crear un schema en Mysql workbench

![worckbench_1](src/worckbench_1.png)

![worckbench_2](src/worckbench_2.png)

![worckbench_3](src/worckbench_3.png)

### Clase 18 Servicios administrados

Hoy en día muchas empresas ya no tienen instalados en sus servidores los RDBMS sino que los contratan a otras personas. Estos servicios administrados cloud te permiten concentrarte en la base de datos y no en su administración y actualización.

Introducción a google cloud, toma el curso para configurarlo.

## Modulo 4 SQL hasta en la sopa

### Clase 19 Historia de SQL

**SQL** significa Structured Query Language y tiene una estructura clara y fija. Su objetivo es hacer un solo lenguaje para consultar cualquier manejador de bases de datos volviéndose un gran estándar.

Ahora existe el **NOSQL** o Not Only Structured Query Language que significa que no sólo se utiliza SQLen las bases de datos no relacionales.

### Clase 20 DDL create

SQL tiene dos grandes sublenguajes. Entre esos el DDL:

**DDL o Data Definition Language** que nos ayuda a crear la estructura de una base de datos. Nos ayuda a crear los cimientos, las relaciones, las entidades (todo lo practicado anteriormente en los diagramas) en una base de datos real. Existen 3 grandes comandos:

**- Create**: Nos ayuda a crear bases de datos, tablas, vistas, índices, etc.

-**Alter**: Ayuda a alterar o modificar entidades. Por ejemplo, modificar una tabla agregandole una columna, modificar una columna o cambiando el tipo de datos.

**- Drop**: Nos ayuda a borrar. Hay que tener cuidado al utilizarlo. Al hacer drop podemos borrar una columna, una tabla completa o incluso toda la base de datos.

**3 objetos que manipularemos con el lenguaje DDL:**

- Database o bases de datos
- Table o tablas. Son la traducción a SQL de las entidades
- View o vistas: Se ofrece la proyección de los datos de la base de datos de forma entendible.

![SQL_create_database](src/SQL_create.png)

![SQL_create](src/SQL_create_database.png)

Seleccionamos el schema  como default, de forma gráfica aunque con la terminal seria el use database.

![worckbench_default_schema.png](src/worckbench_default_schema.png)

El comando Create Table

![create_table_slide](src/create_table_slide.png)

El creamos con workbench la tabla anterior, definimos  cada uno de los campos de manera sencilla posterior damos apply

![worckbench_new_table_1.png](src/worckbench_new_table_1.png)

![worckbench_new_table_2_apply.png](src/worckbench_new_table_2_apply.png)

![worckbench_new_table_3.png](src/worckbench_new_table_3.png)

### Clase 21 CREATE VIEW y DDL ALTER

#### Create view

Las vistas lo que hacen es tomar datos de la base de datos, ponerlos en una forma presentable y ponerlo en algo que podamos consultar de manera concurrente. El comando view tiene dos partes principales, la palabra Create View, y el nombre de la vista.
Por convención, cuando es una vista se pone v_ al inicio para dar a entender que es una vista y no una tabla. Luego veremos la sentencia del select

Esta vez tendremos una vista para, por ejemplo, consultar solamente los clientes de brasil.


![workbench_create_view.png](src/workbench_create_view.png)

Para iniciar el ejercicio insertamos datos en la BD,  copiamos la sentencia
`SELECT * FROM platziblog.people;`, nos movemos a views y damos click derecho y create view.

Views ya cuenta con la parte inicial de la sentencia de create view, pegamos debajo el select y damos apply

```mysql
CREATE VIEW 'new_view' AS
SELECT * FROM platziblog.people;
```

![create_view1](src/create_view1.png)

![create_view2](src/create_view2.png)

![create_view3](src/create_view3.png)

![create_view4](src/create_view4.png)

Parece redundante la información, pero podemos estructurar las consultas junto con otras tablas, y estas vistas mantendrán la consulta sin necesidad de acer la de nuevo incrementando los  datos de forma automática.

Podemos hacer una vista que una varias tablas, que muestre por ejemplo gente de cierta zona de México, y estas vistas toman información de la base de datos por lo que irá actualizandose automatícamente a medida que la base de datos crezca.

Una aplicación útil de las vistas es usarlas como una capa de seguridad dentro de las organizaciones. Por ejemplo: una tabla trabajador tiene todos los datos de una persona (numero de identificación, numero telefonico, dirección, y otros datos que pueden ser sensibles), el administrador de la base de datos lo que hace es crear vistas solo con los datos que son relevantes para consultas en las distintas areas de la empresas sin exponer información de mas.

#### Alter Table

Este comando nos va a permitir modificar nuestra tabla. En este caso, queremos añadir una columna que se llame fecha de nacimiento, de tipo fecha o que sea de tipo año.

Para acceder a _Alter table_ damos click derecho en la tabla base.
Alter table nos va a permitir volver a la columna de edición y modificar alguna columna o añadir. Por ejemplo, añadimos la columna date_of_birth


!![alter_table_1](src/alter_table_1.png)

!![alter_table_2](src/alter_table_2.png)

!![alter_table_3](src/alter_table_3.png)

!![alter_table_4](src/alter_table_4.png)

!![alter_table_1](src/alter_table_1.png)


Ya con esto alteramos nuestra tabla. Podeos modificar todos los parámetros de la tabla (cambiar columnas que ya existen)

Vemos que hay una sentencia que dice **DROP**. Eso se utilizará para borrar una columna. Igualmente se ejecuta la sentencia de ALTER TABLE (porque estamos alterando la tabla) y DROP COLUMN


#### Drop Column Borrando una columna

Click derecho a la columna que queremos borrar y damos en  _delete selected_

!![drop_column_1](src/drop_column_1.png)

!![drop_column_1](src/drop_column_2.png)

### Clase 22 DDL drop

Está puede ser la sentencia **más peligrosa** , sobre todo cuando somos principiantes. Básicamente borra o desaparece de nuestra base de datos algún elemento. La sentencia es muy sencilla, es muy fácil de utilizar.

Su estrcutura es solamente DROP TABLE (en este caso que se desea borrar una tabla) y el nombre de la tabla. Eso es suficiente para borrar la tabla o una base de datos (DROP DATABASE)

En el manejador es muy sencillo borar una tabla, basta con dar click derecho en la tabla que queremos borrar.

Pasos para borrar una tabla

![drop_table](src/drop_table.png)

![drop_table_1](src/drop_table_1.png)

![drop_table_2](src/drop_table_2.png)

![drop_table_3](src/drop_table_3.png)

Pasos para borrar la base de datos o schema

![drop_schema_1](src/drop_schema_1.png)

![drop_schema_2](src/drop_schema_2.png)

![drop_schema_3](src/drop_schema_3.png)

![drop_schema_4](src/drop_schema_4.png)



El editor visual al hacer un DROP te avisa y te da la opción de revisar el código para asegurarte de lo que quieres hacer. En código, podrías borrar cosas sin este aviso.

Las sentencias DDL que hemos visto nos ayudaron a manipular, crear, modificar y borrar la estructura de la base de datos. Nos permite crear la base de datos mismas, las vistas que hay, su estructura y todo lo que obedece según lo que hayamos analizado del negocio o empresa. 
Estas sentencias se van a operar muy poco. Por lo general, se utilizan al inicio de un proyecto, mayormente en la fase de construcción, mantenimiento, a veces se añaden columnas.. Luego, se utiliza el otro lenguaje DML.



### Clase 23 DML

A diferencia de DDL, que tiene que ver con formar la estructura de la base de datos (Que se utiliza al inicio del proyecto), DML consiste principalmente en el _contenido_ de la base de datos, se trata de meter, actualizar, borrar, etc.


**DML** trata del contenido de la base de datos. Son las siglas de Data Manipulation Language y sus comandos son:

**- Insert:** Inserta o agrega nuevos registros a la tabla.

**- Update:** Actualiza o modifica los datos que **ya existen**. Cambiara 

**- Delete:** Esta sentencia es riesgosa porque puede borrar el contenido de una tabla.

**- Select:** Trae información de la base de datos.

#### Insert

Crearemos este comando en una BD nueva llamada platzi_test con la con la estructura del ejercicio anterior

Su estructura es poner INSERT  y a donde lo queremos insertar (INTO). **Es importante mantener el orden** tanto de los campos como en los Values, en los valores podemos dejar valores vacios (considerando los Constraints).

![insert_command.png](src/insert_command.png)

En la seccion de query realizamos el comando

```sql
INSERT INTO people(last_name, first_name, address, city)
VALUES ('Hernandez', 'Laura', 'Calle 21', 'Monterrey');
```

Insertamos los valores con el símbolo de rayo o con ctrl + enter

![insert_command_1.png](src/insert_command_1.png)

![insert_command_2.png](src/insert_command_2.png)

#### Update

Update nos va a modificar o actualizar un campo que ya existe. En el comando, SET es lo que indica qué campos va a tener qué valor.Por ejemplo, cambia el campo last_name por 'Chavez' y city por 'Merida'. Sin embargo, aqui no estamos diciendo en cual campo queremos que se haya tal modificacion. Por eso le ponemos el WHERE y estamos especificando el person_id = 1;

En el ultimo update, al no indicarle en qué registro queremos hacerlo, nos dirá que estamos haciendo un _Update inseguro_. La ventaja de utilizar los clientes visuales es que te advierte también y te frena de hacer cambios masivos. Te indica por qué no corrió tu script y te sugiere cambiar la sentencia antes de arrepentirte


![update_command.png](src/update_command.png)

comandos

```sql
UPDATE people SET last_name = 'Chavez', city = 'Merida'
WHERE person_id = 1;
```

![update_command_1.png](src/update_command_1.png)

![update_command_2.png](src/update_command_2.png)

#### Delete

Esta sentencia borra. Hay que tener mucho cuidado, Aqui indicamos con el comando DELETE FROM, en cual tabla queremos borrar y que campo queremos borrar. En este caso, borraremos a la persona con el person_id = 1. 
Si no especificamos el WHERE, y dejamos solamente DELETE FROM people, borrará toda la tabla (no importa lo que encuentres, borra ese registro)

```sql
DELETE FROM people WHERE person_id = 1;
```

![delete__command_1.png](src/delete__command_1.png)

#### Select

Esta sentencia es poderosa y se utiliza mucho. Lo que hace es _traer_ información de la base de datos. Podemos usarla para traer información de un lugar a otro. Por ejemplo, para llamar una tabla, para llamar ciertos campos de varias tablas, etc. Tambien se puede especificar con la sentencia WHERE y se indica, por ejemplo, de cierta fecha para acá o de cierto address.

![select_command.png](src/select_command.png)

```sql
SELECT first_name, last_name FROM people;
```

![select_command_1.png](src/select_command_1.png)



Generalmente antes de ejecutar un **INSERT** es necesario conocer si ya existe el registro mediante un **SELECT** y, en caso de existir, ejecutar en su lugar un **UPDATE**. El comando **REPLACE** nos sirve para realizar esta comprobación directamente, es decir, si el registro existe hace un UPDATE y sino hace un INSERT.





### Clase 24 Que tan standard es SQL

La utilidad más grande de SQL fue unificar la forma en la que pensamos y hacemos preguntas a un repositorio de datos. Ahora que nacen nuevas bases de datos igualmente siguen tomando elementos de SQL.

Practicamos lo anterior como repaso.

```sql
CREATE TABLE people(
person_id int,
last_name VARCHAR(255),
first_name VARCHAR(255),
address VARCHAR(255),
city VARCHAR(255)
);

INSERT INTO people (last_name, first_name, address, city)
VALUES (‘Hernandez’, ‘Laura’, ‘Calle 21’, ‘Monterrey’);
.

SELECT first_name, last_name FROM people;


DROP TABLE people;
```

Realizamos  lo  mismo en una instancia de postgre en Google Cloud 

Tal cual pegamos crear tabla

```sql
CREATE TABLE people(
person_id int,
last_name VARCHAR(255),
first_name VARCHAR(255),
address VARCHAR(255),
city VARCHAR(255)
);
```

revisamos las tablas con

```sql
\dt
```

Hacemos las operaciones anteriores

```sql

INSERT INTO people (last_name, first_name, address, city)
VALUES (‘Hernandez’, ‘Laura’, ‘Calle 21’, ‘Monterrey’);
.

SELECT first_name, last_name FROM people;


DROP TABLE people;
```

El DDL y DML en ambos  motores de bases de datos es estandar. Utilizan el mismo lenguaje pues todos los comandos se ejecutaron igualmente. Solamente cambian las funciones internas (Por ejemplo, mostrar la tabla con \dt). El día a día con DDL y DML es exactamente el mismo.

### Clase 25 Creando Platziblog: tablas independientes


Ahora vamos a pasar nuestro diagrama físico, que hemos estado trabajando, a nuestra base de datos. Crear el diagrama fisico es una buena práctica para la estructuración de la base de datos y siempre se recomienda. 

Vemos que tenemos 5 entidades principales ( y una tabla adicional para la relación N:M de post-etiquetas)

- Una buena práctica es comenzar creando las entidades que no tienen una llave foránea.
- Generalmente en los nombres de bases de datos se evita usar eñes o acentos para evitar problemas en los manejadores de las bases de datos.

Recordeos uqe las llaves Foraneas se suelen poner en las entidades que tienen la relación _Muchos_




![diagrama_fisico_paso_2](src/diagrama_fisico_paso_2.png)

Creamos el schema `platziblog` y seleccionamos como default y creamos las siguientes tablas

- categorías
  
![platziblog_tabla_etiquetas_1](src/platziblog_tabla_caracteristicas_1.png)

![platziblog_tabla_caracteristicas_2](src/platziblog_tabla_caracteristicas_2.png)

Creamos de igual forma la tabla Etiquetas

![platziblog_tabla_etiquetas_1](src/platziblog_tabla_etiquetas_1.png)

![platziblog_tabla_etiquetas_2](src/platziblog_tabla_etiquetas_2.png)

Tabla Usuarios

![platziblog_tabla_usuarios_1.png](src/platziblog_tabla_usuarios_1.png)

![platziblog_tabla_usuarios_2.png](src/platziblog_tabla_usuarios_2.png)

### Clase 26 Creando Platziblog: tablas dependientes

Es importante el orden en el que creamos las tablas. Como vemos, ahora ya podremos creaer las tablas que contienen las llaves foráneas porque aquellas ya existen. Antes, no podríamos hacerlo. El orden en cual crear las tablas tiene mucho que ver con las dependencias que tienen y la relación entre ellas.

El **Check** no es estandar en todos los manejadores. Por eso, lo dejaremos por fuera. Pero siempre que se pueda debería utilizarse para validar los datos

Al crear un Default/Expression asignamos un valor por defecto que funciona, por ejemplo, cuando las cosas se envían nulas.

Cuando queremos añadir una llave foranea debemos tener cuidado de que debe tener los mismos parámetros. por ejemplo, usuario_id foraneo debe ser del mismo tipo y longitud que usuario_id primary.

Creando Platziblog: tablas dependientes


![platziblog_tabla_post_1.png](src/platziblog_tabla_post_1.png)

![platziblog_tabla_post_2.png](src/platziblog_tabla_post_2.png)

Vamos a la pestaña Foreign Key y asignamos las relaciones, porque hasta ahora no hemos indicado que tenemos campos que son llaves foraneas. En esta pestaña tendremos que indicar cual es la tabla de referencia y el campo de nuestra tabla y el campo de la tabla de referencia. Además, nos pide añadir Qué hacer cuando hay un update. Por ejemplo, 
El comando **“cascade”** sirve para que cada que se haga un update en la tabla principal, se refleje también en la tabla en la que estamos creando la relación.

Otro ejemplo seŕia con el comando **Restrict** en delete. Que quiere decir que, cada vez que alguien quiera borrar un usuario que tenga posts, no lo permita porque antes deben borrarse los posts del usuario.

Asignamos la llave foranea del usuario_id

![platziblog_tabla_post_fk_usuario_id.png](src/platziblog_tabla_post_fk_usuario_id.png)

![platziblog_tabla_post_fk_categorias_id.png](src/platziblog_tabla_post_fk_categorias_id.png)

![platziblog_tabla_post_fk_categorias_id_1.png](src/platziblog_tabla_post_fk_categorias_id_1.png)


**Las Foreing Key options son las siguientes:**

**On update**: Significa qué pasará con las relaciones cuando una de estas sea modificada en sus campos relacionados, Por ejemplo, pueden utilizarse los valores:
  * cascade: Si el id de un usuario pasa de 11 a 12, entonces la relacion se actualizará y el post buscará el id nuevo en lugar de quedarse sin usuario.

  * restrict: _Si el id de un usuario pasa de 11 a 12, no lo permitirá hasta que no sean actualizados antes todos los post relacionados.

  * set null Si el id de un usuario pasa de 11 a 12, entonces los post solo no estará relacionados con nada.

  * no action: Si el id de un usuario pasa de 11 a 12, no se hará nada. Solo se romperá la relación.

**On delete**
_ cascade: Si un usuario es eliminado entonces se borrarán todos los post relacionados.
restrict: No se podrá eliminar un usuario hasta que sean eliminados todos su post relacionados.
_ set null: Si un usuario es eliminado, entonces los post solo no estará relacionados con nada.
no action: Si un usuario es eliminado, no se hará nada. Solo se romperá la relación.




### Clase 27 Creando Platziblog: tablas transitivas

- Las tablas transitivas sirven como puente para unir dos tablas. No tienen contenido semántico. Por ejemplo, en nuestras entidades identificamos una relación N:M en la que lo mejor es hacer una tabla transistiva. No tiene información propia, solo sirve para _ligar_

- **Reverse Engineer** nos reproduce el esquema del cual nos basamos para crear nuestras tablas. Es útil cuando llegas a un nuevo trabajo y quieres entender cuál fue la mentalidad que tuvieron al momento de crear las bases de datos.

Creamos la tabla comentarios.

![platziblog_tabla_comentarios.png](src/platziblog_tabla_comentarios.png)

![platziblog_tabla_comentarios_1.png](src/platziblog_tabla_comentarios_1.png)

Creamos las llaves foráneas para los comentarios de los usuarios

![platziblog_tabla_comentarios_usuarios_fk_1.png](src/platziblog_tabla_comentarios_usuarios_fk_1.png)

![platziblog_tabla_comentarios_usuarios_fk_2.png](src/platziblog_tabla_comentarios_usuarios_fk_2.png)

Creamos las llaves foráneas para los comentarios de los posts

![platziblog_tabla_comentarios_usuarios_fk_1.png](src/platziblog_tabla_comentarios_usuarios_fk_1.png)

![platziblog_tabla_comentarios_usuarios_fk_2.png](src/platziblog_tabla_comentarios_usuarios_fk_2.png)

Ahora solo nos queda crear la tabla intermedia para romper la relacion muchos a muchos.

![diagrama_fisico_paso_3_N_N.png](src/diagrama_fisico_paso_3_N_N.png)

Para ello creamos la tabla intermedia post_etiquetas

![platziblog_tabla_post_etiquetas.png](src/platziblog_tabla_post_etiquetas.png)

![platziblog_tabla_post_etiquetas_1.png](src/platziblog_tabla_post_etiquetas_1.png)

Ligamos las llaves foráneas para post_id

![platziblog_tabla_post_etiquetas_fk_1.png](src/platziblog_tabla_post_etiquetas_fk_1.png)

![platziblog_tabla_post_etiquetas_fk_2.png](src/platziblog_tabla_post_etiquetas_fk_2.png)

Ligamos las llaves foráneas para etiquetas_id

![platziblog_tabla_post_etiquetas_etiquetas_fk_1.png](src/platziblog_tabla_post_etiquetas_etiquetas_fk_1.png)

![platziblog_tabla_post_etiquetas_etiquetas_fk_2.png](src/platziblog_tabla_post_etiquetas_etiquetas_fk_2.png)

#### Reverse Engineer

Seleccionamos la opción Database para acceder a reverse engineer
![reverse_engineer_1](src/reverse_engineer_1.png)

![reverse_engineer_2](src/reverse_engineer_2.png)

![reverse_engineer_3](src/reverse_engineer_3.png)

![reverse_engineer_4](src/reverse_engineer_4.png)

![reverse_engineer_5](src/reverse_engineer_5.png)

![reverse_engineer_6](src/reverse_engineer_6.png)

![reverse_engineer_7](src/reverse_engineer_7.png)

### Clase 28 Por qué las consultas son tan importantes

Las consultas o queries a una base de datos son una parte fundamental ya que esto podría salvar un negocio o empresa.
Alrededor de las consultas a las bases de datos se han creado varias especialidades como ETL o transformación de datos, business intelligence e incluso machine learning.

### Clase 29 Estructura básica de un Query

Los queries son la forma en la que estructuramos las preguntas que se harán a la base de datos. Transforma preguntas en sintaxis. 

La estructura de un Query puede ser simple o compleja según se desee consultar a la base de datos.

El query tiene básicamente 2 partes: **SELECT** y **FROM**. Puede aparecer una tercera como **WHERE** pero el mínimo necesario es tener SELECT Y FROM.

La estrellita o asterisco (*) quiere decir que vamos a seleccionar todo sin filtrar campos.

Antes de iniciar la clase corre este script para rellenar tu base de datos.

Un ejemplo de un Query con su estructura seria: 

```sql
SELECT city, count(*) AS total
FROM people
WHERE active = true
GROUP BY city
ORDER BY total DESC
HAVING total >=2;
```

Aqui tenemos una consulta que nos buscara de personas, aquellas que tengan active = true, agrupados por ciudad y ordenados de forma descendente. Filtrando aquellas ciudades que tengan mas de dos personas


```sql
Script de la base datos platziblog

--creamos la base datos :platziblog

-- nos ubicamos en la base datos  platziblog
use platziblog;

-- CREACIONES DE TABLAS
-- Eliminacion de tablas, va en ese orden por los FK
 drop table comentarios;
 drop table posts_etiquetas;
 drop table posts;
 drop table etiquetas;
 drop table usuarios;
 drop table categorias;


-- CREACIONES DE TABLAS
-- Creación de la tabla usuarios
CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(30) NOT NULL,
  `password` varchar(32) NOT NULL,
  `nickname` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY`email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


-- Creación de la tabla categorias
CREATE TABLE `categorias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_categoria`varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


-- Creación de la tabla etiquetas
CREATE TABLE`etiquetas` (
  `id`int(11) NOT NULL AUTO_INCREMENT,
  `nombre_etiqueta`varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


-- Creación de la tabla posts
CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(130) NOT NULL,
  `fecha_publicacion` timestamp NULL DEFAULT NULL,
  `contenido` text NOT NULL,
  `estatus` char(8) DEFAULT 'activo',
  `usuario_id` int(11) DEFAULT NULL,
  `categoria_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `posts_usuarios_idx` (`usuario_id`),
  KEY `posts_categorias_idx` (`categoria_id`),
  CONSTRAINT `posts_categorias` FOREIGN KEY (`categoria_id`) REFERENCES `categorias` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `posts_usuarios` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- Creación de la tabla comentarios
CREATE TABLE `comentarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cuerpo_comentario` text NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `post_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `comentarios_usuario_idx` (`usuario_id`),
  KEY `comentarios_post_idx` (`post_id`),
  CONSTRAINT `comentarios_post` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `comentarios_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Creación de la tabla posts_etiquetas
CREATE TABLE `posts_etiquetas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` int(11) NOT NULL,
  `etiqueta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `postsetiquetas_post_idx` (`post_id`),
  KEY `postsetiquetas_etiquetas_idx` (`etiqueta_id`),
  CONSTRAINT `postsetiquetas_etiquetas` FOREIGN KEY (`etiqueta_id`) REFERENCES `etiquetas` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `postsetiquetas_post` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


-- INSERCIÓN DE VALORES A LAS TABLAS
-- Insert  en la tabla usuarios
INSERT INTO usuarios (login,password,nickname,email) VALUES ('israel','1234','israel','israel@platziblog.com');
INSERT INTO usuarios (login,password,nickname,email) VALUES ('monica','1234','Moni','monica@platziblog.com');
INSERT INTO usuarios (login,password,nickname,email) VALUES ('laura','1234','Lau','laura@platziblog.com');
INSERT INTO usuarios (login,password,nickname,email) VALUES ('edgar','5678','Ed','edgar@platziblog.com');
INSERT INTO usuarios (login,password,nickname,email) VALUES ('perezoso','5678','Oso Pérez','perezoso@platziblog.com');

-- Insert  en la tabla categorias
INSERT INTO categorias (nombre_categoria) VALUES ('Ciencia');
INSERT INTO categorias (nombre_categoria) VALUES ('Tecnología');
INSERT INTO categorias (nombre_categoria) VALUES ('Deportes');
INSERT INTO categorias (nombre_categoria) VALUES ('Espectáculos');
INSERT INTO categorias (nombre_categoria) VALUES ('Economía');

-- Insert  en la tabla etiquetas
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Robótica');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Computación');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Teléfonos Móviles');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Automovilismo');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Campeonatos');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Equipos');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Bolsa de valores');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Inversiones');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Brokers');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Celebridades');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Eventos');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Moda');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Avances');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Nobel');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Matemáticas');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Química');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Física');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Largo plazo');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Bienes Raíces');
INSERT INTO etiquetas (nombre_etiqueta) VALUES ('Estilo');

-- Insert  en la tabla posts
INSERT INTO posts (id, titulo, fecha_publicacion, contenido, estatus, usuario_id, categoria_id)
   VALUES (1,'Se presenta el nuevo teléfono móvil en evento', '2030-04-05 00:00:00', 'Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.',  'activo', 1, 1);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Tenemos un nuevo auto inteligepostsnte','2025-05-04 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.','activo',2,2);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Ganador del premio Nobel por trabajo en genética','2023-12-22 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.','activo',3,3);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Los mejores vestidos en la alfombra roja','2021-12-22 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.','activo',4,4);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Los paparatzi captan escándalo en cámara','2025-01-09 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.','inactivo',4,5);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Se mejora la conducción autónoma de vehículos','2022-05-23 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.','activo',1,5);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Se descubre nueva partícula del modelo estandar','2023-01-10 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.','activo',2,4);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Químicos descubren nanomaterial','2026-06-04 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.','activo',2,3);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('La bolsa cae estrepitosamente','2024-04-03 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.','activo',2,2);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Bienes raices más baratos que nunca','2025-04-11 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.','inactivo',2,1);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Se fortalece el peso frente al dolar','2021-10-09 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.','activo',1,1);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Tenemos ganador de la formula e','2022-11-11 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.','activo',1,2);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Ganan partido frente a visitantes','2023-12-10 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.','activo',2,3);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Equipo veterano da un gran espectaculo','2023-12-01 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.','inactivo',2,4);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Escándalo con el boxeador del momento','2025-03-05 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.','activo',4,5);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Fuccia OS sacude al mundo','2028-10-10 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.','activo',1,5);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('U.S. Robotics presenta hallazgo','2029-01-10 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.\n','activo',1,4);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Cierra campeonato mundial de football de manera impresionante','2023-04-10 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.\n','activo',2,3);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Escándalo en el mundo de la moda','2022-04-11 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.\n','activo',4,2);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Tenemos campeona del mundial de volleiball','2024-09-09 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.\n','inactivo',2,1);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('Se descubre la unión entre astrofísica y fisica cuántica','2022-05-03 00:00:00','Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.\n','inactivo',3,5);
INSERT INTO posts (titulo,fecha_publicacion,contenido,estatus,usuario_id,categoria_id)
  VALUES ('El post que se quedó huérfano','2029-08-08 00:00:00','\'Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna.\n\'','activo',2,3);

-- Insert  en la tabla posts_etiquetas
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (1,43,3);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (2,43,11);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (3,44,2);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (4,44,4);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (5,45,14);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (6,45,13);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (7,46,10);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (8,46,11);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (9,46,12);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (10,46,20);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (11,47,10);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (12,48,1);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (13,48,2);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (14,48,4);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (15,48,13);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (16,49,13);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (17,49,14);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (18,49,17);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (19,50,13);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (20,50,14);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (21,50,16);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (22,51,7);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (23,51,8);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (24,51,9);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (25,51,18);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (26,52,8);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (27,52,18);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (28,53,7);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (29,53,8);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (30,54,4);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (31,54,5);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (32,55,5);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (33,55,6);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (34,56,5);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (35,56,6);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (36,56,10);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (37,58,2);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (38,58,3);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (39,58,13);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (40,59,1);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (41,59,13);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (42,57,10);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (43,60,5);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (44,60,6);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (45,61,10);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (46,61,12);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (47,61,20);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (48,62,5);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (49,62,10);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (50,63,13);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (51,63,14);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (52,63,17);
INSERT INTO `platziblog.posts_etiquetas` (`id`,`post_id`,`etiqueta_id`) VALUES (53,52,19);

```

#### Primer Consulta

```sql
SELECT * 
FROM platziblog.posts
WHERE fecha_publicacion < '2024';
```

### Clase 30 SELECT

**SELECT** se encarga de proyectar o mostrar datos.

- El nombre de las columnas o campos que estamos consultando puede ser cambiado utilizando AS después del nombre del campo y poniendo el nuevo que queremos tener:


El **SELECT** (*) es utilizado para mostrar todo. Una sentencia SELECT no puede estar sola, necesita tambien el FROM para indicar donde realizar la consulta.


Cuando utilizamos SELECT con AS lo que hacemos es renombrar la consulta que estamos trabajando. Por ejemplo, a continuación si queremos referirnos a titulo en esta consulta sería a través de 'encabezado'

```sql
SELECT titulo AS encabezado
FROM platziblog.posts;
```

Existe una función de SELECT para poder contar la cantidad de registros. Esa información (un número) será el resultado del query:

```sql
SELECT COUNT(*)
FROM platziblog.posts;
```

Podemos hacer querys con solo determinados campos ( no todo, con el * ), por ejemplo, consultaremos titulo, fecha de publicacion y estatus.

```sql

SELECT titulo, fecha_publicacion, estatus
FROM platziblog.posts
```



Usando AS para asignar un alias. Si hacemos esto podemos jugar con el nombre de las columas y cambiarlos en la consulta. Notamos como AS se agrega antes de la coma.

Entonces, en Querys mas complejos, podemos referirnos a estas columas mediante los alias.

```sql
SELECT titulo, fecha_publicacion AS publicado_en, estatus  AS estado
FROM platziblog.posts;
```

Contar los registros. Aqui con COUNT(*) nos retornara un conteo final. COUNT va tupla por tupla por todos los registros y muestra el numero final de registros, por ejemplo, 22. 

Tambien puede añadirse un alias

```sql
SELECT COUNT(*) AS numero_post
FROM platziblog.posts;
```

```sql
SELECT COUNT(*) AS total_registros
FROM platziblog.posts
WHERE estatus = 'activo';
```



### Clase 31 FROM

**FROM** indica de dónde se deben traer los datos. Puede mostrar informacion de una tabla pero tambien da la posibildiad de mostrar informacion proveniente de distintas tablas. Por ejemplo, vemos que en nuestra base de datos la informacion esta repartida en distintas tablas para mantener la normalización, pero **FROM** puede ayudar a hacer sentencias y filtros complejos cuando se quieren unir tablas. La sentencia compañera que nos ayuda con este proceso es **JOIN**.

Los diagramas de Venn son círculos que se tocan en algún punto para ver dónde está la intersección de conjuntos. Ayudan mucho para poder formular la sentencia **JOIN** de la manera adecuada dependiendo del query que se quiere hacer.

![teoria_conjuntos](src/Teoria_conjuntos.jpg)

![teoria_conjuntos_sentencias](src/teoria_conjuntos_sentencias.jpg)


Otro tipo de JOIN serian:

* Interseccion / INNER JOIN: Es el mas comun. Tiene que ver con traer los valores que existen tanto en A como en B

* UNION/ FULL OUTER JOIN : Traer todo. No importa si el usuario tiene o no posts, si el posts tiene o no usuario.

*Diferencia simetrica/ FULL OUTER JOIN: Es una union - Interseccion. Trae los datos que esten en A que no esten en B y los datos de B que no esten en A


### Clase 32 Utilizando la sentencia FROM

Comandos de la clase

**Left Join**

Trae todos los usuarios (tabla A), tengan o no tengan algún Post (tabla b)

```sql
SELECT *
FROM usuarios
 LEFT JOIN posts ON usuarios.id = posts.usuario_id;
```

Aqui como vemos se tomo un LEFT JOIN que tomara la tabla de la izquierda (la primera que pasamos) como tabla A. Entonces, hara un LEFT JOIN a partir de los ids de ambas tablas (Sentencia **ON**). Selecciona todo de la tabla usuario y unela con la tabla posts a partir de sus llaves.

Con este query podemos saber cuales posts escribieron cuales usuarios.

**Left Join sin intersección**

```sql
SELECT *
FROM usuarios
  LEFT JOIN posts ON usuarios.id = posts.usuario_id
WHERE posts.usuario_id IS NULL;
```

Con este Query lo que hacemos es sacar a los usuarios que si tienen posts. Por lo tanto, solamente estamos pidiendo los usuarios que no hayan publicado un posts.


Left Join  trae todos los Post (tabla B), tengan o no tengan algún Usuario (tabla A)


Ahora apliquemos el Right Join, es decir, antes habiamos pensando en usuarios que tienen posts, ahora pensaremos en posts que tienen usuarios.

```sql
SELECT *
FROM usuarios
 RIGHT JOIN posts ON usuarios.id = posts.usuario_id;
```
Por ejemplo, esta consulta vemos que nos trajo tambien un posts huerfano que no tienen usuario y los usuarios de los post.


**Right Join sin intersección**

Esta vez vamos a exluir a los usuarios. Es decir, esta consulta me retornara los posts que no tienen usuario.

```sql
SELECT *
FROM usuarios
 RIGHT JOIN posts ON usuarios.id = posts.usuario_id
WHERE posts.usuario_id IS NULL;
```


**Inner Join**

Esta vez queremos las intersecciones. Solamente me importan los datos que estan relacionados (usuarios que tengan posts)


```sql
SELECT *
FROM usuarios
 INNER JOIN posts ON usuarios.id = posts.usuario_id;
```

**Full Join**

Hay manejadores que tienen y no tienen comandos para diferenciar un FULL JOIN y una Diferencia asimetrica. Hay manejadores que tienen un comando FULL OUTER JOIN, pero no es el caso de MYSQL


Esta vez haremos un query un poco mas complejo pero estandar. Haremos una union de todos los usuarios qe tengan posts y luego agarraremos los posts que faltan. Si vemos nuestros diagramas, estariamos tomando todo el conjunto

```sql
SELECT *
FROM usuarios
 LEFT JOIN posts ON usuarios.id = posts.usuario_id
UNION
SELECT *
FROM usuarios
 RIGHT JOIN posts ON usuarios.id = posts.usuario_id;
```

La primera sentencia nos esta trayendo todos los usuarios que tienen posts y la segunda todos los posts que tienen usuario. Estas unidas, nos estarian trayendo todos los usuarios y todos los posts asociados por un id (incluso posts sin usuarios o usuarios sin posts)


Diferencia Asimétrica

Esta vez queremos traer los usuarios sin posts y los posts sin usuarios.

Para esto tendremos que excluir con WHERE y NULL.

```sql
SELECT *
FROM usuarios
 LEFT JOIN posts ON usuarios.id = posts.usuario_id
WHERE posts.usuario_id IS NULL
UNION
SELECT *
FROM usuarios
 RIGHT JOIN posts ON usuarios.id = posts.usuario_id
WHERE posts.usuario_id IS NULL;
```

Asi como en estos ejemplos juntamos dos tablas, podemos traer más y hacer el Query con el FROM tan complejo como se quiera. 


### Clase 33 WHERE

**WHERE** es la sentencia que nos ayuda a filtrar tuplas o registros dependiendo de las características que elegimos.
Esta vez filtramos por columnas. Podemos usarla para filtrar de acuerdo a criterios como una fecha, una cantidad, etc.

- La propiedad **LIKE** nos ayuda a traer registros de los cuales conocemos sólo una parte de la información.
- La propiedad **BETWEEN** nos sirve para arrojar registros que estén en el medio de dos. Por ejemplo los registros con id entre 20 y 30

Queries de la clase

**Filtrando de forma numérica**

Podemos filtrar por ejemplo, que retorne los posts con id >= que 50
```sql
SELECT *
FROM posts
WHERE id <= 50 ;
```

**Filtrando con strings**

El operador = funciona excelente con cadena cuando sabes lo que puede decir. Por ejemplo, el campus estatus tiene dos opciones: activo o inactivo. Podemos hacer un Query con esto. Tambien podriamos utilizar no igual ( != ). Puedes usar los operadores relacionales tranquilamente.
```sql
SELECT *
FROM posts
WHERE estatus = 'activo' ;
```


```sql
SELECT *
FROM posts
WHERE estatus != 'activo' ;
```

Utilizando LIKE % es un wildcard
Por ejemplo, si no conocemos la cadena exacta podriamos utilizar los titulos por alguna caracteristica. El % implica 'lo que sea'. Por ejemplo, selecciona de los posts donde el titulo tenga lo que sea antes y despues de escandalo (parecido a escandalo) 
```sql
-- todos los post con la palabra
SELECT *
FROM posts
WHERE titulo LIKE '%escandalo%' ;
```

Podriamos, por ejemplo, pedir los titulos que comiencen con la palabra escandalo

```sql
-- todos los post que inicien con la palabra
SELECT *
FROM posts
WHERE titulo LIKE 'escandalo%' ;
```

```sql
-- todos los post que terminen con la palabra
SELECT *
FROM posts
WHERE titulo LIKE '%roja' ;
```

**Usando WHERE con fechas**

Con  las fechas podriamos jugar, por ejemplo, a consultar los posts que se hicieron antes o despues de cierto dia.

```sql
SELECT *
FROM posts
WHERE fecha_publicacion > "2025-01-01";
```

```sql
SELECT *
FROM posts
WHERE fecha_publicacion < "2025-01-01";
```

Usando BETWEEN para  definir un rangos

Con esto podemos definir rangos para poder consultar informacion que se encuentre entre dos valores.

```sql
SELECT *
FROM posts
WHERE fecha_publicacion BETWEEN "2025-01-01" AND "2025-12-31";
```

Esto es valido para rangos de cualqueir tipo, no solamente fechas. Por ejemplo, filtremos los posts por ids

```sql
SELECT *
FROM posts
WHERE id BETWEEN 55 AND 62;
```

Otros filtros con fechas

Hasta ahora hemos estado trayendo la fecha completa. Sin embargo, podemos manipular esto un poco. Por ejemplo podemos usar solamente el año. Debido a que la informacion aqui es de tipo DATETIME, sql reconoce cual es el año.

```sql
SELECT *
FROM posts
WHERE YEAR(fecha_publicacion) BETWEEN "2023" AND "2024";
```

```sql
SELECT *
FROM posts
WHERE MONTH(fecha_publicacion) = "04";
```

### Clase 34 Utilizando la sentencia WHERE nulo y no nulo

El valor nulo en una tabla generalmente es su valor por defecto cuando nadie le asignó algo diferente. La sintaxis para hacer búsquedas de datos nulos es **IS NULL**. La sintaxis para buscar datos que no son nulos es **IS NOT NULL** Podriamos considerar estos valores nulos y no nulos como un tipo de dato particular y forma parte de la sintaxis de SQL.

Para posts sin usuario

```sql
SELECT *
FROM posts
WHERE usuario_id IS NULL;
;
```

Para posts con usuario

```sql
SELECT *
FROM posts
WHERE usuario_id IS NOT NULL;
;
```

Para posts con usuario y activo, el uso de AND agrega condiciones de tipo filtro como usar excel. Por ejemplo, podriamos traer los usuarios no nulos pero que tengan estatus activo (y otros parametros)

```sql
SELECT *
FROM posts
WHERE usuario_id IS NOT NULL
	AND estatus ='activo'
    AND id < 50
    AND categoria_id = 2
 	AND YEAR(fecha_publicacion) = '2025'
;

```

### Clase 35 GROUP BY

**GROUP BY** tiene que ver con agrupación. Indica a la base de datos qué criterios debe tener en cuenta para agrupar. Por ejemplo, puedes agrupar registros por pais, o por año, por ejemplo.

Gruop by te permite agrupar estilo pivot tables, e informes.

En el siguiente ejemplo, vamos a seleccionar nuestra estatus de post, vamos a contar y agruparlos por estatus. De esta forma podremos obtener cuantos posts tenemos activos e inactivos. Entonces, nos agrupo nuestros posts activos e inactivos, los sumo y nos lo dio como resultado. Asi como podeos hacer COUNT() podriamos hacer SUM().

En los trabajos suelen pedir cifras finales. En estos casos sirve mucho GROUP 

```sql
SELECT estatus, COUNT(*) AS post_quantity
FROM posts
GROUP BY estatus
;
```

Ejemplo 2 Agrupando por Año

Vamos a agrupar todos los post por año y vamos a contarlos. Esta consulta nos dira cuantos posts se hicieron por año,

```sql
SELECT YEAR(fecha_publicacion) AS post_year, COUNT(*) AS post_quantity
FROM posts
GROUP BY post_year
;
```

Ejemplo 3 Agrupando por Mes

Esta vez no nos importa el año. Queremos saber por ejemplo cuantas publicaciones suelen hacerse por mes.

```sql
SELECT MONTHNAME(fecha_publicacion) AS post_month, COUNT(*) AS post_quantity
FROM posts
GROUP BY post_month
;
```

Ejemplo 4 Agrupando por Mes y estatus

En esta consulta vamos a obtener la cantidad de activos e inactivos de cada mes

```sql
SELECT estatus, MONTHNAME(fecha_publicacion) AS post_month, COUNT(*) AS post_quantity
FROM posts
GROUP BY estatus, post_month 
;
```

### Clase 36 ORDER BY y HAVING

La sentencia **ORDER BY** tiene que ver con el ordenamiento de los datos dependiendo de los criterios que quieras usar.

Por ejemplo, puedes usar los sigueitnes criterios:

- **ASC** sirve para ordenar de forma ascendente.
- **DESC** sirve para ordenar de forma descendente.
- **LIMIT** se usa para limitar la cantidad de resultados que arroja el query.
- **HAVING** tiene una similitud muy grande con **WHERE**, sin embargo el uso de ellos depende del orden. Cuando se quiere seleccionar tuplas agrupadas únicamente se puede hacer con **HAVING**.


Tenemos nuestros datos ordenados por defecto segun como los fuimos incluyendo a la tabla (por el id). Sin embargo, suponiendo que queremos ordenarlos de distinta manera podriamos aplicar los siguientes querys: 

Ejemplo Order by ascendente default

Por defecto podemos ordenarlo de manera ascendente sin hacerlo explicito.
```sql
SELECT *
FROM posts
ORDER BY fecha_publicacion
;
```

Ejemplo Order by ascendente explicito

```sql
SELECT *
FROM posts
ORDER BY fecha_publicacion ASC
;
```

Ejemplo Order by descendente

```sql
SELECT *
FROM posts
ORDER BY fecha_publicacion DESC
;
```

Ordenando con strings se toma el orden alfabetico.
Podemos ordenar por string tanto de forma ascendente como descendente.

```sql
SELECT *
FROM posts
ORDER BY titulo ASC
;
```

Ejemplo Order by ascendente explicito y limite de 5 registros
Esta sentencia puede ser un complemento. La sentencia LIMIT podriamos usarla para limitar los primeros 5 resultados, por ejemplo. Esto funciona si no quiero traer todos los posts. Al consultar ordenando por orden ascendente y con LIMIT podriamos tener los primeros 5 posts que se publicaron.

```sql
SELECT *
FROM posts
ORDER BY fecha_publicacion ASC
LIMIT 5
;
```

**HAVING** es similar a **WHERE** aunque no muy utilizada, pero es necesaria cuando quieres hacer un filtro con datos agrupados por un ORDER BY.
 **HAVING** siempre va despues del **GROUP BY** cuando queremos hacer una consulta de seleccion de tuplas agrupados.

 Es decir, si quisieramos ejecutar el siguiente script: 

```sql
SELECT MONTHNAME(fecha_publicacion) AS post_month, estatus, COUNT(*) AS post_quantity
FROM posts
WHERE post_quantity > 1
GROUP BY estatus, post_month
ORDER BY post_month
;
```
Tendriamos problemas. Nos daría un error. En esta consulta la intencion seria contar los posts de cada mes segun su estatus (post activos e inactivos de enero, por ejemplo). Ordenarlos segun su estatos y el mes de manera ascendente por defecto.

Sin embargo, al ejecutarse vemos que nos dice que no conoce la columna post_quantity. Esto es porque esta columna existirá luego de haber hecho la agrupacion. El where al consultarla antes no sabe que existe. Para estos casos podemos usar HAVING para decir que queremos agruparlos pero solamente los meses con mas de un post.

 Por ejemplo,

```sql
SELECT MONTHNAME(fecha_publicacion) AS post_month, estatus, COUNT(*) AS post_quantity
FROM posts
GROUP BY estatus, post_month
HAVING post_quantity > 1
ORDER BY post_month
;
```

HAVING y WHERE tienen muchas similitudes y con sintaxis similar pero nos ayuda cuando queremos hacer consultas mas dinamicas.


Ya en este punto tenemos todas las herramientas para hacer querys complejos. 

### Clase 37 El interminable agujero de conejo (Nested queries)

Los **Nested queries** significan que dentro de un query podemos hacer otro query. Esto sirve para hacer join de tablas, estando una en memoria. También teniendo un query como condicional del otro.

Este proceso puede ser tan profundo como quieras, teniendo infinitos queries anidados.
Se le conoce como un *producto cartesiano* ya que se multiplican todos los registros de una tabla con todos los del nuevo query. Esto provoca que el query sea difícil de procesar por lo pesado que puede resultar, y se considera como no escalable.

Debemos utilizarlo en Querys que sepamos que no van a estar creciendo constantemente.

Ejemplo 1
En este ejemplo estamos seleccionando una tabla que aun no existe si no que es resultado de un query. Luego, eso estara agrupado y ordenado

```sql
SELECT new_table_projection.date, COUNT(*) AS posts_count
FROM (
SELECT DATE(MIN(fecha_publicacion)) AS date, year(fecha_publicacion) AS post_year
FROM posts
GROUP BY post_year
) AS new_table_projection
GROUP BY new_table_projection.date
ORDER BY new_table_projection.date
```

Ejemplo 2

Esta vez haremos un ejemplo pero tomando una fecha MAX.

```sql
SELECT *
FROM posts
WHERE fecha_publicacion = (
SELECT MAX(fecha_publicacion)
FROM posts
);
```

### Clase 38 Como convertir una pregunta en un query SQL

Esto no siempre es una transformacion directa. Muchas de las sutilezas se van adquiriendo al ir enfrentandose a retos segun se vayan presentando. Por eso es importante tener proyectos personales de temas que te interesen para ir tomando temas y responder preguntas.

Veremos a que equivale aproximadamente cada sentencia del Query

#### De pregunta a Query

- **SELECT:** Lo que quieres mostrar. En cuanto a qué datos y que informacion nos conviene presentar al usuario.

- **FROM:** De dónde voy a tomar los datos (tablas unicas o con joins). 

- **WHERE:** Los filtros de los datos que quieres mostrar. No quiero toda la informacion, solo cierta informacion relevante y por eso debo aplicar algunos grupos.

- **GROUP BY:** Los rubros por los que me interesa agrupar la información. Por cuales grupos quiero seleccionar la informacion? por nombre de equipo, por torneo, por caratula, reloj digital o analogico, por cualquier campo que nos interese mostrar o para sacar conteos o sumas.

- **ORDER BY:** El orden en que quiero presentar mi información. Me interesa ordenarlos por las fechas? Mostrar los 10 primeros? hay algun top que me interese mostrar?

- **HAVING:** Los filtros que quiero que mis datos agrupados tengan. Quiero filtrar nuevamente pero una vez que ya los tengo agrupados, que ya sume, por ejemplo.



### Clase 39 Preguntandole a la base de datos

Tomemos algunas preguntas para hacerle a nuestras bases de datos con la estructura que ya hemos trabajado.


**GROUP_CONCAT** toma el resultado del query y lo pone como campo separado por comas.

Criterios.

**DISTINCT:** Evita duplicidad en los valores.
**ORDER BY:** Sirve para decidir el orden de concatenación del campo.
**:** Es el separador a utilizar para separar los valores (por defecto, el separador es una coma “,”).

**Preguna 1 Cuantas etiquetas estan ligadas a los blogposts**

```sql
SELECT posts.titulo, COUNT(*) num_etiquetas
FROM posts
 INNER JOIN posts_etiquetas ON posts.id = posts_etiquetas.post_id
 INNER JOIN etiquetas ON etiquetas.id = posts_etiquetas.etiqueta_id
GROUP BY posts.id
ORDER BY num_etiquetas DESC
;
```

Usando GROUP_CONCAT para tener campos separados por comas. Por ejemplo podemos tener el nombre del posts y las etiquetas separadas por comas que le corresponden

```sql
SELECT posts.titulo, GROUP_CONCAT(nombre_etiqueta)
FROM posts
 INNER JOIN posts_etiquetas ON posts.id = posts_etiquetas.post_id
 INNER JOIN etiquetas ON etiquetas.id = posts_etiquetas.etiqueta_id
GROUP BY posts.id
;
```

![GROUP_CONCAT](src/GROUP_CONCAT.png)

Si ahora queremos saber que posts no tienen etiquetas podriamos aplicar el siguiente Query:

```sql
SELECT *
FROM etiquetas
 LEFT JOIN posts_etiquetas ON etiquetas.id = posts_etiquetas.etiqueta_id
WHERE posts_etiquetas.etiqueta_id IS NULL
;
```

Tambien podriamos hacer una variante para consultar cual etiqueta aun no tiene post.

### Clase 40 Consultando PlatziBlog

Puedes usar una abreviación para evitar escribir lo mismo cada vez.
Ejemplo:

FROM categorias AS c

Pregunta: Que categoria tiene mas posts escritos

```sql
SELECT c.nombre_categoria, COUNT(*) AS cant_posts
FROM categorias AS c
 INNER JOIN posts AS p ON c.id = p.categoria_id
GROUP BY c.id
ORDER BY cant_posts DESC
LIMIT 1
;
```

Pregunta: Que persona tiene mas posts escritos

```sql
SELECT u.nickname, COUNT(*) AS cant_posts
FROM usuarios AS u
 INNER JOIN posts AS p ON u.id = p.usuario_id
GROUP BY u.id
ORDER BY cant_posts DESC
;
```

```sql
SELECT u.nickname, COUNT(*) AS cant_posts, GROUP_CONCAT(nombre_categoria)
FROM usuarios AS u
 INNER JOIN posts AS p ON u.id = p.usuario_id
 INNER JOIN categorias AS c ON c.id = p.categoria_id
GROUP BY u.id
ORDER BY cant_posts DESC
;
```

Que usuarios no han escrito nada

```sql
SELECT *
FROM usuarios
  LEFT JOIN posts ON usuarios.id = posts.usuario_id 
WHERE posts.usuario_id IS NULL
;
```

## Modulo 4 Introduccion a la bases de datos NO relacionales

### Clase 41 Que son y cuales son los tipos de bases de datos no relacionales

Respecto a las bases de datos no relacionales, no existe un solo tipo aunque se engloben en una sola categoría.

#### Tipos de bases de datos no relacionales:

- **Clave - valor:** Son ideales para almacenar y extraer datos con una clave única. Manejan los diccionarios de manera excepcional. Ejemplos: **DynamoDB, Cassandra**. Es muy rapido hacer consultas porque utilizan una busqueda por Hash pero es necesario tener las claves. Hacer queries mas complicados puede traer ciertos problemas. 
- **Basadas en documentos:** Son una implementación de clave valor que varía en la forma semiestructurada en que se trata la información. Ideal para almacenar datos JSON y XML. Ejemplos: **MongoDB, Firestore**. Por ejemplo, podrias utilizarlo para almacenar la imagen viva de una aplicacion web y extraerla rapidamente (por ejemplo, el estado de un jugador en cierto juego.)
- **Basadas en grafos:** Basadas en teoría de grafos, sirven para entidades que se encuentran interconectadas por múltiples relaciones. Ideales para almacenar relaciones complejas. Ejemplos: **neo4j, TITAN**. Es muy utilizada para hacer redes neuronales por las relaciones complejas que pueden existir. Podria hacerse la analogia a las entidades y sus relaciones pero a otro nivel, muchas veces todas conectadas entre todas.
- **En memoria:** Pueden ser de estructura variada, pero su ventaja radica en la velocidad, ya que al vivir en memoria la extracción de datos es casi inmediata. Ejemplos: **Memcached, Redis**. Sin embargo, son volatiles. Si las manejas en un servidor y este se reinicia probablemente tengas que indexar de nuevo. Hay que trabajar en ir almacenando la informacion en memoria de mas duracion (De memoria principal a disco duro)
- **Optimizadas para búsquedas:** Pueden ser de diversas estructuras, su ventaja radica en que se pueden hacer queries y búsquedas complejas de manera sencilla. Ejemplos: **BigQuery, Elasticsearch**. Estan pensadas para hacer Queries muy rapidos. Se utilizan mucho en BussinessIntelligence. Incluso en modelos de machine learning

Cada base de datos de este tipo surgen para responder a problemas en los que las bases de datos relacionales podian presentar fallos. Sin embargo, puedes aplicar las bases de datos relacionales a multiples problemas. Estas bases no relacionales tienen funciones más especificas pero resuelven de forma excelenete los problemas para los que estan diseñadas.

### Clase 42 Servicios administrados y jerarquía de datos

**Firebase** es un servicio de Google donde puedes tercerizar muchos elementos en la nube. Es muy útil para mantener el estado de una aplicacion web o android, por ejemplo. 


Un aspecto importante es que ya en este tipo de bases de datos cambia la jerarquía. No funciona con tablas como la relacionales.

**Jerarquía de datos**:


**1. Base de Datos:** Contiene toda la información que se quiere guardar.

**2. Colección:** Es igual a las tablas en las bases de datos relacionales. Son objetos que agrupan (Documentos) la información que se desea guardar.

**3. Documento:** Es la información que se quiere guardar. Se guarda en un formato muy parecido al formato JSON (es un lenguaje que se utiliza para comunicarse con diferentes lenguajes o aplicaciones). Los documentos dentro de ellos contienen datos.

![jerarquia_firestore](src/jerarquia_firestore.png)

## Modulo 5 Manejo de modelos de datos en bases de datos no relacionales

### Clase 43 Top level collection con Firebase

El modelo de bases de datos no relacionales es un poco más cercano al mundo real en su comportamiento.

- Las top level collections son las colecciones que se tienen de inmediato o entrada en el proyecto. A nivel de "raiz". Puedes crear una coleccion, que tendra ciertos documentos.
- **Firebase** es un servicio que tiene múltiples opciones y está pensado principalmente para aplicaciones móviles y web.

Para esta clase creamos una bd en firebase <https://console.firebase.google.com/u/0/?pli=1>

Para consultar la documentacion oficial podemos ir a: 
https://firebase.google.com/docs

Seguimos  los pasos sencillos de la pagina para crear nuestra base de datos "platziblog"

Creamos proyecto

![firebase_intro_1](src/firebase_intro_1.png)

![firebase_intro_2](src/firebase_intro_2.png)

![firebase_intro_3](src/firebase_intro_3.png)

Panel Inicial

![firebase_intro_4](src/firebase_intro_4.png)

Para crear una Top level collection (las que estan a nivel de la ruta principal) damos en simbolo plus, y creamos /people

![firebase_intro_5](src/firebase_intro_5.png)

![firebase_intro_6](src/firebase_intro_6.png)

![firebase_intro_7](src/firebase_intro_7.png)

### Clase 44 Creando y borrando documentos en Firestore

Jugamos con la interface observamos los tipos de datos que podemos crear en los documentos:

    - String: Cualquier tipo de valor alfanumérico

    - Number: Soporta enteros y flotantes.

    - Boolenan: Los clásicos valores True y False

    - Map: Permite agregar un documento dentro de otro.

    - Array: Permite agregar un conjunto de datos (soporte multi type) sin nombre e identificador.

    - Null: Indica que no se ha definido un valor.

    - Timestamp: Permite almacenar fechas (guarda el año, mes, día y hora).

    - Geopoint: Guarda una localización geográfica (coordenadas latitud-longitud).

    - Reference: Permite referencia un documento (relaciona dos documentos, no importa su colección).


Ejemplos

![firebase_tipos_datos_1](src/firebase_tipos_datos_1.png)

![firebase_tipos_datos_2](src/firebase_tipos_datos_2.png)

![firebase_tipos_datos_3](src/firebase_tipos_datos_3.png)

![firebase_tipos_datos_4](src/firebase_tipos_datos_4.png)



Las bases de datos no relacionales presentan una ventaja respecto a las relacionales. En las relacionales es necesario esquematizar y pensar en las entidades y sus relaciones. Aquí vemos, por ejemplo, que firestone nos permite crear documentos sin esa rigidez. Podriamos crear un post con fecha de publicacion y otro sin fecha de publicacion. Sin embargo, esa flexibilidad puede traer como consecuencia que, al momento de realizar una consulta y pedir que ordene los posts por fecha de publicacion, pueden haber documentos que no tengan los campos requeridos.

Es cuestión de plantearse las necesitades del proyecto.

### Clase 45 Colecciones vs subcolecciones

La particularidad de las top level collections es que existen en el primer nivel de manera intrínseca. Las subcolecciones ya no vivirán al inicio de la base de datos. Cuando creamos una colección y accedemos a sus documentos vemos que tienen la opcion de crear coleccion dentro del documento. Estas subcolecciones no se pueden ver si no se accede al documento de la coleccion.

Si tienes una entidad separada que vas a referenciar desde muchos lugares es recomendado usar un top level collection. Por el otro lado si se necesita hacer algo intrínseco al documento es aconsejable usar subcolecciones.

Creamos la coleccion posts

![colecciones_vs_subcolecciones_1](src/colecciones_vs_subcolecciones_1.png)

![colecciones_vs_subcolecciones_2](src/colecciones_vs_subcolecciones_2.png)

![colecciones_vs_subcolecciones_3](src/colecciones_vs_subcolecciones_3.png)

![colecciones_vs_subcolecciones_4](src/colecciones_vs_subcolecciones_4.png)

![colecciones_vs_subcolecciones_5](src/colecciones_vs_subcolecciones_5.png)

![colecciones_vs_subcolecciones_6](src/colecciones_vs_subcolecciones_6.png)


Aquí lo que tenemos es una coleccion post, que tiene un documento y ese documento tiene una coleccion intrinseca. Al acceder a esa subcoleccion vemos que nos meustra los detalles de otros documentos (como las etiquetas)


Las buenas practicas sugieren que, si vas a ocupar los elementos de la coleccion de manera independiente, hacer queries separados, o varios objetos o documentos diferentes tendran referencia a esa coleccion, vale la pena tener la entindad en top level colection. Por otro lado, si tendremos elementos que nos interesen solamente en el contexto de nuestro articulo o nuestro blogpost, vale la pena guardarla como subcoleccion de esa noticia en particular


Un top level collection se utilizaria para relaciones de tipo “agregacion”. Mientras que una sub collection se utilizaria para relaciones tipo “composicion”.

Por ejemplo:

Tenemos Estudiantes, Cursos y Notas. Los estudiantes tiene cursos y los cursos tiene estudiantes. Si se elimina un curso los estudiantes no deben ser eliminados. Lo mismo si se elimina un estudiante los cursos no deben ser elimiandos. Esto es una relacion de agregacion. Aqui se usaria top level collection para estudiantes y cursos.

Los estudiantes tienen notas y las notas pertenecen a un estudiante. Si se elimina un estudiante, tiene sentido eliminar las notas. Esto es una relacion de composicion. Aqui se usarian las subcollections. El estudiante tendría una subcollection de notas.

### Clase 46 Recreando Platziblog

Firestore, es una base de datos basada en documentos, pensada en lo siguiente:

Mantener el estado de tu aplicación.
En como se verán reflejados los datos en el frontend para el usuario.
Podemos hacer consultas sencillas en base a las top level collecttion. Ahora si queremos hacer consultas mas complejas podríamos usar big query, que es un data wharehouse.


En firestore hay algunas excepciones y detalles respecto a nuestra base de datos relacional. Por ejemplo, no existen tablas transistivas y tampoco un autoincremento (eso lo maneja Google). Pero, en general, debemos ser capaces de tener la misma data que tenemos en nuestra base de datos relacional en nuestra base de datos de firestore. 

El primer paso para hacerlo es ir a nuestro diagrama físico para ir partiendo nuestro proyecto. Debemos preguntarnos cuales entidades deberian ser una top level collection y cuales deberian ser documentos.

No hay una sola respuesta, depende de los usos que quieras darle. Depende, en la planeación, como vas a consultarlo. Por ejemplo si vamos a pensar en hacer consultas del usuario para mostrarlo como algo independiente entonces no tiene sentido ponerlo como un documento. No tendría sentido entrar a cada post a revisar las listas de usuarios a cada momento. 

Si por el contrario, no se necesita hacer una lista de usuarios para consultas, entonces si vale la pena tenerlos dentro de los documentos. En este momento haremos este enfoque, haremos los usuarios dentro de los posts y los posts entonces que indiquen que usuario los creo.

En las bases de datos pensadas el documentos el enfoque es distinto. Estas bases de datos no estan pensadas para hacer queries y relacionar información sino que estan pensadas para mantener el estado actual de una aplicación. Por ejemplo, en una llamada del post que se muestre toda la información pertinenente como las etiquetas, las catergorias, los comentarios y el usuario que la creo. Por ello, al momento de usar una base de datos no relacional, debe considerarse cual es el uso que le vamos a dar y elegir la herramienta que mejor se adapte.

### Clase 47 Construyendo Platziblog en Firestore


Hay muchos esquemas que podemos tratar. En este caso, vamos a elegir hacer las categorias, los usuarios y los posts como top level collections para poder hacer consultas sobre ellos.

Construimos categorias "espectaculos","deportes" y "ciencia" como top level collection

![Platziblog_firebase_1](src/Platziblog_firebase_1.png)

![Platziblog_firebase_2](src/Platziblog_firebase_2.png)

Creamosen top level la coleccion usuarios

![Platziblog_firebase_3](src/Platziblog_firebase_3.png)

Creamos la top level posts con dos articulos. Esto lo hacemos para mostrar que podemos almacenar toda la informacion que teniamos en nuestra base de datos relacional sin problemas.

![Platziblog_firebase_4](src/Platziblog_firebase_4.png)

![Platziblog_firebase_5](src/Platziblog_firebase_5.png)


Aunque aqui no tenemos las relaciones, podemos usar la referencia. Como cada post es publicado por un usuario (vemos que hay una relacion clara entre post-usuarios), podemos agarrar la referencia de la coleccion y añadirla en los campos de los documentos (como un campo author) de tipo referencia

Ahora hacemos la relacion del top level collection del usuario (Forma /usuarios/SaadnSqxKP0oI) agregando un campo en un documento posts usando el campo reference agregando el usuario

![Platziblog_firebase_6](src/Platziblog_firebase_6.png)

![Platziblog_firebase_7](src/Platziblog_firebase_7.png)

Igualmente vamos a hacer una referencia a las categorias. Por ejemplo, un post que sea de Ciencias y el otro post que sea de Deportes.

![Platziblog_firebase_8](src/Platziblog_firebase_8.png)

![Platziblog_firebase_9](src/Platziblog_firebase_9.png)

Finalmente agregamos las etiquetas de cada post como subcolecciones.

![Platziblog_firebase_10](src/Platziblog_firebase_10.png)



Aunque vemos que el enfoque es distinto, de igual modo estamos guardando la misma informacion y las relaciones. Al entrar a un post podemos saber sus propiedades, a que categoria pertenece, que usuario lo publicó, si se encuentra activo o inactivo, etc.


### Clase 48 Proyecto final: transformando tu proyecto en una db no relacional

Dentro de las bases de datos relacionales tenemos diferentes niveles de datos. En primer lugar tenemos las Bases de Datos o Esquemas como repositorios donde vivirán los datos que nos interesa guardar. Dentro del esquema existen las Tablas que provienen del concepto de entidades; y a su vez dentro de las tablas tenemos las tuplas o renglones.

Cuando trabajamos con bases de datos basadas en documentos como Firestore, aún existe la figura de la base de datos, sin embargo cambiaremos las tablas en favor de las colecciones y las tuplas en lugar de los documentos.

Recuerda:

Tabla -> Colección

Tupla -> Documento

Dentro de las Colecciones existen 2 grandes tipos. Las Top level collection o colecciones de nivel superior y las subcollections o subcolecciones. Estas últimas viven únicamente dentro de un documento padre.

¿Cómo saber cuál escoger?

Para determinar si tu colección debe ser top level o subcolección no hay una regla escrita en piedra y más bien tiene que ver con el caso de uso en particular y con la experiencia que hayas ganado como desarrollador.

Lo cierto es que no hay una sola forma de estructurar nuestra DB basada en documentos, y por tanto no existe una respuesta correcta, sin embargo a continuación te ofrezco un par de reglas guía que puedes utilizar para transformar tu proyecto que ya trabajaste en bases de datos relacionales en un proyecto no relacional.

#### Regla 1. Piensa en la vista de tu aplicación

La primera pista que te puedo dar es que pienses en un inicio en la manera en que los datos serán extraídos. En el caso de una aplicación, la mejor forma de pensarlo es en términos de las vistas que vas a mostrar a un momento determinado en la aplicación.

Es decir, al armar la estructura en la base de datos que sea un espejo o que al menos contenga todos los datos necesarios para llenar las necesidades que tiene nuestra parte visual en la aplicación.

En el caso de Platziblog por ejemplo si tienes una vista de un blog post individual, generalmente conviene mostrar además de los datos inherentes al post como el contenido, datos adicionales como las etiquetas que tiene o por ejemplo el autor (o autores si es colaborativo), en este caso tal vez convenga guardar estas dos “entidades” (autores y etiquetas) como subcolecciones de cada documento blog post.

Regla 2. La colección tiene vida propia

Esta regla se refiere a que la excepción a la regla 1 es cuando tenemos un caso en que la “entidad” que tiene necesidad de vivir y modificarse constantemente de manera independiente a las otras colecciones. Por ejemplo en Platziblog podemos en el ejemplo anterior hacer una excepción a autores porque nos conviene tenerlas como top level collection en el sentido que se añadan, borren, cambien o listen los usuarios sin depender del blog post.

Experimenta aplicando estas dos reglas a un proyecto que ya conozcas en una base de datos relacional y trata de convertirla en un proyecto de Firestore y comentanos los retos a los que te enfrentaste.

## Modulo 6 Bases de datos en la vida real

### Clase 49 Bases de datos en la vida real

Durante mucho tiempo se utilizaron las bases de datos relacionales para todo. Lo hizo muy bien por un tiempo, tanto así que Facebook utilizaba MySql. Este paradigma se rompe en el momento en que las aplicaciones que utilizamos se masifican (Big Data). Esto fue una exigencia mayor a las bases de datos. Al usar estas bases de datos cuando se llegaba a tal punto empezaban a tener problemas procesando los datos y el uso particular de datos.

Ahora tenemos diversos tipos de bases de datos dependiendo de la necesidad que quieres atacar.

Para datos historicos, queries complejos usar bigquery optimizado para datawherehouse. 

Para datos del estado de nuestra aplicacion usa colecciones con mongodb o firebase. Nos ayuda a tener los datos que viven actualmente en la aplicacion. Nos permite guardar y extraer los datos de manera completa pero no nos pide hacer Queries muy complejos.

Incluso puedes usar dos bases de datos en un mismo proyecto, guardar datos de mongo, convertirlos pasarlos a bigquery y hacer analisis sobre ellos. Podrias usar Firestore, transformarlos y pasarlos a BigQuery y meter incluso elementos de machinelearning. 

### Clase 50 Big Data

**Big Data** es un concepto que nace de la necesidad de manejar grandes cantidades de datos. La tendencia comenzó con compañías como **YouTube** al tener la necesidad de guardar y consultar mucha información de manera rápida.

Es un gran movimiento que consiste en el uso de diferentes tipos de bases de datos. En youtube se guardas miles de horas de videos por segundo. Hay que manejar grandes cantidades de informacion en muy poco tiempo y de manera eficiente.

Ejemplos: Cassandra. Nace de la necesidad de Facebook de guardar y sacar mucha información por segundo. Tiene desventajas como que las llaves ya estan definidas, problemas para hacer ciertos Joins, desventajas que no la hacen tan flexible. Pero, para sacar y meter datos de manera rapida, es muy efectiva.

### Clase 51 Data warehouse

**Data Warehouse** trata de guardar cantidades masivas de datos para la posteridad. Allí se guarda todo lo que no está viviendo en la aplicación pero es necesario tenerlo.
Debe servir para guardar datos por un largo periodo de tiempo y estos datos se deben poderse usar para encontrar cuestiones interesantes para el negocio. Un modo claro sería guardar los posts de facebook o de twitter; todo esto a pesar de que entra por segundo, el histórico no se usa en el momento actual de la aplicación pero es información relevante que es bueno guardar en otro lado (en un DataWarehouse).
Toda la información de Facebook y Youtube desde sus inicios se guarda en un gran almacen de datos.

Google usa **BigTable**. BigTable usa una sola tabla; Una gran tabla con mucha información. No sirve tanto para hacer consultas.

**Data Warehouse** es un archivo historico, archivo muerto, en  otra base de datos. Sirve para dos actividades principales:

- Guarda una gran cantidad de datos de forma "eterna".
- Poder extraer los datos para hacer analitica.

BigQuery es muy utilizado para almacenar una gran cantidad de datos pero tambien permite hacer consultas y meterle datos de distintas bases de datos.

### Clase 52 Data mining

El **Data Mining** se dedica a minar datos, a extraerlos de donde sea que estén (archivos muertos, base de datos actual, etc…) y hacer sentido de ellos para darles un uso.

Incluso de volver a guardar los datos pero hacerlos de forma aprovechable (Hay muchos datos en brutos de empresa que estan aislados, bases de datos que no estan normalizada, etc). Surge al mismo tiempo que el DataWarehouse y BusinessIntelligence; eran conceptos que estaban ligados.

### Clase 53 ETL

**ETL** son las siglas de Extract, Transform, Load (extraer, transformar y cargar). Se trata de tomar datos de archivos muertos y convertirlos en algo que sea de utilidad para el negocio.
También ayuda a tomar los datos vivos de la aplicación, transformarlos y guardarlos en un data warehouse periódicamente.

En Data mining ya vemos que muchas empresas pueden tener la información de forma no coherente. ETL significa tomar datos de un lugar, aplicarle procesos de transformacion, limpieza, procesamiento y cargarlos en otro lado.

Es una gran herramienta; podemos tomar la información viva de una aplicacion (o de un juego) y transformarla para almacenarla de una forma mas aprovechable. 

### Clase 54 Business intelligence

**Business Intelligence** es una parte muy importante de las carreras de datos ya que es el punto final del manejo de estos. Su razón de ser es tener la información lista, clara y que tenga todos los elementos para tomar decisiones en una empresa.
Es necesario tener una buena sensibilidad por entender el negocio, sus necesidades y la información que puede llevar a tomar decisiones en el momento adecuado al momento de realizar business intelligence. Consiste en evaluar patrones, la segmentacion de los clientes, sus preferencais, comportamientos históricos, mejores meses, etc.

### Clase 55 Machine Learning

**Machine Learning** tiene significados que varían. Es una serie de técnicas que involucran la inteligencia artificial y la detección de patrones.
Machine learning para datos tiene un gran campo de acción y es un paso más allá del business intelligence.
Nos ayuda a hacer modelos que encuentran patrones fortuitos para hacer correlaciones inesperadas. Sirve para ayudar a la toma de decisiones oportunas en cualquier ambito (organizaciones,empresas,gobiernos).

En BI tienes tienes a una persona buscando patrones; en ML no se intenta ir por un patron, se van por patrones fortuitos. Agarrar el mar de datos, aplicar un modelo que de conclusiones.




**Tiene dos casos de uso particulares:**

- Clasificación: Relacionado con un pool de datos, por ejemplo una cantidad masiva de blogpost. Podria servir para clasificar por procesamiento de lenguaje natural y reconocer patrones para clasificar los temas.
- Predicción: Por ejemplo, quieres analizar donde compran mas, patrones de ventas. Relaciones que quiza en un principio no te imaginas

### Clase 56 Data Science

**Data Science** es aplicar todas las técnicas de procesamiento de datos. En su manera más pura tiene que ver con gente con un background de estadísticas y ciencias duras.

### Clase 57 Por que aprender bases de datos hoy

¡Has concluido el curso! Ahora tienes potentes herramientas y posibilidades para ingresar en este apasionante campo.

Llevaste diagramas a bases de datos, exploraste un poco el mundo de las bases de datos no relacionales, hicimos un proyecto en firestore y transformamos Platzi blog de una base de datos relacional en una base de datos de documentos.

Dentro de las posibilidades que tienes hoy en día puedes hacer: Machine learning, ETL, Data Warehouse, Data mining, entre otros.

Recuerda practicar mucho con el proyecto. Te invito a que tomes el examen y verifiques tus conocimientos. ¡Exitos!

## Bonus

### Clase 58 Bases de datos relacionales vs no relacionales

Las bases de datos relacionales han estado entre nosotros durante un largo tiempo y han sido usadas por grandes como Google, Amazon, entre otros. Aún son usadas por bancos, aseguradoras, etc.

Las bases de datos no relacionales surgen cuando las grandes empresas sintieron necesidad de guardar y extraer grandes cantidades de datos en muy cortos periodos de tiempo, como YouTube.
