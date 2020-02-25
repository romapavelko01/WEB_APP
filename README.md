# WEB_APP
## A web-app map-creator

App.py is a python module for creating a web app, given the user's twitter account as an input. The map contains the account's "following"
people's locations on the map (up to 50)

###  Incorporation (flask, etc.)
 App.py is built on flask micro-framework, having some HTML and CSS in it for visible effect; of course it is mainly structured around main.py, python program for getting friends and their locations info out of a json file. The main.py, with the use of opencage library, converts the friends' locations into lists of coordinates and then, using folium package, creates a web map.

### Examples
![alt text](https://github.com/romapavelko01/WEB_APP/blob/master/Image%202-25-20%20at%2013.35.jpg?raw=true)

#### p.s. 
It is actually my first web-app project I have ever done, so don't be too hard on it.
