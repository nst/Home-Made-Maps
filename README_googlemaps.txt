googlemaps 1.0.2
16 Oct 2009
README
=================

This is a Python 2 module that provides access to the Google Maps and Local 
Search AJAX APIs.  It has the following features:

* Geocoding: convert a postal address to latitude and longitude
* Reverse Geocoding: convert a latitude and longitude to a postal address
* Driving Directions: turn-by-turn instructions for getting from one point to 
  another, distance and duration of travel
* Local Search: find businesses and other points of interest near a given 
  location  

You will need a Google Maps API key and/or URL of the website where the
information will be used (a referrer URL) to comply with Google's terms
of service.  Google also imposes additional restrictions on their
service, including limiting the number of queries per day.  This 
software is not related to Google Inc. in any way.  See the included HTML 
documentation in doc/html or the interactive help for more.


Dependencies
------------
This module should work with Python 2.3 - 2.6+, and with Python 3+ via 2to3.
Its only dependency is the json module, included with Python versions 2.6 and
later and available for download as simplejson for earlier versions.


Installation
------------
You can install this package with easy_install using:

    easy_install googlemaps
    
Or if you have already downloaded the .tar.gz archive:

    tar xzvf googlemaps-1.0.2.tar.gz
    cd googlemaps-1.0.2
    python setup.py install


Contact Information
-------------------
Author: John Kleint
Internet: http://py-googlemaps.sourceforge.net
E-mail: py-googlemaps-general@lists.sourceforge.net


Copyright and Licensing
-----------------------
This is free software, Copyright 2009 John Kleint, licensed under what is
effectively a "Lesser Affero General Public License."  It is identical to
the GNU LGPLv3 but refers to the GNU Affero GPL v3 instead of the standard
GNU GPL v3.  

In plain English, the intent of this license is the following:

1. You are free to use this library unmodified, without obligation, for any 
purpose.

2. If you modify this library and distribute software using the modified
library, you must make your modified version of this library freely available 
under the same terms as this library.  

3. If you modify this library and use it to provide a network service,
you must make your modified version of this library freely available under 
the same terms as this library.  

4. In any case, software using this library can be licensed however you like.

See the files LICENSE.txt and AGPLv3.txt for details.


Changelog
---------
Version 1.0.2:
Refactored GoogleMapsError to contain status codes.

Version 1.0.1:
Fixed local search throwing an exception if Google returned fewer results
than requested.

Version 1.0:
Initial Release

