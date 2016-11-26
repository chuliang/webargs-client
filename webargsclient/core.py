import warnings

from webargs.core import argmap2schema
#from webargs.core.ma import Schema
from marshmallow import Schema


def get_schema(argmap):
    if isinstance(argmap, Schema):
        return argmap
    else:
        return argmap2schema(argmap)()


def dump(data, argmap):
    schema = get_schema(argmap)
    if not schema.strict:
        warnings.warn("It is highly recommended that you set strict=True on your schema "
            "so that the parser's error handler will be invoked when expected.", UserWarning)
    return schema.dump(data)
