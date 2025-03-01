
class RawImageSource:
    def __init__(self, file, width, height, pixel_format):
        self._file = file
        self._width = width
        self._height = height
        self._pixel_format = pixel_format

    def __str__(self):
        return f'{self.__class__.__name__}({self._file.name}, {self._width}, {self._height}, {self._pixel_format})'
