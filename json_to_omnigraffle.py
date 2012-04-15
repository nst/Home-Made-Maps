#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
- json_to_omnigraffle.py creates applescript code to show places in omnigraffle
- the places are spread according to their travel time from center

$ python places_to_applescript.py --center_lat 46.516765 --center_lon 6.630904 --show_radius True --places map.json > map.txt

$ osascript map.txt
"""

from math import *
import json
import argparse

offset_x = 538
offset_y = 677

place_radius = 1
scale_factor = 7

text_w = 30.0
text_h = 14.0

def bearing(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    delta_lon = lon2 - lon1

    y = sin(delta_lon) * cos(lat2)
    x = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(delta_lon)
    
    return atan2(y, x)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--places', required=True, type=file)
    parser.add_argument('-lat', '--center_lat', required=True, type=float)
    parser.add_argument('-lon', '--center_lon', required=True, type=float)
    parser.add_argument('-r', '--show_radius', required=False, type=bool)
    args = parser.parse_args()
    
    places = json.load(args.places)
    
    print "tell application \"OmniGraffle Professional 5\""
    print "\ttell canvas of front window"

    if args.show_radius:
        
        x = offset_x
        y = offset_y
        
        print "make new line at end of graphics with properties {point list: {{%f, %f}, {%f, %f}}}" % (x-20, y, x+20, y)
        print "make new line at end of graphics with properties {point list: {{%f, %f}, {%f, %f}}}" % (x, y-20, x, y+20)
    
        for radius in range(15, 120, 15):
            
            radius = radius * scale_factor
            
            x = offset_x - radius
            y = offset_y - radius
            
            print "\t\tmake new shape at end of graphics with properties {textPosition: {0.100000, 0.150000}, fill: no fill, draws shadow: false, size: {%f, %f}, flipped vertically: true, name: \"Circle\", origin: {%f, %f}, textSize: {0.800000, 0.700000}, flipped horizontally: true}" % (radius * 2, radius * 2, x, y)
    
    for p in places:
        
        b = bearing(args.center_lat, args.center_lon, p['lat'], p['lon'])
        angle = degrees(b)
    
        x = ((sin(b) * p['minutes'] * scale_factor) * 1) + offset_x
        y = ((cos(b) * p['minutes'] * scale_factor) * 1 * -1) + offset_y
        
        print "\t\tmake new shape at end of graphics with properties {textPosition:{0.1, 0.15}, draws shadow:false, size:{%f, %f}, name:\"Circle\", origin:{%f, %f}, textSize:{0.8, 0.7}}" % (place_radius * 2, place_radius * 2, x - place_radius, y - place_radius)
        print "\t\tmake new shape at end of graphics with properties {fill:no fill, draws shadow:false, size:{%f, %f}, side padding:0, autosizing:full, vertical padding:0, origin:{%f, %f}, text:{text:\"%s\", size: 9, alignment: left}, draws stroke:false}" % (text_w, text_h, x+10, y - place_radius - text_h/2.0, p['name'])
        print ""
    
    print "\tend tell"
    print "end tell"
