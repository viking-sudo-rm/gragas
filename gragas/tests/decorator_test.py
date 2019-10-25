from unittest import TestCase

from gragas.decorator import decorator


class TestDecorator(TestCase):

    def test_fn_decorated(self):
        @decorator
        def f(fn):
            return fn

    def test_decorate_noncallable(self):
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
