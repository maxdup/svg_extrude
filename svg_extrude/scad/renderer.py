from typing import Iterator
from contextlib import contextmanager
from tempfile import mkstemp
import os
import subprocess
from io import IOBase


class Renderer:
    def __init__(self):
        pass

    @contextmanager
    def render_file(self, output_file_name: str, *, verbose=False) -> Iterator[IOBase]:
        # Create a temporary file
        handle, path = mkstemp(suffix=".scad")

        try:
            with os.fdopen(handle, "w") as scad_file:
                yield scad_file

            if verbose:
                with open(path, "r") as f:
                    print(f.read())

            # Call OpenSCAD
            # noinspection SpellCheckingInspection
            command = ["openscad", "-o", output_file_name, path]
            subprocess.run(command, capture_output=True, check=True)
        finally:
            os.remove(path)