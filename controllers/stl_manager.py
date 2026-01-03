import vtk
import math
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class STLManager:
    def __init__(self, vtk_widget: QVTKRenderWindowInteractor, viewer_label):
        """
        vtk_widget: QVTKRenderWindowInteractor instance from UI
        """
        self.viewerInfoLabel = viewer_label
        self.vtk_widget = vtk_widget
        self.renderer = vtk.vtkRenderer()
        self.vtk_widget.GetRenderWindow().AddRenderer(self.renderer)
        self.actors = {}  # key: stl_number, value: vtkActor
        self.transforms = {}
        self.object_centers = {}

        # Initialize interactor
        self.vtk_widget.Initialize()
        self.vtk_widget.Start()

        # Set background color 
        self.renderer.SetBackground(0.0588, 0.0902, 0.1686)
        
        self.setup_camera_info()
        
        
        
    def setup_camera_info(self):
        """
        Sets up live camera info updates for viewerInfoLabel.
        """
        # Store initial camera vectors for reference
        camera = self.renderer.GetActiveCamera()
        self._initial_camera_pos = camera.GetPosition()
        self._initial_focal_point = camera.GetFocalPoint()

        # Add observer for interaction end (rotate, pan, zoom)
        self.vtk_widget.GetRenderWindow().GetInteractor().AddObserver(
            "EndInteractionEvent", lambda obj, evt: self.update_camera_info()
        )

        # Initial update
        self.update_camera_info()     
        
    def update_camera_info(self):
        """
        Update viewerInfoLabel with camera position, focal point, distance,
        azimuth and elevation relative to initial camera orientation.
        """
        camera = self.renderer.GetActiveCamera()
        pos = camera.GetPosition()
        focal = camera.GetFocalPoint()
        distance = camera.GetDistance()

        # Compute vector from focal to camera
        dx = pos[0] - focal[0]
        dy = pos[1] - focal[1]
        dz = pos[2] - focal[2]

        # Azimuth: angle in XY plane
        azimuth = math.degrees(math.atan2(dy, dx))
        # Elevation: angle from XY plane
        xy_dist = math.hypot(dx, dy)
        elevation = math.degrees(math.atan2(dz, xy_dist))

        # Update label
        self.viewerInfoLabel.setText(
            f"3D Viewer | Pos: ({pos[0]:.1f}, {pos[1]:.1f}, {pos[2]:.1f}) | "
            f"Dist: {distance:.1f} | Az: {azimuth:.1f}° | El: {elevation:.1f}°"
        )   

    def load_stl(self, file_path, stl_number):
        # Remove old actor if it exists
        if stl_number in self.actors:
            old_actor = self.actors[stl_number]
            self.renderer.RemoveActor(old_actor)
            
        reader = vtk.vtkSTLReader()
        reader.SetFileName(file_path)
        reader.Update()

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(reader.GetOutput())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        transform = vtk.vtkTransform()
        actor.SetUserTransform(transform)

        self.actors[stl_number] = actor
        self.transforms[stl_number] = transform 
        
        center = actor.GetCenter()
        self.object_centers[stl_number] = center
                
        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()
        self.vtk_widget.GetRenderWindow().Render()

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

    def clear_stl(self, stl_number):
        if stl_number in self.actors:
            self.renderer.RemoveActor(self.actors[stl_number])
            del self.actors[stl_number]
            del self.transforms[stl_number]

            self.vtk_widget.GetRenderWindow().Render()


    def set_translation(self, stl_number, x, y, z):
        if stl_number not in self.transforms:
            return

        transform = self.transforms[stl_number]
        transform.Identity()
        transform.Translate(x, y, z)

        self.vtk_widget.GetRenderWindow().Render()

    def set_rotation(self, stl_number, rx, ry, rz):
        if stl_number not in self.transforms:
            return

        transform = self.transforms[stl_number]
        transform.Identity()
        transform.RotateX(rx)
        transform.RotateY(ry)
        transform.RotateZ(rz)

        self.vtk_widget.GetRenderWindow().Render()

    def set_transform(self, stl_number, tx, ty, tz, rx, ry, rz):
        """Combined translation + rotation"""
        if stl_number not in self.transforms:
            return

        transform = self.transforms[stl_number]
        transform.Identity()
        transform.Translate(tx, ty, tz)
        transform.RotateX(rx)
        transform.RotateY(ry)
        transform.RotateZ(rz)

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
        

    
