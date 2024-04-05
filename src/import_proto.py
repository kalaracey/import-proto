import glob
import os
import subprocess

import protoc


class ImportProtoException(Exception):
    pass

def import_proto(path: str) -> None:
    """Setup python protocol buffer directory."""

    _proto_dir = os.path.dirname(os.path.abspath(path))

    _proto_files = glob.glob('**/*.proto', root_dir=_proto_dir, recursive=True)
    _args = [protoc.PROTOC_EXE, "-I.", "--python_out=.", *_proto_files]

    # print("protoc cwd:", _proto_dir)
    # print("protoc args:", _args)

    rc = subprocess.call(
        _args,
        cwd=_proto_dir,
    )

    if rc != 0:
        raise ImportProtoException(f"Protoc failed (exit code {rc}).")

