"""
Main module for crating a web map of
the user's input account's following people and
their locations.
"""
import json
import ssl
import urllib.error
import urllib.request
from random import choice as ch

import folium
from opencage.geocoder import OpenCageGeocode

from Lab_3_3 import twurl

KEY = '9a05b0c1fd3b4387932903a5456254da'
GEOCODER = OpenCageGeocode(KEY)


# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py


def collect_acc():
    """
    (None) -> (str)
    Collects an account name from the user.
    """
    acct_name = input('Enter Twitter Account:')
    return acct_name


def collect_data(inp_acc, tw_url, ctx_inp):
    """
    (str, str, ssl.SSLContext) -> (dict)
    Given the url's and account name,
    converts a json file of twitter info
    into a dict.
    """
    url = twurl.augment(tw_url,
                        {'screen_name': inp_acc, 'count': '50'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx_inp)
    data = connection.read().decode()
    js_data = json.loads(data)
    return js_data


def main_loc(inp_dict):
    """
    Given a dict, transformed from a json file,
    returns a dict with the locations,
    represented as coordinates.
    """
    res_dict = {}
    for i in inp_dict['users']:
        res_dict[i['screen_name']] = i['location']
    for key in res_dict:
        try:
            result = GEOCODER.geocode(res_dict[key], no_annotations='1')
            lng = result[0]['geometry']['lng']
            lat = result[0]['geometry']['lat']
            res_dict[key] = [lat, lng]
        except IndexError:
            pass
    return res_dict


def create_map(inp_dict):
    """
    (dict) -> (None)
    Creates a web-map according to the given dict
    of friends and their locations.
    """
    final_map = folium.Map(zoom_start=5)
    fg_fr = folium.FeatureGroup(name="Friends locations")
    tool_tip = "Click me!"
    colors = [
        'lightred', 'lightgreen', 'black', 'lightgray', 'green',
        'darkgreen', 'red', 'cadetblue', 'darkred', 'pink',
        'lightblue', 'darkpurple', 'beige', 'purple',
        'darkblue', 'gray', 'orange', 'blue'
    ]
    styles = ['cloud', 'info-sign']
    for i in inp_dict:
        try:
            fg_fr.add_child(folium.Marker(location=inp_dict[i],
                                          popup=i,
                                          icon=folium.Icon(color=ch(colors),
                                                           icon=ch(styles)),
                                          tooltip=tool_tip))
        except ValueError:
            pass
    final_map.add_child(fg_fr)
    final_map.save('templates/MyMap.html')
    # html_string = final_map.get_root().render()
    # file_path = 'templates/MyMap.html'
    # html_file = open(file_path, 'w')
    # html_file.write(html_string)
    # html_file.close()


def main_func(inp_acc):
    """
    (None) -> (None)
    Main function for creating a map accoring to
    a given account name.
    :return:
    """
    twitter_url = 'https://api.twitter.com/1.1/friends/list.json'
    ctx_th = ssl.create_default_context()
    ctx_th.check_hostname = False
    ctx_th.verify_mode = ssl.CERT_NONE
    if inp_acc != '':
        final_dict = collect_data(inp_acc, twitter_url, ctx_th)
        create_map(main_loc(final_dict))


if __name__ == "__main__":
    ACC = collect_acc()
    main_func(ACC)
    print("Please, check your map!")
