import os
import json
from clint.textui import colored
from ckanator.settings import DOCKER_FILES_PATH
from ckanator.dockerfiles.client import ClinetDockerBase


class CreageNeighborhood(ClinetDockerBase):
    """
    Clase que representa la accion de crear
    un neighborhood de imagenes para crear
    el CKAN SWARM pormedio de la CLI Tool
    """
    def run(self):
        """
        Metodo que realiza el build de las imagenes
        """
        print "########### START BUILDING IMAGES ###########"
        # Se hace build de cada dockerfile
        for dockerfile_path in DOCKER_FILES_PATH:
            print "#############################################"
            print "Building {0}".format(dockerfile_path[0])
            try:
                self.build(dockerfile_path)


    def build(self, dockerfile_path):
        """
        Realiza el build de un dockerfile
        """
        for line in self.client.build(dockerfile=dockerfile_path[1], rm=True, tag=dockerfile_path[0], path=dockerfile_path[2]):
            self.print_line_clean(line)
            self.responses.append(line)

    def print_line_clean(self, line):
        """
        Imprime la salida en consola
        dependiendo de la salida del build
        """
        import re
        import json

        r_unwanted = re.compile("[\n\t\r]")
        line = json.loads(line.replace('\n', ''))

        if line.get('stream', ''):
            print colored.cyan(r_unwanted.sub("", line.get('stream', '')))
        elif line.get('error', ''):
            print colored.red(r_unwanted.sub("", line.get('error', '')))
