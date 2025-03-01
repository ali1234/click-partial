class Source:
    def __init__(self, file, *args, **kwargs):
        self._file = file
        self._args = args
        self._kwargs = kwargs

    def __str__(self):
        return f'Source({self._file.name}, {self._args}, {self._kwargs})'


class Sink(Source):
    def __str__(self):
        return f'Sink({self._file.name}, {self._args}, {self._kwargs})'