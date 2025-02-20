# Climate Change Data Visualization

## Overview
This project focuses on analyzing and visualizing global temperature anomalies using netCDF datasets. It extracts, processes, and represents climate data through time-series analysis and geospatial mapping. The visualizations help in understanding historical climate trends and global temperature variations over time.

## Technologies Used
- **Python** – For data processing and visualization
- **netCDF4** – To read and process climate data from netCDF files
- **NumPy** – For numerical computations and data manipulation
- **Matplotlib** – For plotting time-series graphs
- **Basemap & Cartopy** – For geospatial visualization and mapping

## Features
- **Time-Series Analysis:** Tracks global temperature anomalies over time.
- **Geospatial Visualization:** Uses Cartopy and Basemap to map temperature variations.
- **Data Handling:** Efficiently reads and processes large netCDF climate datasets.
- **Interactive & Informative Plots:** Provides clear insights into climate change trends.

## Installation & Setup
### Prerequisites
Ensure you have Python installed along with the required libraries. Install dependencies using:
```bash
pip install numpy matplotlib netCDF4 cartopy basemap
```

### Running the Project
1. Clone the repository:
```bash
git clone https://github.com/yourusername/climate-data-visualization.git
```
2. Navigate to the project directory:
```bash
cd climate-data-visualization
```
3. Run the script:
```bash
python climate_visualization.py
```

## Data Source
The project uses **GISTEMP v4** datasets, which provide global historical temperature anomaly records.

## Output
- **Time-Series Graph:** Displays the global temperature anomaly trend from 1880 to the present.
- **Geospatial Map:** A heatmap representation of temperature anomalies across different regions.

## Contribution
Feel free to fork the repository and submit pull requests for improvements.

## License
This project is licensed under the MIT License.
