import click
import click_partial as partial

from example_objects import *


@partial.argument(type=click.File('rb'))
@partial.instanced
@click.option('--width', type=int, required=True)
@click.option('--height', type=int, required=True)
@click.option('--pixel-format', type=click.Choice(('L', 'RGB', 'RGBA')), default='RGB')
def rawimage(image, width, height, pixel_format):
    return RawImageSource(image, width, height, pixel_format)


@click.group()
def cli():
    pass


@cli.command()
@rawimage('image')
def show(image):
    print(image)
    ... # show the image


@cli.command()
@rawimage('image1')
@rawimage('image2')
def blend(image1, image2):
    print(image1, image2)
    ... # blend the images



if __name__ == '__main__':
    cli()
