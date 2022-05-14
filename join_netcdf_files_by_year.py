################################################################################
#JOINING NETCDF ANNUAL FILES                                                   #
#OF NASA NEX GDDP CMIP6 DATASET                                                #
################################################################################

#Author: Julio Montenegro Gambini, M.Sc.,
#PhD fellow - Technische Universiteit Delft (TU Delft), Netherlands.

#Current version: 1.0

#©Copyright 2022.
#This script is strictly under license GPLv3
#License details: https://www.gnu.org/licenses/gpl-3.0.en.html

# Please, when using this script, cite as: "Montenegro, J. (2022). Tools for
# handling NASA NEX GDDP CMIP6 climate change datasets"

#Loading the required packages
import os
import glob
import netCDF4
import xarray as xr

#IMPORTANT!: All the downloaded annual netCDF files will be located in only one folder.
#Each model, ssp trajectory and variable must have an unique folder.

#Using xarray library to join the files in a loop
ds = xr.merge([xr.open_dataset(f) for f in glob.glob(r'D:/RESEARCH/CMIP6/R SCRIPTS CMIP6/NNGDDP_CMIP6_R/*.nc')])
ds.to_netcdf(r'D:/RESEARCH/CMIP6/R SCRIPTS CMIP6/NNGDDP_CMIP6_R/joined_nc.nc')
#Let`s open to verify the created netCDF file
ds1 = xr.open_dataset(r'D:/RESEARCH/CMIP6/R SCRIPTS CMIP6/NNGDDP_CMIP6_R/joined_nc.nc')

#Finally, the new file called "joined_nc.nc" will contain all the daily data of the downloaded annual netCDF files.
