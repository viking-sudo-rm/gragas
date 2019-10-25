from functools import wraps
import logging

from gragas.decorator import decorator


@decorator
class fixme:

    """Decorator indicating that a function is fundamentally broken."""

    def __init__(self, reason: str = None):
        self.reason = reason

    def __call__(self, callback):
        name = getattr(callback, "__name__", callback)
        self._log(name)

        @wraps(callback)
        def wrapped_callback(*args):
            self._log(name)
            return callback(*args)

        return callback

    def _log(self, name):
        logging.warning("FIXME %s: %s" % (name, self.reason))
