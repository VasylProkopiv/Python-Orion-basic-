# from functools import wraps

def accepts(*types):
    def check_accepts(func_):
        assert len(types) == func_.__code__.co_argcount

        def wrap(*args, **kwargs):
            try:
                for (a, t) in zip(args, types):
                    assert isinstance(a, t), \
                        "argument %r does not match %s" % (a, t)
                return func_(*args, **kwargs)
            except (TypeError, AssertionError) as ex:
                print(ex.args)
        wrap.__name__ = func_.__name__
        return wrap

    return check_accepts


@accepts(int, (int, float), int)
def func(arg1, arg2, arg3):
    return arg1 * arg2 * arg3


print("Example #1:")
print(func(3, 2.0, 6)) # -> 36.0
print("\nExample #2:")
print(func(3, '2', 6)) # -> AssertionError: arg '2' does not match (<class 'int'>, <class 'float'>)
print("\nExample #3:")
print(func(3, 2)) # -> TypeError: func() missing 1 required positional argument: 'arg3'


class CheckTypes:
    def __init__(self, *types):
        self.types = types

    def __call__(self, func_):
        assert len(self.types) == func_.__code__.co_argcount

        def wrap(*args, **kwargs):
            try:
                for (a, t) in zip(args, self.types):
                    assert isinstance(a, t), \
                        "argument %r does not match %s" % (a, t)
                return func_(*args, **kwargs)
            except (TypeError, AssertionError) as ex:
                print(ex.args)

        wrap.__name__ = func_.__name__
        return wrap


@CheckTypes(float, (int, float), int)
def func(arg1, arg2, arg3):
    return arg1 * arg2 * arg3


print("Example #4:")
print(func(3.0, 2.0, 10)) # -> 60.0

print("\nExample #5:")
print(func('3', '2', 6)) # -> AssertionError: argument '3' does not match <class 'float'>)

print("\nExample #6:")
print(func(1.0, 2)) # -> TypeError: func() missing 1 required positional argument: 'arg3'