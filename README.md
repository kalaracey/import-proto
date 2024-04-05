# Overview

This package allows for automatic recompilation of protocol buffers on import.

# Setup

Create a directory with all your protocol buffer definitions in it, like `proto/`.

Create `proto/__init__.py` with the following contents:

```python
from import_proto import import_proto

import_proto(__file__)
```

Now, if you have defined a message `Qux` in `proto/foo/bar/baz.proto` like

```protobuf
// proto/foo/bar/baz.proto

message Qux {
    int corge = 1;
}

```

you can import it like so:

```python
from proto.foo.bar.baz_pb2 import Qux

q = Qux(corge=123)

print(q)
# => corge: 123
```

The protocol buffer compiler will run on each import.

# Known issues:
  * The protocol buffer compiler should not re-run if the protocol buffer definition files have not changed.