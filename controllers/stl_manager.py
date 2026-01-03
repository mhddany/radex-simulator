import vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class STLManager:
    def __init__(self, vtk_widget: QVTKRenderWindowInteractor):
        """
        vtk_widget: QVTKRenderWindowInteractor instance from your UI
        """
        self.vtk_widget = vtk_widget
        self.renderer = vtk.vtkRenderer()
        self.vtk_widget.GetRenderWindow().AddRenderer(self.renderer)
        self.actors = {}  # key: stl_number, value: vtkActor

        # Initialize interactor
        self.vtk_widget.Initialize()
        self.vtk_widget.Start()

        # Set background color 
        self.renderer.SetBackground(0.0588, 0.0902, 0.1686)

    def load_stl(self, file_path: str, stl_number: int, color=(0.83, 0.83, 0.83)):
        """Load STL file and display it"""
        # Read STL
        reader = vtk.vtkSTLReader()
        reader.SetFileName(file_path)
        reader.Update()
        polydata = reader.GetOutput()

        self.display_polydata(polydata, stl_number, color)

    def display_polydata(self, polydata, stl_number: int, color=(0.83, 0.83, 0.83)):
        """Display a vtkPolyData mesh"""
        # Remove previous actor if exists
        if stl_number in self.actors:
            self.renderer.RemoveActor(self.actors[stl_number])

        # Mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(polydata)

        # Actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(*color)
        actor.GetProperty().EdgeVisibilityOn()
        actor.GetProperty().SetEdgeColor(0.2, 0.2, 0.2)
        actor.GetProperty().SetLineWidth(1.0)

        # Store reference
        self.actors[stl_number] = actor

        # Add actor
        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()
        self.vtk_widget.GetRenderWindow().Render()

    def clear_stl(self, stl_number: int):
        """Remove STL actor"""
        if stl_number in self.actors:
            self.renderer.RemoveActor(self.actors[stl_number])
            del self.actors[stl_number]
            self.vtk_widget.GetRenderWindow().Render()

    def move_actor(self, stl_number: int, x=0, y=0, z=0):
        """Translate actor in 3D space"""
        if stl_number in self.actors:
            self.actors[stl_number].SetPosition(x, y, z)
            self.vtk_widget.GetRenderWindow().Render()

    def rotate_actor(self, stl_number: int, rx=0, ry=0, rz=0):
        """Rotate actor around X, Y, Z axes"""
        if stl_number in self.actors:
            self.actors[stl_number].RotateX(rx)
            self.actors[stl_number].RotateY(ry)
            self.actors[stl_number].RotateZ(rz)
            self.vtk_widget.GetRenderWindow().Render()

    def validate_stl(self, file_path):
        """
        Check if the STL file can be read and has polygons.
        Returns True if valid, False otherwise.
        """
        try:
            reader = vtk.vtkSTLReader()
            reader.SetFileName(file_path)
            reader.Update()
            polydata = reader.GetOutput()
            
            # Check if polydata has at least one polygon
            if polydata.GetNumberOfPolys() > 0:                
                return True
            else:                
                return False
        except Exception as e:
            print("STL validation error:", e)
            return False