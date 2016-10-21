import os

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

DOCKER_FILES_PATH = (
    ('ckan/ckan-postgres', os.path.join(CURRENT_PATH, 'dockerfiles/ckan-postgres/Dockerfile'), os.path.join(CURRENT_PATH, 'dockerfiles/ckan-postgres')),
    ('ckan/ckan-solr', os.path.join(CURRENT_PATH, 'dockerfiles/ckan-solr/Dockerfile'), os.path.join(CURRENT_PATH, 'dockerfiles/ckan-solr')),
    ('ckan/ckan-base', os.path.join(CURRENT_PATH, 'dockerfiles/ckan/Dockerfile'), os.path.join(CURRENT_PATH, 'dockerfiles/ckan')),
    ('ckan/ckan-plugins', os.path.join(CURRENT_PATH, 'dockerfiles/ckan-plugins/Dockerfile'), os.path.join(CURRENT_PATH, 'dockerfiles/ckan-plugins')),
)