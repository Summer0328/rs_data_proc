#!/bin/bash

## Introduction:  calculate the NDVI and NDWI for Landsat8

# the similar script are in Landuse_DL-RSE2020paper/landsat/msi_landsat8.py

#authors: Huang Lingcao
#email:huanglingcao@gmail.com
#add time: 26 April, 2021

# Exit immediately if a command exits with a non-zero status. E: error trace
set -eE -o functrace

function landsat8_ndvi () {
    b5=$1
    b4=$2
    out=$3
    gdal_calc.py --calc="(A-B)/(A+B)" --outfile=${out} -A ${b5} -B ${b4} --type=Float32
}

function landsat8_ndvi () {
    b5=$1
    b6=$2
    out=$3
    gdal_calc.py --calc="(A-B)/(A+B)" --outfile=${out} -A ${b5} -B ${b6} --type=Float32
}

dir=~/Data/Arctic/YK_delta_permafrost_depth/LC08_L1TP_078017_20130617_20170309_01_T1
out=${dir}/LC08_L1TP_078017_20130617_20170309_ndvi.tif
landsat8_ndvi ${dir}/LC08_L1TP_078017_20130617_20170309_01_T1_B5.TIF ${dir}/LC08_L1TP_078017_20130617_20170309_01_T1_B4.TIF  ${out}



dir=~/Data/Arctic/YK_delta_permafrost_depth/LC08_L1TP_078017_20130617_20170309_01_T1
out=${dir}/LC08_L1TP_078017_20130617_20170309_ndwi.tif
landsat8_ndvi ${dir}/LC08_L1TP_078017_20130617_20170309_01_T1_B5.TIF ${dir}/LC08_L1TP_078017_20130617_20170309_01_T1_B6.TIF  ${out}





