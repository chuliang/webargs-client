import functools


from webargsclient import core


def inject_kwargs(argmap, locations=None):
    print('inject_kwargs', argmap, locations)

    def decorator(func):
        print('decorator', func)

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            print('wrapper', self, args, kwargs)
            data = {}
            params = {}

            # dump data to schema
            schema = core.get_schema(argmap)
            result = core.dump(kwargs, schema)
            # for each
            for name, field in schema.fields.items():
                value = result.data.get(name)
                if field.metadata.get('location') == 'json':
                    data[name] = value
                else:
                    params[name] = value

            if not params:
                params = None
            if not data:
                data = None
            return func(self, params=params, data=data)
        wrapper.__wrapped__ = func
        return wrapper
    return decorator

