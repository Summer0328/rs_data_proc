#!/usr/bin/env python
# Filename: dem_common.py 
"""
introduction: put some variables

authors: Huang Lingcao
email:huanglingcao@gmail.com
add time: 26 March, 2021
"""

import os,sys

machine_name = os.uname()[1]

# some folder paths
if machine_name == 'uist':
    ArcticDEM_tmp_dir = '/Bhaltos2/lingcaoHuang/ArcticDEM_tmp_dir'

elif machine_name == 'ubuntu':  # tesia
    ArcticDEM_tmp_dir = '/home/lihu9680/Bhaltos2/lingcaoHuang/ArcticDEM_tmp_dir'

elif 'login' in machine_name or 'shas' in machine_name or 'sgpu' in machine_name:   # curc
    ArcticDEM_tmp_dir = '/scratch/summit/lihu9680/ArcticDEM_tmp_dir'
else:
    ArcticDEM_tmp_dir = './'

tarball_dir = os.path.join(ArcticDEM_tmp_dir,'tarballs')    # strip version of ArcticDEM

arcticDEM_reg_tif_dir = os.path.join(ArcticDEM_tmp_dir,'registration_tifs')
relative_dem_dir = os.path.join(ArcticDEM_tmp_dir,'dem_relative_8bit')

grid_dem_diffs_dir = os.path.join(ArcticDEM_tmp_dir,'grid_dem_diffs')
grid_dem_diffs_8bit_dir = os.path.join(ArcticDEM_tmp_dir,'grid_dem_diffs_8bit')
grid_dem_diffs_segment_dir = os.path.join(ArcticDEM_tmp_dir,'grid_dem_diffs_segment_results')

grid_matchtag_sum_dir = os.path.join(ArcticDEM_tmp_dir,'grid_matchtag_sum_tifs')

dem_slope_8bit_dir = os.path.join(ArcticDEM_tmp_dir,'dem_slope_8bit')
dem_slope_dir = os.path.join(ArcticDEM_tmp_dir,'dem_slope')
dem_hillshade_dir = os.path.join(ArcticDEM_tmp_dir,'dem_hillshade')
dem_tpi_8bit_dir = os.path.join(ArcticDEM_tmp_dir, 'dem_tpi_8bit')

grd_hillshade_newest_on_top_dir = os.path.join(ArcticDEM_tmp_dir, 'dem_hillshade_newest_top_grid')

dem_headwall_shp_dir = os.path.join(ArcticDEM_tmp_dir, 'dem_headwall_shp')
grid_dem_headwall_shp_dir = os.path.join(ArcticDEM_tmp_dir, 'dem_headwall_shp_grid')
grid_hillshade_newest_HDLine_dir = os.path.join(ArcticDEM_tmp_dir, 'dem_hillshade_newest_HWLine_grid')


dem_hillshade_subImages_headwall = os.path.join(ArcticDEM_tmp_dir, 'dem_hillshade_subImages_headwall')


grid_dem_subsidence_select = os.path.join(ArcticDEM_tmp_dir,'grid_dem_subsidence_select')

# the mosaic version of AricticDEM
arcticDEM_tile_tarball_dir = os.path.join(ArcticDEM_tmp_dir, 'arcticdem_mosaic_tarballs')
arcticDEM_tile_reg_tif_dir = os.path.join(ArcticDEM_tmp_dir, 'arcticdem_mosaic_reg_tifs')
arcticDEM_tile_hillshade_dir = os.path.join(ArcticDEM_tmp_dir, 'arcticdem_mosaic_hillshade')
arcticDEM_tile_slope_8bit_dir = os.path.join(ArcticDEM_tmp_dir, 'arcticdem_mosaic_slope_8bit')
arcticDEM_tile_slope_dir = os.path.join(ArcticDEM_tmp_dir, 'arcticdem_mosaic_slope')
arcticDEM_tile_tpi_8bit_dir = os.path.join(ArcticDEM_tmp_dir, 'arcticdem_mosaic_tpi_8bit')
# dem_pattern = '*reg_dem.tif'


# surface water mask
mask_water_dir = os.path.join(os.path.dirname(ArcticDEM_tmp_dir), 'global_surface_water' , 'extent_epsg3413')

grid_20_shp = os.path.expanduser('~/Data/Arctic/ArcticDEM/grid_shp/ArcticDEM_grid_20km.shp')
dem_strip_shp = os.path.expanduser('~/Data/Arctic/ArcticDEM/BROWSE_SERVER/indexes/ArcticDEM_Strip_Index_Rel7/ArcticDEM_Strip_Index_Rel7.shp')


# rts results
grid_rts_shp_dir = os.path.join(ArcticDEM_tmp_dir, 'grid_rts_shp')


if __name__ == '__main__':
    pass