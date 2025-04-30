from pyiron_workflow import as_function_node

from ase import Atoms as Atoms
import numpy as np
from typing import Optional


@as_function_node("plot")
def Plot3d(
    structure: Atoms,
    camera: str = "orthographic",
    particle_size: float = 1.0,
    select_atoms: np.ndarray|None = None,
    view_plane: np.array = np.array([0, 0, 1]),
    distance_from_camera: float = 1.0,
):
    """Display atomistic structure (ase.Atoms) using nglview"""
    from structuretoolkit import plot3d

    return structure.plot3d(
        camera=camera,
        particle_size=particle_size,
        select_atoms=select_atoms,
        view_plane=view_plane,
        distance_from_camera=distance_from_camera,
    )
