#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:02:21 2023

@author: marina
"""

import ee
import geemap


ee.Authenticate()
ee.Initialize()

poi = [-56.164810605875374,-34.89628099314082]

roi = ee.Geometry.BBox(poi[0] - 0.05, poi[1]-0.05, poi[0] + 0.05, poi[1]+0.05)
timelapse = geemap.landsat_timelapse(
    roi,
    out_gif='landsat.gif',
    start_year=1984,
    end_year=2022,
    start_date='01-01',
    end_date='12-31',
    bands=['Red', 'Green', 'Blue'],
    frames_per_second=2,
    title='Landsat Timelapse',
    progress_bar_color='blue',
    mp4=True,
)
geemap.show_image(timelapse)