import os
import glob
import netCDF4
import xarray as xr

ds = xr.merge([xr.open_dataset(f) for f in glob.glob(r'D:/RESEARCH/CMIP6/R SCRIPTS CMIP6/NNGDDP_CMIP6_R/*.nc')])
ds.to_netcdf(r'D:/RESEARCH/CMIP6/R SCRIPTS CMIP6/NNGDDP_CMIP6_R/joined_nc.nc')

ds1 = xr.open_dataset(r'D:/RESEARCH/CMIP6/R SCRIPTS CMIP6/NNGDDP_CMIP6_R/joined_nc.nc')
