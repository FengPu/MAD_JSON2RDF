# -*- coding: utf-8 -*-
#    This file is part of MAD.
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
#    JSON2RDF.py
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
.. module:: JSON2RDF
   :platform: Unix, Linux, Windows
   :synopsis: A useful module indeed.

.. moduleauthor:: Feng-Pu Yang <fengpuyang@gmail.com>


"""
import json
import codecs
from configobj import ConfigObj
from rdflib import URIRef, BNode, Literal
from rdflib import Graph


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
             3. atomic JSON object's type: to determine a tuple: primary key
                is_a type (optional)

        '''
        self.g = Graph()

    def node_factory(self, node_type):
        pass

    def add_triple(self, s, p, o):
        s_node = URIRef(s)
        p_node = URIRef(p)
        o_node = Literal(o)
        self.g.add((s_node, p_node, o_node))

    def getSerializedStr(self):
        return self.g.serialize(format='xml')

    def getSerializedStrByFormat(self, output_format):
        return self.g.serialize(format=output_format)

    def clear(self):
        self.g = Graph()

    def json_object_translator(self, json_obj):
        keys = json_obj.keys()
        idURI = ""
        if "ID" in keys:
            idURI = Vocabulary.ID_PREFIX + json_obj["ID"]
            if "Category" in keys:
                self.add_triple(idURI, Vocabulary.CATEGORY, json_obj["Category"])
            if "Telephone" in keys:
                self.add_triple(idURI, Vocabulary.TELEPHONE, json_obj["Telephone"])
            if "Name" in keys:
                self.add_triple(idURI, Vocabulary.NAME, json_obj["Name"])
            if "District" in keys:
                self.add_triple(idURI, Vocabulary.DISTRICT, json_obj["District"])
            if "Longitude" in keys:
                self.add_triple(idURI, Vocabulary.LONGITUDE, json_obj["Longitude"])
            if "Latitude" in keys:
                self.add_triple(idURI, Vocabulary.LATITUDE, json_obj["Latitude"])
            if "MoreInfo" in keys:
                self.add_triple(idURI, Vocabulary.MOREINFO, json_obj["MoreInfo"])
        else:
            pass # TODO: Log errors 

        
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
                self.json_object_translator(json_obj)
            return self.getSerializedStr()    
        except ValueError:
            print 'exception'


class Vocabulary(object):
    #TODO: initialize this class from configuration file
    #Object_ID_Prefix
    ID_PREFIX = "http://openisdm.com/MAD/facility/"
    #Attributes
    NAME = "http://openisdm.com/MAD/property/hasName"
    TYPE = "http://openisdm.com/MAD/property/hasType"
    CATEGORY = "http://openisdm.com/MAD/property/hasCategory"
    DISTRICT = "http://openisdm.com/MAD/property/hasDistrict"
    ADDRESS = "http://openisdm.com/MAD/property/hasAddress"
    TELEPHONE = "http://openisdm.com/MAD/property/hasTelephone"
    LATITUDE = "http://openisdm.com/MAD/property/latitude"
    LONGITUDE = "http://openisdm.com/MAD/property/longitude"
    MOREINFO = "http://openisdm.com/MAD/property/moreInfo"
    #Facility Categories
    SHELTER_INDOOR = "SHELTER INDOOR"
    SHELTER_OUTDOOR = "SHELTER OUTDOOR"
    MEDICAL = "MEDICAL"
    RESCUE = "RESCUE"
    LIVELIHOOD = "LIVELIHOOD"
    COMMUNICATION = "COMMUNICATION"
    VOLUNTEER_ASSOCIATION = "VOLUNTEER ASSOCIATION"
    TRANSPORTATION = "TRANSPORTATION"
    
    
    

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
    config['Attributes']["Telephone"] = "http://cool_uri/hasTelephone"
    config['Attributes']["Latitude"] = "http://cool_uri/hasLatitude"
    config['Attributes']["Longitude"] = "http://cool_uri/hasLongitude"
    config['Attributes']["MoreInfo"] = "http://cool_uri/hasMoreInfo"
    config.write()


def main():
    j2r = JSON2RDF()
    reset_test_data()
    with codecs.open('./test_data/example3.json', 'r', encoding='utf8') as f:
        json_str = f.read()
    print j2r.translate(json_str)
if __name__ == "__main__":
    main()
