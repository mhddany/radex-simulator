
from PySide6.QtWidgets import QWidget, QFileDialog, QDialog, QVBoxLayout, QLabel, QProgressBar
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer, QObject, QThread, Signal
from PySide6.QtGui import QPixmap, QColor
from ui.ui_widget import Ui_Widget 
from controllers.stl_manager import STLManager
from controllers.surf_to_tet_mesh import Surf2TetMesh
import os
import vtk
import pyvista as pv

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Radiation Exchange Simulator")
        
        # Connect sidebar buttons to stacked widget
        self.setup_connections()
        self.switch_page(0, self.geometryButton)  # Default to settings first page
            
        # Initialize STL Manager
        self.stl_manager = STLManager(
            vtk_widget=self.vtkViewer,      # QVTKRenderWindowInteractor from UI
            viewer_label=self.mainTitleViewLabel  # QLabel from UI
        )

        # Initialize Surface to Tetrahedral Mesh converter
        self.surf2tetmesh = Surf2TetMesh(
            vtk_widget=self.tetViewer
        )
        
        # Initialize controls
        self.setup_transform_controls()
        
        self._define_tetgen_defaults()
        self.init_tetgen_controls()
        self.resetMeshingAButton.clicked.connect(lambda: self.reset_tetgen_object("A"))
        self.resetMeshingBButton.clicked.connect(lambda: self.reset_tetgen_object("B"))

        
        # Connect buttons
        self.uploadFileAButton.clicked.connect(lambda: self.open_stl_file(1))
        self.uploadFileBButton.clicked.connect(lambda: self.open_stl_file(2))
        self.resetPositionAButton.clicked.connect(lambda: self.reset_object_transform(1))
        self.resetPositionBButton.clicked.connect(lambda: self.reset_object_transform(2))
        self.validationPositionButton.clicked.connect(self.check_objects_overlap)

        # rotate viewer
        #self.validationPositionButton.clicked.connect(lambda: self.rotate_for_gif(steps=360, angle_per_step=2, interval_ms=30))
        
        self.generateMeshButton.clicked.connect(self.generate_tet_meshes)
        # QThread placeholder
        self.tetgen_thread = None
        self.tetgen_worker = None
        
        # Define surface color (same for both)
        self.surface_color = (0.5647, 0.6314, 0.7255)  # #90a1b9

        # Define edge colors per mesh
        self.edge_colors = {
            1: (0.0235, 0.827, 0.953),  # #06d3f3 for mesh 1
            2: (0.945, 0.537, 0.016),   # #f18904 for mesh 2
        }
        
        # init thermal controls
        self.init_thermal_controls()




    def setup_connections(self):
        # Dictionary mapping buttons to main stackedWidget page index
        button_page_map = {
            self.geometryButton: 0,
            self.positioningButton: 5,
            self.meshingButton: 1,
            self.materialsButton: 2,
            self.simulationButton: 3,
            self.resultsButton: 4,
        }

        for button, page_index in button_page_map.items():
            button.clicked.connect(lambda checked, btn=button, idx=page_index: self.switch_page(idx, btn))


    def switch_page(self, index, button):
        self.stackedWidget.setCurrentIndex(index)

        viewer_map = {
            self.geometryButton: 0,
            self.positioningButton: 0,
            self.meshingButton: 1,
            self.materialsButton: 1,
        }

        width_map = {
            self.materialsButton: 400,
            self.positioningButton: 700,
            self.simulationButton: 700,
            self.meshingButton: 700
        }

        # Viewer page
        if button in viewer_map:
            self.viewerStackedWidget.setCurrentIndex(viewer_map[button])

        # Minimum width
        self.settingsLayout.setMaximumWidth(width_map.get(button, 400))
                
        
        
    def update_status(self, message: str, success: bool = True):
        """
        Update the status bar with a message and appropriate styling.

        Parameters:
            message (str): The message to display.
            success (bool): True for good/success messages, False for bad/error messages.
        """
        if success:
            # Good message style
            self.statusLayout.setStyleSheet("background-color: #032e15; border-color: #7bf1a8;")
            self.statusMessageLabel.setStyleSheet("color: #7bf1a8;")
            self.statusIcon.setPixmap(QPixmap(":/icons/icons/check_green.svg"))
        else:
            # Bad message style
            self.statusLayout.setStyleSheet("background-color: #460809; border-color: #ffa2a2;")
            self.statusMessageLabel.setStyleSheet("color: #ffa2a2;")
            self.statusIcon.setPixmap(QPixmap(":/icons/icons/warning_red.svg"))

        self.statusMessageLabel.setText(message)
        
    def set_busy_status_style(self):
        """Apply busy (working) style to status bar."""
        self.statusLayout.setStyleSheet("background-color: #1e293b; border-color: #60a5fa;")
        self.statusMessageLabel.setStyleSheet("color: #93c5fd;")
        self.statusIcon.setPixmap(QPixmap(":/icons/icons/info.svg"))
        
    def start_status_animation(self, base_message="Generating FEM mesh"):
        """
        Start animated 'working' message in the status bar.
        """
        self._status_base_message = base_message
        self._status_dot_count = 0

        # apply busy style once
        self.set_busy_status_style()
        self.statusMessageLabel.setText(base_message)

        # timer for animation
        self._status_timer = QTimer(self)
        self._status_timer.timeout.connect(self._update_status_animation)
        self._status_timer.start(400)
        
    def _update_status_animation(self):
        self._status_dot_count = (self._status_dot_count + 1) % 4
        dots = "." * self._status_dot_count
        self.statusMessageLabel.setText(
            f"{self._status_base_message}{dots}"
        )
        
    def stop_status_animation(self, message, success=True):
        """
        Stop busy animation and show final status message.
        """
        if hasattr(self, "_status_timer"):
            self._status_timer.stop()
            self._status_timer.deleteLater()

        # reuse your existing logic
        self.update_status(message, success)





    def open_stl_file(self, stl_number):
        dialog = QFileDialog(self)
        dialog.setNameFilter("STL Files (*.stl)")
        dialog.setFileMode(QFileDialog.ExistingFile)
        if dialog.exec():
            file_path = dialog.selectedFiles()[0]
            file_name = os.path.basename(file_path)

            # Validate STL
            valid = self.stl_manager.validate_stl(file_path)

            # Load STL if valid
            if valid:
                self.stl_manager.load_stl(
                    file_path, 
                    stl_number, 
                    surface_color=self.surface_color, 
                    edge_color=self.edge_colors[stl_number]
                )

            # Update individual STL UI
            if stl_number == 1:
                self.stl1_valid = valid
                icon_label = self.objectALoadedIcon
                text_label = self.objectALoadedLabel
            elif stl_number == 2:
                self.stl2_valid = valid
                icon_label = self.objectBLoadedIcon
                text_label = self.objectBLoadedLabel
            else:
                return

            # Update icon and label color
            if valid:
                icon_label.setPixmap(QPixmap(":/icons/icons/check_green.svg"))
                text_label.setStyleSheet("color: #f1f5f9;")
                text_label.setText(f"{file_name} loaded")
                print(f"STL {stl_number} imported successfully")
            else:
                icon_label.setPixmap(QPixmap(":/icons/icons/warning_red.svg"))
                text_label.setStyleSheet("color: #ffa2a2;")
                print(f"STL {stl_number} import unsuccessful: No polygons found.")

            # --- Check if both STLs are loaded ---
            if getattr(self, "stl1_valid", False) and getattr(self, "stl2_valid", False):
                # Both loaded successfully
                self.readyPositioningIcon.setPixmap(QPixmap(":/icons/icons/check_green.svg"))
                self.readyPositioningLabel.setStyleSheet("color: #f1f5f9;")
                
                self.update_status("Both STL files loaded successfully. Ready for positioning!", success=True)
                print("Both STL files loaded successfully. Ready for positioning!")
            else:
                print("Not ready for positioning: One or both STLs missing.")
                self.statusMessageLabel.setText("Not ready for positioning: One or both STLs missing.")


    def _parameter_name_from_label(self, label: QtWidgets.QLabel) -> str:
            """
            Extract parameter name from QLabel objectName.
            Example: 'maxVolumeALabel' or 'maxVolumeBLabel' -> 'maxVolume'
            """
            name = label.objectName()

            for suffix in ("ALabel", "BLabel", "Label"):
                if name.endswith(suffix):
                    return name.replace(suffix, "")

            return name  # fallback
        
    def _define_tetgen_defaults(self):
        self.tetgen_defaults = {
            "A": {
                "maxvolume": 100,
                "mindihedral": 20,
                "minratio": 15,
                "psc": 10,
                "order": 0,
            },
            "B": {
                "maxvolume": 100,
                "mindihedral": 20,
                "minratio": 15,
                "psc": 10,
                "order": 0,
            },
        }
    
    def reset_tetgen_object(self, obj: str):
        """
        Reset TetGen controls for Object A or B.
        obj must be "A" or "B"
        """
        d = self.tetgen_defaults[obj]

        getattr(self, f"maxvolume{obj}Slider").setValue(d["maxvolume"])
        getattr(self, f"mindihedral{obj}Slider").setValue(d["mindihedral"])
        getattr(self, f"minratio{obj}Slider").setValue(d["minratio"])
        getattr(self, f"psc{obj}Slider").setValue(d["psc"])
        getattr(self, f"order{obj}comboBox").setCurrentIndex(d["order"])
        self.update_status(f"TetGen settings for Object {obj} reset", success=True)
    
    def init_tetgen_controls(self):
        """
        Initialize TetGen sliders, combo boxes, and value labels
        for both Object A and Object B.
        """

        def init_slider(slider, label, min_v, max_v, default, scale=1.0, suffix=""):
            slider.setMinimum(min_v)
            slider.setMaximum(max_v)
            slider.setValue(default)
            slider.setSingleStep(1)
            slider.setTracking(True)
            
            param_name = self._parameter_name_from_label(label)

            def update_label(val):
                real_value = val * scale
                label.setText(f"{param_name}: {real_value:g}{suffix}")

            slider.valueChanged.connect(update_label)
            update_label(default)

        def init_combobox(combo):
            combo.clear()
            combo.addItems(["1. Linear", "2. Quadratic"])
            combo.setCurrentIndex(0)
            
        # -------- Object A --------
        init_slider(self.maxvolumeASlider, self.maxvolumeALabel,
                    1, 100, 100, scale=0.01)

        init_slider(self.mindihedralASlider, self.mindihedralALabel,
                    5, 35, 20, suffix="°")

        init_slider(self.minratioASlider, self.minratioALabel,
                    10, 40, 15, scale=0.1)

        init_slider(self.pscASlider, self.pscALabel,
                    5, 30, 10, scale=0.1)

        init_combobox(self.orderAcomboBox)

        # -------- Object B --------
        init_slider(self.maxvolumeBSlider, self.maxvolumeBLabel,
                    1, 100, 100, scale=0.01)

        init_slider(self.mindihedralBSlider, self.mindihedralBLabel,
                    5, 35, 20, suffix="°")

        init_slider(self.minratioBSlider, self.minratioBLabel,
                    10, 40, 15, scale=0.1)

        init_slider(self.pscBSlider, self.pscBLabel,
                    5, 30, 10, scale=0.1)

        init_combobox(self.orderBcomboBox)

    def init_thermal_controls(self):
        """
        Initialize thermal properties controls (slider + spinbox + material combo)
        for Object A and Object B.
        """
        # Material database
        self.material_properties = {
            "Aluminium": {
                "T0": 25,
                "emissivity": 0.09,
                "cp": 900,
                "k": 237,
            },
            "Steel": {
                "T0": 25,
                "emissivity": 0.70,
                "cp": 500,
                "k": 50,
            },
            "Copper": {
                "T0": 25,
                "emissivity": 0.03,
                "cp": 385,
                "k": 401,
            },
            "Ceramic": {
                "T0": 25,
                "emissivity": 0.95,
                "cp": 700,
                "k": 30,
            },
        }
        # Helper: slider <-> spinbox
        def init_slider_spinbox(
            slider, spinbox,
            min_v, max_v, step,
            default,
            scale=1.0
        ):
            """
            scale is used when slider works in integer space
            but the physical value is float (e.g. emissivity).
            """
            slider.setMinimum(int(min_v / scale))
            slider.setMaximum(int(max_v / scale))
            slider.setSingleStep(1)
            slider.setValue(int(default / scale))

            spinbox.setMinimum(min_v)
            spinbox.setMaximum(max_v)
            spinbox.setSingleStep(step)
            spinbox.setValue(default)

            # slider -> spinbox
            slider.valueChanged.connect(
                lambda v: spinbox.setValue(v * scale)
            )

            # spinbox -> slider
            spinbox.valueChanged.connect(
                lambda v: slider.setValue(int(v / scale))
            )

        # Helper: material selection
        def init_material_combobox(combo, setters):
            combo.clear()
            combo.addItems(self.material_properties.keys())

            def on_material_changed(material):
                props = self.material_properties[material]
                setters(props)

            combo.currentTextChanged.connect(on_material_changed)

        # Object A
        init_slider_spinbox(
            self.matAInitTemperatureSlider, self.matAInitTemperatureSpinner,
            min_v=273, max_v=1273, step=10, default=298
        )

        init_slider_spinbox(
            self.matAEmissivitySlider, self.matAEmissivitySpinner,
            min_v=0.0, max_v=1.0, step=0.01, default=0.09,
            scale=0.01
        )

        init_slider_spinbox(
            self.matACpSlider, self.matACpSpinner,
            min_v=100, max_v=2000, step=10, default=900
        )

        init_slider_spinbox(
            self.matAKappaSlider, self.matAKappaSpinner,
            min_v=1, max_v=500, step=1, default=298
        )

        def set_material_A(props):
            self.matAInitTemperatureSpinner.setValue(props["T0"])
            self.matAEmissivitySpinner.setValue(props["emissivity"])
            self.matACpSpinner.setValue(props["cp"])
            self.matAKappaSpinner.setValue(props["k"])

        init_material_combobox(self.matAPresetsComboBox, set_material_A)

        # Object B
        init_slider_spinbox(
            self.matBInitTemperatureSlider, self.matBInitTemperatureSpinner,
            min_v=273, max_v=1273, step=10, default=298
        )

        init_slider_spinbox(
            self.matBEmissivitySlider, self.matBEmissivitySpinner,
            min_v=0.0, max_v=1.0, step=0.01, default=0.70,
            scale=0.01
        )

        init_slider_spinbox(
            self.matBCpSlider, self.matBCpSpinner,
            min_v=100, max_v=2000, step=10, default=500
        )

        init_slider_spinbox(
            self.matBKappaSlider, self.matBKappaSpinner,
            min_v=1, max_v=500, step=1, default=50
        )

        def set_material_B(props):
            self.matBInitTemperatureSpinner.setValue(props["T0"])
            self.matBEmissivitySpinner.setValue(props["emissivity"])
            self.matBCpSpinner.setValue(props["cp"])
            self.matBKappaSpinner.setValue(props["k"])

        init_material_combobox(self.matBPresetsComboBox, set_material_B)

    def setup_transform_controls(self):
        # ---------- COMMON SETTINGS ----------
        translation_spinboxes = [
            self.xTranslationASpinbox,
            self.yTranslationASpinbox,
            self.zTranslationASpinbox,
            self.xTranslationBSpinbox,
            self.yTranslationBSpinbox,
            self.zTranslationBSpinbox,
        ]

        for sb in translation_spinboxes:
            sb.setRange(-1000.0, 1000.0)
            sb.setDecimals(3)
            sb.setSingleStep(0.1)
            sb.setValue(0.0)

        rotation_sliders = [
            self.xRotationASlider,
            self.yRotationASlider,
            self.zRotationASlider,
            self.xRotationBSlider,
            self.yRotationBSlider,
            self.zRotationBSlider,
        ]

        for sl in rotation_sliders:
            sl.setRange(-180, 180)   # real degrees
            sl.setSingleStep(1)
            sl.setPageStep(10)
            sl.setValue(0)           # center = 0°

        # ---------- OBJECT A (STL 1) ----------
        self.xTranslationASpinbox.valueChanged.connect(lambda _: self.update_transform(1))
        self.yTranslationASpinbox.valueChanged.connect(lambda _: self.update_transform(1))
        self.zTranslationASpinbox.valueChanged.connect(lambda _: self.update_transform(1))

        self.xRotationASlider.valueChanged.connect(lambda _: self.update_transform(1))
        self.yRotationASlider.valueChanged.connect(lambda _: self.update_transform(1))
        self.zRotationASlider.valueChanged.connect(lambda _: self.update_transform(1))

        # ---------- OBJECT B (STL 2) ----------
        self.xTranslationBSpinbox.valueChanged.connect(lambda _: self.update_transform(2))
        self.yTranslationBSpinbox.valueChanged.connect(lambda _: self.update_transform(2))
        self.zTranslationBSpinbox.valueChanged.connect(lambda _: self.update_transform(2))

        self.xRotationBSlider.valueChanged.connect(lambda _: self.update_transform(2))
        self.yRotationBSlider.valueChanged.connect(lambda _: self.update_transform(2))
        self.zRotationBSlider.valueChanged.connect(lambda _: self.update_transform(2))



    def update_transform(self, stl_number):
        if stl_number not in self.stl_manager.actors:
            return

        actor = self.stl_manager.actors[stl_number]
        transform = self.stl_manager.transforms[stl_number]
        cx, cy, cz = self.stl_manager.object_centers[stl_number]

        # ---- Read UI values ----
        if stl_number == 1:
            tx = self.xTranslationASpinbox.value()
            ty = self.yTranslationASpinbox.value()
            tz = self.zTranslationASpinbox.value()

            rx = self.xRotationASlider.value()
            ry = self.yRotationASlider.value()
            rz = self.zRotationASlider.value()
            
            self.xRotationUnitPositionALabel.setText(f"{rx}°")
            self.yRotationUnitPositionALabel.setText(f"{ry}°")
            self.zRotationUnitPositionALabel.setText(f"{rz}°")
        else:
            tx = self.xTranslationBSpinbox.value()
            ty = self.yTranslationBSpinbox.value()
            tz = self.zTranslationBSpinbox.value()

            rx = self.xRotationBSlider.value()
            ry = self.yRotationBSlider.value()
            rz = self.zRotationBSlider.value()

            self.xRotationUnitPositionBLabel.setText(f"{rx}°")
            self.yRotationUnitPositionBLabel.setText(f"{ry}°")
            self.zRotationUnitPositionBLabel.setText(f"{rz}°")

        # ---- Build transform ----
        transform.Identity()

        # 1) User translation (world space)
        transform.Translate(tx, ty, tz)

        # 2) Move pivot to object center
        transform.Translate(cx, cy, cz)

        # 3) Rotate around local axes
        transform.RotateX(rx)
        transform.RotateY(ry)
        transform.RotateZ(rz)

        # 4) Move back from center
        transform.Translate(-cx, -cy, -cz)

        actor.SetUserTransform(transform)

        self.vtkViewer.GetRenderWindow().Render()
        
    def reset_object_transform(self, stl_number: int):
        """
        Reset translation, rotation, and labels for a single STL object.
        """
        if stl_number == 1:
            translations = (self.xTranslationASpinbox, self.yTranslationASpinbox, self.zTranslationASpinbox)
            rotations = (self.xRotationASlider, self.yRotationASlider, self.zRotationASlider)
            rotation_labels = (self.xRotationUnitPositionALabel, self.yRotationUnitPositionALabel, self.zRotationUnitPositionALabel)
        elif stl_number == 2:
            translations = (self.xTranslationBSpinbox, self.yTranslationBSpinbox, self.zTranslationBSpinbox)
            rotations = (self.xRotationBSlider, self.yRotationBSlider, self.zRotationBSlider)
            rotation_labels = (self.xRotationUnitPositionBLabel, self.yRotationUnitPositionBLabel, self.zRotationUnitPositionBLabel)
        else:
            return  # invalid object number

        # Reset translation spinboxes
        for sb in translations:
            sb.blockSignals(True)
            sb.setValue(0.0)
            sb.blockSignals(False)

        # Reset rotation sliders
        for sl in rotations:
            sl.blockSignals(True)
            sl.setValue(0)
            sl.blockSignals(False)

        # Reset rotation labels
        for lbl in rotation_labels:
            lbl.setText("0°")

        # Apply transform to actor
        self.update_transform(stl_number)

    def check_objects_overlap(self):
        """
        Check if Object A and Object B overlap using world-transformed bounding boxes.
        Returns True if overlapping, False otherwise.
        """
        # Ensure both objects are loaded
        if 1 not in self.stl_manager.actors or 2 not in self.stl_manager.actors:
            print("One or both objects not loaded.")
            self.update_status("One or both objects not loaded.", success=False)
            return False

        actor1 = self.stl_manager.actors[1]
        actor2 = self.stl_manager.actors[2]

        # Get transformed bounds (world coordinates)
        bounds1 = self.get_actor_world_bounds(actor1)
        bounds2 = self.get_actor_world_bounds(actor2)

        # Check overlap on all axes
        overlap_x = (bounds1[0] <= bounds2[1]) and (bounds1[1] >= bounds2[0])
        overlap_y = (bounds1[2] <= bounds2[3]) and (bounds1[3] >= bounds2[2])
        overlap_z = (bounds1[4] <= bounds2[5]) and (bounds1[5] >= bounds2[4])

        is_overlapping = overlap_x and overlap_y and overlap_z

        # Update UI label
        if is_overlapping:
            print("Objects are overlapping!")
            self.update_status("Objects are overlapping!", success=False)
        else:
            print("Objects do not overlap.")
            self.update_status("Objects do not overlap.", success=True)

        return is_overlapping

    def get_actor_world_bounds(self, actor: vtk.vtkActor):
        """
        Returns the actor's bounding box in world coordinates, considering transformations.
        """
        polydata = actor.GetMapper().GetInput()
        
        # Apply actor transform to all points
        transform = actor.GetMatrix()
        points = polydata.GetPoints()
        transformed_points = []

        for i in range(points.GetNumberOfPoints()):
            x, y, z = points.GetPoint(i)
            # Homogeneous coordinates for transformation
            pt = [x, y, z, 1.0]
            world_pt = [0.0, 0.0, 0.0, 0.0]
            transform.MultiplyPoint(pt, world_pt)
            transformed_points.append(world_pt[:3])

        # Compute AABB in world coordinates
        xs, ys, zs = zip(*transformed_points)
        return (min(xs), max(xs), min(ys), max(ys), min(zs), max(zs))
 
    def rotate_for_gif(self, steps, angle_per_step, interval_ms):
        """
        Smoothly rotate the VTK camera for GIF recording.

        steps: number of frames
        angle_per_step: degrees per frame
        interval_ms: delay between frames (ms)
        """
        self._gif_step = 0

        # Get renderer & camera
        renderer = self.vtkViewer.GetRenderWindow().GetRenderers().GetFirstRenderer()
        camera = renderer.GetActiveCamera()

        # Optional: ensure nice rotation center
        camera.SetViewUp(0, 0, 1)
        renderer.ResetCameraClippingRange()

        def rotate_once():
            if self._gif_step >= steps:
                self._gif_timer.stop()
                return

            camera.Azimuth(angle_per_step)
            renderer.ResetCameraClippingRange()
            self.vtkViewer.GetRenderWindow().Render()

            self._gif_step += 1

        self._gif_timer = QTimer(self)
        self._gif_timer.timeout.connect(rotate_once)
        self._gif_timer.start(interval_ms)
        
    def generate_tet_meshes(self):
        """
        Convert the loaded STL meshes into tetrahedral FEM meshes using TetGen.

        Workflow:
        1. Check that STL meshes have been loaded.
        2. Add the transformed PyVista meshes from the STL manager to Surf2TetMesh.
        3. Generate tetrahedral meshes using TetGen with parameters taken from the widget.
        4. Display the tetrahedral meshes in the dedicated VTK viewer.
        5. Switch the stacked widget to the TetMesh viewer tab.

        Notes:
        - Expects exactly two STL meshes to be loaded (stl_number=1 and stl_number=2).
        - TetGen parameters (maxvolume, order, etc.) are read directly from widget UI components.
        """
        if not hasattr(self.stl_manager, "stl_mesh") or len(self.stl_manager.stl_mesh) < 2:
            self.update_status("Error: Not enough STL meshes loaded. Please load two STL files first.", success=False)
            return

        # Add STL meshes to Surf2TetMesh
        for stl_number, mesh in self.stl_manager.stl_mesh.items():
            try:                
                self.stl_manager.update_pyvista_mesh_from_actor(stl_number)
                self.surf2tetmesh.add_stl_mesh(stl_number, mesh)
                print(f"Added STL {stl_number} to Surf2TetMesh")
                self.update_status(f"Added STL {stl_number} to Surf2TetMesh", success=True)
            except Exception as e:
                print(f"Failed to add STL {stl_number} to Surf2TetMesh: {e}")                
                self.update_status(f"Failed to add STL {stl_number} to Surf2TetMesh: {e}", success=False)
                continue

        self.start_status_animation("Generating FEM mesh")

        # Create worker and thread
        self.tetgen_thread = QThread()
        self.tetgen_worker = TetGenWorker(self.surf2tetmesh, self)
        self.tetgen_worker.moveToThread(self.tetgen_thread)

        self.tetgen_thread.started.connect(self.tetgen_worker.run)
        self.tetgen_worker.finished.connect(self.on_tetgen_finished)
        self.tetgen_worker.finished.connect(self.tetgen_thread.quit)
        self.tetgen_worker.finished.connect(self.tetgen_worker.deleteLater)
        self.tetgen_thread.finished.connect(self.tetgen_thread.deleteLater)

        self.tetgen_thread.start()

    def on_tetgen_finished(self, success: bool, message: str):
        """Handle completion of TetGen worker"""
        # Stop animation and show final status
        self.stop_status_animation(message, success=success)

        if success:
            # Update node/element labels
            self.surf2tetmesh.update_mesh_count_labels(self)

            # Switch to TetMesh viewer
            self.viewerStackedWidget.setCurrentIndex(1)

            # Display all generated Tet meshes
            try:
                self.surf2tetmesh.display_tet_meshes()
                print("Tet meshes displayed successfully.")
            except Exception as e:
                print(f"Failed to display Tet meshes: {e}")
    

class TetGenWorker(QObject):
    """Worker to generate TetGen meshes in a background thread."""
    finished = Signal(bool, str)  # success flag, message

    def __init__(self, surf2tetmesh: Surf2TetMesh, parent_widget: QWidget):
        super().__init__()
        self.surf2tetmesh = surf2tetmesh
        self.parent_widget = parent_widget

    def run(self):
        """Called in a separate thread to generate TetGen meshes."""
        try:
            self.surf2tetmesh.generate_fem_mesh(self.parent_widget)
            self.finished.emit(True, "Mesh generation completed")
        except Exception as e:
            self.finished.emit(False, f"Mesh generation failed: {e}")
