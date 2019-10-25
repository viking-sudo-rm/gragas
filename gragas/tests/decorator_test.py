from unittest import TestCase

from gragas.decorator import decorator


class TestDecorator(TestCase):

    def test_fn_decorated(self):

        @decorator
        def f():
            pass

    def test_decorator_fails(self):
        with self.assertRaises(ValueError):
            decorator(3)

    def test_class_decorated(self):

        @decorator
        class A:
            def __call__(self):
                pass

    def test_class_decorated_fail(self):

        with self.assertRaises(ValueError):
            @decorator
            class B:
                pass
