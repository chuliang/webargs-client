import functools


from webargsclient import core


def inject_kwargs(argmap, locations=None):
    print('inject_kwargs', argmap, locations)

    def decorator(func):
        print('inject_kwargs decorator', func)

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            print('inject_kwargs wrapper', self, args, kwargs)
            data = {}
            params = {}
            matchdict = {}

            # dump data to schema
            schema = core.get_schema(argmap)
            result = core.dump(kwargs, schema)
            # for each
            for name, field in schema.fields.items():
                value = result.data.get(name)
                print('', name, value, field.metadata, field)
                if field.metadata.get('location') == 'json':
                    data[name] = value
                elif field.metadata.get('location') == 'matchdict':
                    matchdict[name] = value
                else:
                    params[name] = value

            if not params:
                params = None
            if not data:
                data = None
            if not matchdict:
                matchdict = None
            return func(self, params=params, data=data, matchdict=matchdict)
        wrapper.__wrapped__ = func
        return wrapper
    return decorator


def inject_route(_route):
    print('inject_route', _route)

    def decorator(func):
        print('inject_route decorator', func)

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            print('inject_route wrapper', self, args, kwargs)
            if not _route:
                return func(self, *args, **kwargs)
            kwargs['route'] = _route
            if kwargs.get('matchdict'):
                kwargs['route'] = kwargs['route'].format(**kwargs.get('matchdict'))
            return func(self, *args, **kwargs)
        wrapper.__wrapped__ = func
        return wrapper
    return decorator

