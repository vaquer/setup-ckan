from docker import Client


class ClinetDockerBase(object):
    def __init__(self, *args, **kwargs):
        self.options = kwargs.get('options', {})
        self.args = args
        self.kwargs = kwargs
        self.client = Client(base_url='unix://var/run/docker.sock')
        self.responses = []

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself')
