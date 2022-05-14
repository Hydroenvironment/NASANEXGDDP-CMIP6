################################################################################
# EXTRACTION OF DAILY DATA FROM                                                #
# NETCDF FILES OF NASA NEX GDDP CMIP6 PRODUCT                                  #
################################################################################

#Author: Julio Montenegro Gambini, M.Sc.,
#PhD fellow - Technische Universiteit Delft (TU Delft), Netherlands.

#Current version: 1.0

#©Copyright 2022.
#This script is strictly under license GPLv3
#License details: https://www.gnu.org/licenses/gpl-3.0.en.html

# Please, when using this script, cite as: "Montenegro, J. (2022). Tools for
# handling NASA NEX GDDP CMIP6 climate change datasets"

####'--------------Workspace cleaning (required)------------------------
rm(list = ls())
dev.off()

####'--------------Installing packages (required)------------------------
pkg <- c("dplyr", "raster", "ncdf4", "rgdal", "lattice", "latticeExtra", "sp")

sapply(
  pkg,
  function(x) {
    is.there <- x %in% rownames(installed.packages())
    if (is.there == FALSE) {
      install.packages(x, dependencies = T)
    }
  }
)

#Then, let`s load the packages
library(dplyr)
library(ncdf4)
library(raster)
library(sp)
library(rgdal)
library(lattice)
library(latticeExtra)

####'---------------Setting working directory (required)------------------------
setwd('D:/RESEARCH/CMIP6/R SCRIPTS CMIP6/NNGDDP_CMIP6_R')

####'---------------Loading point shapefile (required)------------------------
shp.wgs <- readOGR(dsn = "D:/RESEARCH/CMIP6/R SCRIPTS CMIP6/NNGDDP_CMIP6_R", 
                   layer = "Test_points")

####'---------------Extracting data from point shapefile------------------------
#First, identify the netCDF files (.nc) located in the folder
nc_files<-list.files(pattern=".nc")
#The test shapefile is located in this repository, and at first it has UTM WGS84 projection
#Then let`s change to lat/lon coordinates
shp_geo<-spTransform(shp.wgs,CRS("+proj=longlat +datum=WGS84"))
#Adjusting the coordinates according to the netCDF projection
shp_geo@coords[,1]<-360+shp_geo@coords[,1]
#Let`s create an empty dataframe
df <- data.frame()
#We need a loop for extracting the data from each netCDF file
for (i in nc_files) {
  #Loop using all the files
  cmip6.brick = brick(i)  
  pp.cuenca.daily <- data.frame(86400*t(extract(cmip6.brick,shp_geo)))
  df<-rbind(df,pp.cuenca.daily)
}
#CAUTION!: Remove "86400" in the loop if the variable under study is not precipitation
#If it is temperature (tasmax, tasmin or tas), the line would be: t(extract(cmip6.brick,shp_geo))-273.15
#The test shapefile has an attribute with station names
colnames(df) <- shp_geo@data$ESTACIONES
write.csv(df, "CMIP6.csv")

####'---------------Extract from just one NetCDF file----------------------------
cmip6.brick = brick("pr_pr_day_ACCESS-CM2_ssp585_r1i1p1f1_gn_2099.nc")  
#Checking NetCDF file characteristics
cmip6.brick
#How many layers does it have?
nlayers(cmip6.brick)
#Generating a simple plot of the first 12 days
spplot(cmip6.brick[[1:12]])

####'---------------Examining the point shapefile------------------------
#In this section we are only focused on the shapefile
shp.wgs <- readOGR(dsn = "D:/RESEARCH/CMIP6/R SCRIPTS CMIP6/NNGDDP_CMIP6_R", layer = "Test_points")
crs(shp.wgs)
coordinates(shp.wgs)
#Transforming from UTM to geographical coordinates
shp_geo<-spTransform(shp.wgs,CRS("+proj=longlat +datum=WGS84"))
#Checking the new coordinates of each point
coordinates(shp_geo)
#Configuring coordinates in 0 to 360° range
shp_geo@coords[,1]<-360+shp_geo@coords[,1]
#See new changes
shp_geo@coords[,1]
plot(shp.wgs, col= "blue", main = "Points", axes=T, asp=1) #trying a simple plot
shpRp   = spTransform(shp.wgs, proj4string(cmip6.brick))
coordinates(shpRp)
#View(shp.wgs@data)

####'---------------Plotting data from just one NetCDF file------------------------
#Let`s choose any of the netCDF files, in this case we will evaluate precipitation data:
cmip6.brick = brick("pr_pr_day_ACCESS-CM2_ssp585_r1i1p1f1_gn_2099.nc")
#Time to extract the data!
pp.cuenca.daily <-86400*t(extract(cmip6.brick,shp_geo))
#CAUTION!: Remove "86400" of the previous line if the variable on study is not precipitation
#If it is temperature (tasmax, tasmin or tas), the line would be: t(extract(cmip6.brick,shp_geo))-273.15
#Let`s have a loot at it!
#View(pp.cuenca.daily)
colnames(pp.cuenca.daily) <- shp_geo@data$ESTACIONES
#What is the range of the data values?
range(pp.cuenca.daily)
plot(pp.cuenca.daily[,5], type = "l", col= "blue", ylim= c(0, 53), ylab = "Precipitation (mm/day)",
     xlab = "time (days)", main= "Area average precipitation (mm)")
