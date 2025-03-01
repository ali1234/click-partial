import click
import click_partial as partial

from example_objects import *


@partial.argument(type=click.File('rb'))
@click.option('-a', type=int, default=1)
@click.option('-b', type=int, default=2)
@click.option('-c', type=int, default=3)
@partial.instanced
@click.option('--x', type=int, default=9)
def source(file, x, a, b, c):
    return Source(file, x, a, b, c)


@partial.argument(type=click.File('wb'))
@click.option('-d', type=int, default=4)
@click.option('-e', type=int, default=5)
@click.option('-f', type=int, default=6)
@partial.instanced
@click.option('--y', type=int, default=9)
def sink(file, y, d, e, f):
    return Sink(file, y, d, e, f)


@click.group()
def cli():
    pass


@cli.command()
@source('source')
def command1(source):
    print(source)


@cli.command()
@sink('sink')
def command2(sink):
    print(sink)


@cli.command()
@source('source')
@sink('sink')
def command3(source, sink):
    print(source, sink)


@cli.command()
@source('source1')
@source('source2')
@sink('sink')
def command4(source1, source2, sink):
    print(source1, source2, sink)


@cli.command()
@source('source')
@sink('sink1')
@sink('sink2')
def command5(source, sink1, sink2):
    print(source, sink1, sink2)


if __name__ == '__main__':
    cli()
