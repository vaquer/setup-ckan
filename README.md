# setup-ckan

Setup-ckan es una serie de scripts basados en Docker pensados para instalar una versión limpia de CKAN 2.5.2 lista para usarse con un minimo de esfuerzo y conocimientos técnicos. 

Los scripts sin extendibles, lo que permite al usuario mas experimentado y avanzado en conocimientos informaticos satisfacer necesidades mas complejas que una instalación convencional de CKAN no logre cubrir. 


### Requerimientos
  - [Python](https://www.python.org/).
  - [Docker](https://www.docker.com/).

**Nota: Las siguientes instrucciones no pretenden instruir al usuario en el uso de tecnologias basadas en Docker. Para mas información sobre los requerimientos ir al sitio oficial que esta referenciado en cada elemento de los requerimientos**

### Instalacion

Para usar setup-ckan en su ambiente es necesario seguir los siguientes pasos.

**Nota: Los siguientes comandos de consola se basan en un sistema operativo Linux Debian Like. Pueden cambiar para otras distribuciones**

1. Se clona el repositorio github.

```sh
$ git clone git@github.com:opintel/setup-ckan.git
```
2. Se instala la aplicación
```sh
$ python setup-ckan/setup.py develop
```
### Uso
Finalmente para levantar el ecosistema de CKAN es necesario correr los siguientes comandos.

```sh
$ ckanator createneighborhood
$ ckanator runserver --port=<puerto> --postgrespass=<postgrespass> --siteurl=<host>
```

Para corroborar la instalación se debe revisar el puerto y host por medio del navegador.

### Creacion de usuario master
Para la creación de un usuario master se deben tener instaladas y levantadas las instancias del ecosistema de CKAN previamente. Para corroborar la instalación y el estado de las instancias correr el siguiente comando que arrojará un listado de las instancias que estan corriendo actualmente en el host:

```sh
$ ckanator create admin --username=<username> --password=<password>
```

Una vez que se ejecuta el comando el sistema pedira por medio de preguntas los datos del nuevo administrador que deberan ser proporcionados para su creación.