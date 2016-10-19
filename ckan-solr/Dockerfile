# Build: docker build -t ckan/ckan-solr
# Base image
FROM ubuntu:14.04

MAINTAINER bcessa <ben@pixative.com>

USER root

# Install dependencies
#RUN \
#  DEBIAN_FRONTEND=noninteractive \
#  apt-get update && \
#  apt-get install -y \
#    solr-tomcat
#    openjdk-6-jdk \

# Add CKAN schema
#ADD start.sh /start.sh
#ADD https://raw.githubusercontent.com/ckan/ckan/master/ckan/config/solr/schema.xml /etc/solr/conf/schema.xml
# Agregamos esquema aumentado para busquedas geo-espaciales
#ADD schema.xml /etc/solr/conf/schema.xml
#ADD jetty /etc/default/jetty

#RUN mkdir /usr/java
#RUN ln -s /usr/lib/jvm/java-7-openjdk-amd64 /usr/java/default
#RUN chown jetty /var/log/jetty

# Adjust configuration file
#RUN \
#  chmod 644 /etc/solr/conf/schema.xml && \
#  sed -i 's/NO_START=1/NO_START=0/' /etc/default/jetty && \
#  sed -i 's/#JETTY_HOST=$(uname -n)/JETTY_HOST=0.0.0.0/' /etc/default/jetty && \
#  sed -i 's/#JETTY_USER=jetty/JETTY_USER=root/' /etc/default/jetty && \
#  sed -i 's/#JETTY_PORT=8080/JETTY_PORT=8983/' /etc/default/jetty

# Entrypoint
#CMD ["/start.sh"]
ENV CATALINA_HOME /usr/share/tomcat6
ENV CATALINA_BASE /var/lib/tomcat6

#Install the packages we need
RUN apt-get -q -y update
RUN DEBIAN_FRONTEND=noninteractive apt-get -q -y install solr-tomcat

ADD schema.xml /etc/solr/conf/schema.xml

EXPOSE 8080
CMD ["/usr/share/tomcat6/bin/catalina.sh", "run"]