# @file createSidebar.py
#
# Copyright IBM Corporation 2022
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import json
import yaml
import requests
import urllib3

from xml.dom import minidom

def loadIconXML():
    inputfile = './input/ibm.xml'
    file = minidom.parse(inputfile)
    shapes = file.getElementsByTagName('shape')
    return shapes

def loadAllCategories():
    inputfile = './input/categories.yml'
    stream = open(inputfile, 'r')
    data = yaml.load(stream, Loader=yaml.FullLoader)
    return data

def loadMaps():
    inputfile = './input/maps.yml'
    stream = open(inputfile, 'r')
    data = yaml.load(stream, Loader=yaml.FullLoader)
    return data

def loadSubsetCategories():
    inputfile = './input/categories-subset.yml'
    stream = open(inputfile, 'r')
    data = yaml.load(stream, Loader=yaml.FullLoader)
    return data

def findSidebarMap(maps, member):
    mapdict = maps.values()
    for maparray in mapdict:
        for map in maparray:
            if map['source'] == member:
                return map
    return None

def isShapeName(shapes, name):
    for shape in shapes:
        if shape.attributes['name'].value == name:
            return True
    return False

xmldata = loadIconXML()
#catdata = loadAllCategories()
catdata = loadSubsetCategories()
mapdata = loadMaps()

if catdata != None and mapdata != None:
    catdict = catdata.values()
    print('{')
    print('  "Sidebars": {')
    print('    "Icons": {')
    for categoryarray in catdict:
        catcount = len(categoryarray)
        for category in categoryarray:
            catcount = catcount - 1
            subcategories = category['subcategories']
            subcount = len(subcategories)
            for subcategory in subcategories:
                subcount = subcount - 1
                print('')
                if subcategory['name'] == 'none':
                    print('      "' + category['name'] + '": {')
                else:
                    print('      "' + category['name'] + ' - ' + subcategory['name'] + '": {')
                members = subcategory['members']
                memcount = len(members)
                for member in members:
                    #if isShapeName(xmldata, member):
                        memcount = memcount - 1
                        map = findSidebarMap(mapdata, member)
                        if map != None:
                            if memcount == 0:
                                print('        "' + member + '": {"icon": "' + member + '", "format": "$BASE_ICON", "$BASE_ICON_DEFAULT_PROPERTIES": null, "' + map['mapper'] + '": "' + map['target'] + '"}')
                            else:
                                print('        "' + member + '": {"icon": "' + member + '", "format": "$BASE_ICON", "$BASE_ICON_DEFAULT_PROPERTIES": null, "' + map['mapper'] + '": "' + map['target'] + '"},')
                        else:
                            if memcount == 0:
                                print('        "' + member + '": {"icon": "' + member + '", "format": "$BASE_ICON", "$BASE_ICON_DEFAULT_PROPERTIES": null}')
                            else:
                                print('        "' + member + '": {"icon": "' + member + '", "format": "$BASE_ICON", "$BASE_ICON_DEFAULT_PROPERTIES": null},')

                if subcount == 0 and catcount == 0:
                    print('      }')
                else:
                    print('      },')

    print('    }')
    print('  },')

    print('')
    print('  "Variables": {')
    print('    "$BASE_ICON": {"type": "nodel", "layout": "collapsed", "weight": null, "header": true, "container": false},')
    print('    "$BASE_ICON_DEFAULT_PROPERTIES": {"text": null, "subtext": null, "color": "$BASE_ICON_DEFAULT_COLOR", "badge": "$BASE_ICON_DEFAULT_BADGE", "style": "$BASE_ICON_DEFAULT_STYLE", "ignore": false},')
    print('    "$BASE_ICON_DEFAULT_COLOR": {"line": "coolgray",  "fill": null, "font": null},')
    print('    "$BASE_ICON_DEFAULT_BADGE": {"form": null, "color": "blue", "text": null},')
    print('    "$BASE_ICON_DEFAULT_STYLE": {"dashed": false, "double": false, "strikethrough": false, "multiplicity": false}')
    print('  }')

    print('}')

