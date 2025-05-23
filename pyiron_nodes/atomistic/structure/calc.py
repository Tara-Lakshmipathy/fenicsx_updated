from __future__ import annotations

from typing import Optional

from ase import Atoms
from pyiron_workflow import as_function_node


@as_function_node("volume")
def Volume(structure: Atoms|None = None) -> float:
    return structure.get_volume()


@as_function_node("number_of_atoms")
def NumberOfAtoms(structure: Atoms|None = None) -> int:
    return structure.get_number_of_atoms()
