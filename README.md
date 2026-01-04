# RadEx Simulator  
*A 3D thermal radiation exchange simulator for engineering applications*

![RadEx Simulator Demo](ui/assets/app_layout.gif)

---

## Badges

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Qt](https://img.shields.io/badge/Qt-PySide6-green)
![VTK](https://img.shields.io/badge/VTK-Visualization-orange)
![Status](https://img.shields.io/badge/status-work%20in%20progress-yellow)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## Overview

**RadEx Simulator** is a desktop application for simulating **transient thermal radiation exchange between two 3D objects**.  
The application follows a **pipeline-driven engineering workflow**, allowing users to import geometry, define physical properties, and analyze heat exchange over time through an intuitive GUI.

This project is developed as a **portfolio project** demonstrating skills in **scientific computing, geometry processing, and GUI development**.

---

## Key Features

- Import and visualize **STL geometries** for two independent objects  
- Interactive **3D positioning and inspection**  
- **Tetrahedral mesh generation** per object  
- Surface-based **radiative view factor computation**  
- Definition of **thermal parameters**:
  - Emissivity  
  - Initial temperature  
  - Heat capacity  
  - Thermal conductivity  
- **Transient thermal simulation** with configurable time step and duration  
- Clean, **pipeline-oriented user interface**

---

## Simulation Pipeline

![Pipeline Overview](docs/pipeline.gif)

1. **Geometry Upload**  
   Load STL files for two bodies.

2. **Positioning**  
   Translate and orient objects in 3D space while preventing overlap.

3. **Meshing**  
   Generate tetrahedral meshes for each object.

4. **Materials**  
   Assign radiative and thermal properties.

5. **Simulation**  
   Compute transient radiative heat exchange.

6. **Results**  
   Analyze and visualize temperature evolution.

---

## Technologies Used

- **Python 3**
- **PySide6 / Qt Designer** – GUI development
- **VTK** – 3D visualization and interaction
- **STL & mesh processing libraries**
- **Qt Stylesheets (QSS)** – UI styling

---

## Project Structure
RadEx Simulator/
├── ui/ # Qt Designer .ui files
├── styles/ # Global QSS stylesheets
├── simulation/ # Thermal simulation logic
├── geometry/ # STL handling and meshing
├── visualization/ # VTK rendering
├── docs/ # GIFs and documentation assets
├── main.py # Application entry point
└── README.md


---

## Status

🚧 **Work in progress**

Planned improvements:
- Internal heat conduction modeling  
- Support for more than two bodies  
- Material property database  
- Export of results (CSV, plots, images)

---

## Motivation

The goal of this project is to combine **engineering simulation methods** with **modern desktop UI development**, focusing on modular design, usability, and visualization quality.  
It is intended as a demonstration of skills relevant to **simulation software development and scientific visualization**.

---

## License

This project is provided for **educational and portfolio purposes**.  



