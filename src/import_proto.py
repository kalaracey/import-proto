import glob
import os
import subprocess
import sys

import protoc


class ImportProtoException(Exception):
    pass


def import_proto(path: str) -> None:
    """Setup python protocol buffer directory."""

    _proto_dir = os.path.dirname(os.path.abspath(path))

    if sys.version_info[0] > 3 or (sys.version_info[0] == 3 and sys.version_info[1] >= 10):
        _proto_files = glob.glob('**/*.proto', root_dir=_proto_dir, recursive=True)
        _args = [protoc.PROTOC_EXE, "-I.", "--python_out=.", *_proto_files]
    else:
        _proto_files = glob.glob(_proto_dir + '/**/*.proto', recursive=True)
        _proto_files = [os.path.relpath(f, _proto_dir) for f in _proto_files]
        _args = [protoc.PROTOC_EXE, "-I.", "--python_out=.", *_proto_files]

    # print("protoc cwd:", _proto_dir)
    # print("protoc args:", _args)

    rc = subprocess.call(
        _args,
        cwd=_proto_dir,
    )

    if rc != 0:
        raise ImportProtoException(f"Protoc failed (exit code {rc}).")

