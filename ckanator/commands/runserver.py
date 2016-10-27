import os
import subprocess
from clint.textui import colored
from ckanator.settings import CURRENT_PATH
from ckanator.dockerfiles.client import ClinetDockerBase


class RunServer(ClinetDockerBase):
    """
    Clase que representa la accion de levantar
    el SWARM con el ambiente de ckan por
    medio del CLI Tool
    """
    def run(self):
        """
        Metodo que ejecuta el script
        que levanta el CKAN SWARM
        """
        response = None
        site_url = self.options.get('--siteurl')
        postgres_password = self.options.get('--postgrespass')
        sh_script_path = os.path.join(CURRENT_PATH, 'dockerfiles/run-server.sh')

        if not site_url:
            print colored.red("Debes definir una url base. Ejemplo: http://localhost")
            return False

        if not postgres_password:
            print colored.red("Debes definir una contraseña para la Base de Datos")
            return False

        # Parametrizamos los datos ingresados por el usuario
        os.environ.setdefault('SITE_CKAN_URL', site_url)
        os.environ.setdefault('POSTGRES_CKAN_PASSWORD_CLI', postgres_password)

        # Se crea el SWARM
        print subprocess.call(['bash', sh_script_path])
