from __future__ import annotations

from pyiron_workflow import as_function_node, as_macro_node
from typing import Optional


# from pyiron_workflow.workflow import Workflow


@as_function_node("structure")
def Bulk(
    name: str,
    crystalstructure: str|None = None,
    a: float|None = None,
    c: float|None = None,
    c_over_a: float|None = None,
    u: float|None = None,
    orthorhombic: bool = False,
    cubic: bool = False,
):
    from pyiron_atomistics import _StructureFactory

    return _StructureFactory().bulk(
        name,
        crystalstructure,
        a,
        c,
        c_over_a,
        u,
        orthorhombic,
        cubic,
    )


@as_macro_node("structure")
def CubicBulkCell(
    self, element: str, cell_size: int = 1, vacancy_index: int|None = None
):
    from pyiron_nodes.atomistic.structure.transform import (
        CreateVacancy,
        Repeat,
    )

    self.bulk = Bulk(name=element, cubic=True)
    self.cell = Repeat(structure=self.bulk, repeat_scalar=cell_size)

    self.structure = CreateVacancy(structure=self.cell, index=vacancy_index)
    return self.structure
