# setup-ckan

Scripts de instalación de CKAN v2.5.2 basadas en Docker.

### Requerimientos
  - [Docker](https://www.docker.com/)

### Instalacion
```sh
  git clone git@github.com:opintel/setup-ckan.git
  docker build -t ckan/postgres setup-ckan/ckan-postgres
  docker build -t ckan/ckan-solr setup-ckan/ckan-solr
  docker build -t ckan/ckan-base setup-ckan/ckan-base
  docker build -t ckan/ckan-plugins setup-ckan/ckan-plugins
```
### Uso
Se deben correr los siguientes comandos en consola

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
