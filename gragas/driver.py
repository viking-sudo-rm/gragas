"""A decorator for registering experiment drivers."""

from typing import Type
from argparse import ArgumentParser, Namespace


class Driver:

    """Base class for driver registries.
    
    For example, various main driver methods could be annotated like:
    ```python
    @Driver.register()
    def main(args):
        pass
    ```

    At the bottom of the Python file, the following code should be added:
    ```python
    parser = ArgumentParser()
    Driver.add_arguments(parser)
    Driver.run(parser.parse_args())
    ```

    Then, we can choose to run `main` from the CLI by adding the flag `--driver=main`.
    """

    default = None
    registry = {}
    flag_str = "driver"

    @classmethod
    def new(cls, name: str, flag: str = flag_str) -> Type["Driver"]:
        new_type = type(name, (cls,), {})
        new_type.default = None
        new_type.registry = {}
        new_type.flag_str = flag
        return new_type

    @classmethod
    def add_arguments(cls, parser: ArgumentParser) -> None:
        """Add arguments that specify the experiment."""
        parser.add_argument(f"--{cls.flag_str}", type=str, default=cls.default, choices=list(cls.registry))
    
    @classmethod
    def run(cls, args: Namespace) -> None:
        """Run an experiment driver specified by args."""
        exp = getattr(args, cls.flag_str)
        cls.registry[exp](args)

    @classmethod
    def register(cls, name: str = None, default: bool = False):
        """Decorator to register a driver via `Driver.register()`."""
        def _closure(callback):
            new_name = name or callback.__name__
            cls.registry[new_name] = callback
            if default:
                cls.default = new_name
        return _closure
