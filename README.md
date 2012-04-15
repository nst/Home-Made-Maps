Here are two Python scripts to generate what I call a "centered time-distance map" (see below).

The idea is to consider the observer's location as the center of the map. Places are then shown in the same direction as on a usual map, but at a distance proportional to the travel time needed to reach them.

The process to generate such a map can be broken down this way:

1. enter the places you're interested in a Google Map
2. export the Google map as a KML file
3. use retrieve the durations needed to reach each point, store them in a JSON file
4. compute (x,y) position for each point
5. generate Apple Script code to draw the points in OmniGraffle

First, enter the places in a Google map and export it as a KML file

    $ curl "http://maps.google.com/maps/ms?msa=0&msid=210545173139138797518.0004a6dcfefdc6b4ae2bc&output=kml" -o map.kml

Then, extract the coordinates and get the travel time to them, with the kml_to_json.py script.

    $ python kml_to_json.py \
    --start "Place de la Gare 1, Lausanne" \
    --places map.kml \
    > map.json

The kml_to_json.py script converts the KML file into an array of destinations with GPS coordinates and adds the time needed to reach them from the start address.

    [
        {
            "lat": 46.537136, 
            "minutes": 10, 
            "lon": 6.639862, 
            "name": "Sauvabelin"
        }, 
        {
            "lat": 46.4533, 
            "minutes": 34, 
            "lon": 6.942905, 
            "name": "Les Avants"
        }
    ]

The json_to_omnigraffle.py script computes the (x, y) coordinates in the Mercator projection and generates Apple Script code to draw these places in [OmniGraffle](http://www.omnigroup.com/products/omnigraffle/).

    $ python json_to_omnigraffle.py --center_lat 46.515533 --center_lon 6.6297428  --show_radius True --places map.json > map.txt

Finally, open a new document in Omni Graffle and execute the script.

    $ osascript map.txt

You'll end up with a nice map such as this one. You can then add roads and, and tweak the points position manually.

You can find other home made maps on [http://seriot.ch/maps.php](http://seriot.ch/maps.php).

<a href="http://seriot.ch/maps/touristic_map_lausanne.pdf">
    <img src="http://seriot.ch/maps/touristic_map_lausanne.png" border="1" />
</a>
