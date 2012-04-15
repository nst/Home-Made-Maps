#!/usr/bin/python

"""
from google kml to json with time and travel distance

$ curl "http://maps.google.com/maps/ms?msa=0&msid=210545173139138797518.0004a6dcfefdc6b4ae2bc&output=kml" > map.kml

$ python kml_to_json.py --start "place de la gare 1, lausanne" --places map.kml > map.json
"""

import xml.dom.minidom
import re
import json
import sys
import argparse

from googlemaps import GoogleMaps

api_key = "ABQIAAAAyj5pErQ2rt4sNoP8_DBVcxQqgwkBz2GMttiD5juD_pXeJYXxeBRiygJvZWY_J3-nSAR3nvEmuLIi3Q"
gmaps = GoogleMaps(api_key)

def name_lon_lat_list_in_kml_generator(kml_file):

    doc = xml.dom.minidom.parse(kml_file)
        
    for placemark_dom in doc.getElementsByTagName('Placemark'):
    
        point = placemark_dom.getElementsByTagName("Point")[0]
        coord_node = point.getElementsByTagName("coordinates")[0]
        coord = coord_node.firstChild.nodeValue
        
        name_node = placemark_dom.getElementsByTagName("name")[0]
        name = name_node.firstChild.nodeValue
        
        m = re.match(r"(\S+),(\S+),\S+", coord)
        
        if not m:
            sys.stderr.write("-- skip coord: %s, name: %s\n" % (coord, name))
            continue
        
        lat, lon = float(m.group(1)), float(m.group(2))
        
        yield (name, lat, lon)

def name_lon_lat_time_dictionaries(start_address, kml_file):
    
    ll = gmaps.address_to_latlng(start_address)
    
    sys.stderr.write("\nstart from: %s %s\n" % (start_address, ll))
    
    l = []

    for (name, lon, lat) in name_lon_lat_list_in_kml_generator(kml_file):
        sys.stderr.write("\n%s\n" % name)
        sys.stderr.write("%f %f\n" % (lon, lat))
    
        destination = "%f,%f" % (lat, lon)
        
        try:
            directions = gmaps.directions(start_address, destination)
        except Exception, e:
            print e
            continue
            
        minutes = directions['Directions']['Duration']['seconds'] / 60
        sys.stderr.write("-- time [min]: %d\n" % minutes)
        
        d = {'name':name, 'lon':lon, 'lat':lat, 'minutes':minutes}
        
        l.append(d)
        
    return l

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--start', required=True, help="toto")
    parser.add_argument('-p', '--places', required=True, type=file)
    args = parser.parse_args()
    
    l = name_lon_lat_time_dictionaries(args.start, args.places)
    
    print json.dumps(l, indent = 4)
    