# setup-ckan

Setup-ckan es una serie de scripts basados en Docker pensados para instalar una versión limpia de CKAN 2.5.2 lista para usarse con un minimo de esfuerzo y conocimientos técnicos. 

Los scripts sin extendibles, lo que permite al usuario mas experimentado y avanzado en conocimientos informaticos satisfacer necesidades mas complejas que una instalación convencional de CKAN no logre cubrir. 


### Requerimientos
  - [Docker](https://www.docker.com/).

**Nota: Las siguientes instrucciones no pretenden instruir al usuario en el uso de tecnologias basadas en Docker. Para mas información sobre los requerimientos ir al sitio oficial que esta referenciado en cada elemento de los requerimientos**

### Instalacion

Para usar setup-ckan en su ambiente es necesario seguir los siguientes pasos.

**Nota: Los siguientes comandos de consola se basan en un sistema operativo Linux Debian Like. Pueden cambiar para otras distribuciones**

1. Se clona el repositorio github.

```sh
  git clone git@github.com:opintel/setup-ckan.git
```
2. Se construyen las imagenes Docker
```sh
  docker build -t ckan/postgres setup-ckan/ckan-postgres
  docker build -t ckan/ckan-solr setup-ckan/ckan-solr
  docker build -t ckan/ckan-base setup-ckan/ckan-base
  docker build -t ckan/ckan-plugins setup-ckan/ckan-plugins
```
### Uso
Finalmente para levantar el ecosistema de CKAN es necesario correr los siguientes comandos.

```sh
# Postgres
docker run --name postgres-ckan \         
  -e POSTGRES_DB=ckan_default \                               
  -e USER_DATASTORE=ckan \                                                                 
  -e DATABASE_DATASTORE=datastore_default \
  -e POSTGRES_USER=ckan \
  -e POSTGRES_PASSWORD=super-secure-pass \
  -d -P ckan/postgres

# Solr
docker run \
  --name ckan-solr \
  -d -p 8983:8983 ckan/ckan-solr

# CKAN
docker run \
  --name ckan \
  -e INIT_DBS=true \ 
  -e TEST_DATA=true \
  -e CKAN_SITE_URL=http://localhost/ \ 
  --link ckan-solr:solr \
  --link postgres-ckan:postgres \
  -d -p 5000:5000 ckan/ckan-plugin
```

Para corroborar la instalación se debe revisar el puerto 5000 del host por medio del navegador.

### Creacion de usuario master
Para la creación de un usuario master se deben tener instaladas y levantadas las instancias del ecosistema de CKAN previamente. Para corroborar la instalación y el estado de las instancias correr el siguiente comando que arrojará un listado de las instancias que estan corriendo actualmente en el host:
```sh
  docker ps
```

Despues ejecutar el siguiente comando para la creación del usuario administrador en base a la documentación de [CKAN](http://docs.ckan.org/en/latest/sysadmin-guide.html#creating-a-sysadmin-account).
```sh
$ docker exect -it ckan CKAN_HOME/bin/paster --plugin=ckan sysadmin add {{usuario}} -c  /project/development.ini
```
**Nota: Sustituir {{usuario}} por el nombre de usuario requerido**

Una vez que se ejecuta el comando el sistema pedira por medio de preguntas los datos del nuevo administrador que deberan ser proporcionados para su creación.