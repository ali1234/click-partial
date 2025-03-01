import click
from example_objects import *


@click.group()
def cli():
    pass


@cli.command()
@click.argument('image', type=click.File('rb'))
@click.option('--image-width', type=int, required=True)
@click.option('--image-height', type=int, required=True)
@click.option('--image-pixel-format', type=click.Choice(('L', 'RGB', 'RGBA')), default='RGB')
def show(image, image_width, image_height, image_pixel_format):
    image = RawImageSource(image, image_width, image_height, image_pixel_format)
    print(image)
    ... # show the image


@cli.command()
@click.argument('image1', type=click.File('rb'))
@click.option('--image1-width', type=int, required=True)
@click.option('--image1-height', type=int, required=True)
@click.option('--image1-pixel-format', type=click.Choice(('L', 'RGB', 'RGBA')), default='RGB')
@click.argument('image2', type=click.File('rb'))
@click.option('--image2-width', type=int, required=True)
@click.option('--image2-height', type=int, required=True)
@click.option('--image2-pixel-format', type=click.Choice(('L', 'RGB', 'RGBA')), default='RGB')
def blend(image1, image1_width, image1_height, image1_pixel_format, image2, image2_width, image2_height, image2_pixel_format):
    image1 = RawImageSource(image1, image1_width, image1_height, image1_pixel_format)
    image2 = RawImageSource(image2, image2_width, image2_height, image2_pixel_format)
    print(image1, image2)
    ... # blend the images


if __name__ == '__main__':
    cli()
