from types import FunctionType


def decorator(callback):
    """Decorator indicating that an object is a decorator."""
    call = getattr(callback, "__call__", None)
    if (not isinstance(callback, FunctionType) and
            not isinstance(call, FunctionType)):
        name = getattr(callback, "__name__", callback)
        raise ValueError("Decorator %s is not callable." % name)
    return callback
