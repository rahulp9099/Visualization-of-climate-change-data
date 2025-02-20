import netCDF4 as nc #netCDF stands for (network Common Data Form) and it is used to read netCDF file
import numpy as np #This module used for the numerical operation
import matplotlib.pyplot as plt #This module used for the purpose of plotting
from mpl_toolkits.basemap import Basemap
import cartopy.crs as ccrs #used for creating maps and helps in adding geographic features
import cartopy.feature as cfeature #used for  creating maps and helps in adding geographic features
import netCDF4 as nc #netCDF stands for (network Common Data Form) and it is used to read netCDF file 

# Path to the downloaded netCDF file
file_path = 'C:/Users/rahul/OneDrive/Desktop/climate_project/gistemp1200_GHCNv4_ERSSTv5.nc' #specifies the file path of the netCDF file to be read
try:
    # Open the dataset
    ds = nc.Dataset(file_path, mode='r') #it tries to open the netCDF file in the read mode like if it fails it will jump to 'except' block

    # Display basic information about the dataset
    print(ds) #prints the basic information about the dataset like dimensions, variables and attributes
    
    # Extract variables
    time = ds.variables['time'][:] #time
    lat = ds.variables['lat'][:] #latitude
    lon = ds.variables['lon'][:] #longitude
    temp_anomaly = ds.variables['tempanomaly'][:] #temperature anomaly

    # Close the dataset-
    
    ds.close() #closes the netCDF file to free up the resources
 
    # Convert time units
    base_date = np.datetime64('1880-01-01', 'D')  # Starting date
    dates = base_date + time  # Convert time to dates
    #Converts the time variable from the 'netCDF' file into actual dates, starting from "January 1, 1880"

    # Select a specific location for the time series (e.g., global average)
    global_temp_anomaly = np.mean(temp_anomaly, axis=(1, 2))
    #Calculates the global average temperature anomaly by "averaging over all latitudes and longitudes" for each time step

    # Plot the time series graph
    plt.figure(figsize=(14, 8)) #creates new figure with a specified size
    plt.plot(dates, global_temp_anomaly, label='Global Temperature Anomaly') #Plots the global temperature anomaly against time
    plt.xlabel('Year') #labels x-axis and y-axis 
    plt.ylabel('Temperature Anomaly (°C)') #labels x-axis and y-axis 
    plt.title('Global Temperature Anomaly Over Time') #adds a title to the plot
    plt.legend() #Adds a legend to the plot
    plt.grid(True) #Adds a grid to the plot
    plt.show() #Display the plot

    # Select a specific time slice for visualization
    # Let's select the last available time step
    time_index = -1  # Last time step
    temp_data = temp_anomaly[time_index, :, :] 
    #Selects the temperature anomaly data for the last time step available in the dataset

    # Plot the data using Cartopy
    plt.figure(figsize=(14, 8)) #create a new figure 
    ax = plt.axes(projection=ccrs.PlateCarree()) 
    ax.coastlines() #It is a command and adds a new geographic figure like coastlines 
    ax.add_feature(cfeature.BORDERS) #It is a command and Adds a new geographic figure like borders
    ax.add_feature(cfeature.LAND, edgecolor='black') #It is a command and Adds a new geographic figure like land
    ax.add_feature(cfeature.OCEAN) #It is a command and adds a new geographic figure like oceans
    ax.add_feature(cfeature.LAKES, edgecolor='black') #It is a command and adds a new geographic figure like lakes
    ax.add_feature(cfeature.RIVERS) #It is a command and adds a new geographic figure like rivers

    # Create a meshgrid for lat/lon
    lon_grid, lat_grid = np.meshgrid(lon, lat) # It is a numpy library and Creates a 2D grid of latitude and longitude values for plotting the data

    # Plot temperature anomaly data
    c_scheme = ax.pcolormesh(lon_grid, lat_grid, temp_data, transform=ccrs.PlateCarree(), cmap='coolwarm') #Plots the temperature anomaly data using a color map
    plt.colorbar(c_scheme, label='Temperature Anomaly (°C)') #Adds a color bar to the plot to show the temperature anomaly values

    # Add title and labels
    plt.title(f'Temperature Anomaly on {str(dates[time_index])}') #Adds a title showing the date of the selected time slice
    plt.xlabel('Longitude') #Labels the x-axis and y-axis
    plt.ylabel('Latitude')  #Labels the x-axis and y-axis

    # Show the plot
    plt.show() #helps to display the plot

except OSError as e:
    print(f"Error opening file: {e}") #Handles the case where the file cannot be opened and prints an error message