import click
from example_objects import *


@click.group()
def cli():
    pass


@cli.command()
@click.argument('source', type=click.File('rb'))
@click.option('--source-x', type=int, default=9)
@click.option('-a', type=int, default=1)
@click.option('-b', type=int, default=2)
@click.option('-c', type=int, default=3)
def command1(source, source_x, a, b, c):
    source = Source(source, source_x, a, b, c)
    print(source)


@cli.command()
@click.argument('sink', type=click.File('wb'))
@click.option('--sink-y', type=int, default=10)
@click.option('-d', type=int, default=4)
@click.option('-e', type=int, default=5)
@click.option('-f', type=int, default=6)
def command2(sink, sink_y, d, e, f):
    sink = Sink(sink, sink_y, d, e, f)
    print(sink)


@cli.command()
@click.argument('source', type=click.File('rb'))
@click.option('--source-x', type=int, default=9)
@click.option('-a', type=int, default=1)
@click.option('-b', type=int, default=2)
@click.option('-c', type=int, default=3)
@click.argument('sink', type=click.File('wb'))
@click.option('--sink-y', type=int, default=10)
@click.option('-d', type=int, default=4)
@click.option('-e', type=int, default=5)
@click.option('-f', type=int, default=6)
def command3(source, source_x, a, b, c, sink, sink_y, d, e, f):
    source = Source(source, source_x, a, b, c)
    sink = Sink(sink, sink_y, d, e, f)
    print(source, sink)


@cli.command()
@click.argument('source1', type=click.File('rb'))
@click.option('--source1-x', type=int, default=9)
@click.argument('source2', type=click.File('rb'))
@click.option('--source2-x', type=int, default=9)
@click.option('-a', type=int, default=1)
@click.option('-b', type=int, default=2)
@click.option('-c', type=int, default=3)
@click.argument('sink', type=click.File('wb'))
@click.option('--sink-y', type=int, default=10)
@click.option('-d', type=int, default=4)
@click.option('-e', type=int, default=5)
@click.option('-f', type=int, default=6)
def command4(source1, source1_x, source2, source2_x, a, b, c, sink, sink_y, d, e, f):
    source1 = Source(source1, source1_x, a, b, c)
    source2 = Source(source2, source2_x, a, b, c)
    sink = Sink(sink, sink_y, d, e, f)
    print(source1, source2, sink)


@cli.command()
@click.argument('source', type=click.File('rb'))
@click.option('--source-x', type=int, default=9)
@click.option('-a', type=int, default=1)
@click.option('-b', type=int, default=2)
@click.option('-c', type=int, default=3)
@click.argument('sink1', type=click.File('wb'))
@click.option('--sink1-y', type=int, default=10)
@click.argument('sink2', type=click.File('wb'))
@click.option('--sink2-y', type=int, default=10)
@click.option('-d', type=int, default=4)
@click.option('-e', type=int, default=5)
@click.option('-f', type=int, default=6)
def command5(source, source_x, a, b, c, sink1, sink1_y, sink2, sink2_y, d, e, f):
    source = Source(source, source_x,a, b, c)
    sink1 = Sink(sink1, sink1_y, d, e, f)
    sink2 = Sink(sink2, sink2_y, d, e, f)
    print(source, sink1, sink2)


if __name__ == '__main__':
    cli()
