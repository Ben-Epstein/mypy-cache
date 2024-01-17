def foo() -> str:
    return "bar"


def foo2() -> str:
    return foo() + "foo"
