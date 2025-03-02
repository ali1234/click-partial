from copy import deepcopy
from functools import wraps

import click


def _partial(mode, **arg_kwargs):
    def _argumentbundle(constructor):
        if hasattr(constructor, '__click_params__') and constructor.__click_params__:
            raise Exception("You must specify whether options are instanced or shared.")
        def _constructor_decorator(name, **construct_kwargs):
            attr_flag = f'__{constructor.__name__}_partial__'

            def _mangle(n):
                return f'{name}_{n}'

            def _mangle_opts(opts):
                for o in opts:
                    if o[1] != '-':
                        raise Exception('Instanced options cannot have short synonyms.')
                return [o.replace('--', f'--{name}-', 1) for o in opts]

            def _construct(kwargs, pop):
                if pop:
                    get = kwargs.pop
                else:
                    get = kwargs.get

                if hasattr(constructor, '__partial_click_params__'):
                    for t, o in constructor.__partial_click_params__:
                        if t == 'instanced':
                            construct_kwargs[o.name] = kwargs.pop(_mangle(o.name))
                        elif t == 'shared':
                            construct_kwargs[o.name] = get(o.name)

                return constructor(kwargs[name], **construct_kwargs)

            def _constructor_wrapper(command):
                first = not hasattr(command, attr_flag)

                @wraps(command)
                def wrapper(**kwargs):
                    kwargs[name] = _construct(kwargs, pop=first)
                    return command(**kwargs)

                if first:
                    setattr(wrapper, attr_flag, True)

                if hasattr(constructor, '__partial_click_params__'):
                    params = getattr(wrapper, '__click_params__', [])
                    for t, o in constructor.__partial_click_params__:
                        if t == 'instanced':
                            oo = deepcopy(o)
                            oo.name = _mangle(o.name)
                            oo.opts = _mangle_opts(o.opts)
                            oo.secondary_opts = _mangle_opts(o.secondary_opts)
                            params.append(oo)
                        elif t == 'shared':
                            if first:
                                params.append(o)
                        else:
                            raise Exception('Internal error: Invalid option type. Please report.')
                    wrapper.__click_params__ = params
                if mode == 'argument':
                    wrapper = click.argument(name, **arg_kwargs)(wrapper)
                elif mode == 'option':
                    wrapper = click.option(f'--{name}', **arg_kwargs)(wrapper)
                else:
                    raise Exception('Internal error: Invalid mode. Please report.')
                return wrapper
            return _constructor_wrapper
        return _constructor_decorator
    return _argumentbundle


@wraps(click.argument)
def argument(**kwargs):
    return _partial('argument', **kwargs)


@wraps(click.option)
def option(**kwargs):
    return _partial('option', **kwargs)


def instanced(f):
    params = getattr(f, '__partial_click_params__', [])
    for o in f.__click_params__:
        if not isinstance(o, click.Option):
            raise Exception("You can only use options.")
        params.append(('instanced', o))
    f.__partial_click_params__ = params
    f.__click_params__ = []
    return f


def shared(f):
    params = getattr(f, '__partial_click_params__', [])
    for o in f.__click_params__:
        if not isinstance(o, click.Option):
            raise Exception("You can only use options.")
        params.append(('shared', o))
    f.__partial_click_params__ = params
    f.__click_params__ = []
    return f