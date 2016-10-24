import docker
import time
from clint.textui import colored
from ckanator.dockerfiles.client import ClinetDockerBase
from ckanator.settings import DOCKER_IMAGES_DETAILS


class RunServer(ClinetDockerBase):
    def run(self):
        response = None
        
        self.load_options_settings()

        for image in DOCKER_IMAGES_DETAILS:
            try:
                if image[0] == 'ckan/ckan-plugins':
                    host = self.client.create_host_config(read_only=False, links=image[4], port_bindings={5000: ('0.0.0.0', 5000)})
                else:
                    host = self.client.create_host_config(read_only=False, port_bindings=image[5])
                container = self.client.create_container(image=image[0], name=image[1], environment=image[2], ports=image[3], host_config=host)
            except docker.errors.APIError, e:
                self.print_error(str(e))
                return

            response = self.client.start(container=container.get('Id'))
            self.print_output(response)
            time.sleep(10)

    def load_options_settings(self):
        DOCKER_IMAGES_DETAILS[0][2]['POSTGRES_PASSWORD'] = self.options.get('postgrespass')

        if self.options.get('port') is not None:
            DOCKER_IMAGES_DETAILS[2][3] = [self.options.get('port')]

        DOCKER_IMAGES_DETAILS[2][2]['CKAN_SITE_URL'] = self.options.get('siteurl', 'http://localhost/')
        print DOCKER_IMAGES_DETAILS

    def print_output(self, text):
        import re
        import json

        if text is None:
            return

        r_unwanted = re.compile("[\n\t\r]")
        response = json.loads(text.replace('\n', ''))

        if line.get('stream', ''):
            print colored.cyan(r_unwanted.sub("", line.get('stream', '')))
        elif line.get('error', ''):
            print colored.red(r_unwanted.sub("", line.get('error', '')))

    def print_error(self, text):
        import re
        import json

        if text is None:
            return

        r_unwanted = re.compile("[\n\t\r]")
        #print text
        #response = json.loads(text.replace('\n', ''))

        print colored.red(r_unwanted.sub("", text))