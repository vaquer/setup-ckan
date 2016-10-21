import os
import json
from clint.textui import puts, colored, indent
from ckanator.dockerfiles.client import ClinetDockerBase
from ckanator.settings import DOCKER_FILES_PATH


class CreageNeighborhood(ClinetDockerBase):
    def run(self):
        print "########### START BUILDING IMAGES ###########"
        for dockerfile_path in DOCKER_FILES_PATH:
            print "#############################################"
            print "Building {0}".format(dockerfile_path[0])
            self.build(dockerfile_path)

    def build(self, dockerfile_path):
        for line in self.client.build(dockerfile=dockerfile_path[1], rm=True, tag=dockerfile_path[0], path=dockerfile_path[2]):
            response = json.loads(line.replace('\n', ''))
            self.print_line_clean(response)
            self.responses.append(line)

    def print_line_clean(self, line):
        import re
        r_unwanted = re.compile("[\n\t\r]")
        if line.get('stream', ''):
            print colored.cyan(r_unwanted.sub("", line.get('stream', '')))
        elif line.get('error', ''):
            print colored.red(r_unwanted.sub("", line.get('error', '')))