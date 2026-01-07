import vtk
import math
import os
import numpy as np
import pyvista as pv
import trimesh
import tetgen
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class STLManager:
    def __init__(self, vtk_widget: QVTKRenderWindowInteractor, viewer_label):
        """
        vtk_widget: QVTKRenderWindowInteractor instance from UI
        """        
        # Store actors, transforms, file paths, centers, and PyVista meshes
        self.actors = {}           # vtkActor per stl_number
        self.transforms = {}       # vtkTransform per stl_number
        self.stl_paths = {}        # file path per stl_number
        self.object_centers = {}   # center per stl_number
        self.stl_mesh = {}         # PyVista PolyData per stl_number
        
        self.viewerInfoLabel = viewer_label
        self.vtk_widget = vtk_widget
        self.renderer = vtk.vtkRenderer()
        self.vtk_widget.GetRenderWindow().AddRenderer(self.renderer)
        
        # Initialize interactor
        self.vtk_widget.Initialize()
        self.vtk_widget.Start()

        # Set background color 
        self.renderer.SetBackground(0.0588, 0.0902, 0.1686)
        
        self.setup_camera_info()
        
        self.tet_meshes = {}   # stl_number -> volume mesh data
        self.stl_paths = {}
        
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

    # -----------------------------
    # Load STL as PyVista + VTK actor
    # -----------------------------
    def load_stl(self, file_path, stl_number, surface_color=(0.83, 0.83, 0.83), edge_color=(0.2, 0.2, 0.2)):
        """
        Load STL as PyVista mesh and VTK actor, replacing any previous actor for this STL number.

        Parameters:
            file_path: str - path to the STL file
            stl_number: int - index of the STL (1 or 2)
            surface_color: tuple - RGB color for mesh surface
            edge_color: tuple - RGB color for mesh edges
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(file_path)

        # --- Remove old actor if it exists ---
        if stl_number in self.actors:
            old_actor = self.actors[stl_number]
            self.renderer.RemoveActor(old_actor)
            del self.actors[stl_number]

        # Remove old PyVista mesh if exists
        if hasattr(self, "stl_mesh") and stl_number in self.stl_mesh:
            del self.stl_mesh[stl_number]

        # --- Load STL as PyVista mesh ---
        mesh = pv.read(file_path)
        self.stl_mesh[stl_number] = mesh

        # --- Create VTK actor from mesh ---
        actor = self._create_actor_from_mesh(mesh, surface_color, edge_color)
        transform = vtk.vtkTransform()
        actor.SetUserTransform(transform)

        # --- Store references ---
        self.actors[stl_number] = actor
        self.transforms[stl_number] = transform
        self.stl_paths[stl_number] = file_path
        self.object_centers[stl_number] = actor.GetCenter()

        # --- Add actor to renderer ---
        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()
        self.vtk_widget.GetRenderWindow().Render()

    # -----------------------------
    # Helper: Create actor from PyVista mesh
    # -----------------------------
    def _create_actor_from_mesh(self, mesh: pv.PolyData, surface_color, edge_color):
        # Convert PyVista mesh to vtkPolyData
        polydata = mesh

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(polydata)

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        prop = actor.GetProperty()
        prop.SetColor(*surface_color)
        prop.EdgeVisibilityOn()
        prop.SetEdgeColor(*edge_color)
        prop.SetLineWidth(1.0)
        prop.SetRepresentationToSurface()

        return actor

    # -----------------------------
    # Apply translation + rotation to PyVista mesh & actor
    # -----------------------------
    def _apply_to_pyvista_mesh(self, stl_number, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0):
        """
        Apply translation and rotation to the PyVista mesh corresponding to stl_number.
        """
        if stl_number not in self.stl_mesh:
            return

        mesh = self.stl_mesh[stl_number]

        # Convert degrees to radians
        rx, ry, rz = np.deg2rad([rx, ry, rz])

        # Rotation matrices
        Rx = np.array([[1, 0, 0],
                       [0, np.cos(rx), -np.sin(rx)],
                       [0, np.sin(rx),  np.cos(rx)]])
        Ry = np.array([[ np.cos(ry), 0, np.sin(ry)],
                       [0, 1, 0],
                       [-np.sin(ry), 0, np.cos(ry)]])
        Rz = np.array([[np.cos(rz), -np.sin(rz), 0],
                       [np.sin(rz),  np.cos(rz), 0],
                       [0, 0, 1]])

        # Combined rotation: X then Y then Z
        R = Rz @ Ry @ Rx

        # Apply rotation
        mesh.points[:] = mesh.points @ R.T

        # Apply translation
        mesh.points[:] += np.array([tx, ty, tz])
    
    def update_pyvista_mesh_from_actor(self, stl_number):
        """
        Apply the current VTK actor transform to the corresponding PyVista mesh.
        Updates self.stl_mesh[stl_number] in-place so TetGen sees the transformed mesh.
        """
        if stl_number not in self.transforms or stl_number not in self.stl_mesh:
            return

        transform = self.transforms[stl_number]
        mesh = self.stl_mesh[stl_number]

        # Get 4x4 transformation matrix from VTK
        vtk_mat = transform.GetMatrix()
        mat_np = np.array([[vtk_mat.GetElement(i, j) for j in range(4)] for i in range(4)])

        # Apply transformation to points
        pts = mesh.points
        pts_hom = np.hstack([pts, np.ones((pts.shape[0], 1))])  # homogeneous
        pts_transformed = (mat_np @ pts_hom.T).T[:, :3]

        # Update mesh in-place
        mesh.points[:] = pts_transformed


    # -----------------------------
    # Overwrite set_transform to update both VTK actor and PyVista mesh
    # -----------------------------
    def set_transform(self, stl_number, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0):
        """Combined translation + rotation"""
        if stl_number not in self.transforms or stl_number not in self.stl_mesh:
            return

        # --- Update VTK actor for visualization ---
        transform = self.transforms[stl_number]
        transform.Identity()
        transform.Translate(tx, ty, tz)
        transform.RotateX(rx)
        transform.RotateY(ry)
        transform.RotateZ(rz)

        # --- Update PyVista mesh for TetGen ---
        self._apply_to_pyvista_mesh(stl_number, tx, ty, tz, rx, ry, rz)

        # --- Render VTK widget ---
        self.vtk_widget.GetRenderWindow().Render()

    # -----------------------------
    # Helper: Convert vtkTransform to 4x4 numpy matrix
    # -----------------------------
    @staticmethod
    def _vtk_transform_to_numpy_matrix(vtk_transform):
        m = vtk_transform.GetMatrix()
        mat = np.eye(4)
        for i in range(4):
            for j in range(4):
                mat[i, j] = m.GetElement(i, j)
        return mat

    # -----------------------------
    # Remove STL
    # -----------------------------
    def clear_stl(self, stl_number):
        if stl_number in self.actors:
            self.renderer.RemoveActor(self.actors[stl_number])
            del self.actors[stl_number]
            del self.transforms[stl_number]
            del self.stl_mesh[stl_number]
            self.vtk_widget.GetRenderWindow().Render()

    # -----------------------------
    # Validation
    # -----------------------------
    def validate_stl(self, file_path):
        try:
            mesh = pv.read(file_path)
            return mesh.n_cells > 0
        except Exception as e:
            print("STL validation error:", e)
            return False