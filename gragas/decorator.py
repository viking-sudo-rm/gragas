from types import FunctionType


def decorator(callback):
    """Decorator indicating that an object is a decorator."""
    name = getattr(callback, "__name__", callback)
    call = getattr(callback, "__call__", None)
    if not callable(call):
        raise ValueError(f"Attribute __call__ of {name} is not callable.")
    elif isinstance(callback, type):
        if not isinstance(call, FunctionType):
            raise ValueError(f"Class {name} has no __call__ method.")
        else:
            return callback
    elif not isinstance(callback, FunctionType):
        raise ValueError(f"{name} is not a class or function.")
    else:
        return callback
