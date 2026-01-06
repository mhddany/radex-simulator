import gmsh
import numpy as np
import os
import vtk


def stl_to_tet_mesh(
    stl_path: str,
    lc_min: float = 0.5,
    lc_max: float = 3.0,
    element_order: int = 1,
    optimize: bool = True,
):
    """
    Convert a closed STL surface into a tetrahedral FEM mesh using Gmsh.

    Parameters
    ----------
    stl_path : str
        Path to STL file (must be closed / watertight).
    lc_min : float
        Minimum characteristic length.
    lc_max : float
        Maximum characteristic length.
    element_order : int
        1 = linear tetrahedra, 2 = quadratic tetrahedra.
    optimize : bool
        Enable mesh optimization.

    Returns
    -------
    mesh : dict
        Dictionary containing nodes, tetrahedra, and surface triangles.
    """

    if not os.path.exists(stl_path):
        raise FileNotFoundError(stl_path)

    gmsh.initialize()
    gmsh.model.add("stl_volume")

    # -----------------------------
    # Global mesh options
    # -----------------------------
    gmsh.option.setNumber("Mesh.CharacteristicLengthMin", lc_min)
    gmsh.option.setNumber("Mesh.CharacteristicLengthMax", lc_max)
    gmsh.option.setNumber("Mesh.ElementOrder", element_order)
    gmsh.option.setNumber("Mesh.Algorithm3D", 10)  # HXT
    gmsh.option.setNumber("Mesh.Optimize", int(optimize))
    gmsh.option.setNumber("Mesh.OptimizeNetgen", int(optimize))
    gmsh.option.setNumber("Mesh.StlLinearDeflection", 0.1)
    gmsh.option.setNumber("Mesh.StlAngularDeflection", 0.5)

    # -----------------------------
    # Import STL
    # -----------------------------
    gmsh.merge(stl_path)

    # Create geometry from mesh
    gmsh.model.mesh.classifySurfaces(
        40 * np.pi / 180.0,  # angle (radians)
        True,               # includeBoundary
        True                # forceParametrizablePatches
    )

    gmsh.model.mesh.createGeometry()

    # -----------------------------
    # Create volume
    # -----------------------------
    surfaces = gmsh.model.getEntities(dim=2)
    surface_tags = [s[1] for s in surfaces]

    loop = gmsh.model.geo.addSurfaceLoop(surface_tags)
    volume = gmsh.model.geo.addVolume([loop])
    gmsh.model.geo.synchronize()

    # -----------------------------
    # Physical groups
    # -----------------------------
    gmsh.model.addPhysicalGroup(2, surface_tags, tag=1)
    gmsh.model.setPhysicalName(2, 1, "RadiatingSurface")

    gmsh.model.addPhysicalGroup(3, [volume], tag=10)
    gmsh.model.setPhysicalName(3, 10, "SolidVolume")

    # -----------------------------
    # Generate mesh
    # -----------------------------
    gmsh.model.mesh.generate(3)

    # -----------------------------
    # Extract nodes
    # -----------------------------
    node_tags, node_coords, _ = gmsh.model.mesh.getNodes()
    nodes = node_coords.reshape((-1, 3))

    # -----------------------------
    # Extract tetrahedral elements
    # -----------------------------
    tet_type = 4 if element_order == 1 else 11  # 4-node or 10-node tets
    elem_types, elem_tags, elem_node_tags = gmsh.model.mesh.getElements(dim=3)

    tets = None
    for etype, enodes in zip(elem_types, elem_node_tags):
        if etype == tet_type:
            tets = np.array(enodes).reshape((-1, 4 if element_order == 1 else 10))
            break

    if tets is None:
        gmsh.finalize()
        raise RuntimeError("No tetrahedral elements found.")

    # -----------------------------
    # Extract surface triangles
    # -----------------------------
    tri_type = 2 if element_order == 1 else 9
    elem_types, _, elem_node_tags = gmsh.model.mesh.getElements(dim=2)

    triangles = None
    for etype, enodes in zip(elem_types, elem_node_tags):
        if etype == tri_type:
            triangles = np.array(enodes).reshape((-1, 3 if element_order == 1 else 6))
            break

    gmsh.finalize()

    return {
        "nodes": nodes,              # (N, 3)
        "tetrahedra": tets - 1,       # zero-based indexing
        "triangles": triangles - 1,   # zero-based indexing
    }

def display_tet_meshes(self):
    # Optional: clear previous tet actors
    if not hasattr(self, "tet_actors"):
        self.tet_actors = {}

    for stl_number, mesh in self.tet_meshes.items():
        # Remove old tet actor
        if stl_number in self.tet_actors:
            self.renderer.RemoveActor(self.tet_actors[stl_number])

        actor = tet_mesh_to_vtk_actor(
            mesh["nodes"],
            mesh["tetrahedra"]
        )

        self.tet_actors[stl_number] = actor
        self.renderer.AddActor(actor)

    self.renderer.ResetCamera()
    self.vtk_widget.GetRenderWindow().Render()



def tet_mesh_to_vtk_actor(nodes, tets):
    points = vtk.vtkPoints()
    for p in nodes:
        points.InsertNextPoint(*p)

    ugrid = vtk.vtkUnstructuredGrid()
    ugrid.SetPoints(points)

    for tet in tets:
        cell = vtk.vtkTetra()
        for i, idx in enumerate(tet):
            cell.GetPointIds().SetId(i, int(idx))
        ugrid.InsertNextCell(cell.GetCellType(), cell.GetPointIds())

    # Mapper
    mapper = vtk.vtkDataSetMapper()
    mapper.SetInputData(ugrid)

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # Visual style for testing
    actor.GetProperty().SetRepresentationToWireframe()
    actor.GetProperty().SetOpacity(0.5)

    return actor

def generate_tet_meshes(self):
        for stl_number, stl_path in self.stl_paths.items():
            mesh = stl_to_tet_mesh(
                stl_path,
                lc_min=0.5,
                lc_max=2.0
            )
            self.tet_meshes[stl_number] = mesh

        self.display_tet_meshes()