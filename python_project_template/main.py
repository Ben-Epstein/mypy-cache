import json
import os

os.environ["TZ"] = "UTC"


def foo() -> str:
    json.dumps({"foo": "bar"})
    # mypy issue here
    return 5
