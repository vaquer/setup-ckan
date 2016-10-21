from setuptools import setup, find_packages
from ckanator import __version__
#from ckanator.cli import main

setup(
    name='ckanator',
    version=__version__,
    description='CLI Tool based in python to install a CKAN instance',
    url='https://github.com/opintel/setup-ckan',
    author='Francisco Vaquero',
    author_email='francisco@opi.la',
    keywords='ckan, cli',
    install_requires=['docopt', 'docker-py', 'clint'],
    include_package_data=True,
    entry_points = {
        'console_scripts': [
            'ckanator=ckanator.cli:main',
        ]
    }
)