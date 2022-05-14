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


import os
import glob
import netCDF4
import xarray as xr

ds = xr.merge([xr.open_dataset(f) for f in glob.glob(r'D:/RESEARCH/CMIP6/R SCRIPTS CMIP6/NNGDDP_CMIP6_R/*.nc')])
ds.to_netcdf(r'D:/RESEARCH/CMIP6/R SCRIPTS CMIP6/NNGDDP_CMIP6_R/joined_nc.nc')

ds1 = xr.open_dataset(r'D:/RESEARCH/CMIP6/R SCRIPTS CMIP6/NNGDDP_CMIP6_R/joined_nc.nc')