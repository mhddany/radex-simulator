
import pyvista as pv
from PySide6.QtWidgets import QWidget
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import tetgen
import vtk

class Surf2TetMesh:
    """
    Convert STL surface meshes to tetrahedral FEM meshes and store them.
    """
    def __init__(self, vtk_widget: QWidget = None):
        """
        Initialize Surf2TetMesh.
        parent: optional QWidget to host the VTK viewer
        """
        # Mesh storage
        self.stl_mesh = {}       # {stl_number: pv.PolyData}
        self.tet_meshes = {}     # {stl_number: PyVista TetGen meshes or vtkUnstructuredGrid}
        self.tet_actors = {}     # {stl_number: vtkActor}

        # Create VTK viewer for tetrahedral meshes
        self.tet_viewer = vtk_widget
        self.tet_renderer = vtk.vtkRenderer()
        self.tet_viewer.GetRenderWindow().AddRenderer(self.tet_renderer)
          
        self.tet_renderer.UseFXAAOn()
        self.tet_renderer.SetBackground(0.0588, 0.0902, 0.1686)      
        
        # Initialize interactor
        self.tet_viewer.Initialize()
        self.tet_viewer.Start()


    def add_stl_mesh(self, stl_number, mesh: pv.PolyData):
        """
        Add a PyVista STL mesh.
        """
        self.stl_mesh[stl_number] = mesh

    def generate_fem_mesh(self, maxvolume=1.0, order=1, mindihedral=20, minratio=1.5, psc=1.0, verbose=0):
        """
        Generate tetrahedral FEM meshes for all STL meshes stored.
        """
        for stl_number, mesh in self.stl_mesh.items():
            vertices = mesh.points
            faces = mesh.faces.reshape(-1, 4)[:, 1:]  # skip leading 3

            tet = tetgen.TetGen(vertices, faces)
            tet.tetrahedralize(
                order=order,
                mindihedral=mindihedral,
                minratio=minratio,
                maxvolume=maxvolume,
                psc=psc,
                verbose=verbose
            )

            self.tet_meshes[stl_number] = tet.grid
            print(f"STL {stl_number} → {tet.grid.n_cells} tetrahedra")

    def tet_mesh_to_vtk_actor(self, tet_mesh):
        """
        Convert TetGen mesh (pyvista.UnstructuredGrid) to VTK actor for rendering.
        """
        points = vtk.vtkPoints()
        for p in tet_mesh.points:
            points.InsertNextPoint(*p)

        ugrid = vtk.vtkUnstructuredGrid()
        ugrid.SetPoints(points)

        # Assuming tetrahedral cells
        for i in range(tet_mesh.n_cells):
            cell = vtk.vtkTetra()
            cell_pts = tet_mesh.cell_faces(i).reshape(-1)  # get cell point indices
            for j, idx in enumerate(cell_pts[:4]):
                cell.GetPointIds().SetId(j, int(idx))
            ugrid.InsertNextCell(cell.GetCellType(), cell.GetPointIds())

        mapper = vtk.vtkDataSetMapper()
        mapper.SetInputData(ugrid)

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetRepresentationToWireframe()
        actor.GetProperty().SetOpacity(0.5)

        return actor
    
    def display_tet_meshes(self):
        """
        Display all tetrahedral meshes in the dedicated tet_viewer.
        """
        # Clear previous actors
        self.tet_renderer.RemoveAllViewProps()
        self.tet_actors = {}

        # Define surface color (same for both)
        surface_color = (0.5647, 0.6314, 0.7255)  # #90a1b9

        # Define edge colors per mesh
        edge_colors = {
            1: (0.0235, 0.827, 0.953),  # #06d3f3 for mesh 1
            2: (0.945, 0.537, 0.016),   # #f18904 for mesh 2
        }

        for stl_number, tet_mesh in self.tet_meshes.items():
            # Convert PyVista mesh to vtkUnstructuredGrid if needed
            if isinstance(tet_mesh, pv.UnstructuredGrid):
                vtk_mesh = tet_mesh.cast_to_unstructured_grid()
            else:
                vtk_mesh = tet_mesh

            # Mapper and actor
            mapper = vtk.vtkDataSetMapper()
            mapper.SetInputData(vtk_mesh)
            actor = vtk.vtkActor()
            actor.SetMapper(mapper)

            # Set surface and edge colors
            edge_color = edge_colors.get(stl_number, (0.2, 0.2, 0.2))  # default gray if missing
            prop = actor.GetProperty()
            prop.SetColor(*surface_color)
            prop.EdgeVisibilityOn()
            prop.SetEdgeColor(*edge_color)
            prop.SetLineWidth(1.0)
            prop.SetRepresentationToSurface()

            # Store actor and add to renderer
            self.tet_actors[stl_number] = actor
            self.tet_renderer.AddActor(actor)

        # Store actor
        self.tet_actors[stl_number] = actor
        self.tet_renderer.AddActor(actor)

        self.tet_renderer.ResetCamera()
        self.tet_viewer.GetRenderWindow().Render()

        print(f"Displayed {len(self.tet_meshes)} tetrahedral meshes.")

    def display_stl_meshes(self):
        """
        Display all STL meshes that have been loaded into Surf2TetMesh.
        Uses the same tet_renderer style logic but for surface meshes.
        """
        # Clear previous actors
        self.tet_renderer.RemoveAllViewProps()
        self.tet_actors = {}

        # Define surface color (same for both)
        surface_color = (0.5647, 0.6314, 0.7255)  # #90a1b9

        # Define edge colors per mesh
        edge_colors = {
            1: (0.0235, 0.827, 0.953),  # #06d3f3 for mesh 1
            2: (0.945, 0.537, 0.016),   # #f18904 for mesh 2
        }

        for stl_number, stl_mesh in self.stl_mesh.items():
            # PyVista PolyData can be used directly with vtkPolyDataMapper
            vtk_mesh = stl_mesh

            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInputData(vtk_mesh)

            actor = vtk.vtkActor()
            actor.SetMapper(mapper)

            # Set surface and edge colors
            edge_color = edge_colors.get(stl_number, (0.2, 0.2, 0.2))  # default gray if missing
            prop = actor.GetProperty()
            prop.SetColor(*surface_color)
            prop.EdgeVisibilityOn()
            prop.SetEdgeColor(*edge_color)
            prop.SetLineWidth(1.0)
            prop.SetRepresentationToSurface()

            # Store actor and add to renderer
            self.tet_actors[stl_number] = actor
            self.tet_renderer.AddActor(actor)

        self.tet_renderer.ResetCamera()
        self.tet_viewer.GetRenderWindow().Render()

        print(f"Displayed {len(self.stl_mesh)} STL meshes.")
