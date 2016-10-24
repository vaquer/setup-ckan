#!/usr/bin/env python
"""
ckanator

Usage:
   ckanator createneighborhood
   ckanator runserver [--port=<port>] (--postgrespass=<postgrespass> --siteurl=<siteurl>)
"""
from inspect import getmembers, isclass
from docopt import docopt
from ckanator import __version__ as VERSION


def main():
    from ckanator import commands
    options = docopt(__doc__, version=VERSION)

    for key, value in options.iteritems():
        if hasattr(commands, key) and value:
            module = getattr(commands, key)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'ClinetDockerBase'][0]
            command = command(options=options)
            command.run()