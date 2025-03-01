from copy import deepcopy
from functools import wraps

import click


@wraps(click.argument)
def argument(*arg_args, **arg_kwargs):
    def _argumentbundle(constructor):
        def _constructor_decorator(name):
            attr_flag = f'__{constructor.__name__}_partial__'

            def _mangle(n):
                return f'{name}_{n}'

            def _mangle_opts(opts):
                return [o.replace('--', f'--{name}-') for o in opts]

            def _construct(kwargs, pop):
                if pop:
                    get = kwargs.pop
                else:
                    get = kwargs.get
                construct_kwargs = {
                    o.name: get(o.name) for o in constructor.__click_params__
                }
                if hasattr(constructor, '__instanced_click_params__'):
                    construct_kwargs.update({
                        o.name: kwargs.pop(_mangle(o.name)) for o in constructor.__instanced_click_params__
                    })
                return constructor(kwargs[name], **construct_kwargs)

            def _constructor_wrapper(command):
                first = not hasattr(command, attr_flag)

                @wraps(command)
                def wrapper(**kwargs):
                    kwargs[name] = _construct(kwargs, pop=first)
                    return command(**kwargs)


                if first:
                    setattr(wrapper, attr_flag, True)
                    if hasattr(wrapper, '__click_params__'):
                        wrapper.__click_params__.extend(constructor.__click_params__)
                    else:
                        wrapper.__click_params__ = constructor.__click_params__.copy()

                if hasattr(constructor, '__instanced_click_params__'):
                    for o in constructor.__instanced_click_params__:
                        oo = deepcopy(o)
                        oo.name = _mangle(o.name)
                        oo.opts = _mangle_opts(o.opts)
                        wrapper.__click_params__.append(oo)

                wrapper = click.argument(name, *arg_args, **arg_kwargs)(wrapper)
                return wrapper
            return _constructor_wrapper
        return _constructor_decorator
    return _argumentbundle

def instanced(f):
    f.__instanced_click_params__ = f.__click_params__
    f.__click_params__ = []
    return f