#!/bin/bash

# introduction: select a few tiles and reproject

# run this script in Bhaltos2/lingcaoHuang/global_surface_water

#authors: Huang Lingcao
#email:huanglingcao@gmail.com
#add time: 17 May, 2021



# reproject to Polar Stereographic North
t_prj=EPSG:32646
out_dir=extent_UTM46N_Goalpara

mkdir -p ${out_dir}

# 170W_80N, 170W_70N, 160W_80N,160W_70N,150W_80N,150W_70N

for tile in 80E_30N 80E_20N 90E_30N 90E_20N ;do
  echo $tile
  tif=$(ls extent/*${tile}*)
  echo $tif

  # re-project
  basename=$(basename $tif)
  output=${out_dir}/${basename}
  echo $output
  gdalwarp -r near -t_srs ${t_prj} -tr 30 30 -co compress=lzw $tif ${output}

done





