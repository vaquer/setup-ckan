from clint.textui import colored
from ckanator.settings import DOCKER_FILES_PATH
from ckanator.dockerfiles.client import ClinetDockerBase


class CreageNeighborhood(ClinetDockerBase):
    """
    Clase: Comando para la creacion de imagenes
    Docker necesarias para construir un SWARM
    que corre CKAN y sus dependencias
    """
    def run(self):
        """
        Funcion: Hace build de las imagenes
        en base a los Dockerfiles especificados
        en los settings. Retorna True si el build
        es exitoso, False si algo falla.

        Return: Boolean
        """

        self.imprime_centrado('COMENZANDO LA CONSTRUCCION DE LAS IMAGENES')
        # Se hace build de cada dockerfile
        for dockerfile_path in DOCKER_FILES_PATH:
            # Output para el usuario
            self.imprime_centrado('*')
            self.imprime_centrado("Building {0}".format(dockerfile_path[0]))
            self.imprime_centrado('*')
           
            if not self.contruir_imagen(dockerfile_path):
                return False

        # Output para el usuario
        self.imprime_centrado('*')
        self.imprime_centrado("Imagenes Docker creadas con exito")
        self.imprime_centrado('*')

        return True

    def contruir_imagen(self, dockerfile_path):
        """
        Funcion: Realiza el build de un dockerfile
        Return: Boolean
        """
        try:
           for line in self.client.build(dockerfile=dockerfile_path[1], rm=True, tag=dockerfile_path[0], path=dockerfile_path[2]):
                # Imprimir la salida en pantalla
                self._imprime_output_formateado(line)
                # Guardado del log de la salida del proceso
                self.responses.append(line)    
        except TypeError, e:
            self.errors = colored.red(str(e))
            return False

        return True

    def _imprime_output_formateado(self, line):
        """
        Metodo: Imprime la salida en consola
        formateada en base al tipo de salida
        Error o Stream
        """
        import re
        import json

        # Remueve caracteres no deseados
        regex_no_deseados = re.compile("[\n\t\r]")
        # Conversion a JSON para mejor manejo
        line = json.loads(line.replace('\n', ''))

        if line.get('stream', ''):
            print colored.cyan(regex_no_deseados.sub("", line.get('stream', '')))
        elif line.get('error', ''):
            print colored.red(regex_no_deseados.sub("", line.get('error', '')))
