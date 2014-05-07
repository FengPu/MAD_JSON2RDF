# -*- coding: utf-8 -*-
#    This file is part of X2R.
#
#    MAD is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MAD is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with MAD.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
# Module Name:
#
#    extractor.py
#
# Abstract:


#
# Author:
#
#    Feng-Pu Yabg 
#
# Project:
#
#    MAD
#
# -*-

"""
.. module:: extractor
   :platform: Unix, Linux, Windows
   :synopsis: A useful module indeed.

.. moduleauthor:: Feng-Pu Yang <fengpuyang@gmail.com>


"""
import json
import codecs
from configobj import *

class JSON2RDF:
    """
    """

    def __init__(self):
        '''This is the init. method

        :returns:  s.

        TODO: init based on the mapping file
        The mapping file defines:
             1. JSON Key -> predicateURI
             2. primary key -> subject
             3. atomic JSON object's type: to determine a tuple: primary key is_a type (optional)

        '''
        pass

    def translate(self, json_str):
        '''This function is used to extract URIs.
        :param json_str: valid JSON string.
        :type json_str: str.
        :returns:  str. RDF string for the input json_str.

        '''
        try:
            raw_data = json.loads(json_str)
            print 'pass'
            for json_obj in raw_data:
                print json_obj
        except ValueError:
            print 'exception'

def reset_test_data():
    config = ConfigObj()
    config.filename = 'mapping.conf'
    config['ObjectTypeUri'] = "http://cool_uri/facility"
    config['ObjectId'] = "ID"
    config['Attributes'] = {}
    config['Attributes']["Name"] = "http://cool_uri/hasName"
    config['Attributes']["Type"] = "http://cool_uri/hasType"
    config['Attributes']["District"] = "http://cool_uri/hasDistrict"
    config['Attributes']["Address"] = "http://cool_uri/hasAddress"
    config['Attributes']["Telephon"] = "http://cool_uri/hasTelephon"
    config['Attributes']["Latitude"] = "http://cool_uri/hasLatitude"
    config['Attributes']["Longitude"] = "http://cool_uri/hasLongitude"
    config['Attributes']["MoreInfo"] = "http://cool_uri/hasMoreInfo"
    config.write()

def main():
    j2r = JSON2RDF()
    reset_test_data()
    json_str = ""
    with codecs.open('./test_data/example.json','r',encoding='utf8') as f:
        json_str = f.read()
    print json_str
    j2r.translate(json_str)

if __name__ == "__main__":
    main()